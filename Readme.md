# BLE Beacon Tracker with Whitelist-Based Anomaly Detection

## 📘 Project Summary
This project uses a Raspberry Pi Zero 2 W to monitor Bluetooth Low Energy (BLE) devices in the environment. It scans for nearby BLE advertisements, logs any new devices, and tracks changes in device names. A whitelist system prevents redundant alerts and helps detect spoofing attempts or impersonation through MAC and name inconsistencies.

---

## 🎯 Objectives
- Monitor BLE MAC addresses and names
- Log newly discovered devices
- Detect and report if a known MAC changes its advertised name
- Store logs in a CSV file for analysis
- Use a whitelist to suppress repeated alerts

---

## 📦 Dependencies & Installation

### 🛠️ System Packages
```bash
sudo apt update
sudo apt install python3-pip bluetooth bluez libglib2.0-dev pkg-config libbluetooth-dev
```

### 🐍 Python Package
```bash
pip3 install bluepy
```

---

## 📁 Project Files
| File                  | Description                                      |
|-----------------------|--------------------------------------------------|
| `ble_whitelist_logger.py` | Main Python script for BLE scanning and logging |
| `whitelist.csv`       | Tracks known MAC–Name pairs                      |
| `ble_device_log.csv`  | Logs new devices or name changes                 |

---

## ▶️ Usage
1. Power on your Raspberry Pi Zero 2 W with BLE enabled.
2. Run the logger script:
```bash
sudo python3 ble_whitelist_logger.py
```
3. The script scans for 5 seconds in each loop, logs new devices, and updates the whitelist.

---

## 🧪 Example Log Output
```
Timestamp              | MAC                  | Name           | Event
2025-06-17 14:01:23    | 40:48:6E:56:61:F8    | Nokia-61-F8    | New Device Found
2025-06-17 14:04:10    | 40:48:6E:56:61:F8    | NOKIA-F8       | Name Change Detected
```

---

## 📌 Notes
- Ensure no other BLE scanner (like `bluetoothctl scan on`) is running.
- If `bluepy` fails to install, verify `libbluetooth-dev` and `libglib2.0-dev` are installed.
- For custom alerts (e.g., push notifications), you can expand the logging logic.

---

## 📚 References
- [BlueZ Official Docs](http://www.bluez.org/)
- [bluepy GitHub](https://github.com/IanHarvey/bluepy)
- [Kali Linux ARM Setup](https://www.kali.org/get-kali/#kali-arm)

---

**Author:** 🐉 Kali GPT | Project Contributor: [Your Name]
