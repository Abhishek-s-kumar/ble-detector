from bluepy.btle import Scanner
import csv
import time
from datetime import datetime

WHITELIST_FILE = "whitelist.csv"
LOG_FILE = "ble_device_log.csv"

# Load existing whitelist
def load_whitelist():
    whitelist = {}
    try:
        with open(WHITELIST_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                whitelist[row['MAC']] = row['Name']
    except FileNotFoundError:
        pass
    return whitelist

# Append to whitelist
def update_whitelist(mac, name):
    with open(WHITELIST_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([mac, name])

# Log changes
def log_change(mac, name, event):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([now, mac, name, event])
    print(f"[{now}] {event}: {mac} ({name})")

# Initialize log file headers if needed
def initialize_logs():
    for file_path, headers in [(WHITELIST_FILE, ['MAC', 'Name']), (LOG_FILE, ['Timestamp', 'MAC', 'Name', 'Event'])]:
        try:
            with open(file_path, 'r') as f:
                pass
        except FileNotFoundError:
            with open(file_path, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(headers)

initialize_logs()
scanner = Scanner()

print("Scanning for BLE devices. Press Ctrl+C to stop.")
whitelist = load_whitelist()

try:
    while True:
        devices = scanner.scan(5.0)
        for dev in devices:
            mac = dev.addr
            name = dev.getValueText(9) or "Unknown"

            if mac not in whitelist:
                log_change(mac, name, "New Device Found")
                update_whitelist(mac, name)
                whitelist[mac] = name
            elif whitelist[mac] != name:
                log_change(mac, name, "Name Change Detected")
                whitelist[mac] = name
        time.sleep(5)

except KeyboardInterrupt:
    print("Scan stopped by user.")
