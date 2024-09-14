import socket

def get_ipv4_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # 不需要实际连接到8.8.8.8，仅用于获取本地网卡的IP地址
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    except Exception as e:
        local_ip = "127.0.0.1"
    finally:
        s.close()
    return local_ip

if __name__ == "__main__":
    ipv4_address = get_ipv4_address()
    print(f"当前设备的IPv4地址是: {ipv4_address}")
