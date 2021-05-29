function appendMessage(userName, message) {
    let messagesArea = document.querySelector("#messages-area")
    messagesArea.innerHTML += `<div class="chat-message">` +
                                `<span style="color: #f7a628;">${userName}</span><br>` + 
                                `<span style="color: #9E9E9E;">${message}</span>`  +
                              `</div>`
}