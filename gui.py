
import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title("buttons function")
window.geometry("500x500")

entry = tk.Entry(window, width=18, font=("Arial", 30), borderwidth=1, relief="sunken")
entry.grid(row=0, column=0, columnspan=4)

def update(value):
   current=entry.get()
   entry.delete(0,tk.END)
   entry.insert(tk.END,current + value)
def clear(value):
   entry.delete(0,tk.END)
buttons = [
   '1', '2', '3', '-',
   '4', '5', '6', '*',
    '7', '8', '9', '/',
    '0', '.', '=', '+','C'
]

row = 1
col = 0

for button in buttons:
    if button == '=':
        tk.Button(window, text=button, width=6, height=2,command=lambda value= button: update(value), font=("Arial", 18)).grid(row=row, column=col)
    elif button=='C':
      tk.Button(window, text=button, width=6, height=2,command=lambda value= button: clear(value), font=("Arial", 18)).grid(row=row, column=col)
    else:
        tk.Button(window, text=button, width=6, height=2,command=lambda value= button: update(value), font=("Arial", 18)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()















