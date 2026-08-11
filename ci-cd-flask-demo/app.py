from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    """Used by CI/CD pipeline and load balancer for post-deploy verification."""
    return jsonify(status="ok"), 200


@app.route("/api/greet/<name>", methods=["GET"])
def greet(name):
    if not name.isalpha():
        return jsonify(error="name must be alphabetic"), 400
    return jsonify(message=f"Helloo, {name}!"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
