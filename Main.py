import tkinter as tk
from tkinter import messagebox

# Create the main application window
app = tk.Tk()
app.title("Student Marksheet")
app.geometry("700x500")

def calculate_results():
    # Define grade to points mapping
    grade_to_points = {"A": 10, "B": 9, "C": 8, "D": 7, "P": 6, "F": 0}
    total_points = 0
    total_credits = 0
    
    try:
        for i in range(4):
            grade = grade_entries[i].get().upper()
            credits = int(credit_entries[i].get())
            if grade in grade_to_points:
                points = grade_to_points[grade] * credits
                total_points += points
                total_credits += credits
                result_labels[i].config(text=f"{points}")
            else:
                result_labels[i].config(text="Invalid Grade")
        
        if total_credits == 0:
            raise ValueError("Total credits cannot be zero.")
        
        sgpa = total_points / total_credits
        total_credits_label.config(text=str(total_credits))
        sgpa_label.config(text=f"{sgpa:.2f}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Frame for student information
info_frame = tk.Frame(app, padx=20, pady=20)
info_frame.pack(side=tk.TOP, fill=tk.X)

tk.Label(info_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(info_frame, text="Registration Number:").grid(row=1, column=0, padx=5, pady=5)
tk.Label(info_frame, text="Roll Number:").grid(row=2, column=0, padx=5, pady=5)

name_entry = tk.Entry(info_frame)
reg_entry = tk.Entry(info_frame)
roll_entry = tk.Entry(info_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)
reg_entry.grid(row=1, column=1, padx=5, pady=5)
roll_entry.grid(row=2, column=1, padx=5, pady=5)

# Frame for subject information
subject_frame = tk.Frame(app, padx=20, pady=10)
subject_frame.pack(side=tk.TOP, fill=tk.X)

tk.Label(subject_frame, text="Subject").grid(row=0, column=0, padx=5, pady=5)
tk.Label(subject_frame, text="Credits").grid(row=0, column=1, padx=5, pady=5)
tk.Label(subject_frame, text="Grade").grid(row=0, column=2, padx=5, pady=5)
tk.Label(subject_frame, text="Points").grid(row=0, column=3, padx=5, pady=5)

subjects = ["CS 101", "MA 101", "PH 101", "EC 101"]
grade_entries = []
credit_entries = []
result_labels = []

for i, subject in enumerate(subjects):
    tk.Label(subject_frame, text=subject).grid(row=i+1, column=0, padx=5, pady=5)
    
    credit_entry = tk.Entry(subject_frame)
    credit_entry.grid(row=i+1, column=1, padx=5, pady=5)
    credit_entries.append(credit_entry)
    
    grade_entry = tk.Entry(subject_frame)
    grade_entry.grid(row=i+1, column=2, padx=5, pady=5)
    grade_entries.append(grade_entry)
    
    result_label = tk.Label(subject_frame, text="0")
    result_label.grid(row=i+1, column=3, padx=5, pady=5)
    result_labels.append(result_label)

# Frame for results
result_frame = tk.Frame(app, padx=20, pady=20)
result_frame.pack(side=tk.TOP, fill=tk.X)

tk.Label(result_frame, text="Total Credits:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(result_frame, text="SGPA:").grid(row=1, column=0, padx=5, pady=5)

total_credits_label = tk.Label(result_frame, text="0")
total_credits_label.grid(row=0, column=1, padx=5, pady=5)

sgpa_label = tk.Label(result_frame, text="0.00")
sgpa_label.grid(row=1, column=1, padx=5, pady=5)

# Calculate button
calculate_button = tk.Button(result_frame, text="Calculate", command=calculate_results, bg="blue", fg="white")
calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

# Run the application
app.mainloop()
