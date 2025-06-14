const navBtn = document.querySelector('.nav-btn'),
  navContent = document.querySelector('.nav-content')

// navBtn.addEventListener('click', () => {
//   navContent.classList.toggle('left-[0px]')
//   navContent.classList.toggle('opacity-100')
// })

document.addEventListener('DOMContentLoaded', function () {
  let navbar = document.getElementById('navbar');
  let logoWhite = document.getElementById('logo-white');
  let logoBlack = document.getElementById('logo');

  // Listen for the scroll event
  window.addEventListener('scroll', function () {
    // Check if the scroll position is greater than 0
    if (window.scrollY > 1) {
      logoWhite.classList.remove('hidden');
      logoBlack.classList.add('hidden');
      navbar.classList.remove('bg-black/30')
      navbar.classList.add('bg-[#2D2D2D]')
    } else {
      logoBlack.classList.remove('hidden');
      logoWhite.classList.add('hidden');
      navbar.classList.remove('bg-[#2D2D2D]')
      navbar.classList.add('bg-black/30')
    }
  });
});


// Swiper

// let swiper = new Swiper(".mySwiper", {
//   spaceBetween: 30,
//   centeredSlides: true,
//   preventInteractionOnTransition: true,
//   loop: true,
//   speed: 25000,
//   autoplay: {
//     delay: 0,
//     disableOnInteraction: true,
//   },
// });

let swiperAbout = new Swiper(".aboutSwiper", {
  slidesPerView: 2,
  spaceBetween: 30,
  loop: true,
  breakpoints: {
    768:{
     slidesPerView: 4,
    }
  },
  autoplay: {
    delay: 3000, // Set the delay in milliseconds (e.g., 5000 for 5 seconds)
    disableOnInteraction: false, // Allow navigation while autoplay is active
  },
});



// function startMarquee() {
//   const container = document.getElementById("marqueeContainer");
//   const content = document.getElementById("marqueeContent");
//
//   const containerWidth = container.clientWidth;
//   const contentWidth = content.clientWidth;
//
//   let position = 0;
//
//   function move() {
//     position--;
//     if (position < -containerWidth) {
//       position = containerWidth;
//     }
//     content.style.transform = `translateX(${position}px)`;
//     requestAnimationFrame(move);
//   }
//
//   move();
// }
//
//
// document.addEventListener("DOMContentLoaded", startMarquee);



// awards 

// function animateValue(obj, start, end, duration) {
//   let startTimestamp = null;
//   const step = (timestamp) => {
//     if (!startTimestamp) startTimestamp = timestamp;
//     const progress = Math.min((timestamp - startTimestamp) / duration, 1);
//     obj.innerHTML = Math.floor(progress * (end - start) + start);
//     if (progress < 1) {
//       window.requestAnimationFrame(step);
//     }
//   };
//   window.requestAnimationFrame(step);
// }

// const obj1 = document.getElementById("value-1");
// const obj2 = document.getElementById("value-2");
// const obj3 = document.getElementById("value-3");
// const obj4 = document.getElementById("value-4");
// animateValue(obj1, 0, 14, 1000);
// animateValue(obj2, 0, 2500, 2500);
// animateValue(obj3, 0, 225, 2000);
// animateValue(obj4, 0, 120, 1500);

new PureCounter();

// lang
const langBtn = document.querySelector('.lang-btn'),
    langMenu = document.querySelector('.lang-menu')

langBtn.addEventListener('click' , (e) => {
    e.stopImmediatePropagation()
    langMenu.classList.toggle('grid-rows-[1fr]')
})
window.addEventListener('click', e => {
    if (e.target !== langBtn) {
        langMenu.classList.remove('grid-rows-[1fr]')
    }
})


// modal product-inner
window.addEventListener("DOMContentLoaded",()=>{
    const modal = document.querySelector("#modal");
    const btnModal = document.querySelector("#button");
    const btnModalClose = document.querySelector("#buttonForm");
    
    btnModal.addEventListener("click",()=>{
        if(modal.classList.contains('scale-0')){
            modal.classList.remove("scale-0");
        }
    })
    
    window.addEventListener("click",(e)=>{
        let target = e.target
        if(target.tagName == "FORM"){
            modal.classList.add('scale-1');
        }else if(target == modal){
            modal.classList.add('scale-0')
            modal.classList.remove("scale-1")
        }
    })
    btnModalClose.addEventListener('click',()=>{
        modal.classList.add("scale-0");
        modal.classList.remove("scale-1")
    })
})