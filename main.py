from tkinter import *
from tkinter import messagebox

def check():
    usernm=usernm_input.get()
    passw=password_input.get()
    if usernm=="sneha" and passw=="1234":
        messagebox.showinfo("welcome","Login Sucessful")
    else:
        messagebox.showerror("oops","Invalid data")

root=Tk() #create object of Tk class simple oop


# change title
root.title("Login page")

#control window size
root.minsize(400,400) #we cannot minimize it than 400

#set fix size for window
root.geometry('350x500')

# bg color
root.config(background="black")

#login label added..
text_label=Label(root,text="Login",fg="white",bg="black")
text_label.pack()
text_label.config(font=('verdana,30'))

#user name label added
usernm_label=Label(root,text="User Name",fg="white",bg="black")
usernm_label.pack(pady=(30,5),padx=(15,20)) #pady for top and bottom and padx for left and right
usernm_label.config(font=('verdana,25'))

#textbox for user name
usernm_input=Entry(root,width=500)
usernm_input.pack(pady=(15,5),padx=(5,15),ipady=2,ipadx=1500) #ipady for y axis means height
usernm_input.insert(0,"Enter username")

#password label added
password_label=Label(root,text="Password",fg="white",bg="black")
password_label.pack(pady=(30,5),padx=(15,20)) #pady for top and bottom and padx for left and right
password_label.config(font=('verdana,25'))

#textbox for password
password_input=Entry(root,width=500)
password_input.pack(pady=(15,5),padx=(3,15),ipady=2,ipadx=1500) #ipady for y axis means height
password_input.insert(0,"Enter password")

login_btn=Button(root,text="Login",width=10,command=check)
login_btn.pack(pady=(30,5),padx=(15,20))
login_btn.config(font=('Verdana,1'))

root.mainloop()


