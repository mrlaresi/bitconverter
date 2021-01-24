import tkinter as tk
from textwidget import TextWidget
import converters as cnvrt
from container import Container

class IpContainer(Container):
    ip = ""
    mask = ""
    subnet = ""

    def __init__(self, parent, headers, converters, bases=""):
        super().__init__(parent, headers, converters, bases)

    def _handle_typing(self, event, target):
        '''Handler for user input into the fields'''
        strings = self.widgets[target].get_input()
        func = self._switch_case(self.converters, target)
        ret = func(strings)
        if target == self.headers[0]:
            self.ip = ret
        elif target == self.headers[1]:
            self.mask = ret

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
                
    def grid(self):
        super().grid()

    def forget(self):
        super().forget()

    def set_colors(self, bg, lbg, txt):
        super().set_colors(bg, lbg, txt)

    def _switch_case(self, dictionary, arg):
        return super().switch_case(dictionary, arg)