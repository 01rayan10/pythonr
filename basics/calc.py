import tkinter as tk
from tkinter import ttk

def on_click(btn_text):
    if btn_text == "C":
        entry_var.set("")
    elif btn_text == "=":
        expr = entry_var.get()
        try:
        
            result = eval(expr)
            entry_var.set(str(result))
        except Exception:
            entry_var.set("Error")
    else:
        entry_var.set(entry_var.get() + btn_text)

root = tk.Tk()
root.title("calc")

entry_var = tk.StringVar()
entry = ttk.Entry(root, textvariable=entry_var, font=("Segoe UI", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+",
    "C","(",")","**"
]

r = 1
c = 0
for b in buttons:
    cmd = lambda x=b: on_click(x)
    ttk.Button(root, text=b, command=cmd).grid(row=r, column=c, ipadx=10, ipady=10, sticky="nsew", padx=2, pady=2)
    c += 1
    if c > 3:
        c = 0
        r += 1

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(r+1):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()