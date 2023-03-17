import tkinter as tk
#https://tkdocs.com/tutorial/grid.html

events = []

def handle_keypress(event):
    print(event.char)

while True:
    if events == []:
        continue

    event = events[0]

    if event.type == "keypress":
        handle_keypress(event)
