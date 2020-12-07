#!/usr/bin/env python

import tkinter as tk
import converters as cnvrt

elements = {}
TYPES = ["decimal", "hexa", "octa", "string", "binary"]
BASE = [10, 16, 2, 8, 0]
CHARS = "0123456789abcdef"
focus = ""
frames = []


def switch_case(dictionary, arg):
    '''Returns a function from dictionary based on a input string arg.
       Implementation to replace missing switch case in python.'''
    return dictionary.get(arg, "")
    

def handle_string(target):
    string = elements[target]["text"].get("1.0", tk.END)
    elements["binary"]["text"].insert(0, cnvrt.str_to_bina(string))

def update(source):
    '''Updates all fields expect the one that is the source of the event'''
    strings = elements[source]["text"].get("1.0", tk.END).splitlines()
    base = elements[source]["base"] + 1
    # Check if input starts with prefix
    for string in strings:
        if string.startswith("0x") or string.startswith("0b") or string.startswith("0o"):
            string = string[2:]
        for c in string:
            if c.lower() not in CHARS[0:base]:
                return
    for key in elements:
        if key != source:
            f = switch_case(converters, key)
            elements[key]["text"].insert("1.0", f(strings, elements[source]["base"]))

def handle_typing(event, target):
    '''Handler for user input into the fields'''
    #frames[1].grid()
    for key in elements.keys():
        if key != target:
            elements[key]["text"].delete("1.0", tk.END)
    update(target)

def handle_activate(event):
    global focus
    if (event.widget == focus):
        return
    focus = event.widget
    for key in elements.keys():
        elements[key]["text"].delete("1.0", tk.END)


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
            frames.append(frame)
            frame.grid(row=i, column=j, padx=5, pady=5)
            lbl = tk.Label(master=frame, text=TYPES[index], height=1)
            text = tk.Text(master=frame, wrap="word", width=40, height=3, insertbackground="whitesmoke")
            # Assign event handler to the entry field
            text.bind(
                "<KeyRelease>", 
                lambda event, 
                target=TYPES[index]: handle_typing(event, target))
            text.bind("<FocusIn>", handle_activate)
            lbl.pack()
            text.pack()
            elements[TYPES[index]] = {
                "text": text, 
                "lbl": lbl, 
                "base": BASE[index]}
            index += 1
    frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=2
            )
    window.columnconfigure(0, weight=1, minsize=75)
    window.rowconfigure(2, weight=1, minsize=50)
    frame.grid(row=2, columnspan=2)
    lbl = tk.Label(master=frame, text=TYPES[index], height=2)
    text = tk.Text(master=frame, width=43, height=4, wrap="word")
    lbl.pack()
    text.pack()

    btn = tk.Button
    # Calculate window sizes
    window_width = window.winfo_reqwidth()
    window_height = window.winfo_reqheight()
    pos_right = int(window.winfo_screenwidth()/2 - window_width/2)
    pos_down = int(window.winfo_screenheight()/2 - window_height/2)

    # Open tkinter window on the center of the screen by offsetting it
    window.geometry("+{}+{}".format(pos_right,pos_down))

    #frames[1].grid_remove()

    window.mainloop()

# Switches for the switch case
converters = {
    "decimal": cnvrt.decimal,
    "hexa": cnvrt.hexa,
    "binary": cnvrt.binary,
    "octa": cnvrt.octa
}

if __name__ == "__main__":
    main()