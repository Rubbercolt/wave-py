from tkinter import *

window = Tk()
window.title('Calculator')
window.minsize(width=500, height=500)

def calculate():
    try:
        expression = input.get()
        result = eval(expression)
        word.config(text="Result: " + str(result))
    except Exception as e:
        word.config(text="Error: " + str(e))

button = Button(text="Calculate", command=calculate)
button.pack()

word = Label(text='Enter an expression (e.g., 2+2)')
word.pack()

input = Entry()
input.pack()

window.mainloop()
