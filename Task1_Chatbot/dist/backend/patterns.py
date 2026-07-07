patterns = {

    # Greetings
    "greeting": [
        r"\bhi\b",
        r"\bhello\b",
        r"\bhey\b",
        r"\bgood morning\b",
        r"\bgood afternoon\b",
        r"\bgood evening\b"
    ],

    "how_are_you": [
        r"how are you",
        r"how are u"
    ],

    "name": [
        r"your name",
        r"who are you"
    ],

    "bye": [
        r"\bbye\b",
        r"\bgoodbye\b",
        r"\bsee you\b"
    ],

    # Programming Languages
    "python": [r"\bpython\b"],
    "java": [r"\bjava\b"],
    "cpp": [r"c\+\+", r"\bcpp\b"],
    "c": [r"\bc language\b", r"\bc programming\b"],
    "javascript": [r"javascript", r"\bjs\b"],
    "html": [r"\bhtml\b"],
    "css": [r"\bcss\b"],
    "sql": [r"\bsql\b"],

    # Computer Science
    "dbms": [r"\bdbms\b"],
    "os": [r"operating system", r"\bos\b"],
    "network": [r"computer network", r"\bnetwork\b"],
    "datastructure": [r"data structure"],
    "algorithm": [r"algorithm"],
    "oop": [r"oop", r"object oriented"],
    "compiler": [r"compiler"],

    # AI
    "ai": [r"\bai\b", r"artificial intelligence"],
    "ml": [r"machine learning"],
    "dl": [r"deep learning"],
    "nlp": [r"natural language processing", r"\bnlp\b"],
    "cv": [r"computer vision"],
    "chatgpt": [r"chatgpt"],
    "genai": [r"generative ai"],

    # Web
    "frontend": [r"frontend"],
    "backend": [r"backend"],
    "fullstack": [r"full stack"],
    "flask": [r"flask"],
    "django": [r"django"],
    "react": [r"react"],
    "node": [r"node"],

    # College
    "mca": [r"\bmca\b"],
    "bca": [r"\bbca\b"],
    "project": [r"project"],

    # Fun
    "joke": [r"joke"],
    "fact": [r"fact"],
    "motivation": [r"motivate", r"motivation", r"quote"],

    # Date & Time
    "time": [r"time"],
    "date": [r"date"],

    # Calculator
    "math": [
        r"^\d+\s*[\+\-\*\/]\s*\d+$"
    ]
}