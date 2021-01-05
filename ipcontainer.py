import tkinter as tk
from math import ceil
from textwidget import TextWidget
import converters as cnvrt

class IpContainer:
    frames = []
    ip = ""
    mask = ""
    subnet = ""

    def __init__(self, parent, headers, converters, bases=""):
        self.parent = parent
        self.headers = headers
        self.bases = bases
        self.widgets = {}

        self.converters = converters

        self.mainframe = tk.Frame(master=parent, relief=tk.RAISED)

        index = 0
        # Create grid layout and the components
        for i in range(ceil(len(self.headers) / 2)):  # row
            self.mainframe.rowconfigure(i, weight=1)
            for j in range(2):  # column
                self.mainframe.columnconfigure(j, weight=1)
                frame = tk.Frame(
                    master=self.mainframe,
                    relief=tk.RAISED,
                    highlightthickness=2,
                )
                self.frames.append(frame)
                # Cell of the text widget
                frame.grid_rowconfigure(1, weight=1)
                frame.grid_columnconfigure(1, weight=1)

                # Make last cell fill two columns if cell count not divisible
                # by two
                if len(self.headers) % 2 != 0 and index > len(self.headers)-2:
                    frame.grid(row=i, column=j, padx=5, pady=5, sticky="NSEW", columnspan=2)
                else: 
                    frame.grid(row=i, column=j, padx=5, pady=5, sticky="NSEW")

                # Create widgets
                widget = TextWidget(frame, self.headers[index])
                if bases != "":
                    widget.set_base(bases[index])
                
                widget.set_typing_handler(self._handle_typing)

                self.widgets[headers[index]] = widget
                
                index += 1
    
                
    def grid(self):
        self.mainframe.grid(row=0, column=1, sticky="NSEW")

    def forget(self):
        self.mainframe.grid_forget()

    def set_colors(self, bg, lbg, txt):
        '''Set colors of the UI'''
        for frame in self.frames:
            frame.config(bg=lbg, highlightbackground=lbg)
        self.mainframe.config(bg=bg)
        for key in self.widgets:
            self.widgets[key].set_colors(bg, lbg, txt)

    def _handle_typing(self, event, target):
        '''Handler for user input into the fields'''
        #print(event.widget.get("1.0", tk.END))
        strings = self.widgets[target].get_input().split()
        func = self._switch_case(self.converters, target)
        ret = func(strings)
        if target == self.headers[0]:
            self.ip = ret
        elif target == self.headers[1]:
            self.mask = ret

        print(self.mask)
        # Calculate subnet address from input
        if self.ip != "" and self.mask != "":
            func = self._switch_case(self.converters, "Subnet")
            self.subnet = func(self.ip, self.mask)
        else:
            self.subnet = ""
            self.widgets['Subnet'].delete()
            self.widgets["Broadcast"].delete()
            self.widgets["First address"].delete()
            self.widgets["Last address"].delete()

        
        if self.subnet != "":
            self.widgets['Subnet'].delete()
            self.widgets['Subnet'].insert(self.subnet)

            func = self._switch_case(self.converters, "Broadcast")
            ret = func(self.subnet, self.mask)
            self.widgets["Broadcast"].delete()
            self.widgets["Broadcast"].insert(ret)
            
            func = self._switch_case(self.converters, "Last address")
            ret = func(self.subnet, self.mask)
            self.widgets["Last address"].delete()
            self.widgets["Last address"].insert(ret)

            func = self._switch_case(self.converters, "First address")
            ret = func(self.subnet)
            self.widgets["First address"].delete()
            self.widgets["First address"].insert(ret)

                
    def _switch_case(self, dictionary, arg):
        '''Returns a function from dictionary based on a input string arg.
        Implements switch case missing from Python.'''
        return dictionary.get(arg, "")