from tkinter import *
from mydb import Database
from tkinter import messagebox
class NLPApp:
    def __init__(self):
        self.root=Tk()
        self.dbo=Database()
        self.root.title("NLPApp")
        self.root.iconbitmap("resorces/mainlogo_crop.ico")
        self.root.geometry('350x600')
        self.root.configure(bg="#34495E")

        self.login_gui()


        self.root.mainloop()
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    def login_gui(self):
        self.clear()
        heading=Label(self.root,text='NLPApp')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'),bg="#34495E",fg="white")
        #email
        label1=Label(self.root,text="Enter Email",bg="#34495E",fg="white")
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=3)
        #passward
        label2=Label(self.root,text="Enter Password",bg="#34495E",fg="white")
        label2.pack(pady=(10,10))

        self.password_input=Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=3)

        #login button
        login_btn=Button(self.root,text='Login',width=30,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3=Label(self.root,text="Not a Member?")
        label3.pack(pady=(20,10))

        redirect_btn=Button(self.root,text='Register Now',command=self.register_gui)    
        redirect_btn.pack(pady=(10,10))

    def register_gui(self):
        self.clear()
        #name
        label0=Label(self.root,text="Enter your Name",bg="#34495E",fg="white")
        label0.pack(pady=(10,10))

        self.name_input=Entry(self.root,width=50)
        self.name_input.pack(pady=(5,10),ipady=3)       

        #email
        label1=Label(self.root,text="Enter Email",bg="#34495E",fg="white")
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=3)
        #passward
        label2=Label(self.root,text="Enter Password",bg="#34495E",fg="white")
        label2.pack(pady=(10,10))

        self.password_input=Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=3)

        register_btn=Button(self.root,text='Register',width=30,height=2,command=self.perform_registration)
        register_btn.pack(pady=(10,10))

        label3=Label(self.root,text="Already Registered?..")
        label3.pack(pady=(20,10))

        redirect_btn=Button(self.root,text='Login Now',command=self.login_gui)    
        redirect_btn.pack(pady=(10,10))

    def perform_registration(self):
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.password_input.get()
        response=self.dbo.add_data(name,email,password)
        if response:
            messagebox.showinfo('Success.','Registration sucessful,You can Login')
            self.login_gui()
        else:
            messagebox.showerror('Error','Email already exist')
    def perform_login(self):
        email=self.email_input.get()
        password=self.password_input.get()
        response=self.dbo.search(email,password)
        if response:
            messagebox.showinfo('Success','Login Successful.')
            self.home_gui()
        else :
            messagebox.showerror('Error','Incorrect email/password')
    def home_gui(self):
        self.clear()

        heading=Label(self.root,text='NLPApp')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'),bg="#34495E",fg="white")

        sentiment_btn=Button(self.root,text='Sentiment Analysis',width=30,height=4,command=self.sentiment_gui)    
        sentiment_btn.pack(pady=(10,10))

        ner_btn=Button(self.root,text='Named Entity Recognition',width=30,height=4)    
        ner_btn.pack(pady=(10,10))

        emotion_btn=Button(self.root,text='Emotion Prediction',width=30,height=4)    
        emotion_btn.pack(pady=(10,10))

        #logout
        logout_btn=Button(self.root,text='Logout',command=self.login_gui)    
        logout_btn.pack(pady=(10,10))

    def sentiment_gui(self):
        self.clear()
        heading=Label(self.root,text='NLPApp')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'),bg="#34495E",fg="white")

        heading=Label(self.root,text='Sntiment Analysis')
        heading.pack(pady=(10,20))
        heading.configure(font=('verdana',24,'bold'),bg="#34495E",fg="white")

        label1=Label(self.root,text="Enter the text")
        label1.pack(pady=(10,10))

        self.sentiment_input=Entry(self.root,width=50)
        self.sentiment_input.pack(pady=(5,10),ipady=10)

        sentiment_btn=Button(self.root,text='Perform analysis')    
        sentiment_btn.pack(pady=(10,10))

        self.sentiment_result=Label(self.root,text='',bg='#34495E',fg=white)
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.config(font=('verdana',16))

        goback_btn=Button(self.root,text='Go Back',command=self.home_gui)    
        goback_btn.pack(pady=(10,10))
nlp=NLPApp()