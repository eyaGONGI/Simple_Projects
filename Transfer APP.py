from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os
import cv2

root=Tk()
root.title("Shareit")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False,False)

def select_file():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title='Select Image File',
                                        filetype=(('file_type','*.txt'),('all files','*.*')))

def sender():
    s=socket.socket()
    host=socket.gethostname()
    port=8080
    s.bind((host,port))
    s.listen(1)
    print(host)
    print('waiting for any incoming connections....')
    conn,addr=s.accept()
    file=open(filename,'rb')
    file_data=file.read(1024)
    conn.send(file_data)
    print("Data has been transmitted successfully ..")

def Send():
    window=Toplevel(root)
    window.title("Send")
    window.geometry('450x560+500+200')
    window.configure(bg="#f4fdfe")
    window.resizable(False,False)

    #icon
    image_icon1=PhotoImage(file="C:/Users/user/AppData/Local/Programs/Python/Python39/Transfer App/images/send.jpg")
    window.iconphoto(False,image_icon1)
    Sbackground=PhotoImage(file="C:/Users/user/AppData/Local/Programs/Python/Python39/Transfer App/images/sender.png")
    Label(window,image=Sbackground).place(x=25,y=0)

    Mbackground=PhotoImage(file="C:/Users/user/AppData/Local/Programs/Python/Python39/Transfer App/images/id.png")
    Label(window,image=Mbackground,bg='#f4fdfe').place(x=100,y=260)

    host=socket.gethostname()
    Label(window,text=f'ID: {host}', bg='white', fg='black').place(x=140,y=290)

    Button(window,text=" + select file", width=10,height=1,font='arial 14 bold',bg="#fff",fg="#000",command=select_file).place(x=160,y=150)
    Button(window,text="SEND", width=8, height=1,font='arial 14 bold', bg='#000',fg="#fff").place(x=300,y=150)
    window.mainloop()

def Receive():
    main=Toplevel(root)
    main.title("Receive")
    main.geometry('450x560+500+200')
    main.configure(bg='#f4fdfe')
    main.resizable(False,False)

    def receiver():
        ID=SenderID.get()
        filename1=incoming_file.get()

        s=socket.socket()
        port=8080
        s.connect((ID,port))
        file=open(filename,'wb')
        file_data=s.recv(1024)
        file.write(file_data)
        file.close()
        print('File has been received successfully')

    
    #icon
    
    image_icon1=PhotoImage(file="C:/Users/user/AppData/Local/Programs/Python/Python39/Transfer App/images/receive.png")
    main.iconphoto(False,image_icon1)
    Hbackground=PhotoImage(file="C:/Users/user/AppData/Local/Programs/Python/Python39/Transfer App/images/receiver.jpg")
    Label(main,image=Hbackground).place(x=70,y=0)


    img=cv2.imread("C:/Users/user/AppData/Local/Programs/Python/Python39/Transfer App/images/profile.png")
    cv2.imwrite("C:/Users/user/AppData/Local/Programs/Python/Python39/Transfer App/images/profile.png",img)
    logo=PhotoImage(file="C:/Users/user/AppData/Local/Programs/Python/Python39/Transfer App/images/profile.png")
    Label(main,image=logo,bg="#f4fdfe").place(x=20,y=320)

    Label(main,text="Receive",font=('arial',20),bg='#f4fdfe').place(x=90,y=320)

    Label(main, text="Input sender id",font=('arial',10,'bold'),bg='#f4fdfe').place(x=20,y=390)
    SenderID=Entry(main,width=25,fg='black',border=2,bg='white',font=('arial',15))
    SenderID.place(x=20,y=410)
    SenderID.focus()

    Label(main, text="filename for the incoming file:",font=('arial',10,'bold'),bg='#f4fdfe').place(x=20,y=450)
    incoming_file=Entry(main,width=25,fg='black',border=2,bg='white',font=('arial',15))
    incoming_file.place(x=20,y=470)

    imageicon=PhotoImage(file="C:/Users/user/AppData/Local/Programs/Python/Python39/Transfer App/images/arrow.png")
    rr=Button(main,text="Receive",compound=LEFT,image=imageicon,width=130,bg="#39c790",font="arial 14 bold",command=receiver)
    rr.place(x=20,y=510)

    main.mainloop()
    
#icon
image_icon=PhotoImage(file="C:/Users/user/AppData/Local/Programs/Python/Python39/Transfer App/images/icon.png")
root.iconphoto(False,image_icon)

Label(root,text="File Transfer",font=('Acumin Variable Concept',20,'bold'),bg="#f4fdfe").place(x=20,y=30)
Frame(root,width=400,height=2,bg="#f3f5f6").place(x=25,y=80)


send_image=PhotoImage(file="C:/Users/user/AppData/Local/Programs/Python/Python39/Transfer App/images/send.jpg")
send=Button(root,image=send_image,bg="#f4fdfe",bd=0,command=Send)
send.place(x=50,y=100)

receive_image=PhotoImage(file="C:/Users/user/AppData/Local/Programs/Python/Python39/Transfer App/images/receive.png")
receive=Button(root,image=receive_image,bg="#f4fdfe",bd=0,command=Receive)
receive.place(x=300,y=100)

#label
Label(root,text="Send",font=("Acumin Variable Concept",17,"bold"),bg="#f4fdfe").place(x=65,y=200)
Label(root,text="Receive",font=("Acumin Variable Concept",17,"bold"),bg="#f4fdfe").place(x=300,y=200)

background=PhotoImage(file="C:/Users/user/AppData/Local/Programs/Python/Python39/Transfer App/images/background.png")
Label(root,image=background).place(x=45,y=250)



root.mainloop()
