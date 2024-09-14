import mss
from flask import Flask, render_template, Response, request
from PIL import Image
import io
from qr_code import url_qr
from mouse import mouse_left_click
import threading
app = Flask(__name__)

@app.route('/')
def index():
    monitor_id = int(request.args.get('monitor_id', 1))
    return render_template('index.html',video_tag=f'<img id="screenshot" src="/video_feed?monitor_id={monitor_id}" alt="Screen Image" style="width:100%;" onclick="sendClick(event,{monitor_id})">')

def get_monitor_by_id(monitor_id):
    with mss.mss() as sct:
        monitors = sct.monitors
        if 0 < monitor_id < len(monitors):
            return monitors[monitor_id]
        else:
            return None

def capture_screen(mointor_id=1):
    with mss.mss() as sct:
        while True:
            monitor = get_monitor_by_id(mointor_id)  # 这里选择第一个显示器

            # 抓取指定显示器的内容
            screenshot = sct.grab(monitor)

            # 将图像数据转换为 PIL Image 对象
            img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

            # 创建一个 BytesIO 对象
            img_byte_arr = io.BytesIO()

            # 将图像保存为 JPEG 编码到 BytesIO 对象中
            img.save(img_byte_arr, format='JPEG',quality=30)

            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + img_byte_arr.getvalue() + b'\r\n')
            # time.sleep(0.1)  # Adjust sleep time for desired frame rate

@app.route('/video_feed')
def video_feed():
    monitor_id = int(request.args.get('monitor_id', 1))
    return Response(capture_screen(monitor_id), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/click', methods=['POST'])
def handle_click():
    monitor_id = int(request.form['monitor_id'])
    x = float(request.form['x'])
    y = float(request.form['y'])

    mouse_left_click(monitor_id, x, y)
    return '', 204

@app.route('/key_press', methods=['POST'])
def handle_key_press():
    import pyautogui
    key = request.form['key']
    pyautogui.keyDown(key)
    return '', 204

@app.route('/key_release', methods=['POST'])
def handle_key_release():
    import pyautogui
    key = request.form['key']
    pyautogui.keyUp(key)
    return '', 204
def display_image_non_blocking(image):
    # 创建一个新线程来显示图像
    def show_image():
        image.show()

    thread = threading.Thread(target=show_image)
    thread.start()
if __name__ == '__main__':
    host='0.0.0.0'
    port=5000
    display_image_non_blocking(url_qr(port))
    app.run(host=host, port=port)
