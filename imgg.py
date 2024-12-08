from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import ttkbootstrap as ttk  # Import ttkbootstrap for modern styling

# Main window setup
win = Tk()
win.title("Image Steganography by HETC")
win.geometry('800x600')
win.attributes('-alpha', 0.95)  # Making the window slightly transparent

# Load background and logo images
bg_image = Image.open("D:/img1/O.jpg")
bg_image = bg_image.resize((1920, 1080), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
logo_image = Image.open("D:/img1/1.png")
logo_image = logo_image.resize((200, 200), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

# Set background image
background_label = Label(win, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Display logo in the upper left corner
logo_label = Label(win, image=logo_photo, bg='#2c3e50')
logo_label.place(x=10, y=10, anchor=NW)

# Center frame for main content
center_frame = Frame(win, bg='#2c3e50', width=800, height=500)
center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Heading
Label(center_frame, text='IMAGE STEGANOGRAPHY BY HETC', font='Helvetica 40 bold', bg='#2c3e50', fg='white').pack(pady=(10, 20))

# Global variables for storing selected file and hidden message
open_file = None
hide_msg = None

# LSB Steganography Functions
def encode_image(img_path, message):
    """Encode a message into an image using LSB steganography."""
    img = Image.open(img_path)
    encoded = img.copy()
    width, height = img.size
    message += "###"  # End marker to identify message end
    binary_message = ''.join(format(ord(i), '08b') for i in message)
    data_index = 0
    pixels = list(encoded.getdata())

    for i in range(len(pixels)):
        if data_index < len(binary_message):
            pixel = list(pixels[i])
            for j in range(3):  # Modify RGB values
                if data_index < len(binary_message):
                    pixel[j] = pixel[j] & ~1 | int(binary_message[data_index])
                    data_index += 1
            pixels[i] = tuple(pixel)
        else:
            break

    encoded.putdata(pixels)
    return encoded

def decode_image(img_path):
    """Decode a message from an image using LSB steganography."""
    img = Image.open(img_path)
    binary_message = ''
    pixels = list(img.getdata())

    for pixel in pixels:
        for color in pixel[:3]:  # Only process RGB channels
            binary_message += str(color & 1)

    # Convert binary to characters
    message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
    return message.split("###")[0]  # Extract message before end marker

# Button Functions
def open_img():
    global open_file
    open_file = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           title='Select File Type',
                                           filetypes=(('PNG file', '.png'), ('JPG file', '.jpg'), ('All file', '.')))
    if open_file:
        img = Image.open(open_file)
        img = img.resize((250, 220), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        lf1.configure(image=img)
        lf1.image = img

def hide():
    global hide_msg
    password = code.get()
    if password == '1234':
        msg = text1.get(1.0, END).strip()
        if open_file and msg:
            try:
                hide_msg = encode_image(open_file, msg)
                messagebox.showinfo('Success', 'Your message is successfully hidden in the image. Please save your image.')
            except Exception as e:
                messagebox.showerror('Error', f'Error encoding image: {e}')
        else:
            messagebox.showerror('Error', 'Please select an image and enter a message to hide.')
    elif password == '':
        messagebox.showerror('Error', 'Please enter Secret key')
    else:
        messagebox.showerror('Error', 'Wrong Secret Key')
        code.set('')

def save_img():
    if hide_msg:
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            hide_msg.save(save_path)
            messagebox.showinfo('Saved', 'Image has been successfully saved.')
    else:
        messagebox.showerror('Error', 'No hidden message to save')

def show():
    password = code.get()
    if password == '1234':
        if open_file:
            try:
                show_msg = decode_image(open_file)
                text1.delete(1.0, END)
                text1.insert(END, show_msg if show_msg else "No hidden message found.")
            except Exception as e:
                messagebox.showerror('Error', f'Error decoding image: {e}')
        else:
            messagebox.showerror('Error', 'Please select an image first')
    elif password == '':
        messagebox.showerror('Error', 'Please enter Secret key')
    else:
        messagebox.showerror('Error', 'Wrong Secret Key')
        code.set('')

# Frame for Image Preview
f1 = Frame(center_frame, width=350, height=320, bg='#34495e', bd=5, relief="ridge")
f1.pack(side=LEFT, padx=10, pady=10)
lf1 = Label(f1, bg='#34495e', text="Image Preview", font="Arial 20 bold", fg="white")
lf1.place(relx=0.5, rely=0.5, anchor=CENTER)

# Frame for Input Text
f2 = Frame(center_frame, width=350, height=320, bg='#f5f5f5', bd=5, relief="ridge")
f2.pack(side=RIGHT, padx=10, pady=10)
text1 = Text(f2, font='Arial 20 bold', wrap=WORD, bg='#f5f5f5', fg='#2c3e50')
text1.place(relwidth=1, relheight=1)

# Label and Entry for Secret Key
Label(center_frame, text='Enter Secret Key', font='Helvetica 24 bold', bg='#2c3e50', fg='yellow').pack(pady=(20, 5))
code = StringVar()
e = ttk.Entry(center_frame, textvariable=code, font='Helvetica 20 bold', show='*')
e.pack(pady=5)

# Buttons with centered placement
button_frame = Frame(center_frame, bg='#2c3e50')
button_frame.pack(pady=20)
open_button = ttk.Button(button_frame, text='Open Image', style="primary.TButton", command=open_img)
open_button.grid(row=0, column=0, padx=10)
save_button = ttk.Button(button_frame, text='Save Image', style="success.TButton", command=save_img)
save_button.grid(row=0, column=1, padx=10)
hide_button = ttk.Button(button_frame, text='Hide Data', style="danger.TButton", command=hide)
hide_button.grid(row=0, column=2, padx=10)
show_button = ttk.Button(button_frame, text='Show Data', style="warning.TButton", command=show)
show_button.grid(row=0, column=3, padx=10)

win.mainloop()
