import tkinter as tk
from math import ceil
from textwidget import TextWidget
from container import Container

class NumContainer(Container):

    def __init__(self, parent, headers, converters, bases=""):
        super().__init__(parent, headers, converters, bases)

    def _handle_typing(self, event, target):
        '''Handler for user input into the fields'''
        for key in self.widgets:
            if key != target:
                self.widgets[key].delete()
        
        strings = self.widgets[target].get_input()
        for key in self.widgets:
            if key != target:
                func = self._switch_case(self.converters, key)
                self.widgets[key].insert(func(strings, self.widgets[target].get_base()))

    def grid(self):
        super().grid()

    def forget(self):
        super().forget()

    def set_colors(self, bg, lbg, txt):
        super().set_colors(bg, lbg, txt)
                
    def _switch_case(self, dictionary, arg):
        return super().switch_case(dictionary, arg)