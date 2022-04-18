import tkinter

window=tkinter.Tk()
window.title("Mani")
def func():
    tkinter.Label(window,text= "Python").pack()

tkinter.Button(window,text ="What you do?",command=func).pack()
window.mainloop()