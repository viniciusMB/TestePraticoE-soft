const hamburger = document.querySelector('.hamburger');
const navLinks =  document.querySelector('.nav-links');
const links = document.querySelectorAll('.nav-links li');
const main = document.querySelector('.main')

var clickCount=2;

hamburger.addEventListener('click', () => {
    clickCount++;
    if (clickCount%2 == 1){
        navLinks.classList.toggle("open");
        main.classList.toggle("open");
    }

    if (clickCount%2 == 0){
        navLinks.classList.toggle("open");
        setTimeout(() => main.classList.toggle("open"), 800);
    }

    
});