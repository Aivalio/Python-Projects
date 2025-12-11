"""
This script uses the 'qrcode' Python library to convert a user-provided URL
into a QR code image and save it as a PNG file.
"""

import qrcode

# Ask the user to enter a URL they want to convert into a QR code
url = input("Enter your URL: ")

# Ask the user for the filename to save the QR code image
filename = input("Filename you want to save it as: ")

# Ensure the file ends with '.png'
if not filename.lower().endswith(".png"):
    filename += ".png"

# Generate the QR code image from the URL
img = qrcode.make(url)

# Save the generated image with the filename provided
img.save(filename)

print(f"QR code saved as {filename}")
