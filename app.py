from flask import Flask, render_template, Response, request
import pyautogui
from PIL import ImageGrab
import io
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def capture_screen():
    while True:
        screenshot = ImageGrab.grab()
        buffered = io.BytesIO()
        screenshot.save(buffered, format="JPEG", quality=30)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffered.getvalue() + b'\r\n')
        # time.sleep(0.1)  # Adjust sleep time for desired frame rate

@app.route('/video_feed')
def video_feed():
    return Response(capture_screen(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/click', methods=['POST'])
def handle_click():
    x = float(request.form['x'])
    y = float(request.form['y'])
    screen_width, screen_height = pyautogui.size()
    screen_x = int(x * screen_width)
    screen_y = int(y * screen_height)
    pyautogui.click(screen_x, screen_y)
    return '', 204

@app.route('/key_press', methods=['POST'])
def handle_key_press():
    key = request.form['key']
    pyautogui.keyDown(key)
    return '', 204

@app.route('/key_release', methods=['POST'])
def handle_key_release():
    key = request.form['key']
    pyautogui.keyUp(key)
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
