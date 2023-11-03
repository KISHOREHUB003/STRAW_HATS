const navLinks = document.querySelectorAll('nav ul li a');

    navLinks.forEach(link => {
      link.addEventListener('click', smoothScroll);
    });

    function smoothScroll(e) {
      e.preventDefault();

      const targetId = e.target.getAttribute('href');
      const targetPosition = document.querySelector(targetId).offsetTop;

      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
      });
    }