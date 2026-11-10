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
      b.type = 'button'; b.className = 'btn btn-secondary'; b.textContent = 'Try again';
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
    result.hidden = false;
    $('keyStatus').textContent = statusText;
    result.focus({ preventScroll: true });
    result.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  function showKey(data) {
    $('keyStatus').textContent = 'Your Pro key is ready';
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
    mail.textContent = 'We also sent it to ' + data.email + '. Check your spam folder if you do not see it.';
    mail.hidden = false;
  }
  function pollCheckout(checkoutId, tries) {
    api('GET', '/v1/checkout/' + checkoutId).then(function (d) {
      if (d.status === 'ready') return showKey(d);
      if (tries > 0) return setTimeout(function () { pollCheckout(checkoutId, tries - 1); }, 2500);
      $('keyStatus').textContent = 'Payment received. Your key will arrive by email in a few minutes.';
    }).catch(function () {
      if (tries > 0) return setTimeout(function () { pollCheckout(checkoutId, tries - 1); }, 4000);
      $('keyStatus').textContent = 'Payment received. Your key will arrive by email in a few minutes.';
    });
  }
  $('copyKey').addEventListener('click', function () {
    var key = $('keyValue').getAttribute('data-key') || $('keyValue').textContent, btn = this;
    (navigator.clipboard ? navigator.clipboard.writeText(key) : Promise.reject()).then(function () {
      btn.textContent = 'Copied';
      setTimeout(function () { btn.textContent = 'Copy key'; }, 2000);
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
        showResult('Payment approved. Preparing your key…');
        pollCheckout(checkoutId, 36); // about 90 seconds; PayPal's webhook creates the key
      },
      onError: function () { slotMessage(slots.yearly, 'Something went wrong with PayPal. No money was taken.', true); }
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
          showResult('Payment received. Preparing your key…');
          if (r.status === 'ready') showKey(r); else pollCheckout(checkoutId, 36);
        }).catch(function (e) {
          // Card declined: let the buyer pick another way to pay.
          if (e.data && e.data.issue === 'INSTRUMENT_DECLINED') return actions.restart();
          slotMessage(slots.lifetime, 'The payment could not be completed. If money was taken, your key will still arrive by email.', true);
        });
      },
      onError: function () { slotMessage(slots.lifetime, 'Something went wrong with PayPal. No money was taken.', true); }
    }).render(slots.lifetime);
  }

  api('GET', '/v1/config').then(function (cfg) {
    if (cfg.env !== 'live') $('testBanner').hidden = false;
    var byId = {};
    cfg.products.forEach(function (p) { byId[p.sku] = p; });
    var base = 'https://www.paypal.com/sdk/js?client-id=' + encodeURIComponent(cfg.paypal_client_id) + '&components=buttons';
    var yearly = byId[SKU_YEARLY];
    if (yearly && yearly.paypal_plan_id) {
      loadScript(base + '&vault=true&intent=subscription', 'paypalSub')
        .then(function (pp) { renderYearly(pp, yearly); })
        .catch(function () { slotMessage(slots.yearly, 'PayPal could not load. Check your connection.', true); });
    } else {
      slotMessage(slots.yearly, 'Yearly is not available right now.', false);
    }
    loadScript(base + '&intent=capture&currency=USD', 'paypalOrder')
      .then(function (pp) { renderLifetime(pp); })
      .catch(function () { slotMessage(slots.lifetime, 'PayPal could not load. Check your connection.', true); });
  }).catch(function () {
    slotMessage(slots.yearly, 'Checkout is not available right now. Please try again later.', true);
    slotMessage(slots.lifetime, 'Checkout is not available right now. Please try again later.', true);
  });

  // ---- Lost key ----------------------------------------------------------

  $('lostKey').addEventListener('submit', function (e) {
    e.preventDefault();
    var input = $('lostEmail'), msg = $('lostMsg'), btn = this.querySelector('button');
    var email = input.value.trim();
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) { msg.textContent = 'Enter the email address you used with PayPal.'; input.focus(); return; }
    btn.disabled = true; msg.textContent = 'Sending…';
    api('POST', '/v1/keys/resend', { email: email }).then(function (r) {
      msg.textContent = r.message || 'If we have a key for this email, we sent it again.';
    }).catch(function () {
      msg.textContent = 'Could not send right now. Please try again in a few minutes.';
    }).then(function () { btn.disabled = false; });
  });
})();
