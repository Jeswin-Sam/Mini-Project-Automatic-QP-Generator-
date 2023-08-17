import tkinter as tk
from tkinter import filedialog
from upload_function import *



def open_upload_page():
    # Function to open the upload question bank page
    upload_page = tk.Toplevel(root)
    upload_page.title("Upload Question Bank")
    upload_page.state('zoomed')

    # Set the window size and position
    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create the dropdowns for Department, Year, Subject, Unit, Part
    department_label = tk.Label(upload_page, text="Department")
    department_label.pack()
    department_var = tk.StringVar()
    department_dropdown = tk.OptionMenu(upload_page, department_var, "CSE", "ECE", "EEE", "MECH", "CIVIL")
    department_dropdown.configure(bg="#ffffff", fg="#000000", font=("Arial", 12), width=15)
    department_dropdown.pack(pady=5)
    

    year_label = tk.Label(upload_page, text="Year")
    year_label.pack()
    year_var = tk.StringVar()
    year_dropdown = tk.OptionMenu(upload_page, year_var, "1st Year", "2nd Year", "3rd Year", "4th Year")
    year_dropdown.configure(bg="#ffffff", fg="#000000", font=("Arial", 12), width=15)
    year_dropdown.pack(pady=5)

    subject_label = tk.Label(upload_page, text="Subject")
    subject_label.pack()
    subject_var = tk.StringVar()
    subject_dropdown = tk.OptionMenu(upload_page, subject_var, "Subject 1", "Subject 2", "Subject 3")
    subject_dropdown.configure(bg="#ffffff", fg="#000000", font=("Arial", 12), width=15)
    subject_dropdown.pack(pady=5)

    unit_label = tk.Label(upload_page, text="Unit")
    unit_label.pack()
    unit_var = tk.StringVar()
    unit_dropdown = tk.OptionMenu(upload_page, unit_var, "Unit-1", "Unit-2", "Unit-3", "Unit-4", "Unit-5")
    unit_dropdown.configure(bg="#ffffff", fg="#000000", font=("Arial", 12), width=15)
    unit_dropdown.pack(pady=5)

    part_label = tk.Label(upload_page, text="Part")
    part_label.pack()
    part_var = tk.StringVar()
    part_dropdown = tk.OptionMenu(upload_page, part_var, "A", "B")
    part_dropdown.configure(bg="#ffffff", fg="#000000", font=("Arial", 12), width=15)
    part_dropdown.pack(pady=5)
    
    
    def upload_question_bank():
        selected_department = department_var.get()
        selected_year = year_var.get()
        selected_subject = subject_var.get()
        selected_unit = unit_var.get()
        selected_part = part_var.get()

        
        upload_questions(dept = selected_department, 
                         year = selected_year, 
                         subject = selected_subject, 
                         unit = selected_unit, 
                         part = selected_part, 
                         file_name = file_path)
        
        
        print("Selected Department:", selected_department)
        print("Selected Year:", selected_year)
        print("Selected Subject:", selected_subject)
        print("Selected Unit:", selected_unit)
        print("Selected Part:", selected_part)
        print("Selected File:", file_path)
   

    # Add the upload file button
    def browse_file():
        global file_path
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        
    upload_file_btn = tk.Button(upload_page, text="Upload File", command=browse_file, padx=10, pady=5) 
    upload_file_btn.pack(pady=10)
    
    upload_page.grab_set()

    upload_btn = tk.Button(upload_page, text="Upload", command=upload_question_bank, padx=10, pady=5)
    upload_btn.pack(pady=10)
    
    

def open_generate_page():
    # Function to open the generate question paper page
    generate_page = tk.Toplevel(root)
    generate_page.title("Generate Question Paper")
    generate_page.state('zoomed')
    
    # Set the window size and position
    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create the dropdowns for Department, Year, Subject, Unit, Part
    department_label = tk.Label(generate_page, text="Department")
    department_label.pack()
    department_var = tk.StringVar()
    department_dropdown = tk.OptionMenu(generate_page, department_var, "CSE", "ECE", "EEE", "MECH", "CIVIL")
    department_dropdown.configure(bg="#ffffff", fg="#000000", font=("Arial", 12), width=15, relief="solid")
    department_dropdown.pack(pady=5)

    year_label = tk.Label(generate_page, text="Year")
    year_label.pack()
    year_var = tk.StringVar()
    year_dropdown = tk.OptionMenu(generate_page, year_var, "1st Year", "2nd Year", "3rd Year", "4th Year")
    year_dropdown.configure(bg="#ffffff", fg="#000000", font=("Arial", 12), width=15, relief="solid")
    year_dropdown.pack(pady=5)

    subject_label = tk.Label(generate_page, text="Subject")
    subject_label.pack()
    subject_var = tk.StringVar()
    subject_dropdown = tk.OptionMenu(generate_page, subject_var, "Subject 1", "Subject 2", "Subject 3")
    subject_dropdown.configure(bg="#ffffff", fg="#000000", font=("Arial", 12), width=15, relief="solid")
    subject_dropdown.pack(pady=5)

    unit_label = tk.Label(generate_page, text="Unit")
    unit_label.pack()
    unit_var = tk.StringVar()
    unit_dropdown = tk.OptionMenu(generate_page, unit_var, "1", "2", "3", "4", "5")
    unit_dropdown.configure(bg="#ffffff", fg="#000000", font=("Arial", 12), width=15, relief="solid")
    unit_dropdown.pack(pady=5)

    part_label = tk.Label(generate_page, text="Part")
    part_label.pack()
    part_var = tk.StringVar()
    part_dropdown = tk.OptionMenu(generate_page, part_var, "A", "B")
    part_dropdown.configure(bg="#ffffff", fg="#000000", font=("Arial", 12), width=15, relief="solid")
    part_dropdown.pack(pady=5)
    
    def generate_question_paper():
        # Get the selected options from the dropdowns
        selected_department = department_var.get()
        selected_year = year_var.get()
        selected_subject = subject_var.get()
        selected_unit = unit_var.get()
        selected_part = part_var.get()

        # Print the selected values
        print("Selected Department:", selected_department)
        print("Selected Year:", selected_year)
        print("Selected Subject:", selected_subject)
        print("Selected Unit:", selected_unit)
        print("Selected Part:", selected_part)

    # Add the generate button
    generate_btn = tk.Button(generate_page, text="Generate", command=generate_question_paper, padx=10, pady=5)
    generate_btn.configure(bg="#ff0000", fg="#ffffff", font=("Arial", 12), relief="raised")
    generate_btn.pack(pady=10)



# Create the main window
root = tk.Tk()
root.title("Automatic Question Paper Generator")
root.state('zoomed')

# Set the window size and position
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")


# Create the buttons
upload_btn = tk.Button(root, text="Upload Question Bank", command=open_upload_page, relief=tk.RAISED, bg="#4CAF50", fg="white", font=("Arial", 12), padx=10, pady=5)

generate_btn = tk.Button(root, text="Generate Question Paper", command=open_generate_page, relief=tk.RAISED, bg="#4CAF50", fg="white", font=("Arial", 12),padx=10, pady=5)

# Add the buttons to the window
upload_btn.pack(pady=10)
generate_btn.pack(pady=10)

# Run the main window loop
root.mainloop()
