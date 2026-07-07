const chatBox = document.getElementById("chatBox");
const typing = document.getElementById("typing");

function getCurrentTime() {

    const now = new Date();

    return now.toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });

}

function addMessage(sender, message) {

    const wrapper = document.createElement("div");

    wrapper.className = `message ${sender}`;

    const avatar = sender === "user" ? "👤" : "🤖";

    wrapper.innerHTML = `

        <div class="avatar">${avatar}</div>

        <div class="bubble">

            <h4>${sender === "user" ? "You" : "AI Assistant"}</h4>

            <p>${message}</p>

            <span class="time">${getCurrentTime()}</span>

        </div>

    `;

    chatBox.appendChild(wrapper);

    chatBox.scrollTop = chatBox.scrollHeight;

}

function showTyping() {

    typing.classList.remove("hidden");

}

function hideTyping() {

    typing.classList.add("hidden");

}

function clearChat() {

    chatBox.innerHTML = "";

}