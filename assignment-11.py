"""
Create a gui based form to take input from the user and then navigate to the particular site from where the user came to know about the content

for example:
create a form where the user is enquiring about the respective course
and in the form there is an option for asking where the user came to know about it, for eg: instagram ads or YouTube ads

and then when clicking the submit button
take the user to the faq page of that site
"""

import tkinter as tk
import webbrowser as wb

root = tk.Tk(className="Assignment 11")

label1 = tk.Label(root, text="Netflix Form", font=(50))
label1.grid()

label2 = tk.Label(root, text="First Name: ")
label2.grid()
entry1 = tk.Entry(root, width=20)
entry1.grid()

label3 = tk.Label(root, text="Last Name: ")
label3.grid()
entry2 = tk.Entry(root, width=20)
entry2.grid()

label4 = tk.Label(root, text="Email: ")
label4.grid()
entry3 = tk.Entry(root, width=20)
entry3.grid()

label5 = tk.Label(root, text="Enter Movie/TV Series Name: ")
label5.grid()
entry4 = tk.Entry(root, width=20)
entry4.grid()

label6 = tk.Label(root, text="Select the website where you got to know about us?")
label6.grid()
error_label = tk.Label(root)
error_label.grid()

selection = tk.StringVar()
dropdown = tk.OptionMenu(root, selection, "Youtube Ads", "Facebook Ads", "Instagram Ads")
dropdown.grid()

urls = {
    "YouTube Ads": "https://support.google.com/youtube/?hl=en#topic=9257498",
    "Facebook Ads": "https://www.facebook.com/help",
    "Instagram Ads": "https://help.instagram.com/",
}

def on_submit():
    if entry1.get() == None or entry2.get() == None or entry3.get() == None or entry4.get() == None:
        error_label["text"] = "invalid information provided."
    else:
        url = urls[selection.get()]
        try:
            with open("backend.txt", "+a") as f:
                f.writelines(f"first_name: {entry1.get()}\nlast_name: {entry2.get()}\nemail: {entry3.get()}\ncontent: {entry4.get()}\nwebsite: {selection.get()}")
        except IOError:
            print("an error occurred.")
        
        wb.open(url)
        wb.open("https://help.netflix.com/en")

btn = tk.Button(root, text="Submit Form", command=on_submit)
btn.grid()

tk.mainloop()

