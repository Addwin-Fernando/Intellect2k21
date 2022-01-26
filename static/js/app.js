const navbar = document.getElementById("nav");
const topic = document.getElementById("heading");
const navList = document.querySelectorAll(".list");

window.addEventListener("scroll", function(){
    const scrollHeight = window.pageYOffset;
    const navHeight = navbar.getBoundingClientRect().height;
    if(scrollHeight > navHeight){
        navbar.classList.add('nav-disp');
        navbar.classList.add('shadow');
        topic.classList.add('heading');
        navList.forEach(function(e){
            e.classList.add("heading")
        })
    }
    else{
        navbar.classList.remove('nav-disp');
        navbar.classList.remove('shadow');
        topic.classList.remove('heading');
        navList.forEach(function(e){
            e.classList.remove("heading")
        })
    }
    
})

// function sendEmail() {
//     const mail = 'mailto:intellect2k21@gmail.com';
//     const a = document.createElement('a');
//     a.href = mail;
//     a.click();
// };