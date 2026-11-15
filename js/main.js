const toggle = document.getElementById('themeToggle');
toggle.addEventListener('click', () => {
  const dark = document.documentElement.dataset.theme !== 'dark';
  document.documentElement.dataset.theme = dark ? 'dark' : 'light';
  toggle.firstElementChild.textContent = dark ? '☀' : '☾';
});
