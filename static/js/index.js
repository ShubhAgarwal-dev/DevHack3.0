const popsignup = document.querySelector(".signupform")
const btn2 = document.querySelector(".section .btn2")
const btn3 = document.querySelector(".signupform .btn3")

console.log(btn2)
console.log(popsignup)

btn2.addEventListener("click", ()=>{
    popsignup.style.display = "block";
})
btn3.addEventListener("click", ()=>{
    popsignup.style.display = "none";
})