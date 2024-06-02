from tkinter import *
# Hold onto a global reference for the root window
root = None
# Hold onto the Text Entry Box also
entryBox = None
def buttonPushed():
    global entryBox
    txt = entryBox.get()
    print("The text is:" + txt)
def createTextBox(parent):
    global entryBox
    entryBox = Entry(parent)
    entryBox.pack()
def main():
    global root
    root = Tk() # Create the root (base) window where all widgets go
    myButton = Button(root, text="Show Text",command=buttonPushed)
    myButton.pack()
    createTextBox(root)
    root.mainloop() # Start the event loop
main()
