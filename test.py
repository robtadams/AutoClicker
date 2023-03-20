# https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter
# https://tkdocs.com/tutorial/grid.html
import tkinter as tk

window = tk.Tk()

def handle_keypress(event):
    print(event.char)

def handle_click(event):
    print("The button was clicked!")

button = tk.Button(text="Click me!")

button.pack()

button.bind("<Button-1>", handle_click)

window.bind("<Key>", handle_keypress)

window.mainloop()
