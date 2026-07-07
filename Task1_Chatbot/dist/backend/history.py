import json
import os

FILE = "../data/history.json"


def save_chat(user, bot):

    history = []

    if os.path.exists(FILE):

        with open(FILE, "r") as file:

            try:

                history = json.load(file)

            except:

                history = []

    history.append({

        "user": user,

        "bot": bot

    })

    with open(FILE, "w") as file:

        json.dump(history, file, indent=4)