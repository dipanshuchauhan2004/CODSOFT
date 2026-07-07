import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from chatbot import get_bot_response

HOST = "localhost"
PORT = 5000


class ChatServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(b"AI Rule-Based Chatbot Server Running")

    def do_POST(self):

        if self.path != "/chat":
            self.send_error(404)
            return

        content_length = int(self.headers["Content-Length"])

        body = self.rfile.read(content_length)

        data = json.loads(body.decode())

        user_message = data.get("message", "")

        bot_reply = get_bot_response(user_message)

        response = {
            "reply": bot_reply
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        self.wfile.write(json.dumps(response).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.end_headers()


if __name__ == "__main__":

    print("=" * 60)
    print(" AI Rule-Based Chatbot Server Running ")
    print("=" * 60)
    print(f"http://{HOST}:{PORT}")
    print("=" * 60)

    server = HTTPServer((HOST, PORT), ChatServer)
    server.serve_forever()