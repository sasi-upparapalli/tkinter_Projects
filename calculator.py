import tkinter as tk
from tkinter import StringVar

def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            expression = entry.get()
            result = eval(expression)
            entry.set(result)
        except Exception:
            entry.set("Error")
    elif text == "C":
        entry.set("")
    else:
        entry.set(entry.get() + text)

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x400")

entry = StringVar()

entry_field = tk.Entry(root, textvar=entry, font="Arial 20", bd=5, relief=tk.SUNKEN, justify='right')
entry_field.pack(fill="x", ipadx=8, pady=10, padx=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for btn_text in row:
        button = tk.Button(
            frame, 
            text=btn_text, 
            font="Arial 18", 
            height=2, 
            width=5,
            bg='#CCCCCC' if btn_text not in ['=', 'C', '/', '*', '-', '+'] else '#FFA500'
        )
        button.pack(side="left", padx=5, pady=5)
        button.bind("<Button-1>", click)

root.mainloop()