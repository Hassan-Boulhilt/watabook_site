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

// Language dropdown (a <details>): close on Escape or on a click elsewhere.
(function () {
  var dd = document.querySelector('.lang-switch details');
  if (!dd) return;
  document.addEventListener('click', function (e) {
    if (!dd.contains(e.target)) dd.removeAttribute('open');
  });
  window.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') dd.removeAttribute('open');
  });
})();

// "Download" buttons: phones go straight to their own store; everyone else
// lands on the hero's App Store / Google Play badges (the href fallback).
(function () {
  var ua = navigator.userAgent || '';
  var ios = /iPhone|iPad|iPod/.test(ua) ||
    (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  var android = /Android/i.test(ua);
  if (!ios && !android) return;
  document.querySelectorAll('.js-download').forEach(function (a) {
    var url = a.getAttribute(ios ? 'data-ios' : 'data-android');
    if (url) a.href = url;
  });
})();
