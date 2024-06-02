from tkinter import *
root = Tk() # Create the root (base) window where all widgets go
w = Label(root, text="Hello, world!") # Create a label with words
w.pack() # Put the label into the window
myButton = Button(root, text="Exit")
myButton.pack()
root.mainloop() # Start the event loop