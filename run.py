from app import create_app
from app.socketio_config import socketio

app = create_app()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001, debug=True)