import qrcode

# Get user input for the URLs to encode (separated by commas)
urls = input("Enter the URLs to encode (separated by commas): ")

# Create a QR code instance and add the data
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(urls)
qr.make(fit=True)

# Generate the QR code image and save it as a PNG file
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")
