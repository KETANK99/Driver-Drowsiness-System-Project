from tkinter import *

ws = Tk()
ws.title('Driver Drowsiness Detection System')


img = PhotoImage(file="C:\\A\\AI-For-Road-Safety-main\\AI-For-Road-Safety-main\\New folder\\Img\\24.png")
Label(
    ws,
    image=img
).pack()

def login_windo():
    ws.destroy()
    import Code_login


def resigter_windo():
    ws.destroy()
    import Code_register

def exit():
    ws.destroy()

Login_btn = Button(text="SIGN IN ", bg="#836FFF", fg="white", font=("time new roman", 15), bd=0, cursor="hand1",command=login_windo
                    ).place(x=900, y=70)
Registre_btn = Button(text="SIGN UP", bg="#836FFF", fg="white", font=("time new roman", 15), bd=0, cursor="hand1",command=resigter_windo
                  ).place(x=900, y=140)
Exit_btn = Button(text=" Exit       ", bg="#836FFF", fg="white", font=("time new roman", 15), bd=0, cursor="hand1",command=exit
                  ).place(x=900, y=210)






ws.mainloop()