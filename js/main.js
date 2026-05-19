const CONTACT_EMAIL = "avinashds@yahoo.com";
const WHATSAPP_NUMBER = "919845224651";

function initHeroCarousel() {
  const root = document.querySelector(".hero-carousel");
  if (!root) {
    return;
  }

  const slides = Array.from(root.querySelectorAll(".hero-carousel__slide"));
  const dots = Array.from(root.querySelectorAll(".hero-carousel__dot"));
  const prev = root.querySelector(".hero-carousel__control--prev");
  const next = root.querySelector(".hero-carousel__control--next");
  const viewport = root.querySelector(".hero-carousel__viewport");

  if (slides.length < 2) {
    return;
  }

  let index = slides.findIndex(function (slide) {
    return slide.classList.contains("is-active");
  });
  if (index < 0) {
    index = 0;
  }

  const reducedMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)",
  ).matches;
  let timer;

  function setSlide(nextIndex) {
    index = (nextIndex + slides.length) % slides.length;
    slides.forEach(function (slide, slideIndex) {
      const active = slideIndex === index;
      slide.classList.toggle("is-active", active);
      slide.setAttribute("aria-hidden", active ? "false" : "true");
    });
    dots.forEach(function (dot, dotIndex) {
      const active = dotIndex === index;
      dot.classList.toggle("is-active", active);
      dot.setAttribute("aria-selected", active ? "true" : "false");
    });
  }

  function goNext() {
    setSlide(index + 1);
  }

  function goPrev() {
    setSlide(index - 1);
  }

  function resetTimer() {
    clearInterval(timer);
    if (!reducedMotion) {
      timer = setInterval(goNext, 6000);
    }
  }

  if (prev) {
    prev.addEventListener("click", function () {
      goPrev();
      resetTimer();
    });
  }

  if (next) {
    next.addEventListener("click", function () {
      goNext();
      resetTimer();
    });
  }

  if (viewport) {
    viewport.addEventListener("keydown", function (event) {
      if (event.key === "ArrowLeft") {
        event.preventDefault();
        goPrev();
        resetTimer();
      } else if (event.key === "ArrowRight") {
        event.preventDefault();
        goNext();
        resetTimer();
      }
    });
  }

  dots.forEach(function (dot) {
    dot.addEventListener("click", function () {
      const target = Number.parseInt(dot.getAttribute("data-slide"), 10);
      if (!Number.isNaN(target)) {
        setSlide(target);
        resetTimer();
      }
    });
  });

  setSlide(index);
  resetTimer();
}

function initPrestoEmbed() {
  if (window.location.href.indexOf("console") !== -1) {
    return;
  }
  if (document.body.classList.contains("page-pay-online")) {
    return;
  }

  const script = document.createElement("script");
  script.src =
    "https://s3-ap-southeast-1.amazonaws.com/staging-websites/presto-shopping/presto_connections.js";
  script.async = true;
  script.onload = function () {
    if (typeof PrestoEmbedManager === "undefined") {
      return;
    }
    PrestoEmbedManager.init({
      controller:
        "https://s3-ap-southeast-1.amazonaws.com/staging-websites/presto-shopping/connections_controller.html",
      configParams: {
        merchant_id: "5cca8fc31e4cd66c8b00209f",
        app_id: "59d4cc24a4d34100046255b6",
        merchant_name: "Fibronet",
        merchant_logo: "",
      },
      shoppingWindowOptions: {
        environment: "production",
        merchantType: "connections",
        currency: "rupee",
      },
    });
  };
  document.body.appendChild(script);
}

function getPlanNameFromCard(card) {
  const tag = card?.querySelector(".plan__tag-num")?.textContent?.trim() || "";
  const speed =
    card?.querySelector(".plan__speed-num")?.textContent?.trim() || "";
  let name = "Fibronet";
  if (tag) {
    name += " " + tag;
  }
  if (speed) {
    name += " (" + speed + " Mbps)";
  }
  return name;
}

function buildPlanEnquiryMessage(planName) {
  return (
    "Hi, I would like to enquire about the following plan:\n\n" +
    "Plan: " +
    planName +
    "\n\nName:\nAddress:\nPhone:\nPreferred billing cycle (30/90/180 days):\n"
  );
}

function openWhatsAppEnquiry(message) {
  const url =
    "https://wa.me/" + WHATSAPP_NUMBER + "?text=" + encodeURIComponent(message);
  window.open(url, "_blank", "noopener,noreferrer");
}

function initPlanChooseButtons() {
  document.querySelectorAll("[data-plan-cta]").forEach(function (button) {
    button.addEventListener("click", function () {
      const card = button.closest(".plan");
      const planName = getPlanNameFromCard(card);
      openWhatsAppEnquiry(buildPlanEnquiryMessage(planName));
    });
  });
}

initHeroCarousel();
// initPrestoEmbed();
initPlanChooseButtons();

const nav = document.querySelector(".site-nav");
const toggle = document.querySelector(".nav-toggle");
if (toggle && nav) {
  function setNavOpen(open) {
    nav.classList.toggle("is-open", open);
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  }

  toggle.addEventListener("click", function () {
    setNavOpen(!nav.classList.contains("is-open"));
  });
  nav.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", function () {
      setNavOpen(false);
    });
  });
}

const header = document.querySelector(".site-header");
if (header) {
  window.addEventListener(
    "scroll",
    function () {
      header.classList.toggle("is-scrolled", window.scrollY > 8);
    },
    { passive: true },
  );
}

document.querySelectorAll(".nav-submenu-toggle").forEach(function (btn) {
  const item = btn.closest(".nav-item--has-submenu");
  if (!item) {
    return;
  }
  if (btn.getAttribute("aria-expanded") === "true") {
    item.classList.add("is-open");
  }
  btn.addEventListener("click", function (event) {
    event.stopPropagation();
    const open = item.classList.toggle("is-open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  });
});

document.addEventListener("click", function () {
  document
    .querySelectorAll(".nav-item--has-submenu.is-open")
    .forEach(function (openItem) {
      openItem.classList.remove("is-open");
      const toggleBtn = openItem.querySelector(".nav-submenu-toggle");
      if (toggleBtn) {
        toggleBtn.setAttribute("aria-expanded", "false");
      }
    });
});

document.addEventListener("keydown", function (event) {
  if (event.key !== "Escape") {
    return;
  }
  document
    .querySelectorAll(".nav-item--has-submenu.is-open")
    .forEach(function (openItem) {
      openItem.classList.remove("is-open");
      const toggleBtn = openItem.querySelector(".nav-submenu-toggle");
      if (toggleBtn) {
        toggleBtn.setAttribute("aria-expanded", "false");
        toggleBtn.focus();
      }
    });
});

function showContactThanks(form) {
  const status =
    form.querySelector("#response") ||
    form.querySelector(".contact-form__status");
  const message =
    "Thank you for contacting us. We shall get back to you at the earliest!";
  if (status) {
    status.hidden = false;
    status.textContent = message;
  } else {
    window.alert(message);
  }
  form.reset();
}

function applyPrestoIframeTransparency(iframe) {
  if (!iframe || iframe.dataset.prestoTransparent === "true") {
    return;
  }
  iframe.setAttribute("allowtransparency", "true");
  iframe.style.background = "transparent";
  iframe.style.backgroundColor = "transparent";
  iframe.dataset.prestoTransparent = "true";
}

function initPrestoIframeTransparency() {
  const selector =
    'iframe[src*="presto"], iframe[src*="connections_controller"], iframe[src*="presto-apps"], iframe[src*="/embed/presto-pay"]';
  document.querySelectorAll(selector).forEach(applyPrestoIframeTransparency);

  const observer = new MutationObserver(function (mutations) {
    mutations.forEach(function (mutation) {
      mutation.addedNodes.forEach(function (node) {
        if (!(node instanceof Element)) {
          return;
        }
        if (node.matches("iframe")) {
          applyPrestoIframeTransparency(node);
        }
        node.querySelectorAll("iframe").forEach(applyPrestoIframeTransparency);
      });
    });
  });
  observer.observe(document.body, { childList: true, subtree: true });
}

initPrestoIframeTransparency();

document.querySelectorAll(".contact-form").forEach(function (form) {
  form.addEventListener("submit", function (event) {
    event.preventDefault();
    const name = form.querySelector("#customerName")?.value.trim() || "";
    const email = form.querySelector("#customerEmail")?.value.trim() || "";
    const phone = form.querySelector("#customerPhone")?.value.trim() || "";
    const message = form.querySelector("#customerMessage")?.value.trim() || "";

    if (!email && !phone) {
      window.alert("Please enter your email or phone no.");
      return;
    }

    const subject = encodeURIComponent("Contact from fibronet.in");
    const body = encodeURIComponent(
      "Name: " +
        name +
        "\nEmail: " +
        email +
        "\nPhone: " +
        phone +
        "\n\n" +
        message,
    );
    window.location.href =
      "mailto:" + CONTACT_EMAIL + "?subject=" + subject + "&body=" + body;
    showContactThanks(form);
  });
});
