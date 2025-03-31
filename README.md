# Image_Steganography
Overview

This project is an implementation of Image Steganography using LSB (Least Significant Bit) encoding in Python with Tkinter for GUI. It allows users to hide a secret message inside an image and later retrieve the hidden message using a secret key.

Features

Hide text messages inside an image using LSB steganography.

Retrieve hidden messages from a steganographic image.

User-friendly GUI built with Tkinter and ttkbootstrap.

Image preview functionality.

Password protection for encoding/decoding.

Supports PNG and JPG image formats.

Technologies Used

Python

Tkinter (for GUI)

PIL (Pillow) (for image processing)

ttkbootstrap (for modern-styled UI)

Installation

Prerequisites

Make sure you have Python 3.x installed on your system. You also need the following dependencies:

pip install pillow ttkbootstrap

Usage

Run the application

python app.py

Steps to hide a message:

Click on "Open Image" and select an image.

Enter the secret message in the text box.

Enter the secret key (default: 1234).

Click "Hide Data" to encode the message into the image.

Click "Save Image" to store the encoded image.

Steps to retrieve a message:

Click on "Open Image" and select the encoded image.

Enter the secret key (default: 1234).

Click "Show Data" to extract and display the hidden message.

Screenshots

(Add screenshots of the GUI here)

File Structure

Image-Steganography/
│-- app.py            # Main application file
│-- requirements.txt  # Dependencies
│-- assets/           # Contains sample images (optional)
│-- README.md         # Project Documentation

Contributing

Feel free to contribute by reporting issues or suggesting features.

