import tkinter as tk
from math import ceil
from textwidget import TextWidget

class FrameContainer:
    frames = []
    changed = False

    def __init__(self, parent, headers, converters, bases=""):
        self.parent = parent
        self.headers = headers
        self.bases = bases
        self.widgets = {}
        self.focus = ""

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
                widget.set_activate_handler(self._handle_activate)

                self.widgets[headers[index]] = widget
                
                index += 1
                if (index > len(self.headers)-1):
                    break

    
                
    def grid(self):
        self.mainframe.grid(row=0, column=1, sticky="NSEW")

    def forget(self):
        self.mainframe.grid_forget()

    def set_colors(self, bg, lbg, txt):
        for frame in self.frames:
            frame.config(bg=lbg, highlightbackground=lbg)
        self.mainframe.config(bg=bg)
        for key in self.widgets:
            self.widgets[key].set_colors(bg, lbg, txt)

    def _handle_typing(self, event, target):
        '''Handler for user input into the fields'''
        #print(event.widget.get("1.0", tk.END))
        if (self.changed):
            #self.widgets[target].reset_input()
            self.changed = False
        for key in self.widgets.keys():
            if key != target:
                self.widgets[key].delete()
        self._update(target)

    def _handle_activate(self, event):
        '''Handler for user changing focused text widget'''
        if (event.widget == self.focus):
            return
        self.focus = event.widget
        self.changed = True

    def _update(self, source):
        '''Updates all fields expect the one that is the source of the event'''
        strings = self.widgets[source].get_input().split()
        for key in self.widgets:
            if key != source:
                func = self._switch_case(self.converters, key)
                self.widgets[key].insert(func(strings, self.widgets[source].get_base()))
                
    def _switch_case(self, dictionary, arg):
        '''Returns a function from dictionary based on a input string arg.
        Implementation to replace missing switch case in python.'''
        return dictionary.get(arg, "")