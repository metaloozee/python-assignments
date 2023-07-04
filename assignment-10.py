import tkinter as tk
import webbrowser as wb

root = tk.Tk(className="Assignment 10")


label = tk.Label(root, text="Search a place on Google Maps")
label.grid()
entry = tk.Entry(root, font=("Segoe UI", 20), width=30)
entry.grid()

def display():
    place = entry.get()
    wb.open("https://www.google.com/maps/place/" + place)
    
btn = tk.Button(root, text="Search", font=("Segoe UI", 10), command=display)
btn.grid()


root.mainloop()