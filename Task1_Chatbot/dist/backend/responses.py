from datetime import datetime

responses = {

    "greeting":"Hello 👋 Welcome! How can I help you today?",

    "how_are_you":"I'm doing great! Thanks for asking 😊",

    "name":"I'm an AI Rule-Based Chatbot developed in Python.",

    "bye":"Goodbye! Have a wonderful day.",

    "python":"Python is a high-level programming language used in AI, Machine Learning, Web Development and Data Science.",

    "java":"Java is an object-oriented language widely used for enterprise software and Android development.",

    "cpp":"C++ is a powerful object-oriented language used in game development and system programming.",

    "c":"C is a procedural programming language and the foundation of many modern languages.",

    "javascript":"JavaScript is the scripting language used to create interactive web pages.",

    "html":"HTML is the standard markup language used to create web pages.",

    "css":"CSS is used to style HTML webpages.",

    "sql":"SQL is used to store, retrieve and manage data in databases.",

    "dbms":"DBMS stands for Database Management System.",

    "os":"An Operating System manages computer hardware and software resources.",

    "network":"Computer Networking connects multiple computers to share data.",

    "datastructure":"A Data Structure organizes data efficiently.",

    "algorithm":"An Algorithm is a step-by-step procedure to solve a problem.",

    "oop":"OOP stands for Object-Oriented Programming.",

    "compiler":"A Compiler converts source code into machine code.",

    "ai":"Artificial Intelligence enables machines to simulate human intelligence.",

    "ml":"Machine Learning is a subset of AI that learns from data.",

    "dl":"Deep Learning uses neural networks with multiple layers.",

    "nlp":"Natural Language Processing allows computers to understand human language.",

    "cv":"Computer Vision enables computers to understand images and videos.",

    "chatgpt":"ChatGPT is an AI chatbot developed by OpenAI.",

    "genai":"Generative AI creates text, images, music and more.",

    "frontend":"Frontend is the user interface of a website.",

    "backend":"Backend handles server-side logic and databases.",

    "fullstack":"A Full Stack Developer works on both frontend and backend.",

    "flask":"Flask is a lightweight Python web framework.",

    "django":"Django is a powerful Python web framework.",

    "react":"React is a JavaScript library for building user interfaces.",

    "node":"Node.js allows JavaScript to run outside the browser.",

    "mca":"MCA stands for Master of Computer Applications.",

    "bca":"BCA stands for Bachelor of Computer Applications.",

    "project":"This Rule-Based Chatbot is developed using HTML, CSS, JavaScript and Python with Regex Pattern Matching.",

    "joke":"Why do programmers prefer dark mode? Because light attracts bugs! 😄",

    "fact":"Did you know? Python was named after Monty Python, not the snake.",

    "motivation":"Success is the sum of small efforts repeated every day.",

    "time":datetime.now().strftime("Current Time: %I:%M %p"),

    "date":datetime.now().strftime("Today's Date: %d-%m-%Y"),

    "unknown":"Sorry, I don't understand that question. Please ask something related to programming, AI, MCA, or computer science."

}