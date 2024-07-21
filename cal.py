from tkinter import *

main_window = Tk()
main_window.title('Simple calculator')


def clear():
    display_box.delete(0, END)


first_number = 0
math = ''


def calc(math_type):
    global first_number, math
    math = math_type
    first_number = display_box.get()
    clear()


def equal():
    result = ''
    global first_number
    second_number = display_box.get()
    clear()
    if math == 'add':
        result = int(first_number) + int(second_number)
    elif math == 'minus':
        result = int(first_number) - int(second_number)
    elif math == 'div':
        result = int(first_number) / int(second_number)
    elif math == 'mul':
        result = int(first_number) * int(second_number)
    elif math == 'mod':
        result = int(first_number) % int(second_number)
    elif math == 'exp':
        result = int(first_number) ** int(second_number)
    display_box.insert(0, str(result))


def button_clk(num):
    current_num = display_box.get()
    clear()
    final_num = current_num + num
    display_box.insert(0, final_num)


# creating widgets
display_box = Entry(main_window, width=20, font=('Bold', 28), justify=RIGHT)

button_0 = Button(main_window, text='0', padx=39, pady=10, font=('Bold', 14), command=lambda: button_clk('0'))
button_2 = Button(main_window, text='2', padx=39, pady=10, font=('Bold', 14), command=lambda: button_clk('2'))
button_1 = Button(main_window, text='1', padx=39, pady=10, font=('Bold', 14), command=lambda: button_clk('1'))
button_3 = Button(main_window, text='3', padx=39, pady=10, font=('Bold', 14), command=lambda: button_clk('3'))
button_4 = Button(main_window, text='4', padx=39, pady=10, font=('Bold', 14), command=lambda: button_clk('4'))
button_5 = Button(main_window, text='5', padx=39, pady=10, font=('Bold', 14), command=lambda: button_clk('5'))
button_6 = Button(main_window, text='6', padx=39, pady=10, font=('Bold', 14), command=lambda: button_clk('6'))
button_7 = Button(main_window, text='7', padx=39, pady=10, font=('Bold', 14), command=lambda: button_clk('7'))
button_8 = Button(main_window, text='8', padx=41, pady=10, font=('Bold', 14), command=lambda: button_clk('8'))
button_9 = Button(main_window, text='9', padx=39, pady=10, font=('Bold', 14), command=lambda: button_clk('9'))

button_dot = Button(main_window, text='.', padx=41, pady=10, font=('Bold', 14), command=lambda: button_clk('.'))
button_add = Button(main_window, text='+', padx=39, pady=10, font=('Bold', 14), command=lambda: calc('add'))
button_mul = Button(main_window, text='*', padx=36, pady=10, font=('Bold', 14), command=lambda: calc('mul'))
button_div = Button(main_window, text='/', padx=36, pady=10, font=('Bold', 14), command=lambda: calc('div'))
button_clear = Button(main_window, text='CLEAR', padx=63, pady=10, font=('Bold', 14), command=clear)
button_exp = Button(main_window, text='**', padx=36, pady=10, font=('Bold', 14), command=lambda: calc('exp'))
button_minus = Button(main_window, text='-', padx=36, pady=10, font=('Bold', 14), command=lambda: calc('minus'))
button_mod = Button(main_window, text='%', padx=36, pady=10, font=('Bold', 14), command=lambda: calc('mod'))
button_equal = Button(main_window, text='=', padx=32, pady=10, font=('Bold', 14), command=equal)

# displaying or showing thw widgets

button_0.grid(row=5, column=1, padx=2, pady=2)
button_2.grid(row=4, column=1, padx=2, pady=2)
button_5.grid(row=3, column=1, padx=2, pady=2)
button_8.grid(row=2, column=1, padx=2, pady=2)

button_7.grid(row=2, column=0, padx=2, pady=2)
button_4.grid(row=3, column=0, padx=2, pady=2)
button_1.grid(row=4, column=0, padx=2, pady=2)

button_9.grid(row=2, column=2, padx=2, pady=2)
button_6.grid(row=3, column=2, padx=2, pady=2)
button_3.grid(row=4, column=2, padx=2, pady=2)

button_dot.grid(row=5, column=0, padx=2, pady=2)
button_clear.grid(row=1, column=2, columnspan=3, padx=2, pady=2)
button_exp.grid(row=1, column=1, padx=2, pady=2)
button_add.grid(row=5, column=2, padx=2, pady=2)
button_minus.grid(row=4, column=3, padx=2, pady=2)
button_mul.grid(row=3, column=3, padx=2, pady=2)
button_div.grid(row=2, column=3, padx=2, pady=2)
button_equal.grid(row=5, column=3, padx=2, pady=2)
button_mod.grid(row=1, column=0, padx=2, pady=2)

display_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

main_window.mainloop()
