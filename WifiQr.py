from wifi_qrcode_generator import wifi_qrcode

ssid = "WIFI SSD"  # Replace with your Wi-Fi SSID
hidden = False     
authentication_type = "WPA"
password = "your wifi password"  

qr_code = wifi_qrcode(ssid, hidden=hidden, authentication_type=authentication_type, password=password)

qr_code_img = qr_code.make_image()
qr_code_img.save("Wifi_qr_code.png")
