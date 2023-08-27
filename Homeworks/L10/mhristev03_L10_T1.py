import tkinter as tk

def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        
        bmi = weight / (height ** 2)
        lbl_result.config(text=f"Your BMI: {round(bmi, 2)}")
        
    except ValueError:
        lbl_result.config(text="Please enter valid values")


root = tk.Tk()
root.title("BMI Calculator")

lbl_height = tk.Label(root, text="Height (m):")
lbl_height.pack()

entry_height = tk.Entry(root)
entry_height.pack()

lbl_weight = tk.Label(root, text="Weight (kg):")
lbl_weight.pack()

entry_weight = tk.Entry(root)
entry_weight.pack()

btn_calculate = tk.Button(root, text="Calculate", command=calculate_bmi)
btn_calculate.pack()

lbl_result = tk.Label(root, text="")
lbl_result.pack()

root.mainloop()
