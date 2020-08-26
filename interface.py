from tkinter import *
from functools import partial
import os
from subprocess import call

def run_audit(event):
    print("Beginning the OS audit...")
    rc = call("./audit.sh")

def run_bandit(event):
    print("Beginning the static file analyzer...")
    rc = call("./static_analyzer.sh")

def generate_excel_files(event):
    print("Generating excel files from OS audit...\nCheck your local outputs directory for the content...\n")
    rc = os.system("python3 data_munge.py")

window = Tk()

label = Label(
    text="Ethical Security Scanner GUI",
    fg="white",
    bg="black",
    width=40,
    height=20
)
audit_os_button = Button(
    text="Audit the OS",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
audit_static_files_button = Button(
    text="Audit the Static Files",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
generate_excel_files_button = Button(
    text="Generate Excel Files",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
audit_os_button.bind("<Button-1>",  run_audit)
audit_static_files_button.bind("<Button-1>",  run_bandit)
generate_excel_files_button.bind("<Button-1>",  generate_excel_files)

# Pack all GUI features
label.pack()
audit_os_button.pack()
audit_static_files_button.pack()
generate_excel_files_button.pack()

window.mainloop()
