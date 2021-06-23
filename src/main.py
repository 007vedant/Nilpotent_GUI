import sys
import tkinter as tk
from tkinter import messagebox
from gui import main

"""
    Project: Check if Matrix is Nilpotent
    Course: Advanced Control Systems (EE2002)
    Developer: Vedant Raghuwanshi (118EE0705)

"""


def create_gui_layout(win):
    def cmd():
        try:
            sz = int(inp1.get())
            win.destroy()
            main(sz)
        except ValueError:
            tk.messagebox.showinfo("Error", "Please enter a valid value.")

    def show_info():
        messagebox.showinfo(
            "HELP",
            " Developer: Vedant Raghuwanshi(118EE0705).\n"
            " Project: Check if the matrix is Nilpotent.\n"
            " Course: Advanced Control System (EE2002). ",
        )

    def show_help():
        messagebox.showinfo(
            "HELP",
            " Enter the size of your input matrix inside the box and click Run.\n"
            " A window will popup with a matrix of the given size, with all the default values as inf.\n"
            " Click on each cell, enter the number you want to input in that cell and press Enter to fix it inside the cell.\n"
            " After you have entered all the numbers for the matrix, press Space.\n"
            " A window will popup with the message about the kind of matrix.\n \n"
            " Please go through README.txt to know more. !",
        )

    # Input Widget to get matrix size
    l1 = tk.Label(win, text="Enter Size of Matrix")
    l1.grid(row=0, column=0)
    inp1 = tk.Entry(win)
    inp1.grid(row=0, column=1)

    # Button to call gui runtime
    b1 = tk.Button(win, text="Run", command=cmd)
    b1.grid(row=2, column=1)

    # Button to show help
    b2 = tk.Button(win, text="Help?", command=show_help)
    b2.place(x=5, y=70)

    # Button to show developer info
    b3 = tk.Button(win, text="Info!", command=show_info)
    b3.place(x=220, y=70)


win = tk.Tk()
win.title("IsNilpotent App")
win.geometry("260x100")
win.resizable(False, False)

create_gui_layout(win)

win.mainloop()
sys.exit()
