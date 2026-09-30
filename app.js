const button = document.getElementById('copy');
button.addEventListener('click', async () => {
  const prompt = document.getElementById('prompt');
  const status = document.getElementById('copy-status');
  try {
    await navigator.clipboard.writeText(prompt.textContent);
    status.textContent = 'Copied. Paste it into your agent and choose a project.';
    window.workshopTrack?.('copy-prompt');
  } catch {
    const range = document.createRange();
    range.selectNodeContents(prompt);
    const selection = window.getSelection();
    selection.removeAllRanges(); selection.addRange(range);
    status.textContent = 'Prompt selected. Copy it with your device’s copy command.';
  }
});
