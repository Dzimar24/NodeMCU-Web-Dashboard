# 🎛️ NodeMCU IoT Web Monitor

![MicroPython](https://img.shields.io/badge/MicroPython-1.19+-blue.svg)
![Device](https://img.shields.io/badge/Device-ESP8266-red.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**NodeMCU IoT Web Monitor** adalah sistem monitoring lingkungan sederhana berbasis Internet of Things (IoT). Project ini memungkinkan pengguna untuk mengontrol lampu (LED) melalui Dashboard Web Lokal tanpa memerlukan koneksi internet eksternal.

Project ini dibuat sebagai implementasi protokol **HTTP Web Server** menggunakan socket programming pada microcontroller.

## 📸 Tampilan Dashboard (Demo)

![Web Dashboard Screenshot](https://github.com/Dzimar24/NodeMCU-Web-Dashboard/blob/main/Screenshot%202025-12-04%20231808.png?raw=true)

## ✨ Fitur Utama
* 📡 **Web Server Lokal:** Dashboard kontrol yang di-hosting langsung di dalam chip ESP8266.
* 💡 **Remote Control:** Menyalakan/Mematikan 3 buah LED via browser HP/Laptop.
* 🔄 **Auto Refresh:** Tombol refresh untuk mengambil data sensor terbaru tanpa reload halaman.

## 🛠️ Komponen Hardware
Project ini menggunakan komponen berikut:
1.  **NodeMCU ESP8266**.
2.  **3x LED** (Merah, Kuning, Hijau).
3.  **3x Resistor 330 Ohm** (Untuk pengaman LED).
4.  Kabel Jumper Male to Male & Breadboard.

## 🔌 Skema Rangkaian (Wiring)

Berikut adalah diagram koneksi antar komponen yang dibuat menggunakan Fritzing:

![Skema Rangkaian Fritzing](https://github.com/Dzimar24/NodeMCU-Web-Dashboard/blob/main/webServer_bb.jpg?raw=true)

**Detail Pin Mapping:**

| Komponen | Pin NodeMCU | Keterangan |
| :--- | :--- | :--- |
| **LED Merah** | D5 (GPIO 14) | Output |
| **LED Kuning** | D6 (GPIO 12) | Output |
| **LED Hijau** | D7 (GPIO 13) | Output |


## 🚀 Cara Instalasi

### 1. Persiapan
Pastikan Anda sudah menginstall:
* Python 3.x
* VS Code atau Thonny IDE.
* Firmware MicroPython pada ESP8266.

### 2. Konfigurasi WiFi
Project ini menggunakan file `secrets.py` untuk keamanan. Buat file baru bernama `secrets.py` di folder project, lalu isi dengan:

```python
# secrets.py
SSID = "Nama_WiFi"
PASSWORD = "Password_WiFi"
