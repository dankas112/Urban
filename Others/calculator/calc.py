import tkinter as tk


# Set functions(+, -, x, /):
def summa():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    result = num1 + num2
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, result)


def subtract():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    result = num1 - num2
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, result)


def multiplication():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    result = num1 * num2
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, result)


def division():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    result = num1 / num2
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, result)


# Display:
window = tk.Tk()
window.title('калькулятор')
window.geometry('360x360')
window.resizable(False, False)
# Buttons:
button_add = tk.Button(window, text='+', width=4, height=2, command=summa)  # +
button_add.place(x=300, y=70)
button_sub = tk.Button(window, text='-', width=4, height=2, command=subtract)  # -
button_sub.place(x=300, y=110)
button_mul = tk.Button(window, text='x', width=4, height=2, command=multiplication)  # *
button_mul.place(x=300, y=150)
button_dif = tk.Button(window, text='/', width=4, height=2, command=division)  # /
button_dif.place(x=300, y=190)
# Entry window:
number1_entry = tk.Entry(window)
number1_entry.place(x=100, y=50)
number1 = tk.Label(window, text='Введите 1e число:')
number1.place(x=100, y=25)

number2_entry = tk.Entry(window)
number2_entry.place(x=100, y=100)
number2 = tk.Label(window, text='Введите 2e число:')
number2.place(x=100, y=75)

answer_entry = tk.Entry(window)
answer_entry.place(x=100, y=150)
number2 = tk.Label(window, text='Ответ:')
number2.place(x=100, y=125)

# if button_add:
#     summa()


window.mainloop()



