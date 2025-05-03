/* ----- NAVIGATION BAR FUNCTION ----- */
function myMenuFunction() {
  var menuBtn = document.getElementById("myNavMenu");
  menuBtn.className = menuBtn.className === "nav-menu" ? "nav-menu responsive" : "nav-menu";
}

/* ----- DARK MODE TOGGLE ----- */
const themeButton = document.getElementById('theme-button');
const darkTheme = 'dark';
const lightTheme = 'light';

function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme') === darkTheme ? lightTheme : darkTheme;
  document.documentElement.setAttribute('data-theme', currentTheme);
  themeButton.className = `uil uil-${currentTheme === darkTheme ? 'sun' : 'moon'}`;
  localStorage.setItem('theme', currentTheme);
}

// Load saved theme
const savedTheme = localStorage.getItem('theme') || lightTheme;
document.documentElement.setAttribute('data-theme', savedTheme);
themeButton.className = `uil uil-${savedTheme === darkTheme ? 'sun' : 'moon'}`;

// Toggle theme on click
themeButton.addEventListener('click', toggleTheme);

/* ----- HANDLE NAV LINK CLICKS ----- */
document.querySelectorAll('.nav-link').forEach(function(link) {
  link.addEventListener('click', function() {
      var menu = document.getElementById("myNavMenu");
      if (menu.classList.contains("responsive")) {
          menu.className = "nav-menu";
      }
  });
});

/* ----- ADD SHADOW ON NAVIGATION BAR WHILE SCROLLING ----- */
window.onscroll = function() { headerShadow(); };

function headerShadow() {
  const navHeader = document.getElementById("header");
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
      navHeader.style.boxShadow = "0 1px 6px rgba(0, 0, 0, 0.1)";
      navHeader.style.height = "70px";
      navHeader.style.lineHeight = "70px";
  } else {
      navHeader.style.boxShadow = "none";
      navHeader.style.height = "90px";
      navHeader.style.lineHeight = "90px";
  }
}

/* ----- SCROLL REVEAL ANIMATION ----- */
const sr = ScrollReveal({
  origin: 'top',
  distance: '80px',
  duration: 2000,
  reset: true
});

/* -- HOME -- */
sr.reveal('.featured-text-card', {});
sr.reveal('.featured-name', { delay: 100 });
sr.reveal('.featured-text-info', { delay: 200 });
sr.reveal('.featured-text-btn', { delay: 200 });
sr.reveal('.social_icons', { delay: 200 });
sr.reveal('.featured-image', { delay: 300 });

/* -- PROJECT BOX -- */
sr.reveal('.project-box', { interval: 200 });

/* -- CERTIFICATION CARD -- */
sr.reveal('.certification-card', { interval: 200 });

/* -- HEADINGS -- */
sr.reveal('.top-header', {});

/* -- ABOUT INFO & CONTACT INFO -- */
const srLeft = ScrollReveal({
  origin: 'left',
  distance: '80px',
  duration: 2000,
  reset: true
});

srLeft.reveal('.about-info', { delay: 100 });
srLeft.reveal('.contact-info', { delay: 100 });

/* -- SKILLS & FORM BOX -- */
const srRight = ScrollReveal({
  origin: 'right',
  distance: '80px',
  duration: 2000,
  reset: true
});

srRight.reveal('.skills-gallery', { delay: 100 });
srRight.reveal('.form-control', { delay: 100 });

/* ----- CHANGE ACTIVE LINK ----- */
const sections = document.querySelectorAll('section[id]');

function scrollActive() {
  const scrollY = window.scrollY;
  sections.forEach(current => {
      const sectionHeight = current.offsetHeight,
            sectionTop = current.offsetTop - 50,
            sectionId = current.getAttribute('id');
      const navLink = document.querySelector('.nav-menu a[href*="' + sectionId + '"]');
      if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
          navLink.classList.add('active-link');
      } else {
          navLink.classList.remove('active-link');
      }
  });
}

window.addEventListener('scroll', scrollActive);