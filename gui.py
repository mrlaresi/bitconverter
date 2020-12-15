#!/usr/bin/env python

import tkinter as tk
from windowhandler import WindowHandler

def main():
    # Create new window
    parent = WindowHandler()
    parent.set_colors("gray10", "gray15", "gray90")

    # Calculate window sizes
    '''window_width = window.winfo_reqwidth()
    window_height = window.winfo_reqheight()
    pos_right = int(window.winfo_screenwidth()/2 - window_width/2)
    pos_down = int(window.winfo_screenheight()/2 - window_height/2)

    # Open tkinter window on the center of the screen by offsetting it
    window.geometry("+{}+{}".format(pos_right,pos_down))'''

    parent.start()



if __name__ == "__main__":
    main()