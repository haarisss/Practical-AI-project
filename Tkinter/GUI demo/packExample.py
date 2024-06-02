from tkinter import *
# Hold onto a global reference for the root window
root = None
count = 0 # Click counter
def addButton(root, sideToPack):
    global count
    name = "Button "+ str(count) +" "+sideToPack
    button = Button(root, text=name)
    button.pack(side=sideToPack)
    count +=1
def main():
    global root
    root = Tk() # Create the root (base) window where all widgets go
    for i in range(5):
        addButton(root, TOP)
    root.mainloop() # Start the event loop
main()


