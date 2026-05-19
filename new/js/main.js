(function () {
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
      { passive: true }
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
    document.querySelectorAll(".nav-item--has-submenu.is-open").forEach(function (openItem) {
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
    document.querySelectorAll(".nav-item--has-submenu.is-open").forEach(function (openItem) {
      openItem.classList.remove("is-open");
      const toggleBtn = openItem.querySelector(".nav-submenu-toggle");
      if (toggleBtn) {
        toggleBtn.setAttribute("aria-expanded", "false");
        toggleBtn.focus();
      }
    });
  });

  const CONTACT_EMAIL = "avinashds@yahoo.com";

  function showContactThanks(form) {
    const status = form.querySelector("#response") || form.querySelector(".contact-form__status");
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
          message
      );
      window.location.href = "mailto:" + CONTACT_EMAIL + "?subject=" + subject + "&body=" + body;
      showContactThanks(form);
    });
  });
})();
