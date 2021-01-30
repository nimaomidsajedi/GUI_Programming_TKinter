# Created by: Nima Omidsajedi
# HelloWorld window using Tkinter

from tkinter import *

root = Tk() # Must be used in every Kinter project

myLabel = Label(root, text="Hello World!")  # Create a Label widget from Root

# Pack the Label you want to show in the screen
myLabel.pack()

# Loop the project until you end it
root.mainloop()

