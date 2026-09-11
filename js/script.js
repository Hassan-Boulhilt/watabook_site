// Watabook marketing site — minimal, no scroll gimmicks (the app's design
// system is deliberately restrained: 180ms ease-out, no bounce, no parallax).
(function () {
  var toggle = document.getElementById('mobileToggle');
  var sheet = document.getElementById('mobileSheet');
  if (!toggle || !sheet) return;

  function close() {
    sheet.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
  }

  toggle.addEventListener('click', function () {
    var open = sheet.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
  });

  sheet.querySelectorAll('a').forEach(function (a) {
    a.addEventListener('click', close);
  });

  window.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') close();
  });
})();
