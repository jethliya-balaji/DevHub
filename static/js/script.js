const btn = document.getElementById('hamburger')
const nav = document.getElementById('menu')

btn.addEventListener('click', () => {
    nav.classList.toggle('mobile-menu-bg');
    nav.classList.toggle('mt-4');

    nav.classList.toggle('flex')
    nav.classList.toggle('hidden')
})