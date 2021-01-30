# Created by: Nima Omidsajedi
# Calculator in GUI with Tkinter

from tkinter import *
from tkinter import font as tkFont  # for convenience

root = Tk()  # Must be used in every Tkinter project
root.title('Calculator')
root.resizable(0,0) # Remove the maximize button


##################################################
# Define font
cal_font = tkFont.Font(family='Arial', size=15, weight=tkFont.BOLD)

##################################################
# Define functions

def button_click(number):
   current = cal_input.get()
   cal_input.delete(0, END)
   cal_input.insert(0, str(current) + str(number))


def button_clear():
   cal_input.delete(0, END)


def button_add():
   first_num = cal_input.get()
   global fir_num
   global operand
   operand = "add"
   fir_num = float(first_num)
   cal_input.delete(0, END)


def button_sub():
   first_num = cal_input.get()
   global fir_num
   global operand
   operand = "sub"
   fir_num = float(first_num)
   cal_input.delete(0, END)


def button_dev():
   first_num = cal_input.get()
   global fir_num
   global operand
   operand = "dev"
   fir_num = float(first_num)
   cal_input.delete(0, END)


def button_mult():
   first_num = cal_input.get()
   global fir_num
   global operand
   operand = "mult"
   fir_num = float(first_num)
   cal_input.delete(0, END)


def button_power():
   first_num = cal_input.get()
   global fir_num
   global operand
   operand = "power"
   fir_num = float(first_num)
   cal_input.delete(0, END)

def button_equal():
    second_num = cal_input.get()
    cal_input.delete(0, END)
    if operand == "add":
        cal_input.insert(0, fir_num + float(second_num))
    elif operand == "sub":
        cal_input.insert(0, fir_num - float(second_num))
    elif operand == "dev":
        cal_input.insert(0, fir_num / float(second_num))
    elif operand == "mult":
        cal_input.insert(0, fir_num * float(second_num))
    elif operand == "power":
        cal_input.insert(0, fir_num ** float(second_num))


##################################################
# Define Widgets


cal_input = Entry(root, width=60, borderwidth=5)

btn_1 = Button(root, text="1", padx=50, pady=20, font=cal_font, command=lambda: button_click(1))
btn_2 = Button(root, text="2", padx=50, pady=20, font=cal_font, command=lambda: button_click(2))
btn_3 = Button(root, text="3", padx=50, pady=20, font=cal_font, command=lambda: button_click(3))

btn_4 = Button(root, text="4", padx=50, pady=20, font=cal_font, command=lambda: button_click(4))
btn_5 = Button(root, text="5", padx=50, pady=20, font=cal_font, command=lambda: button_click(5))
btn_6 = Button(root, text="6", padx=50, pady=20, font=cal_font, command=lambda: button_click(6))

btn_7 = Button(root, text="7", padx=50, pady=20, font=cal_font, command=lambda: button_click(7))
btn_8 = Button(root, text="8", padx=50, pady=20, font=cal_font, command=lambda: button_click(8))
btn_9 = Button(root, text="9", padx=50, pady=20, font=cal_font, command=lambda: button_click(9))

btn_0 = Button(root, text="0", padx=50, pady=20, font=cal_font, command=lambda: button_click(0))
btn_add = Button(root, text="+", padx=49, pady=20, font=cal_font, command=button_add)
btn_sub = Button(root, text="-", padx=51, pady=20, font=cal_font, command=button_sub)

btn_dev = Button(root, text="/", padx=52, pady=20, font=cal_font, command=button_dev)
btn_mult = Button(root, text="*", padx=51, pady=20, font=cal_font, command=button_mult)
btn_power = Button(root, text="power", padx=25, pady=20, font=cal_font, command=button_power)

btn_dot = Button(root, text=".", padx=52, pady=20, font=cal_font, command=lambda: button_click("."))
btn_clear = Button(root, text="Clear", padx=30, pady=20, font=cal_font, command=button_clear, bg="red")
btn_equal = Button(root, text="=", padx=50, pady=20, font=cal_font, command=button_equal, bg="green")



cal_input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
btn_0.grid(row=4, column=0)
btn_add.grid(row=4, column=1)
btn_sub.grid(row=4, column=2)
btn_dev.grid(row=5, column=0)
btn_mult.grid(row=5, column=1)
btn_power.grid(row=5, column=2)
btn_dot.grid(row=6, column=0)
btn_clear.grid(row=6, column=1)
btn_equal.grid(row=6, column=2)


root.mainloop()
