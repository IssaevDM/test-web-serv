import flask
import uuid

app = flask.Flask(__name__)

@app.route("/")
def index():
    return str(uuid.uuid4())

if __name__ == "__main__":
    app.run()
