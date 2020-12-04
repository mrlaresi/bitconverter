#!/usr/bin/env python

import tkinter as tk
import converters as cnvrt

elements = {}
types = ["decimal", "hexa", "binary", "string"]


def switch_case(arg):
    '''Implementation for switch cases using dictionary'''
    switch = switches.get(arg, "")
    switch(arg)


def handle_decimal(target):
    string = elements[target]["ent"].get()
    elements["binary"]["ent"].insert(0, cnvrt.deci_to_bina(string))
    elements["hexa"]["ent"].insert(0, cnvrt.deci_to_hexa(string))
    
def handle_hexa(target):
    string = elements[target]["ent"].get()
    elements["binary"]["ent"].insert(0, cnvrt.hex_to_bina(string))
    elements["decimal"]["ent"].insert(0, cnvrt.hex_to_deci(string))

def handle_binary(target):
    string = elements[target]["ent"].get()
    elements["decimal"]["ent"].insert(0, cnvrt.bina_to_deci(string))
    elements["hexa"]["ent"].insert(0, cnvrt.bina_to_hexa(string))

def handle_string(target):
    string = elements[target]["ent"].get()
    elements["binary"]["ent"].insert(0, cnvrt.str_to_bina(string))


def handle_typing(event, target):
    '''Handler for user input into the fields'''
    for key in elements.keys():
        if key != target:
            elements[key]["ent"].delete(0, tk.END)
    switch_case(target)

def handle_activate(event):
    for key in elements.keys():
        elements[key]["ent"].delete(0, tk.END)


def main():
    # Create new window
    window = tk.Tk()

    index = 0
    # Create grid layout and the components
    for i in range(2):
        window.columnconfigure(i, weight=1, minsize=75)
        for j in range(2):
            window.rowconfigure(j, weight=1, minsize=50)
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=2
            )
            frame.grid(row=i, column=j, padx=5, pady=5)
            lbl = tk.Label(master=frame, text=types[index], height=2)
            ent = tk.Entry(master=frame, width=20, insertbackground="whitesmoke")
            # Assign event handler to the entry field
            ent.bind("<KeyRelease>", lambda event, target=types[index]: handle_typing(event, target))
            ent.bind("<FocusIn>", handle_activate)
            lbl.pack()
            ent.pack()
            elements[types[index]] = {"ent": ent, "lbl": lbl}
            index += 1

    # Calculate window sizes
    window_width = window.winfo_reqwidth()
    window_height = window.winfo_reqheight()
    pos_right = int(window.winfo_screenwidth()/2 - window_width/2)
    pos_down = int(window.winfo_screenheight()/2 - window_height/2)

    # Open tkinter window on the center of the screen by offsetting it
    window.geometry("+{}+{}".format(pos_right,pos_down))

    window.mainloop()

# Switches for the switch case. Must be at the bottom of the file to work.
switches = {
    "decimal": handle_decimal,
    "hexa": handle_hexa,
    "binary": handle_binary,
    "string": handle_string
}

if __name__ == "__main__":
    main()