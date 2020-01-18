((form, textarea, button, output, category, confidence) => {
  textarea.addEventListener('input', () => {
    form.classList.remove('predicted');
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    button.disabled = true;
    const oldButtonText = button.innerHTML;
    button.innerHTML = 'Thinking...';
    const text = textarea.value;
    fetch(`/prediction?text=${encodeURIComponent(text)}`)
      .then(response => response.json())
      .then((result) => {
        form.classList.add('predicted');
        output.className = result.category;
        category.innerHTML = result.category;
        confidence.innerHTML = `${Math.round(result.confidence * 100)}%`;
      })
      .finally(() => {
        button.disabled = false;
        button.innerHTML = oldButtonText;
      });
  })
})(
  document.getElementById('form'),
  document.getElementById('text'),
  document.getElementById('button'),
  document.getElementById('output'),
  document.getElementById('category'),
  document.getElementById('confidence'),
);
