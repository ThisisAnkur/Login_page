from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login system")
        self.root.geometry('1100x600+100+50')
     # self.root.resizable(False, False)

     # Background Image
        self.bg = ImageTk.PhotoImage(file= 'D:\Project_LoginUser\Login_img.jpg')
        self.bg_image = Label(self.root, image = self.bg).place(x=0, y=0, relwidth=1,relheight=1)
        
     # Login Frame
        frame_login = Frame(self.root, bg = 'white')
        frame_login.place(x =350, y= 150,width= 500, height=400)

     # Title and subtitle
        title = Label(frame_login, text='Login Here', font=('Impact', 35, 'bold'), fg='#6162FF', bg='white').place(x=90,y=30)
        subtitle = title = Label(frame_login, text='Members Login ', font=('Goudy old style', 15, 'bold'), fg='#1d1d1d', bg='white').place(x=90,y=100)
        
        
     #username
        user = Label(frame_login, text='User name', font=('Goudy old style', 15, 'bold'), fg='grey', bg='white').place(x=90,y=150)
        self.username = Entry(frame_login,  font=('Goudy old style', 15,),  bg='#E7E6E6')
        self.username.place(x=90,y=170, width=320,height=35)


     # Password
        user_password = Label(frame_login, text='Password', font=('Goudy old style', 15, 'bold'), fg='grey', bg='white').place(x=90,y=210)
        self.password = Entry(frame_login,  font=('Goudy old style', 15,),  bg='#E7E6E6')
        self.password.place(x=90, y=240, width=320,height=35)

     # Button
        forget = Button(frame_login, text='Forget Password?',bd =0,cursor="hand2", font=('Goudy old style', 12),  fg='#6162FF', bg='white').place(x=90,y=280)
        submit = Button(frame_login,command=self.check_function,cursor="hand2", text='Login',  font=('Goudy old style', 15), bd =0, bg='#6162FF', fg='white').place(x=90,y=320, width=180,height=40)
    
     # validity of username and password
    def check_function(self):
        if self.username.get() == "" or self.password.get() =="":
            messagebox.showerror('Error', "All fields are required ", parent= self.root)
        elif self.username.get() != "ankur.shivhare1" or self.password.get() !="9098551312":
            messagebox.showerror('Error', "Invalid Username or Password", parent= self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")

root = Tk()
obj = Login(root)
root.mainloop()