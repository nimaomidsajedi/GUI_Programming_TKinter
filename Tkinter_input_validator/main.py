# Created by: Nima Omidsajedi
# Input data validator in GUI with Tkinter

from tkinter import *

root = Tk()  # Must be used in every Tkinter project
root.title('Age validator')
root.geometry("300x300")


# List of functions

def age_function():
    try:
        age = int(age_entry.get())
        if age < 0:
            age_label.config(text="Your age: %d years old \n"
                                  " Sorry you have not been born yet! \n"
                                  " Please come back when you entered to Earth!" % age, fg="purple")
        elif age >= 0 and age <= 2:
            age_label.config(text="Your age: %d years old \n"
                                  " You are too young to use Python! \n"
                                  " Please come back when you learned to talk!" % age, fg="orange")
        elif age > 150:
            age_label.config(text="Your age: %d years old \n"
                                  " Wow you really lived this long!? \n"
                                  " I would be happy to know your long life secret! \n"
                                  " BTW welcome on board!" % age, fg="brown")
        else:
            age_label.config(text="Your age: %d years old \n"
                                  "Finally someone normal to use Python! \n"
                                  "Welcome to the Python developer community!" % age, fg="green")
    except ValueError:
        age_label.config(text="I said enter your age genius! In number!", fg="red")


# List of Widgets

age_label_req = Label(root, text="Enter your age in number to continue:")  # Create a Label widget from Root
age_entry = Entry(root, width=50, borderwidth=1, bg="green", fg="white")
age_button = Button(root, text="Enter you age", padx="30", pady="20", command=age_function)  # Create a Label widget from Root
age_label = Label(root, text="")


# Use Grid for showing the Widgets you want in the screen
age_label_req.grid(row=0, column=0, pady=10)
age_entry.grid(row=1, column=0)
age_button.grid(row=2, column=0, pady=10)
age_label.grid(row=3, column=0, pady=10)

# Loop the project until you end it
root.mainloop()




