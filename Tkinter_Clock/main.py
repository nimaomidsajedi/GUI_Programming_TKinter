# Created by: Nima Omidsajedi
# Clock in GUI with Tkinter

from tkinter import *
from time import strftime

root = Tk()

# Window properties
root.title('Clock')
root.resizable(0,0)  # Remove the maximize button
root.configure(bg='black')


# Define Functions
def system_time():
    time_label.config(text=strftime('%I:%M:%S %p'))
    time_label.after(1000, system_time)
def system_date():
    date_label.config(text=strftime("%Y/%m/%d\n%A"))


# Define Widgets
time_label = Label(root, font=("Arial", 50), background="black", foreground="lime")
date_label = Label(root, font=("Arial", 50), background="black", foreground="lime")

# Define Widgets positions
time_label.grid(row=0, column=0)
date_label.grid(row=1, column=0)

# Call Functions
system_time()
system_date()

mainloop()
