import tkinter as tk
from tkinter import *

# new window
def newWindow():
    root = tk.Tk()
    root.title("3d areodynamics simulator")
    root.geometry("1000x1000") 
    rootFrame = root.Frame(root)
    root.Button(rootFrame, text="Add Model",command=root.destroy ).grid(column = 1,row = 0)
    root.mainloop()
    return root

# Main
root = newWindow()
