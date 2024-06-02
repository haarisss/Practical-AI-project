from tkinter import *
# Hold onto a global reference for the root window
root = None
def buttonPushed():
    global root
    root.destroy() # Kill the root window!
def main():
    global root
    root = Tk() # Create the root (base) window where all widgets go
    w = Label(root, text="Hello, world!") # Create a label with words
    w.pack() # Put the label into the window
    myButton = Button(root, text="Exit",command=buttonPushed)
    myButton.pack()
    root.mainloop() # Start the event loop
main()
