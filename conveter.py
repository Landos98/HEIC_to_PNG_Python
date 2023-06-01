from tkinter import Tk, filedialog
from PIL import Image
import pyheif
import os

# Function to select and load the HEIC image
def load_image():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("HEIC Image", "*.HEIC")])
    return file_path

# Function to save the converted image as PNG in the selected folder
def save_image(image, folder, file_name):
    save_path = os.path.join(folder, file_name)
    image.save(save_path, "PNG")

# Conversion from HEIC to PNG
def convert_to_png(file_path):
    try:
        heif_file = pyheif.read(file_path)
        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        root = Tk()
        root.withdraw()
        folder_path = filedialog.askdirectory()
        if folder_path:
            file_name = os.path.splitext(os.path.basename(file_path))[0] + ".png"
            save_image(image, folder_path, file_name)
            print("The image has been converted and saved successfully as PNG.")
    except Exception as e:
        print("Error converting the image:", str(e))

# Program execution
if __name__ == "__main__":
    print("Script to convert HEIC images to PNG")
    heic_image = load_image()
    if heic_image:
        convert_to_png(heic_image)