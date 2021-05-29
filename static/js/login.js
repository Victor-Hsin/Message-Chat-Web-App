const userName = document.querySelector("#username")
const password = document.querySelector("#password")
const loginBtn = document.querySelector("#loginBtn")
const registerBtn = document.querySelector("#registerBtn")
const msg = document.querySelector("#msg")
const msgText = msg.innerHTML

// check msg variable, and change the text to corresponding color.
if (msgText == "Sign up sucessfully! Please enter the username and password again to log in.") {
    msg.setAttribute("style", "color: green;")
} else {
    msg.setAttribute("style", "color: red;")
}




