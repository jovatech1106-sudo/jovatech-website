document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener("click", function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute("href"));
        if (target) {
            target.scrollIntoView({
                behavior: "smooth"
            });
        }
    });
});

const topBtn = document.getElementById("topBtn");
window.onscroll = function () {
    if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
        topBtn.style.display = "block";
    } else {
        topBtn.style.display = "none";
    }
};
topBtn.addEventListener("click", function () {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});

// ==========================
// SCROLL REVEAL ANIMATION
// ==========================
const reveals = document.querySelectorAll(".reveal");
function revealSections() {
    reveals.forEach(section => {
        const windowHeight = window.innerHeight;
        const revealTop = section.getBoundingClientRect().top;
        const revealPoint = 120;
        if (revealTop < windowHeight - revealPoint) {
            section.classList.add("active");
        }
    });
}
window.addEventListener("scroll", revealSections);
revealSections();

// ==========================
// ANIMATED COUNTER
// ==========================
const counters = document.querySelectorAll(".counter");
counters.forEach(counter => {
    counter.innerText = "0";
    const updateCounter = () => {
        const target = +counter.getAttribute("data-target");
        const current = +counter.innerText;
        const increment = Math.ceil(target / 100);
        if(current < target){
            counter.innerText = current + increment;
            setTimeout(updateCounter,20);
        }else{
            counter.innerText = target;
        }
    };
    updateCounter();
});

// ==========================
// TYPING EFFECT
// ==========================
const text = "Welcome to JOVATECH COMPUTER TECHNOLOGIES";
const typing = document.getElementById("typing");
if (typing) {
    let index = 0;
    function typeWriter() {
        if (index < text.length) {
            typing.innerHTML += text.charAt(index);
            index++;
            setTimeout(typeWriter, 80);
        }
    }
    typeWriter();
}

// ==========================
// HERO IMAGE SLIDER
// ==========================
const hero = document.querySelector(".hero");
if (hero) {
    const images = [
        "/static/images/hero.png",
        "/static/images/laptop-service.jpg",
        "/static/images/phone-service.jpg",
        "/static/images/python-development.jpg",
	"/static/system-administration.jpg",
	"/static/images/training.jpg",
	"/static/images/web-development.jpg"
    ];
    let current = 0;
    setInterval(() => {
        current++;
        if (current >= images.length) {
            current = 0;
        }
        hero.style.backgroundImage =
        `linear-gradient(rgba(0,0,0,.6), rgba(0,0,0,.6)), url('${images[current]}')`;
    }, 5000);
}