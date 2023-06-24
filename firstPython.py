from tkinter import *
window = Tk()

window.title("My fist Python App")
window.geometry("500x500")

result = Label(window)
result.pack()

def add():
    sum = 2+3
    result['text']= sum


btn = Button(window,text="click me" ,command= add)
btn.pack()


window.mainloop()