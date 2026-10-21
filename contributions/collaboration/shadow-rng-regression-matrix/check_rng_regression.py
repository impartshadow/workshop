#!/usr/bin/env python3
"""Regression matrix for backtesting.py random_ohlc_data seed handling.

Fetches the exact random_ohlc_data function from a pinned backtesting.py
revision, then checks for each seed type (Python int, numpy.int64,
RandomState, Generator):

  vary        successive frames from one generator differ
  reproduce   two independently seeded runs give the same three frames
  isolated    a seeded run gives the same frames regardless of the global
              numpy.random seed
  untouched   a seeded run leaves the global numpy.random state unchanged

Usage: python3 check_rng_regression.py [--revision OWNER/REPO@SHA]
Default revision is the PR 1420 head inspected on 2026-10-21.
Only numpy, pandas and the standard library are required.
"""
import argparse
import ast
import json
import sys
import urllib.request
from typing import Generator, Optional

import numpy as np
import pandas as pd

DEFAULT = "machines-6657/backtesting.py@67853901da3699df66dc16c21d4fe0cc9a7b8d8c"


def load_function(revision: str):
    repo, sha = revision.split("@")
    url = f"https://raw.githubusercontent.com/{repo}/{sha}/backtesting/lib.py"
    src = urllib.request.urlopen(url, timeout=30).read().decode()
    node = next(n for n in ast.parse(src).body
                if isinstance(n, ast.FunctionDef) and n.name == "random_ohlc_data")
    ns = {"np": np, "pd": pd, "Optional": Optional, "Generator": Generator}
    exec(ast.get_source_segment(src, node), ns)
    return ns["random_ohlc_data"]


def example_frame() -> pd.DataFrame:
    return pd.DataFrame({
        "Open": np.arange(20.) + 100, "High": np.arange(20.) + 103,
        "Low": np.arange(20.) + 98, "Close": np.arange(20.) + 101,
    }, index=pd.date_range("2020-01-01", periods=20))


SEEDS = {
    "python_int": lambda: 42,
    "numpy_int64": lambda: np.int64(42),
    "RandomState": lambda: np.random.RandomState(42),
    "Generator": lambda: np.random.default_rng(42),
}


def draw(fn, data, seed, n=3):
    gen = fn(data, random_state=seed)
    return [next(gen) for _ in range(n)]


def same(xs, ys):
    return all(x.equals(y) for x, y in zip(xs, ys))


def run(fn):
    data = example_frame()
    results = {}
    for name, make in SEEDS.items():
        a, b = draw(fn, data, make()), draw(fn, data, make())
        np.random.seed(0)
        g0 = draw(fn, data, make())
        np.random.seed(12345)
        g1 = draw(fn, data, make())
        np.random.seed(7)
        before = np.random.get_state()[1].copy()
        draw(fn, data, make())
        after = np.random.get_state()[1]
        results[name] = {
            "vary": not a[0].equals(a[1]),
            "reproduce": same(a, b),
            "isolated": same(g0, g1),
            "untouched": bool(np.array_equal(before, after)),
        }
    return results


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--revision", default=DEFAULT, help="owner/repo@sha")
    args = p.parse_args()
    fn = load_function(args.revision)
    results = run(fn)
    print(json.dumps({"revision": args.revision, "numpy": np.__version__,
                      "pandas": pd.__version__, "results": results}, indent=1))
    ok = all(all(v.values()) for v in results.values())
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
