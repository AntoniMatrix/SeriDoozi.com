/**
 * Read a cookie by name (used for CSRF token).
 */
function getCookie(name) {
  const m = document.cookie.match(new RegExp("(^| )" + name + "=([^;]+)"));
  return m ? decodeURIComponent(m[2]) : "";
}

/**
 * Lightweight wrapper over fetch() for JSON APIs.
 * - Adds CSRF token automatically for non-GET requests
 * - Throws Error with a human-readable message on non-2xx
 */
async function apiFetch(url, { method = "GET", body = null } = {}) {
  const headers = { "Content-Type": "application/json" };
  if (method !== "GET") headers["X-CSRFToken"] = getCookie("csrftoken");

  const res = await fetch(url, {
    method,
    headers,
    body: body ? JSON.stringify(body) : null,
  });

  let data = null;
  try {
    data = await res.json();
  } catch {
    data = null;
  }

  if (!res.ok) {
    const msg = data && data.error ? data.error : "Server request failed";
    throw new Error(msg);
  }
  return data;
}

/**
 * Basic HTML escape to prevent injection when rendering strings into innerHTML.
 */
function esc(s) {
  return (s ?? "")
    .toString()
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

document.addEventListener("DOMContentLoaded", () => {
  const track = document.getElementById("latestOrdersTrack");
  if (!track) return;

  const wrap = track.closest(".orders-slider");
  const prev = wrap.querySelector(".slide-btn.prev");
  const next = wrap.querySelector(".slide-btn.next");

  const getStep = () => {
    const first = track.querySelector(".slide");
    if (!first) return 320;
    const gap = 12;
    return first.getBoundingClientRect().width + gap;
  };

  const updateButtons = () => {
    const maxScroll = track.scrollWidth - track.clientWidth;
    const x = track.scrollLeft;
    const canScroll = track.scrollWidth > track.clientWidth + 2;

    prev.disabled = !canScroll || x <= 2;
    next.disabled = !canScroll || x >= maxScroll - 2;
  };

  prev.addEventListener("click", () => track.scrollBy({ left: -getStep(), behavior: "smooth" }));
  next.addEventListener("click", () => track.scrollBy({ left:  getStep(), behavior: "smooth" }));

  track.addEventListener("scroll", updateButtons);
  window.addEventListener("resize", updateButtons);

  updateButtons();
});


// responsive menu
document.addEventListener('DOMContentLoaded', function() {
  
  const darkOverlay = document.querySelector('.dark');
  const mainMenu = document.querySelector('.mobile-slide_menu:not(.mobile-slide_account)');
  const accountMenu = document.querySelector('.mobile-slide_account');
  const menuButtons = document.querySelectorAll('.mobile-menu');
  
  // پیدا کردن دکمه‌های منو بر اساس آیکون
  let mainMenuBtn, accountMenuBtn;
  menuButtons.forEach(btn => {
    if (btn.querySelector('.bi-list')) {
      mainMenuBtn = btn;
    } else if (btn.querySelector('.bi-person')) {
      accountMenuBtn = btn;
    }
  });

  // تابع بستن همه منوها
  function closeAllMenus() {
    mainMenu.classList.remove('active');
    accountMenu.classList.remove('active');
    darkOverlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  // تابع باز کردن منو
  function openMenu(menu) {
    closeAllMenus();
    menu.classList.add('active');
    darkOverlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  // کلیک روی دکمه منوی اصلی
  if (mainMenuBtn) {
    mainMenuBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      if (mainMenu.classList.contains('active')) {
        closeAllMenus();
      } else {
        openMenu(mainMenu);
      }
    });
  }

  // کلیک روی دکمه منوی حساب کاربری
  if (accountMenuBtn) {
    accountMenuBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      if (accountMenu.classList.contains('active')) {
        closeAllMenus();
      } else {
        openMenu(accountMenu);
      }
    });
  }

  // کلیک روی dark overlay
  darkOverlay.addEventListener('click', closeAllMenus);

  // جلوگیری از بسته شدن منو هنگام کلیک روی خود منو
  mainMenu.addEventListener('click', function(e) {
    e.stopPropagation();
  });

  accountMenu.addEventListener('click', function(e) {
    e.stopPropagation();
  });

  // کلیک در هر جای صفحه
  document.addEventListener('click', function(e) {
    if (!mainMenu.contains(e.target) && !accountMenu.contains(e.target)) {
      closeAllMenus();
    }
  });
});
