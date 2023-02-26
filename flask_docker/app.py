import flask
import uuid

app = flask.Flask(__name__)

@app.route("/")
def index():
    return str(uuid.uuid4())

@socket_.on('connect')
def test_connect():
    app.logger.critical("Connection message")
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response', {'data': 'Connected\n', 'count': session['receive_count']})

if __name__ == "__main__":
    app.run()
