/*===== MENU SHOW =====*/ 
const showMenu = (toggleId, navId) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId)

    if(toggle && nav){
        toggle.addEventListener('click', ()=>{
            nav.classList.toggle('show')
        })
    }
}
showMenu('nav-toggle','nav-menu')

/*===== REMOVE MENU MOBILE =====*/
const navLink = document.querySelectorAll('.nav_link')

function linkAction(){
    const navMenu = document.getElementById('nav-menu')
    navMenu.classList.remove('show')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

/*===== SCROLL SECTIONS ACTIVE LINK =====*/
const sections = document.querySelectorAll('section[id]')

if (activePage !== 'blog') {
    console.log(activePage)
    window.addEventListener('scroll', scrollActive)
    
    function scrollActive(){
        const scrollY = window.scrollY
        
        sections.forEach(current =>{
            const sectionHeight = current.offsetHeight
            const sectionTop = current.offsetTop - 50;
            sectionId = current.getAttribute('id')
            
            if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
                document.querySelector('.nav_menu a[href*=' + sectionId + ']').classList.add('active')
            }else{
                document.querySelector('.nav_menu a[href*=' + sectionId + ']').classList.remove('active')
            }
        })
    }
}
    
/*===== SCROLL REVEAL ANIMATION =====*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '80px',
    duration: 2000,
    reset: true
})

/*SCROLL HOME*/
sr.reveal('.home__title', {})
sr.reveal('.home__scroll', {delay: 200})
sr.reveal('.home__img', {origin:'right', delay: 400})

/*SCROLL ABOUT*/
sr.reveal('.about__img', {delay: 500})
sr.reveal('.about__subtitle', {delay: 300})
sr.reveal('.about__profession', {delay: 400})
sr.reveal('.about__text', {delay: 500})
sr.reveal('.about__social-icon', {delay: 600, interval: 200})

/*SCROLL SKILLS*/
sr.reveal('.skills__subtitle', {})
sr.reveal('.skills__name', {distance: '20px', delay: 50, interval: 100})
sr.reveal('.skills__img', {delay: 400})

/*SCROLL PORTFOLIO*/
sr.reveal('.portfolio__img', {interval: 200})

/*SCROLL CONTACT*/
sr.reveal('.contact__subtitle', {})
sr.reveal('.contact__text', {interval: 200})
sr.reveal('.contact__input', {delay: 400})
sr.reveal('.contact__button', {delay: 600})
sr.reveal('.contact__message', {delay:400})

/*SCROLL BLOG*/
sr.reveal('.blog_card', {delay: 200})
sr.reveal('.blog_card_title', {delay: 200})
sr.reveal('.blog_card_details', {delay: 200})
sr.reveal('.blog_card_content', {delay: 200})
sr.reveal('.blog_card_btn', {delay:200})

/*SCROLL posts*/

sr.reveal('.post_details', {delay: 200})
sr.reveal('.post_card', {delay: 200})
sr.reveal('.post_content', {delay: 200})
sr.reveal('.be-comment-block', {delay:200})


if (activePage !== 'blog'){
    document.addEventListener('DOMContentLoaded', function () {
        const form = document.getElementById('contactForm');
    
        // Add event listener for the submit button
        form.addEventListener('submit', function(event) {
    
            // Display alert to the user
            alert('Your message have been sent. Thanks for reaching out :D');
            
            // Optionally, you can process the form data here
        });
    });
}
