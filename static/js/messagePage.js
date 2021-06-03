function appendMessage(username, message) {
    const messagesArea = document.querySelector("#message-board")
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
    const messageArea = document.querySelector("#message-board")
    messageArea.scrollTop = messageArea.scrollHeight
    storeMessage(userId, message)
    textarea.value = ""
}

function storeMessage(userId, message) {
    const port = window.location.port == "" ? "": ":" + window.location.port
    const url = "http://" + window.location.hostname + port + "/messages"
    fetch(url, {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"userId": userId, "message": message})
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`)
        }
        return response.json()
    })
    .then((json) => {
        console.log(json)
    })
    .catch( (err) => console.log(err))
}

function getHistoryMessages() {
    const port = window.location.port == "" ? "": ":" + window.location.port
    const url = "http://" + window.location.hostname + port + "/messages"
    fetch(url, {
        method: "GET"
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`)
        }
        return response.json()  
    })
    .then((json) => {
        let userMessagesArray = json['userMessages']
        let numberOfMessage = userMessagesArray.length
        for (var i=0; i<numberOfMessage; i++) {
            let username = userMessagesArray[i]["username"]
            let userMessage = userMessagesArray[i]["message"]
            appendMessage(username, userMessage)
        }
    })
    .catch( (err) => console.log(err))
}

function logOut() {
    const port = window.location.port == "" ? "": ":" + window.location.port
    const url = "http://" + window.location.hostname + port + "/logout"
    window.location.replace = url;
}

// append history messages to the message board
getHistoryMessages()