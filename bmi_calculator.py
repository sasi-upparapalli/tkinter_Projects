import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        
        height = float(entry_height.get()) / 100 
        
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi <= 24.9:
            category = "Normal weight"
        elif 25.0 <= bmi <= 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi} ({category})")
        
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height.")
    except ZeroDivisionError:
        messagebox.showerror("Invalid input", "Height cannot be zero.")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x320")
root.config(bg="#00b0d3")

label_title = tk.Label(root, text="Body Mass Index Calculator", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#333333")
label_title.pack(pady=10)

label_weight = tk.Label(root, text="Enter weight (kg):", bg="#f0f0f0")
label_weight.pack()
entry_weight = tk.Entry(root, width=15, bd=2)
entry_weight.pack(pady=5)

label_height = tk.Label(root, text="Enter height (cm):", bg="#f0f0f0")
label_height.pack()
entry_height = tk.Entry(root, width=15, bd=2)
entry_height.pack(pady=5)

btn_calculate = tk.Button(
    root, 
    text="Calculate BMI", 
    command=calculate_bmi, 
    bg="#4CAF50", 
    fg="white", 
    relief=tk.RAISED, 
    padx=10, 
    pady=5, 
    font=("Arial", 10, "bold")
)
btn_calculate.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12, "italic"), bg="#f0f0f0")
result_label.pack(pady=10)

root.mainloop()