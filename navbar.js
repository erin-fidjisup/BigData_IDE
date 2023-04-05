const burgerMenu = document.querySelector('.burger-menu');
const menuLinks = document.querySelector('.menu-links');

burgerMenu.addEventListener('click', () => {
  menuLinks.classList.toggle('active');
});
