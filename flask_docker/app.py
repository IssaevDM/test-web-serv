import flask
import uuid

app = flask.Flask(__name__)

@app.route("/")
def index():
    return str(f"our unique ID:{uuid.uuid4()}")

@socket_.on('connect')
def test_connect():
    app.logger.critical("Connection message")
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response', {'data': 'Connected\n', 'count': session['receive_count']})

@socket_.on('my_event')
def test_message(message):
    app.logger.critical("my_event message")
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
        {'data': message['data'], 'count': session['receive_count']})
    if thread_lock.acquire(blocking=False):
        set_connection_config()
        thread =  Messenger(socket=socket_, credentials=app.config['pg_conn_params'], topics=[app.config['KAFKA_TOPIC']], servers=app.config['KAFKA_BOOTSTRAP_SERVERS'])
        thread.start()



@socket_.on('my_broadcast_event')
def test_broadcast_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
        {'data': message['data'], 'count': session['receive_count']},
        broadcast=True)


@socket_.on('disconnect_request')
def disconnect_request():
    app.logger.critical("Disconnect message")
    @copy_current_request_context
    def can_disconnect():
        disconnect()

    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
        {'data': 'Disconnected!', 'count': session['receive_count']},
        callback=can_disconnect)

if __name__ == "__main__":
    app.run()
