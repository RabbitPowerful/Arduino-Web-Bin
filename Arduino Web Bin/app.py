from flask import Flask, render_template
from flask_socketio import SocketIO
import serial
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app)

serial_data = None
serial_thread = None
SERIAL_PORT = 'COM4'  # Adjust port as needed
BAUD_RATE = 9600

def read_serial():
    global serial_data
    try:
        with serial.Serial(port=SERIAL_PORT, baudrate=BAUD_RATE) as ser:
            while True:
                data = ser.readline().decode().strip()
                serial_data = int(data)  # Assuming the serial data is integer
                socketio.emit('serial_update', serial_data)
                time.sleep(0.1)  # Add a small delay to avoid excessive CPU usage
    except serial.SerialException as e:
        print("Serial Port Error:", e)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    global serial_thread
    if serial_thread is None or not serial_thread.is_alive():
        serial_thread = threading.Thread(target=read_serial)
        serial_thread.start()

if __name__ == '__main__':
    socketio.run(app, debug=True)
