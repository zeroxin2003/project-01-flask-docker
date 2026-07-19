from flask import Flask, jsonify
import socket
import platform

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <html>
    <head><title>My First DevOps Project</title></head>
    <body style="font-family: Arial; max-width: 600px; margin: 80px auto; text-align: center;">
        <h1>🚀 It works!</h1>
        <p>This website is running inside a <strong>Docker container</strong>.</p>
        <hr>
        <p><strong>Hostname:</strong> {socket.gethostname()}</p>
        <p><strong>Platform:</strong> {platform.system()} {platform.release()}</p>
        <p><strong>Python:</strong> {platform.python_version()}</p>
        <hr>
        <p style="color: gray;">Project 01 — Flask + Docker</p>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "ok", "hostname": socket.gethostname()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
