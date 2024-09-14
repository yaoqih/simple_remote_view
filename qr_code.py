import qrcode
from PIL import Image, ImageDraw, ImageFont
import mss
from ip_address import get_ipv4_address

def create_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    return qr.make_image(fill='black', back_color='white').convert('RGB')

def create_combined_image(urls_texts, font_path="arial.ttf", font_size=20, padding=10):
    # 尝试加载字体
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
    
    qr_images = []
    texts = []
    
    for url, text in urls_texts:
        qr_images.append(create_qr_code(url))
        texts.append(text)
    
    # 计算组合图像的宽度和高度
    max_qr_height = max(img.height for img in qr_images)
    text_height = font_size + padding
    combined_width = sum(img.width for img in qr_images)
    combined_height = max_qr_height + text_height + padding
    
    combined_img = Image.new('RGB', (combined_width, combined_height), 'white')
    draw = ImageDraw.Draw(combined_img)
    
    x_offset = 0
    for img, text in zip(qr_images, texts):
        combined_img.paste(img, (x_offset, 0))
        
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        
        text_x = x_offset + (img.width - text_width) / 2
        draw.text((text_x, max_qr_height + padding), text, fill="black", font=font)
        
        x_offset += img.width
    
    return combined_img

def url_qr(port):
    monitor_num = len(mss.mss().monitors)-1
    urls_texts = [(f"http://{get_ipv4_address()}:{port}?monitor_id={i+1}", f"Monitor {i+1}") for i in range(monitor_num)]
    print(urls_texts[0])
    combined_img = create_combined_image(urls_texts)
    return combined_img
