import re
from responses import responses
from patterns import patterns
from datetime import datetime


def get_bot_response(user_input):

    message = user_input.lower().strip()

    # Calculator
    if re.match(r'^\d+\s*[\+\-\*\/]\s*\d+$', message):
        try:
            return f"Answer = {eval(message)}"
        except:
            return "Invalid expression."

    # Dynamic Time
    if "time" in message:
        return datetime.now().strftime("Current Time: %I:%M %p")

    # Dynamic Date
    if "date" in message:
        return datetime.now().strftime("Today's Date: %d-%m-%Y")

    # Pattern Matching
    for intent, regex_list in patterns.items():
        for pattern in regex_list:
            if re.search(pattern, message):
                return responses[intent]

    return responses["unknown"]