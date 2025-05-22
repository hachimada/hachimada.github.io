/* プロジェクトカードの開閉 */
document.querySelectorAll('.card').forEach(card => {
    card.querySelector('.card__header').addEventListener('click', () => {
      card.classList.toggle('open');
    });
  });
  
  /* ダークテーマ切替 */
  const root   = document.documentElement;
  const toggle = document.getElementById('themeToggle');
  toggle.addEventListener('click', () => {
    const dark = root.getAttribute('data-theme') === 'dark';
    root.setAttribute('data-theme', dark ? 'light' : 'dark');
    toggle.innerHTML = dark ? '<i class="fas fa-moon"></i>' : '<i class="fas fa-sun"></i>';
  });
  