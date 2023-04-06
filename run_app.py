from flask_docker import app, socket_

if __name__ == "__main__":
    socket_.init_app(app, cors_allowed_origins='*')
    socket_.run(app, host = "0.0.0.0", port = 8080, debug=True, allow_unsafe_werkzeug=True)

#    ws://localhost:80/socket.io/?EIO=4&transport=websocket