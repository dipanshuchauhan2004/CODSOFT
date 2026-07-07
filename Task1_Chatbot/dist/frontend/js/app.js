const input = document.getElementById("userInput");

const sendBtn = document.getElementById("sendBtn");

const clearBtn = document.getElementById("clearBtn");

async function sendMessage() {

    const message = input.value.trim();

    if (message === "")
        return;

    addMessage("user", message);

    input.value = "";

    showTyping();

    const reply = await sendToBot(message);

    hideTyping();

    addMessage("bot", reply);

}

sendBtn.addEventListener("click", sendMessage);

input.addEventListener("keypress", function (event) {

    if (event.key === "Enter") {

        sendMessage();

    }

});

clearBtn.addEventListener("click", () => {

    clearChat();

    addMessage(
        "bot",
        "Hello 👋<br><br>How can I help you today?"
    );

});