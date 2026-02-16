import tkinter as tk
from tkinter import ttk, messagebox
import math

# Function to update input fields based on shape
def update_fields(event=None):
    shape = shape_var.get()
    
    # Hide all fields first
    for widget in input_frame.winfo_children():
        widget.grid_remove()

    if shape in ["Rectangle"]:
        label1.config(text="Length:")
        label2.config(text="Width:")
        label1.grid(row=0, column=0)
        entry1.grid(row=0, column=1)
        label2.grid(row=1, column=0)
        entry2.grid(row=1, column=1)

    elif shape in ["Triangle"]:
        label1.config(text="Base:")
        label2.config(text="Height:")
        label1.grid(row=0, column=0)
        entry1.grid(row=0, column=1)
        label2.grid(row=1, column=0)
        entry2.grid(row=1, column=1)

    elif shape in ["Circle", "Sphere"]:
        label1.config(text="Radius:")
        label1.grid(row=0, column=0)
        entry1.grid(row=0, column=1)

    elif shape in ["Square"]:
        label1.config(text="Side:")
        label1.grid(row=0, column=0)
        entry1.grid(row=0, column=1)

    elif shape in ["Pentagon", "Hexagon"]:
        label1.config(text="Side:")
        label1.grid(row=0, column=0)
        entry1.grid(row=0, column=1)

# Function to calculate area
def calculate():
    try:
        shape = shape_var.get()
        
        if shape == "Rectangle":
            area = float(entry1.get()) * float(entry2.get())

        elif shape == "Triangle":
            area = 0.5 * float(entry1.get()) * float(entry2.get())

        elif shape == "Circle":
            r = float(entry1.get())
            area = math.pi * r * r

        elif shape == "Square":
            s = float(entry1.get())
            area = s * s

        elif shape == "Pentagon":
            s = float(entry1.get())
            area = (5 * s * s) / (4 * math.tan(math.pi/5))

        elif shape == "Hexagon":
            s = float(entry1.get())
            area = (3 * math.sqrt(3) * s * s) / 2

        elif shape == "Sphere":
            r = float(entry1.get())
            area = 4 * math.pi * r * r   # Surface Area

        result_label.config(text=f"Result = {round(area,2)}")

    except:
        messagebox.showerror("Error", "Enter valid numbers!")

# Main Window
window = tk.Tk()
window.title("Multi Shape Area Calculator")
window.geometry("400x300")

# Shape Selection
shape_var = tk.StringVar()
shape_combo = ttk.Combobox(window, textvariable=shape_var)
shape_combo['values'] = ("Rectangle", "Triangle", "Circle", "Square",
                         "Pentagon", "Hexagon", "Sphere")
shape_combo.current(0)
shape_combo.bind("<<ComboboxSelected>>", update_fields)
shape_combo.pack(pady=10)

# Input Frame
input_frame = tk.Frame(window)
input_frame.pack()

label1 = tk.Label(input_frame, text="")
entry1 = tk.Entry(input_frame)

label2 = tk.Label(input_frame, text="")
entry2 = tk.Entry(input_frame)

# Calculate Button
btn = tk.Button(window, text="Calculate", command=calculate)
btn.pack(pady=15)

# Result Label
result_label = tk.Label(window, text="Result = ")
result_label.pack()

# Initialize fields
update_fields()

window.mainloop()
