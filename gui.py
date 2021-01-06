#!/usr/bin/env python

import tkinter as tk
from windowhandler import WindowHandler

def main():
    # Create new window
    parent = WindowHandler()
    parent.set_colors("gray10", "gray15", "gray90")

    parent.start()


if __name__ == "__main__":
    main()