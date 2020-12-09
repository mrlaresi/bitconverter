#!/usr/bin/env python

import tkinter as tk
import converters as cnvrt

elements = {}
TYPES = ["decimal", "hexa", "octa", "string", "binary"]
BASE = [10, 16, 8, 0, 2]
CHARS = "0123456789abcdef"
focus = ""
changed = False
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
    strings = elements[source]["text"].get("1.0", tk.END).split()
    base = elements[source]["base"] + 1
    # Check if input starts with prefix and is valid
    for string in strings:
        if string.startswith("0x") or string.startswith("0b") or string.startswith("0o"):
            string = string[2:]

    for key in elements:
        if key != source:
            f = switch_case(converters, key)
            elements[key]["text"].insert("1.0", f(strings, elements[source]["base"]))

def handle_typing(event, target):
    '''Handler for user input into the fields'''
    global changed
    if (changed):
        s = event.widget.get("1.0", tk.END)[-2:-1]
        elements[target]["text"].delete("1.0", tk.END)
        event.widget.insert("1.0", s)
        changed = False
    for key in elements.keys():
        if key != target:
            elements[key]["text"].delete("1.0", tk.END)
    update(target)

def handle_activate(event):
    global focus
    global changed
    if (event.widget == focus):
        return
    focus = event.widget
    changed = True


def main():
    # Create new window
    window = tk.Tk(className="Converter")
    window.configure(bg="gray10")

    index = 0
    # Create grid layout and the components
    for i in range(3): #row
        window.rowconfigure(i, weight=1)
        for j in range(2): #column
            window.columnconfigure(j, weight=1)
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                bg="gray15",
                highlightthickness=2,
                highlightbackground="gray15",
            )
            frames.append(frame)
            frame.grid_rowconfigure(1, weight=1)
            frame.grid_columnconfigure(1, weight=1)
            if (index > len(TYPES)-2):
                frame.grid(row=i, columnspan=2, padx=5, pady=5, sticky="NSEW")
            else:
                frame.grid(row=i, column=j, padx=5, pady=5, sticky="NSEW")
            lbl = tk.Label(
                master=frame, 
                text=TYPES[index], 
                height=1,
                bg="gray15",
                fg="gray90"
            )
            text = tk.Text(
                master=frame, 
                wrap="word", 
                width=40, 
                height=3, 
                bg="gray11",
                fg="gray90",
                borderwidth=0,
                insertbackground="whitesmoke"
            )
            if (index > len(TYPES)-2):
                text.config(height=5, width=82,)
            

            # Assign event handler firing on key releaseto the text field
            text.bind(
                "<KeyRelease>", 
                lambda event, 
                target=TYPES[index]: handle_typing(event, target)
            )
            # Assign event handler firing on element getting focus to the text
            # field
            text.bind("<FocusIn>", handle_activate)
            lbl.pack()
            text.pack(expand=True, fill="both")
            elements[TYPES[index]] = {
                "text": text, 
                "lbl": lbl, 
                "base": BASE[index]
            }
            index += 1
            if (index > len(TYPES)-1): 
                break


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
    "octa": cnvrt.octa,
    "string": cnvrt.string
}

if __name__ == "__main__":
    main()