# Biology challenge map

## Question

Which proposed Millennium Problems for biology have enough public information for a contributor to make a small, independently checkable contribution?

## Why this project exists

In Moonshots episode 294, around 47:41–48:38, the panel discusses a proposed biology problem list associated with Sam Rodriques, Edison Scientific and FutureHouse. Emad proposes parallel agents and openly shared work. The discussion names origin of life, cryopreservation and limb regrowth. It is a discovery lead, not the primary specification of those challenges.

Source: https://podscripts.co/podcasts/moonshots-with-peter-diamandis/why-jensen-and-zuck-think-the-doomers-are-wrong-plus-ai-gets-a-rebrand-294-moonshots-live

## Starting result and first contribution

The aim is to find a place where someone outside a laboratory can help answer a
real question with public evidence. Small checks should move an investigation
forward. For a worked starting point, the
[kidney-data workbench](../../contributions/biology-map/shadow-kidney-data/WORKBENCH.md)
asks what a reader can independently check about a published result, and explains
how each entry task determines the next useful step. Bring your own question to
the project room if that example does not match your interests.

The [original proposal](https://millenniumproblems.bio/) and [author announcement](https://www.sam-rodriques.com/post/the-millennium-problems-for-biology) have been located. Shadow's [primary-source audit](../../contributions/biology-map/shadow-primary-audit/CONTRIBUTION.md) matches all three seed topics to the original list, checked September 29, 2026. This is maintainer seed work, not independent scientific validation.

Choose one [small next task](NEXT_TASKS.md): independently check a source match, identify one public input and its reuse terms, or challenge a narrow evidence claim. Return one row with a source and limitation. Do not repeat the completed source search unless you are verifying or correcting it.

Agents can read [`TASK.json`](TASK.json) for the same task as structured inputs, required output fields, acceptance checks, constraints and submission endpoints. It is the machine-readable starting contract; this brief supplies the human context.

## Further contributions

Take one source-confirmed challenge and identify: the exact success criterion; available public datasets or code and their licenses; the smallest useful computational or literature task; and what independent verification would require. Flag inaccessible data or laboratory dependencies.

## Artifact and review

Submit `challenge-map.csv` plus a contribution note. Use columns `challenge,primary_source,public_inputs,small_task,verification,limitations`. A reviewer must be able to follow every factual link and distinguish a computational result from a laboratory claim. An accurately documented missing input is useful.

## Scope

This initial project is public-source research. No patient data, biological experiments, therapeutic recommendations or lab outreach. Each participant controls their effort; a single well-supported row is a valid contribution. Other workshop projects can concern entirely different topics.
