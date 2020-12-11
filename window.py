import tkinter as tk
import converters as cnvrt


class WindowHandler:
    window = ""
    background = "gray10"
    frames = []
    TYPES = ["decimal", "hexa", "octa", "string", "binary"]
    BASE = [10, 16, 8, 0, 2]
    focus = ""
    changed = False
    elements = {}

        # Switches for the switch case
    converters = {
        "decimal": cnvrt.decimal,
        "hexa": cnvrt.hexa,
        "binary": cnvrt.binary,
        "octa": cnvrt.octa,
        "string": cnvrt.string
    }

    def __init__(self):
        self.window = tk.Tk(className="Converter")
        self.window.configure(bg=self.background)

        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=3)
        for i in range(0, 2):
            frame = tk.Frame(
                master=self.window,
                relief=tk.RAISED,
                bg=self.background,
            )
            self.frames.append(frame)
            frame.grid(row=0, column=i, sticky="NSEW")
            frame.grid_rowconfigure(0, weight=1)
            frame.grid_columnconfigure(0, weight=1)
        for i in range(0,2):
            label = tk.Label(
                master=self.frames[0],
                text="asd",
                anchor="nw"
            )
            label.pack()

    def number_converter(self):
        index = 0
        # Create grid layout and the components
        for i in range(3):  # row
            self.frames[1].rowconfigure(i, weight=1)
            for j in range(2):  # column
                self.frames[1].columnconfigure(j, weight=1)
                frame = tk.Frame(
                    master=self.frames[1],
                    relief=tk.RAISED,
                    bg="gray15",
                    highlightthickness=2,
                    highlightbackground="gray15",
                )
                # frames.append(frame)
                frame.grid_rowconfigure(1, weight=1)
                frame.grid_columnconfigure(1, weight=1)
                if (index > len(self.TYPES)-2):
                    frame.grid(row=i, columnspan=2, padx=5,
                               pady=5,     sticky="NSEW")
                else:
                    frame.grid(row=i, column=j, padx=5, pady=5, sticky="NSEW")
                lbl = tk.Label(
                    master=frame,
                    text=self.TYPES[index],
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
                if (index > len(self.TYPES)-2):
                    text.config(height=5, width=82,)

                # Assign event handler firing on key releaseto the text field
                text.bind(
                    "<KeyRelease>",
                    lambda event,
                    target=self.TYPES[index]: self._handle_typing(event, target)
                )
                # Assign event handler firing on element getting focus to the text
                # field
                text.bind("<FocusIn>", lambda event: self._handle_activate(event))
                lbl.pack()
                text.pack(expand=True, fill="both")
                self.elements[self.TYPES[index]] = {
                    "text": text,
                    "lbl": lbl,
                    "base": self.BASE[index]
                }
                index += 1
                if (index > len(self.TYPES)-1):
                    break



    def _update(self, source):
        '''Updates all fields expect the one that is the source of the event'''
        strings = self.elements[source]["text"].get("1.0", tk.END).split()
        base = self.elements[source]["base"] + 1
        # Check if input starts with prefix and is valid
        for string in strings:
            if string.startswith("0x") or string.startswith("0b") or string.startswith("0o"):
                string = string[2:]

        for key in elements:
            if key != source:
                f = switch_case(converters, key)
                self.elements[key]["text"].insert("1.0", f(strings, self.elements[source]["base"]))

    def switch_case(self, dictionary, arg):
        '''Returns a function from dictionary based on a input string arg.
        Implementation to replace missing switch case in python.'''
        return dictionary.get(arg, "")
    

    def mainloop(self):
        self.window.mainloop()
