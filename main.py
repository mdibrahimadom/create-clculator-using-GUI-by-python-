import tkinter as tk
import math

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def insert_text(text):
    entry.insert(tk.END, text)

def calculate_sin():
    try:
        angle = float(entry.get())
        result = math.sin(math.radians(angle))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_cos():
    try:
        angle = float(entry.get())
        result = math.cos(math.radians(angle))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_tan():
    try:
        angle = float(entry.get())
        result = math.tan(math.radians(angle))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_sqrt():
    try:
        num = float(entry.get())
        result = math.sqrt(num)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_log():
    try:
        num = float(entry.get())
        result = math.log(num)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Create the entry field
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Define and create buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("sin", 1, 4), ("cos", 2, 4), ("tan", 3, 4), ("sqrt", 4, 4),
    ("log", 5, 4), ("Clear", 5, 0)
]

for (text, row, column) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, padx=30, pady=20, command=calculate)
    elif text == "Clear":
        btn = tk.Button(root, text=text, padx=20, pady=20, command=clear)
    elif text in ["sin", "cos", "tan"]:
        btn = tk.Button(root, text=text, padx=20, pady=20, command=eval("calculate_" + text))
    elif text == "sqrt":
        btn = tk.Button(root, text=text, padx=20, pady=20, command=calculate_sqrt)
    elif text == "log":
        btn = tk.Button(root, text=text, padx=20, pady=20, command=calculate_log)
    else:
        btn = tk.Button(root, text=text, padx=30, pady=20, command=lambda t=text: insert_text(t))
    btn.grid(row=row, column=column)

root.mainloop()
