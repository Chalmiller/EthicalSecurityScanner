from tkinter import *
from functools import partial
from subprocess import call

def run_audit(event):
    print("Beginning the OS audit...")
    rc = call("./audit.sh")

def run_bandit(event):
    print("Beginning the static file analyzer...")
    rc = call("./static_analyzer.sh")

window = Tk()

label = Label(
    text="Ethical Security Scanner GUI",
    fg="white",
    bg="black",
    width=40,
    height=20
)
audit_button = Button(
    text="Audit the OS",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
audit_button.bind("<Button-1>",  run_audit)

# Pack all GUI features
label.pack()
audit_button.pack()

window.mainloop()
