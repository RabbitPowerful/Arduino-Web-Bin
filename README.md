Smart Waste Segregator
This project demonstrates a Smart Waste Segregator system built using Python, Flask, and Flask-SocketIO. The system reads data from a serial port connected to sensors measuring waste levels and sends this data to a web interface in real-time. The web interface dynamically updates based on the waste levels, allowing users to monitor and manage waste disposal efficiently.


----------------------------------------------------------------------------------------------------------------------------------------

Features:

1.Real-time Monitoring: Displays waste levels in real-time on a web interface.

2.Automatic Segregation: Dynamically switches between different display elements based on waste levels.

3.Flexible Configuration: Easily configurable to adapt to different sensor inputs and waste segregation requirements.


----------------------------------------------------------------------------------------------------------------------------------------


Technologies Used:

1.Python: Backend logic and serial port communication.

2.Flask: Web framework for building the server-side application.

3.Flask-SocketIO: Enables real-time communication between server and client using WebSockets.

4.HTML/CSS/JavaScript: Frontend for displaying waste level data and controlling the user interface.


----------------------------------------------------------------------------------------------------------------------------------------


Setup Instructions:

1.Clone the repository to your local machine.

2.Install the required Python packages using pip install -r requirements.txt.

3.Connect the serial port to the sensor measuring waste levels.

4.Run the Flask application using python app.py.

5.Open the web interface in a browser to monitor waste levels in real-time.


