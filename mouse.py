import ctypes
import time
import mss
# 定义鼠标事件常量
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

def move_mouse_to_relative_position(monitor_id, relative_x, relative_y):
    with mss.mss() as sct:
        monitors = sct.monitors
        if monitor_id < 0 or monitor_id >= len(monitors):
            raise ValueError(f"Invalid monitor_id: {monitor_id}")

        monitor = monitors[monitor_id]
        monitor_left = monitor["left"]
        monitor_top = monitor["top"]
        monitor_width = monitor["width"]
        monitor_height = monitor["height"]

        # 计算绝对位置
        absolute_x = int(monitor_left + relative_x * monitor_width)
        absolute_y = int(monitor_top + relative_y * monitor_height)

        # 移动光标
        return absolute_x, absolute_y

def mouse_left_click(monitor_id,x, y):
    # 移动到指定位置（确保光标在正确的位置）
    x, y = move_mouse_to_relative_position(monitor_id, x, y)
    ctypes.windll.user32.SetCursorPos(x, y)
    
    # 模拟鼠标左键按下和松开
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.01)  # 短暂的延迟，让按下和松开更自然
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, x, y, 0, 0)