import flask

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    who = flask.request.args.get("who", "World")
    return f"hello {who}\n"

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)