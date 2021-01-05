import tkinter as tk

class TextWidget:
    '''Class creates Label and Text field, which are parented to the parent
    parameter. Handles inserting and removing text from the widget.'''
    def __init__(self, parent, header, base=0):
        self.parent = parent
        self.header = header
        self.base = base

        self.lbl = tk.Label(master=parent, text=self.header, height=1)
        self.txt = tk.Text(master=parent, wrap="word", width=40, 
                            height=3,borderwidth=0)

        self.lbl.pack()
        self.txt.pack(expand=True, fill="both")

    def reset_input(self):
        '''Removes input from the active widget leaving only the character
        typed in last. Called upon when user switches text widget and starts
        typing in it.'''
        s = self.txt.get("1.0", tk.END)[-2:-1]
        self.txt.delete("1.0", tk.END)
        self.txt.insert("1.0", s)

    def insert(self, stri):
        '''Inserts text to the text widget'''
        self.txt.insert("1.0", stri)

    def delete(self):
        '''Deletes text from the widget'''
        self.txt.delete("1.0", tk.END)

    # --------------------------------------------
    #       Getters
    # --------------------------------------------

    def get_input(self):
        '''Return the text contained in the widget'''
        return self.txt.get("1.0", tk.END)

    def get_base(self):
        '''Return the base of the stored number'''
        return self.base

    # --------------------------------------------
    #       Setters
    # --------------------------------------------

    def set_typing_handler(self, func):
        '''Set event handler for user input into the text widget'''
        self.txt.bind(
            "<KeyRelease>",
            lambda event,
            target=self.header: func(event, target)
        )

    def set_base(self, base):
        '''Sets the base of the number for conversions'''
        self.base = base

    def set_colors(self, bg, lbg, txt):
        '''Sets color scheme of the widgets'''
        self.lbl.config(bg=lbg, fg=txt)
        self.txt.config(bg=bg, fg=txt, insertbackground=txt)