import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Image in Tkinter")

# Load and resize the image using PIL
image = Image.open("octagon.png")  # Replace with the path to your image
# resized_image = image.resize((300, 300))  # Resize the image (width, height)
photo = ImageTk.PhotoImage(image)

# Create a label widget to hold the resized image
label = tk.Label(root, image=photo)
label.pack()

# button = tk.Button(root, image=photo)
# button.pack()


# Start the Tkinter event loop
root.mainloop()
