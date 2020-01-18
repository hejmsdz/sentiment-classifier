((form, textarea, button, output) => {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    button.disabled = true;
    const oldButtonText = button.innerHTML;
    button.innerHTML = 'Thinking...';
    const text = textarea.value;
    fetch(`/prediction?text=${encodeURIComponent(text)}`)
      .then(response => response.json())
      .then(({ category, confidence }) => {
        output.innerText = `I'm ${Math.round(confidence * 100)}% sure it's ${category}.`;
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
);
