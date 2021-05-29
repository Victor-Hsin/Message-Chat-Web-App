function appendMessage(username, message) {
    let messagesArea = document.querySelector("#messages-area")
    messagesArea.innerHTML += `<div class="chat-message">` +
                                `<span style="color: #f7a628;">${username}</span><br>` + 
                                `<span style="color: #9E9E9E;">${message}</span>`  +
                              `</div>`
}


function postAndStoreMessage(username, userId) {
    const textarea = document.querySelector("#input-message")
    const message = textarea.value 

    appendMessage(username, message)
    // make sure the scroll stop at the bottom which includes the latest message
    const messageArea = document.querySelector("#messages-area")
    messageArea.scrollTop = messageArea.scrollHeight
    storeMessage(userId, message)
    textarea.value = ""
}

function storeMessage(userId, message) {

}
