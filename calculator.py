from tkinter import *

def append_symbol(symbol):
    input_field.insert("end", symbol)

def calculate():
    try:
        expression = input_field.get()
        result = eval(expression)
        word.config(text="Result: " + str(result))
    except Exception as e:
        word.config(text="Error: " + str(e))

window = Tk()
window.title('Calculator')
window.minsize(width=500, height=500)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0
for button_label in buttons:
    if button_label == '=':
        button = Button(text=button_label, command=calculate)
    else:
        button = Button(text=button_label, command=lambda label=button_label: append_symbol(label))
    
    button.grid(row=row_val, column=col_val, padx=10, pady=10)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

word = Label(text='calculate wetin you')
word.grid(row=0, column=0, columnspan=4)

input_field = Entry()
input_field.grid(row=row_val+1, column=0, columnspan=4, padx=10, pady=10)

window.mainloop()
