"""
1) Implement the tkinter and webbrowser module
2) create a gui for taking input from the user and create a button to navigate to a browser site.
3) Also display the user entered text in the command prompt with message of navigating to "..." whichever site you chooses

Note:
[you cannot use Google search]
you can use YouTube, etc.
"""

import tkinter as tk
import webbrowser as wb

root = tk.Tk(className="Assignment 10")


label = tk.Label(root, text="Search a place on Google Maps")
label.grid()
entry = tk.Entry(root, font=("Segoe UI", 20), width=30)
entry.grid()

def display():
    place = entry.get()
    print(f"navigating to https://www.google.com/maps/place/{place}")
    wb.open("https://www.google.com/maps/place/" + place)

btn = tk.Button(root, text="Search", font=("Segoe UI", 10), command=display)
btn.grid()


root.mainloop()