from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('Initiate Drowsiness Detection ')
ws.geometry('1100x650+100+50')
ws.config(bg='#04B2D9')

#img = PhotoImage(file="C:\A\AI-For-Road-Safety-main\AI-For-Road-Safety-main\New folder\Img\car1122.jpg")
#Label(
#    ws,
#    image=img
#).pack()




def init_cam():
    ws.destroy()
    import Drwosinessdect

frame = Frame(
    ws,
    padx=10,
    pady=10
)
frame.pack(pady=20)

starting_bt = Button(text="CLICK TO START MONITORING", bg="#836FFF", fg="black", font=("time new roman", 25), bd=0, cursor="hand1",command=init_cam
                    ).place(x=280, y=300)


ws.mainloop()
