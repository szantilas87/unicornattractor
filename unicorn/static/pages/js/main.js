//Reveal animations

window.sr = ScrollReveal();
sr.reveal('.navbar', {
    duration: 2000,
    origin: 'bottom',
    distance: '30px',
    easing: 'ease-in-out',

});
sr.reveal('.showcase-left', {
    duration: 2000,
    origin: 'top',
    distance: '300px'
});
sr.reveal('.showcase-right', {
    duration: 2000,
    origin: 'right',
    distance: '300px'
});
sr.reveal('.showcase-btn', {
    duration: 2000,
    delay: 1000,
    origin: 'bottom',
    distance: '30px'

});
sr.reveal('#testimonial div', {
    duration: 2000,
    origin: 'bottom',

});
sr.reveal('.info-left', {
    duration: 2000,
    origin: 'left',
    distance: '300px',
    viewFactor: 0.2,
    delay: 1000,
});
sr.reveal('.info-right', {
    duration: 2000,
    origin: 'right',
    distance: '300px',
    viewFactor: 0.2,
    delay: 1000,
});
sr.reveal('.customer1', {
    duration: 2000,
    origin: 'left',
    distance: '300px',
    viewFactor: 0.2,
    delay: 2000,
});
sr.reveal('.customer2', {
    duration: 2000,
    origin: 'top',
    distance: '300px',
    viewFactor: 0.2,
    delay: 2000,
});
sr.reveal('.customer3', {
    duration: 2000,
    origin: 'bottom',
    distance: '300px',
    viewFactor: 0.2,
    delay: 2000,
});
sr.reveal('.customer4', {
    duration: 2000,
    origin: 'right',
    distance: '300px',
    viewFactor: 0.2,
    delay: 2000,
});




// Smooth scroll on main page

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});