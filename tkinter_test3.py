import tkinter as ttk

upload_page = ttk.Toplevel(root)
upload_page.title("Upload Question Bank")
upload_page.geometry("400x300")

# Create the dropdown boxes with custom styles
department_dropdown = ttk.Combobox(upload_page, values=departments)
year_dropdown = ttk.Combobox(upload_page, values=years)
subject_dropdown = ttk.Combobox(upload_page, values=subjects)
unit_dropdown = ttk.Combobox(upload_page, values=units)
part_dropdown = ttk.Combobox(upload_page, values=parts)

# Configure the styles for the dropdown boxes
department_dropdown.configure(style="Dropdown.TCombobox")
year_dropdown.configure(style="Dropdown.TCombobox")
subject_dropdown.configure(style="Dropdown.TCombobox")
unit_dropdown.configure(style="Dropdown.TCombobox")
part_dropdown.configure(style="Dropdown.TCombobox")


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

root.mainloop()