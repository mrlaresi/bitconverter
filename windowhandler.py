import tkinter as tk
from framecontainer import FrameContainer
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
        "Subnet": cnvrt.ip,
        "Subnet Mask": cnvrt.mask,
        "Broadcast": cnvrt.broadcast,
        "First address": cnvrt.ip,
        "Last address": cnvrt.ip
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
        frame = FrameContainer(
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

            
    """def _number_converter(self):
        '''Creates the number converter view'''
        index = 0
        elements = {}
        # Create grid layout and the components
        for i in range(3):  # row
            self.frames[self.CONVERTERS[1]]["frame"].rowconfigure(i, weight=1)
            for j in range(2):  # column
                self.frames[self.CONVERTERS[1]]["frame"].columnconfigure(j, weight=1)
                frame = tk.Frame(
                    master=self.frames[self.CONVERTERS[1]]["frame"],
                    relief=tk.RAISED,
                    bg=self.LIGHTERGROUND,
                    highlightthickness=2,
                    highlightbackground=self.LIGHTERGROUND,
                )
                frame.grid_rowconfigure(1, weight=1)
                frame.grid_columnconfigure(1, weight=1)
                if (index > len(self.NUMBERS)-2):
                    frame.grid(
                        row=i, 
                        columnspan=2, 
                        padx=5, 
                        pady=5, 
                        sticky="NSEW"
                    )
                else:
                    frame.grid(row=i, column=j, padx=5, pady=5, sticky="NSEW")
                lbl = tk.Label(
                    master=frame,
                    text=self.NUMBERS[index],
                    height=1,
                    bg=self.LIGHTERGROUND,
                    fg=self.TEXTCOLOR
                )
                text = tk.Text(
                    master=frame,
                    wrap="word",
                    width=40,
                    height=3,
                    bg="gray11",
                    fg=self.TEXTCOLOR,
                    borderwidth=0,
                    insertbackground="whitesmoke"
                )
                if (index > len(self.NUMBERS)-2):
                    text.config(height=5, width=82,)

                # Assign event handler firing on key release to the text field
                text.bind(
                    "<KeyRelease>",
                    lambda event,
                    target=self.NUMBERS[index]: self._handle_typing(event, target)
                )
                # Assign event handler firing on element getting focus to the
                # text field
                text.bind("<FocusIn>", self._handle_activate)
                lbl.pack()
                text.pack(expand=True, fill="both")
                elements[self.NUMBERS[index]] = {
                    "text": text,
                    "lbl": lbl,
                    "base": self.BASE[index]
                }
                index += 1
                if (index > len(self.NUMBERS)-1):
                    break
        self.frames[self.CONVERTERS[1]]["elements"] = elements
        self.active_frame = self.CONVERTERS[1]
    
    def _ip_converter(self):
        index = 0
        elements = {}
        for i in range(3):  # row
            self.frames[self.CONVERTERS[2]]["frame"].rowconfigure(i, weight=1)
            for j in range(2):  # column
                self.frames[self.CONVERTERS[2]]["frame"].columnconfigure(j, weight=1)
                frame = tk.Frame(
                    master=self.frames[self.CONVERTERS[2]]["frame"],
                    relief=tk.RAISED,
                    bg=self.LIGHTERGROUND,
                    highlightthickness=2,
                    highlightbackground=self.LIGHTERGROUND,
                )
                frame.grid_rowconfigure(1, weight=1)
                frame.grid_columnconfigure(1, weight=1)
                frame.grid(row=i, column=j, padx=5, pady=5, sticky="NSEW")

                lbl = tk.Label(
                    master=frame,
                    text=self.IP[index],
                    height=1,
                    bg=self.LIGHTERGROUND,
                    fg=self.TEXTCOLOR
                )
                text = tk.Text(
                    master=frame,
                    wrap="word",
                    width=40,
                    height=3,
                    bg="gray11",
                    fg=self.TEXTCOLOR,
                    borderwidth=0,
                    insertbackground="whitesmoke"
                )
                # Assign event handler firing on key releaseto the text field
                text.bind(
                    "<KeyRelease>",
                    lambda event,
                    target=self.IP[index]: self._handle_typing(event, target)
                )
                # Assign event handler firing on element getting focus to the
                # text field
                text.bind("<FocusIn>", self._handle_activate)
                lbl.pack()
                text.pack(expand=True, fill="both")
                elements[self.IP[index]] = {
                    "text": text,
                    "lbl": lbl
                }
                index += 1
        self.frames[self.CONVERTERS[2]]["elements"] = elements
        self.frames[self.CONVERTERS[2]]["frame"].grid_forget()
        



    def _update(self, source):
        '''Updates all fields expect the one that is the source of the event'''
        elements = self.frames[self.active_frame]["elements"]
        strings = elements[source]["text"].get("1.0", tk.END).split()
        # Check if input starts with prefix and is valid
        for string in strings:
            if string.startswith("0x") or string.startswith("0b") or string.startswith("0o"):
                string = string[2:]

        for key in elements:
            if key != source:
                func = self._switch_case(self.converters, key)
                if "base" in elements[source].keys():
                    elements[key]["text"].insert("1.0", func(strings, elements[source]["base"]))
                else:
                    elements[key]["text"].insert("1.0", func(strings))

    def _handle_typing(self, event, target):
        '''Handler for user input into the fields'''
        elements = self.frames[self.active_frame]["elements"]
        if (self.changed):
            s = event.widget.get("1.0", tk.END)[-2:-1]
            elements[target]["text"].delete("1.0", tk.END)
            event.widget.insert("1.0", s)
            self.changed = False
        for key in elements.keys():
            if key != target:
                elements[key]["text"].delete("1.0", tk.END)
        self._update(target)

    def _handle_activate(self, event):
        if (event.widget == self.focus):
            return
        self.focus = event.widget
        self.changed = True



    def _switch_case(self, dictionary, arg):
        '''Returns a function from dictionary based on a input string arg.
        Implementation to replace missing switch case in python.'''
        return dictionary.get(arg, "")"""
    
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
