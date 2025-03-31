# Image Steganography Project

This project is a simple image steganography tool built using Python and Tkinter (with ttkbootstrap for modern styling). It allows users to hide and reveal text messages within images using the Least Significant Bit (LSB) technique.

## Features

-   **Image Selection:** Users can select PNG or JPG images to hide or reveal messages.
-   **Message Encoding:** Encodes text messages into the LSB of the selected image's pixels.
-   **Message Decoding:** Decodes hidden messages from images.
-   **Password Protection:** Implements a simple password system to protect the hidden message.
-   **Modern GUI:** Utilizes ttkbootstrap for a modern and visually appealing user interface.
-   **Image Preview:** Displays the selected image within the application.
-   **Save Encoded Image:** Allows users to save the image containing the hidden message.

## Technologies Used

-   Python
-   Tkinter
-   ttkbootstrap
-   PIL (Pillow)

## Prerequisites

-   Python 3.x
-   ttkbootstrap (`pip install ttkbootstrap`)
-   Pillow (`pip install Pillow`)

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Install dependencies:**
    ```bash
    pip install ttkbootstrap Pillow
    ```

3.  **Run the application:**
    ```bash
    python <your_script_name>.py
    ```
    (Replace `<your_script_name>.py` with the actual name of your Python script.)

## Usage

1.  **Open Image:** Click the "Open Image" button and select an image file (PNG or JPG).
2.  **Enter Message:** Type the message you want to hide in the text box.
3.  **Enter Secret Key:** Input the secret key (password) in the provided entry field. The password is "1234" by default.
4.  **Hide Data:** Click the "Hide Data" button to encode the message into the image.
5.  **Save Image:** Click the "Save Image" button to save the encoded image.
6.  **Show Data:** To reveal the hidden message, open the encoded image, enter the correct password, and click the "Show Data" button.

## Project Structure
