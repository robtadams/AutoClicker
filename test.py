#https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter

import tkinter as tk
import tkinter.ttk as ttk
import time

def main():
    window = tk.Tk()

    """
    label = tk.Label(
        text="Hello, Tkinter",
        foreground="white", # Set the text color to white
        background="red",   # Set the background color to red
        width=100,
        height=10
    )
    """

    """
    button = tk.Button(
        text = "Click me!",
        width = 25,
        height = 5,
        bg = "blue",
        fg = "red"
    )
    """
    label = tk.Label(text="Name")
    entry = tk.Entry()
    label.pack()
    entry.pack()
    while window.mainloop():
        entry.get()
        print(entry)

if __name__ == "__main__":
    main()
