'''
Jmoody
ISS 212
4.2025 Wk 12 Tool Development 8 - stego.py
NOTE: USE STEGO IMAGE FILE: drdoes-steg.png
'''

from PIL import Image

#Function that extracts a hidden message from a stego image
def extract_message():
    print("Stego Image Extraction Script")

    #Prompts the user for a image path to the image with the hidden stego message
    stego_image_path = input("Enter the path of the stego image: ").strip()

    #Opens the stego image
    img = Image.open(stego_image_path)

    #Stores the extracted bits
    data = ''
    terminator = '11111111'

    #Loops through every pixel in the image
    for i in range(img.width):
        for j in range(img.height):
            pixel = img.getpixel((i, j))
            for color_channel in range(3):
                #Extracts least significant bits from each color channel
                data += format(pixel[color_channel], '08b')[-1]

    #Locates where the message ends using terminator
    terminator_index = data.find(terminator)

    #Extracts binary data and converts it into readable letters
    message = ''.join([chr(int(data[i:i+8], 2)) for i in range(0, terminator_index, 8)])

    #Prints hidden message
    print(f"Extracted Message: {message}")

if __name__ == "__main__":
    extract_message()
