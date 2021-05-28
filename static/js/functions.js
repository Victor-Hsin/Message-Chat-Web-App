const userName = document.querySelector("#username")
const password = document.querySelector("#password")
const loginBtn = document.querySelector("#loginBtn")
const registerBtn = document.querySelector("#registerBtn")
const form = document.querySelector("#userInfo-form")
const msg = document.querySelector("#msg")
const msgText = msg.innerHTML

// check msg variable, and change the text to corresponding color.
if (msgText == "Sign up sucessfully! Please enter the username and password again to log in.") {
    msg.setAttribute("style", "color: green;")
} else {
    msg.setAttribute("style", "color: red;")
}
// if (msgText === "Incorrect username or password. Please try again.") {
//     msg.setAttribute("style", "color: red;")
// } else if (msgText === "Sign up sucessfully! Please click the LOGIN button to log in.") {
//     msg.setAttribute("style", "color: green;")
// }

function signUpNewAccount(){
    // to-do: fetch flask API to register and login the user
    console.log("logged out")
}




