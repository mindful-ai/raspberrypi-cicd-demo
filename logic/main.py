from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return jsonify(message="Hello from Flask CI/CD")

    return app

    @app.route("/status")
    def status():
        return jsonify(status="OK", environment="raspberry-pi")