async function sendToBot(message) {

    try {

        const response = await fetch("http://localhost:5000/chat", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                message: message

            })

        });

        const data = await response.json();

        return data.reply;

    }

    catch (error) {

        return "Unable to connect to Python server.";

    }

}