const popsignup = document.querySelector(".signupform")
const btn2 = document.querySelector(".section .btn2")
const btn3 = document.querySelector(".signupform .btn3")
const body = document.querySelector("body");
const section = document.querySelector(".section")
const footer = document.querySelector(".footer")

console.log(btn2)
console.log(popsignup)

btn2.addEventListener("click", ()=>{
    popsignup.style.display = "block";
    section.style.opacity = "0.4"
    footer.style.opacity = "0.4"

    
})
btn3.addEventListener("click", ()=>{
    popsignup.style.display = "none";
    section.style.opacity = "1"
    footer.style.opacity = "1"
})