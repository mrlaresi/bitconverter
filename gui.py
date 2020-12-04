#!/usr/bin/python

import tkinter as tk

# Create new window
window = tk.Tk()

elements = {}

index = 0
# Create grid layout and the components
for i in range(2):
    window.columnconfigure(i, weight=1, minsize=75)
    for j in range(2):
        window.rowconfigure(j, weight=1, minsize=50)
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        lbl = tk.Label(master=frame, text="Tekstiloota")
        ent = tk.Entry(master=frame, width=5)
        lbl.pack()
        ent.pack()
        elements[i] = {"ent": ent, "lbl": lbl}
        index += 1
        

'''lbl_deci
ent_deci
lbl_hexa
ent_hexa
lbl_bina
ent_bina
lbl_str
ent_str'''

window.mainloop()