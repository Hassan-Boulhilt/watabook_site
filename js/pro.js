// /pro — PayPal checkout for Watabook Pro (Android) and licence key delivery.
// The licence service creates PayPal orders, receives PayPal webhooks and
// emails the key. This file only shows buttons and the result.
// Only public values here: the PayPal client ID and plan IDs come from the
// service's /v1/config. No secret ever reaches the browser.
(function () {
  'use strict';

  var LIVE_HOST = 'watabook.devandrepair.com';
  var API = location.hostname === LIVE_HOST
    ? 'https://license.devandrepair.com'
    : 'https://license-service-sandbox.hassan-boulhilt.workers.dev';

  var SKU_YEARLY = 'watabook_pro_yearly';
  var SKU_LIFETIME = 'watabook_pro_lifetime';

  var $ = function (id) { return document.getElementById(id); };

  // Messages in the page's language (a JSON block written by build_locales.py).
  var T = {
    thanks: 'Thank you for buying Watabook Pro',
    approved: 'Payment approved. Preparing your key…',
    received: 'Payment received. Preparing your key…',
    ready: 'Your Pro key is ready',
    later: 'Payment received. Your key will arrive by email in a few minutes.',
    sent_to: 'We also sent it to {email}. Check your spam folder if you do not see it.',
    copied: 'Copied',
    try_again: 'Try again',
    paypal_error: 'Something went wrong with PayPal. No money was taken.',
    capture_error: 'The payment could not be completed. If money was taken, your key will still arrive by email.',
    load_error: 'PayPal could not load. Check your connection.',
    unavailable: 'Checkout is not available right now. Please try again later.',
    yearly_unavailable: 'Yearly is not available right now.',
    bad_email: 'Enter the email address you used with PayPal.',
    sending: 'Sending…',
    resent: 'If we have a key for this email, we sent it again. Check your spam folder too.',
    resend_error: 'Could not send right now. Please try again in a few minutes.'
  };
  try {
    var block = $('proStrings');
    if (block) { var loc = JSON.parse(block.textContent); for (var k in loc) T[k] = loc[k]; }
  } catch (e) { /* keep English */ }
  var LOCALE = document.documentElement.lang || 'en';
  var slots = { yearly: $('paySlotYearly'), lifetime: $('paySlotLifetime') };

  function api(method, path, body) {
    return fetch(API + path, {
      method: method,
      headers: body ? { 'content-type': 'application/json' } : {},
      body: body ? JSON.stringify(body) : undefined
    }).then(function (r) {
      return r.json().catch(function () { return {}; }).then(function (data) {
        if (!r.ok) { var e = new Error(data.message || ('HTTP ' + r.status)); e.data = data; e.status = r.status; throw e; }
        return data;
      });
    });
  }

  function loadScript(src, namespace) {
    return new Promise(function (resolve, reject) {
      var s = document.createElement('script');
      s.src = src;
      s.setAttribute('data-namespace', namespace);
      s.onload = function () { resolve(window[namespace]); };
      s.onerror = function () { reject(new Error('PayPal could not load')); };
      document.head.appendChild(s);
    });
  }

  function slotMessage(slot, text, retry) {
    slot.innerHTML = '';
    var p = document.createElement('p');
    p.className = retry ? 'pay-error' : 'pay-loading';
    p.textContent = text;
    if (retry) {
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'btn btn-secondary'; b.textContent = T.try_again;
      b.addEventListener('click', function () { location.reload(); });
      p.appendChild(document.createElement('br'));
      p.appendChild(b);
    }
    slot.appendChild(p);
  }

  // ---- After payment ---------------------------------------------------

  var result = $('keyResult');
  function showResult(statusText) {
    $('planRow').hidden = true;
    $('plansTitle').textContent = T.thanks;
    $('planFine').hidden = true;
    result.hidden = false;
    $('keyStatus').textContent = statusText;
    result.focus({ preventScroll: true });
    result.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  function showKey(data) {
    $('keyStatus').textContent = T.ready;
    // Show the key with wrap points after each dash; copy the plain key.
    var kv = $('keyValue');
    kv.setAttribute('data-key', data.key);
    kv.textContent = '';
    data.key.split('-').forEach(function (part, i, all) {
      kv.appendChild(document.createTextNode(part + (i < all.length - 1 ? '-' : '')));
      if (i < all.length - 1) kv.appendChild(document.createElement('wbr'));
    });
    $('keyBox').hidden = false;
    var mail = $('keyMail');
    mail.textContent = T.sent_to.replace('{email}', data.email);
    mail.hidden = false;
  }
  function pollCheckout(checkoutId, tries) {
    api('GET', '/v1/checkout/' + checkoutId).then(function (d) {
      if (d.status === 'ready') return showKey(d);
      if (tries > 0) return setTimeout(function () { pollCheckout(checkoutId, tries - 1); }, 2500);
      $('keyStatus').textContent = T.later;
    }).catch(function () {
      if (tries > 0) return setTimeout(function () { pollCheckout(checkoutId, tries - 1); }, 4000);
      $('keyStatus').textContent = T.later;
    });
  }
  $('copyKey').addEventListener('click', function () {
    var key = $('keyValue').getAttribute('data-key') || $('keyValue').textContent, btn = this;
    (navigator.clipboard ? navigator.clipboard.writeText(key) : Promise.reject()).then(function () {
      btn.textContent = T.copied;
      var label = btn.getAttribute('data-label') || btn.textContent; btn.setAttribute('data-label', label); setTimeout(function () { btn.textContent = label; }, 2000);
    }).catch(function () {
      var range = document.createRange(); range.selectNodeContents($('keyValue'));
      var sel = getSelection(); sel.removeAllRanges(); sel.addRange(range);
    });
  });

  // ---- Buttons ---------------------------------------------------------

  var style = { layout: 'vertical', color: 'black', shape: 'rect', height: 46, tagline: false };

  function renderYearly(paypal, product) {
    var checkoutId = null;
    slots.yearly.innerHTML = '';
    paypal.Buttons({
      style: Object.assign({ label: 'subscribe' }, style),
      createSubscription: function (data, actions) {
        return api('POST', '/v1/checkout', { sku: SKU_YEARLY }).then(function (c) {
          checkoutId = c.checkout_id;
          return actions.subscription.create({
            plan_id: c.paypal.plan_id || product.paypal_plan_id,
            custom_id: c.checkout_id,
            application_context: { brand_name: 'Watabook', shipping_preference: 'NO_SHIPPING', user_action: 'SUBSCRIBE_NOW' }
          });
        });
      },
      onApprove: function () {
        showResult(T.approved);
        pollCheckout(checkoutId, 36); // about 90 seconds; PayPal's webhook creates the key
      },
      onError: function () { slotMessage(slots.yearly, T.paypal_error, true); }
    }).render(slots.yearly);
  }

  function renderLifetime(paypal) {
    var checkoutId = null;
    slots.lifetime.innerHTML = '';
    paypal.Buttons({
      style: Object.assign({ label: 'pay' }, style),
      createOrder: function () {
        return api('POST', '/v1/checkout', { sku: SKU_LIFETIME }).then(function (c) {
          checkoutId = c.checkout_id;
          return api('POST', '/v1/orders', { checkout_id: c.checkout_id });
        }).then(function (o) { return o.id; });
      },
      onApprove: function (data, actions) {
        return api('POST', '/v1/orders/' + encodeURIComponent(data.orderID) + '/capture').then(function (r) {
          showResult(T.received);
          if (r.status === 'ready') showKey(r); else pollCheckout(checkoutId, 36);
        }).catch(function (e) {
          // Card declined: let the buyer pick another way to pay.
          if (e.data && e.data.issue === 'INSTRUMENT_DECLINED') return actions.restart();
          slotMessage(slots.lifetime, T.capture_error, true);
        });
      },
      onError: function () { slotMessage(slots.lifetime, T.paypal_error, true); }
    }).render(slots.lifetime);
  }

  api('GET', '/v1/config').then(function (cfg) {
    if (cfg.env !== 'live') $('testBanner').hidden = false;
    var byId = {};
    cfg.products.forEach(function (p) { byId[p.sku] = p; });
    var PP_LOCALE = { en: 'en_US', fr: 'fr_FR', de: 'de_DE', es: 'es_ES', 'pt-PT': 'pt_PT', it: 'it_IT' }[LOCALE];
    var base = 'https://www.paypal.com/sdk/js?client-id=' + encodeURIComponent(cfg.paypal_client_id) + '&components=buttons' +
      (PP_LOCALE ? '&locale=' + PP_LOCALE : '');
    var yearly = byId[SKU_YEARLY];
    if (yearly && yearly.paypal_plan_id) {
      loadScript(base + '&vault=true&intent=subscription', 'paypalSub')
        .then(function (pp) { renderYearly(pp, yearly); })
        .catch(function () { slotMessage(slots.yearly, T.load_error, true); });
    } else {
      slotMessage(slots.yearly, T.yearly_unavailable, false);
    }
    loadScript(base + '&intent=capture&currency=USD', 'paypalOrder')
      .then(function (pp) { renderLifetime(pp); })
      .catch(function () { slotMessage(slots.lifetime, T.load_error, true); });
  }).catch(function () {
    slotMessage(slots.yearly, T.unavailable, true);
    slotMessage(slots.lifetime, T.unavailable, true);
  });

  // ---- Lost key ----------------------------------------------------------

  $('lostKey').addEventListener('submit', function (e) {
    e.preventDefault();
    var input = $('lostEmail'), msg = $('lostMsg'), btn = this.querySelector('button');
    var email = input.value.trim();
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) { msg.textContent = T.bad_email; input.focus(); return; }
    btn.disabled = true; msg.textContent = T.sending;
    api('POST', '/v1/keys/resend', { email: email }).then(function (r) {
      msg.textContent = T.resent;
    }).catch(function () {
      msg.textContent = T.resend_error;
    }).then(function () { btn.disabled = false; });
  });
})();
