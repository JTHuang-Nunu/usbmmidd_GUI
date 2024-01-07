import tkinter as tk
import os
import time

# def
def run_command1():
    os.popen("deviceinstaller64 install usbmmidd.inf usbmmidd")
    
def run_command2():
    os.popen("deviceinstaller64 enableidd 1")

def run_command3():
    os.popen("deviceinstaller64 enableidd 0")

def run_command4():
    os.popen("deviceinstaller64 stop usbmmidd")
    os.popen("deviceinstaller64 remove usbmmid")

# create main window
window = tk.Tk()
window.title("usbmmidd-GUI")
window.geometry("500x100")
window.resizable(0, 0) # can't resize


# create button
button1 = tk.Button(window, text="Power on", command=run_command1, width=10, height=5,font=("Arial", 14))
button2 = tk.Button(window, text="Add monitor", command=run_command2,width=10, height=5,font=("Arial", 14))
button3 = tk.Button(window, text="Delete all", command=run_command3,width=10, height=5,font=("Arial", 14))
button4 = tk.Button(window, text="Power off", command=run_command4,width=10, height=5,font=("Arial", 14))

for i in range(4):
    window.grid_columnconfigure(i, weight=10)
window.grid_rowconfigure(0, weight=10)

# button grid
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=0, column=3)

# run main loop
window.mainloop()
