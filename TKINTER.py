# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

from tkinter import *

# def james():
#     message = "scholar james😂"
#     print (message)
#     word.config(text=message)
    # return "scholar james😂"


window = Tk()
window.title('Python app✨✔👌')
window.minsize(width=500, height=500)
def james():
    message = "scholar james😂"
    print (message)
    word.config(text=message)
button = Button(text="ENTER✨", command=james)
button.pack()
word = Label(text='Enter your username')
word.pack()
input = Entry()
input.pack()
window.mainloop()
