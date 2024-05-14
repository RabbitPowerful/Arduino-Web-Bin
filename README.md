Smart Waste Segregator
This project demonstrates a Smart Waste Segregator system built using Python, Flask, and Flask-SocketIO. The system reads data from a serial port connected to sensors measuring waste levels and sends this data to a web interface in real-time. The web interface dynamically updates based on the waste levels, allowing users to monitor and manage waste disposal efficiently.

Features:
Real-time Monitoring: Displays waste levels in real-time on a web interface.
Automatic Segregation: Dynamically switches between different display elements based on waste levels.
Flexible Configuration: Easily configurable to adapt to different sensor inputs and waste segregation requirements.
Technologies Used:
Python: Backend logic and serial port communication.
Flask: Web framework for building the server-side application.
Flask-SocketIO: Enables real-time communication between server and client using WebSockets.
HTML/CSS/JavaScript: Frontend for displaying waste level data and controlling the user interface.

Setup Instructions:
Clone the repository to your local machine.
Install the required Python packages using pip install -r requirements.txt.
Connect the serial port to the sensor measuring waste levels.
Run the Flask application using python app.py.
Open the web interface in a browser to monitor waste levels in real-time.


