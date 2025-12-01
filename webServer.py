import network
import socket
from machine import Pin, ADC
import time
import secrets

MY_SSID = secrets.SSID              #! Username WIFI
MY_PASSWORD = secrets.PASSWORD      #! Password WIFI

ldr = ADC(0)
led1 = Pin(14, Pin.OUT) # D5
led2 = Pin(12, Pin.OUT)  # D6
led3 = Pin(13, Pin.OUT)  # D7

led1.off()
led2.off()
led3.off()

def connectWifi(SSID_TARGET, PASSWORD_TARGET):
   wlan = network.WLAN(network.STA_IF)
   wlan.active(True)
   
   print(f"Connecting to WiFi : {SSID_TARGET}", end="")
   found = False
   try:
      wifiList = wlan.scan()
      for wifi in wifiList:
         ssidScan = wifi[0].decode("utf-8")
         if ssidScan == SSID_TARGET:
            found = True
            print(f"\n WiFi {SSID_TARGET} found")
            break
   except Exception as e:
      print(f"Failed to scan WiFi : {e}")
   
   if not found:
      print(f"\n WiFi {SSID_TARGET} not found")
      return None
   
   print(f"Trying to connect to {SSID_TARGET}....", end="")
   wlan.connect(SSID_TARGET, PASSWORD_TARGET)
   
   timeout = 0
   while not wlan.isconnected() and timeout < 20 :
      time.sleep(1)
      print(".", end="")
      timeout += 1
      
   if wlan.isconnected():
      print("\nConnected to WiFi")
      print("IP address: ", wlan.ifconfig()[0])
      return wlan.ifconfig()[0]
   else:
      status = wlan.status()
      print(f"\nConnection failed with error {status}")
      
      if status == network.STAT_WRONG_PASSWORD:
         print("Wrong password")
      elif status == network.STAT_NO_AP_FOUND:
         print("WiFi not found")
      elif status == network.STAT_CONNECT_FAIL:
         print("Connection failed")
         
      
      return None
   
def webPage(valueOfLight):
   status1 = "ON" if led1.value() == 1 else "OFF"
   status2 = "ON" if led2.value() == 1 else "OFF"
   status3 = "ON" if led3.value() == 1 else "OFF"
   
   html = """
   <html>
      <head>
         <title>NodeMCU Dashboard</title>
         <meta name="viewport" content="width=device-width, initial-scale=1">
         <style>
               body { font-family: Arial; text-align: center; margin-top: 50px; }
               h1 { color: #003366; }
               .box { border: 1px solid #ccc; padding: 20px; margin: 10px; display: inline-block; border-radius: 10px;}
               .btn { background-color: #4CAF50; border: none; color: white; padding: 10px 20px; text-decoration: none; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 5px;}
               .btn-off { background-color: #f44336; }
               .sensor { font-size: 24px; color: orange; font-weight: bold;}
         </style>
      </head>
      <body>
         <h1>🎛️ Ruang Kontrol IoT</h1>
         
         <div class="box">
               <h3>Sensor Cahaya (LDR)</h3>
               <p class="sensor">""" + str(valueOfLight) + """</p>
               <p><a href="/"><button class="btn">Refresh Data</button></a></p>
         </div>
         
         <br>
         
         <div class="box">
            <h3>Kontrol Lampu</h3>
            <p>LED 1 Kuning: <strong>""" + status1 + """</strong></p>
            <a href="/?led1=on"><button class="btn">ON</button></a>
            <a href="/?led1=off"><button class="btn btn-off">OFF</button></a>
            
            <p>LED 2 Merah : <strong>""" + status2 + """</strong></p>
            <a href="/?led2=on"><button class="btn">ON</button></a>
            <a href="/?led2=off"><button class="btn btn-off">OFF</button></a>

            <p>LED 3 Hijau : <strong>""" + status3 + """</strong></p>
            <a href="/?led3=on"><button class="btn">ON</button></a>
            <a href="/?led3=off"><button class="btn btn-off">OFF</button></a>
         </div>
      </body>
   </html>
   """
   return html

ipAddress = connectWifi(MY_SSID, MY_PASSWORD)

if ipAddress :
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.bind(("", 80))
   s.listen(5)
   print(f"Server started, open in URL : {ipAddress}")
   
   while True:
      try:
         conn, addr = s.accept()
         print('Got a connection from %s' % str(addr))
         
         request = conn.recv(1024)
         request = str(request)
         
         if '/?led1=on' in request:
            led1.on()
         if '/?led1=off' in request:
            led1.off()
         if '/?led2=on' in request:
            led2.on()
         if '/?led2=off' in request:
            led2.off()
         if '/?led3=on' in request:
            led3.on()
         if '/?led3=off' in request:
            led3.off()
            
         valueOfLight = ldr.read()
         
         response = webPage(valueOfLight)
         conn.send('HTTP/1.1 200 OK\n')
         conn.send('Content-Type: text/html\n')
         conn.send('Connection: close\n\n')
         conn.sendall(response)
         conn.close()
      
      except OSError as e:
         conn.close()
         print('Connection closed') 
         