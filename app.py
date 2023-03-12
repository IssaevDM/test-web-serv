import flask
import uuid

app = flask.Flask(__name__)

@app.route("/")
def index():
    return str(f"our unique ID:{uuid.uuid4()}")

if __name__ == "__main__":
    app.run()
