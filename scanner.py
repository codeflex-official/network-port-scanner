
import socket
import threading
from datetime import datetime


target = input("Enter Target IP or Domain (e.g. 127.0.0.1 or google.com): ").strip()

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("\n❌ Invalid Hostname / IP. Please check again.")
    exit()

print(f"\n{'='*50}")
print(f"Target: {target} ({target_ip})")
print(f"Scanning Started: {datetime.now()}")
print(f"{'='*50}\n")


def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            print(f"Port {port}: OPEN [ {service} ] ✅")
        s.close()
    except:
        pass


try:
    for port in range(1, 1025):
        t = threading.Thread(target=scan_port, args=(port,))
        t.start()

except KeyboardInterrupt:
    print("\n\n⚠️ Scan Stopped By User!")
    exit()

print(f"\n{'='*50}")
print("✅ Scan Completed!")
print(f"{'='*50}")
