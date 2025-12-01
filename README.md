# 🎛️ NodeMCU IoT Web Monitor

![MicroPython](https://img.shields.io/badge/MicroPython-1.19+-blue.svg)
![Device](https://img.shields.io/badge/Device-ESP8266-red.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**NodeMCU IoT Web Monitor** adalah sistem monitoring lingkungan sederhana berbasis Internet of Things (IoT). Project ini memungkinkan pengguna untuk memantau intensitas cahaya ruangan secara real-time dan mengontrol lampu (LED) melalui Dashboard Web Lokal tanpa memerlukan koneksi internet eksternal.

Project ini dibuat sebagai implementasi protokol **HTTP Web Server** menggunakan socket programming pada microcontroller.

## 📸 Tampilan Dashboard (Demo)

![Web Dashboard Screenshot](https://via.placeholder.com/600x300?text=Upload+Foto+Dashboard+Web+Disini)

## ✨ Fitur Utama
* 📡 **Web Server Lokal:** Dashboard kontrol yang di-hosting langsung di dalam chip ESP8266.
* ☀️ **Monitoring Sensor:** Membaca nilai sensor LDR (Cahaya) secara real-time.
* 💡 **Remote Control:** Menyalakan/Mematikan 3 buah LED via browser HP/Laptop.
* 🔄 **Auto Refresh:** Tombol refresh untuk mengambil data sensor terbaru tanpa reload halaman.

## 🛠️ Komponen Hardware
Project ini menggunakan komponen berikut:
1.  **NodeMCU ESP8266**.
2.  **Sensor LDR** (Light Dependent Resistor) + Resistor 10k Ohm (Voltage Divider).
3.  **3x LED** (Merah, Kuning, Putih).
4.  **3x Resistor 330 Ohm** (Untuk pengaman LED).
5.  Kabel Jumper Male to Male & Breadboard.

## 🔌 Skema Rangkaian (Wiring)

| Komponen | Pin NodeMCU | Keterangan |
| :--- | :--- | :--- |
| **LED Merah** | D5 (GPIO 14) | Output |
| **LED Kuning** | D6 (GPIO 12) | Output |
| **LED Putih** | D7 (GPIO 13) | Output |
| **Sensor LDR** | A0 (ADC 0) | Input Analog |

![Wiring Diagram](https://via.placeholder.com/600x300?text=Foto+Rangkaian+Alat)

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
SSID = "Nama_WiFi_Anda"
PASSWORD = "Password_WiFi_Anda"
