from tkinter import *
from tkinter.filedialog import askopenfile
from PIL import Image
import pytesseract

root = Tk()
root.title('OCR Application')


def zoom_in():
    font_size = output_text['font'].split()[1]
    new_size = int(font_size) + 2
    if new_size>15:
        new_size = 14
    print(new_size)
    output_text.config(font=("TkDefaultFont", new_size))

def zoom_out():
    font_size = output_text['font'].split()[1]
    new_size = int(font_size) - 2
    if new_size<5:
        new_size =5
    output_text.config(font=("TkDefaultFont", new_size))

def open_file():
    file = askopenfile(mode ='r', filetypes =[('All files', '*'),])
    if file is not None:
        image = Image.open(file.name)
        text = pytesseract.image_to_string(image)
        output_text.delete(1.0, END)
        output_text.insert(END, text)

def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output_text.get(1.0, END))

def clear_text():
    output_text.delete(1.0, END)

# Create a Text widget to display the output
output_text = Text(root, height=20, width=80, background='#1e1e1e', foreground='#8b0000', font=("TkDefaultFont", 12))

output_text.pack(padx=10, pady=10)

# Add two buttons for zooming in and out
zoom_in_button = Button(root, text="Zoom In", command=zoom_in)
zoom_in_button.pack(padx = 10, pady = 10)

zoom_out_button = Button(root, text="Zoom Out", command=zoom_out)
zoom_out_button.pack(padx = 10, pady = 10)


btn_open = Button(root, text ='Open', command = open_file)
btn_open.pack(padx = 10, pady = 10)

btn_copy = Button(root, text ='Copy', command = copy_text)
btn_copy.pack(padx = 10, pady = 10)

btn_clear = Button(root, text ='Clear All', command = clear_text)
btn_clear.pack(padx = 10, pady = 10)


root.mainloop()
