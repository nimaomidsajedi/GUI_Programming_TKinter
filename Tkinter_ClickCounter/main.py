# Created by: Nima Omidsajedi
# ClickCounter using Tkinter

from tkinter import *

root = Tk() # Must be used in every Kinter project

my_button_1_counter = 0
my_button_2_counter = 0
my_button_total_counter = 0
my_button_counter_result = 0


# Init labels
if my_button_1_counter == 0:
    message_label_increase_init = Label(root, text="You pushed increase button 0 times!")
    message_label_increase_init.grid(row=2, column=1)
if my_button_2_counter == 0:
    message_label_decrease_init = Label(root, text="You pushed decrease button 0 times!", anchor="e")
    message_label_decrease_init.grid(row=3, column=1)
if my_button_total_counter == 0:
    message_label_total_init = Label(root, text="Total clicks: 0 times!", anchor="e")
    message_label_total_init.grid(row=4, column=1)
if my_button_counter_result == 0:
    message_label_counter_init = Label(root, text="Counter value: 0 times!")
    message_label_counter_init.grid(row=5, column=1)


def button_1_func():
    global my_button_1_counter
    global my_button_2_counter
    global my_button_total_counter
    global my_button_counter_result

    my_button_1_counter = 1 + my_button_1_counter
    my_button_total_counter = my_button_1_counter + my_button_2_counter
    my_button_counter_result = my_button_1_counter - my_button_2_counter
    message_label_increase = Label(root, text="You pushed increase button %d times!" % my_button_1_counter, foreground="green")
    message_label_increase.grid(row=2, column=1)
    message_label_total = Label(root, text="Total clicks: %d times!" % my_button_total_counter, foreground="orange")
    message_label_total.grid(row=4, column=1)
    message_label_counter = Label(root, text="Counter value: %d times!" % my_button_counter_result, foreground="purple")
    message_label_counter.grid(row=5, column=1)

def button_2_func():
    global my_button_1_counter
    global my_button_2_counter
    global my_button_total_counter
    global my_button_counter_result

    my_button_2_counter = 1 + my_button_2_counter
    my_button_total_counter = my_button_1_counter + my_button_2_counter
    my_button_counter_result = my_button_1_counter - my_button_2_counter
    message_label = Label(root, text="You pushed decrease button %d times!" % my_button_2_counter, foreground="red")
    message_label.grid(row=3, column=1)
    message_label_total = Label(root, text="Total clicks: %d times!" % my_button_total_counter, foreground="orange")
    message_label_total.grid(row=4, column=1)
    message_label_counter = Label(root, text="Counter value: %d times!" % my_button_counter_result, foreground="purple")
    message_label_counter.grid(row=5, column=1)


# List of Widgets

myLabel_1 = Label(root, text="*First Button*")  # Create a Label widget from Root
myButton_1 = Button(root, text="Increase Button", padx="30", pady="20", command=button_1_func)  # Create a Label widget from Root
myLabel_2 = Label(root, text="*Second Button*")  # Create a Label widget from Root
myButton_2 = Button(root, text="Decrease Button", padx="30", pady="20", command=button_2_func)  # Create a Label widget from Root

# Use Grid for showing the Labels you want in the screen
myLabel_1.grid(row=0, column=0, pady=10)
myButton_1.grid(row=1, column=0)
myLabel_2.grid(row=0, column=2, pady=10)
myButton_2.grid(row=1, column=2)


# Loop the project until you end it
root.mainloop()




