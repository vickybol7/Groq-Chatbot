from flask import Flask, jsonify
import socket

app = Flask(__name__)

HOST = '127.0.0.1'  # Use '127.0.0.1' if Flask is on the same machine
PORT = 8080         # Port your socket server is listening on

def is_server_online():
    try:
        with socket.create_connection((HOST, PORT), timeout=1):
            return True
    except (ConnectionRefusedError, socket.timeout, OSError):
        return False

@app.route('/', methods=['GET'])
def check_server_status():
    status = is_server_online()
    return jsonify({"server_online": status})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

