from wifi_qrcode_generator import wifi_qrcode

# Parameters for Wi-Fi QR code
ssid = "Zain"  # Replace with your Wi-Fi SSID
hidden = False     # Set to True if the network is hidden
authentication_type = "WPA"  # Use "WPA" for WPA/WPA2-Personal
password = "ALLAHisone!786"  # Replace with your Wi-Fi password

# Generate Wi-Fi QR code
qr_code = wifi_qrcode(ssid, hidden=hidden, authentication_type=authentication_type, password=password)

# Create and save QR code image
qr_code_img = qr_code.make_image()
qr_code_img.save("Wifi_qr_code.png")
