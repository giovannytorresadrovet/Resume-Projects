import base64

# Open the image file in binary mode
with open("C:/Users/giova/Downloads/Security+ News banner-resized.png", "rb") as image_file:
    # Read the image data
    image_data = image_file.read()

# Encode the image data to Base64
encoded_string = base64.b64encode(image_data)

# Print the encoded string
print(encoded_string)
