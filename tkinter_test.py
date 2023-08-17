import tkinter as tk
from PIL import Image, ImageTk

def upload_question_bank():
    # Function to handle the upload question bank button click
    # Add your code here to handle the logic for uploading question bank
    print("Upload question bank button clicked")

def generate_question_paper():
    # Function to handle the generate question paper button click
    # Add your code here to handle the logic for generating question paper
    print("Generate question paper button clicked")

def open_upload_page():
    # Function to open the upload question bank page
    upload_page = tk.Toplevel(root)
    upload_page.title("Upload Question Bank")

    # Add your code here to design the upload question bank page
    # Include dropdowns for Department, Year, Subject, Unit, Part
    # Add an option to upload an excel file using filedialog

def open_generate_page():
    # Function to open the generate question paper page
    generate_page = tk.Toplevel(root)
    generate_page.title("Generate Question Paper")

    # Add your code here to design the generate question paper page
    # Include dropdowns for Department, Year, Subject, Unit, Part

# Create the main window
root = tk.Tk()
root.title("Automatic Question Paper Generator")

# Set the window size and position
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Load the gradient background image
image = Image.open("gradient-background.jpg")  # Replace "gradient_bg.jpg" with your own image path
background_image = ImageTk.PhotoImage(image)

# Create a background label to display the image
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the buttons
upload_btn = tk.Button(root, text="Upload Question Bank", command=open_upload_page, padx=10, pady=5, bg="#337ab7", fg="white")

generate_btn = tk.Button(root, text="Generate Question Paper", command=open_generate_page, padx=10, pady=5, bg="#337ab7", fg="white")

# Add the buttons to the window
upload_btn.pack(pady=10)
generate_btn.pack(pady=10)

# Run the main window loop
root.mainloop()
