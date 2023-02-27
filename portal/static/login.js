const inputs = document.querySelectorAll(".input-field");
const toggle_btn = document.querySelectorAll(".toggle");
const main = document.querySelector("main");
// const bullets = document.querySelectorAll(".bullets span");
// const images = document.querySelectorAll(".image");

inputs.forEach((inp) => {
  inp.addEventListener("focus", () => {
    inp.classList.add("active");
  });
  inp.addEventListener("blur", () => {
    if (inp.value != "") return;
    inp.classList.remove("active");
  });
});

toggle_btn.forEach((btn) => {
  btn.addEventListener("click", () => {
    main.classList.toggle("sign-up-mode");
  });
});

// function moveSlider() {
//   let index = this.dataset.value;

//   let currentImage = document.querySelector(`.img-${index}`);
//   images.forEach((img) => img.classList.remove("show"));
//   currentImage.classList.add("show");

//   const textSlider = document.querySelector(".text-group");
//   textSlider.style.transform = `translateY(${-(index - 1) * 2.2}rem)`;

//   bullets.forEach((bull) => bull.classList.remove("active"));
//   this.classList.add("active");
// }

// bullets.forEach((bullet) => {
//   bullet.addEventListener("click", moveSlider);
// });

var password = document.getElementById("password")
  , confirm_password = document.getElementById("confirm_password");

function validatePassword() {
  if (password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Passwords Don't Match");
  } else {
    confirm_password.setCustomValidity('');
  }
}

password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;

const deg = 6;
const hr = document.querySelector("#hr");
const mn = document.querySelector("#mn");
const sc = document.querySelector("#sc");
setInterval(() => {
  let day = new Date();
  let hh = day.getHours() * 30;
  let mm = day.getMinutes() * deg;
  let ss = day.getSeconds() * deg;
  hr.style.transform = `rotateZ(${hh + (mm / 12)}deg)`;
  mn.style.transform = `rotateZ(${mm}deg)`;
  sc.style.transform = `rotateZ(${ss}deg)`;

})
