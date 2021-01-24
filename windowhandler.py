import tkinter as tk
from numcontainer import NumContainer
from ipcontainer import IpContainer
import converters as cnvrt


class WindowHandler:
    NUMBERS = ["Decimal", "Hexa", "Octa", "String", "Binary"]
    IP = ["IP", "Subnet Mask", "Subnet", "Broadcast", "First address", "Last address"]
    BASE = [10, 16, 8, 0, 2]
    CONVERTERS = ["Menu", "Numbers", "IP adresses"]

    frames = {} # Frames in the main window
    buttons = []

    # Switches for the switch case
    number_converters = {
        "Decimal": cnvrt.decimal,
        "Hexa": cnvrt.hexa,
        "Binary": cnvrt.binary,
        "Octa": cnvrt.octa,
        "String": cnvrt.string,
    }
    ip_converters = {
        "IP": cnvrt.ip,
        "Subnet": cnvrt.subnet,
        "Subnet Mask": cnvrt.mask,
        "Broadcast": cnvrt.broadcast,
        "First address": cnvrt.first_ip,
        "Last address": cnvrt.last_ip
    }

    def __init__(self):
        self.window = tk.Tk(className="Converter")
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=2)

        self._create_frames()
        self.frames[self.CONVERTERS[1]].grid()

    def _create_frames(self):
        '''Creates the base layout for the window'''
        # Create the menu
        self.menu = tk.Frame(master=self.window, relief=tk.RAISED)
        self.menu.grid(row=0, column=0, sticky="NSEW")
        self.menu.grid_rowconfigure(0, weight=1)
        self.menu.grid_columnconfigure(0, weight=1)

        # Number converting view
        frame = NumContainer(
            self.window, 
            self.NUMBERS, 
            self.number_converters, 
            self.BASE
        )
        self.frames[self.CONVERTERS[1]] = frame

        # Ipv4 converting view
        frame = IpContainer(
            self.window, 
            self.IP, 
            self.ip_converters
        )
        self.frames[self.CONVERTERS[2]] = frame

        # Buttons for the menu
        for i in range(1, len(self.CONVERTERS)):
            btn = tk.Button(
                master=self.menu,
                width=20,
                text=self.CONVERTERS[i],
                anchor="nw"
            )
            self.buttons.append(btn)
            btn.pack(fill="x", pady=(5,0), padx=(5,0))
            btn.bind("<Button-1>", self._handle_click)
        # Show number converter by default
        self.active_frame = self.CONVERTERS[1]

    
    def _handle_click(self, event):
        if (event.widget.cget("text") != self.active_frame):
            self.frames[self.active_frame].forget()
            self.active_frame = event.widget.cget("text")
            self.frames[self.active_frame].grid()

    def set_colors(self, bg, lbg, txt):
        self.window.config(bg=bg)
        self.menu.config(bg=bg)
        for key in self.frames:
            self.frames[key].set_colors(bg, lbg, txt)
        for button in self.buttons:
            button.config(bg=lbg, fg=txt,)

    def start(self):
        '''Starts the tkinter instance'''
        self.window.mainloop()
