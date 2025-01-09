import socket

def scan_port(target_ip, target_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, target_port))
        if result == 0:
            print(f"Port {target_port} is open on {target_ip}")
        else:
            print(f"Port {target_port} is closed on {target_ip}")
        sock.close()
    except socket.error as err:
        print(f"Error: {err}")
