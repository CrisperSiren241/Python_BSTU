import tkinter as tk

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x500")

entry = tk.Entry(root, width=30, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, command=lambda t=text: entry.insert(tk.END, t), font=("Arial", 24))
    button.grid(row=row, column=col, padx=5, pady=5)

clear_button = tk.Button(root, text="Сброс", command=lambda: entry.delete(0, tk.END), font=("Arial", 14))
clear_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

calculate_button = tk.Button(root, text="Вычислить", command=calculate, font=("Arial", 14))
calculate_button.grid(row=5, column=2, columnspan=2, padx=10, pady=10)

root.mainloop()
