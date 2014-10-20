import tkinter as tk
import Client
import RoomMenu
import tkinter.messagebox
class LoginClient(tk.Frame):

    def __init__(self,client,master="none"):
        tk.Frame.__init__(self,master)
        self.master = master
        self.client = client
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.username_label = tk.Label(self,text = "Username :")
        self.username_label.grid(row = 0 , column =0 , padx=3)
        
        self.password_label = tk.Label(self,text="Password :")
        self.password_label.grid(row =1 , column =0 , padx=3)

        self.username_entry = tk.Entry(self,width=30)
        self.username_entry.grid(column=1,columnspan=3,row=0,pady=5,padx=5)

        self.password_entry = tk.Entry(self,width=30)
        self.password_entry.grid(column=1,columnspan=3,row=1,pady=5,padx=5)

        self.login_btn = tk.Button(self,text="Login",command=self.client_login)
        self.login_btn.grid(column =0 ,row=2,pady=20,padx=5)

        self.reg_btn = tk.Button(self,text="Register",command=self.client_register)
        self.reg_btn.grid(column =1 , row=2 , pady=20 , padx=5)

    def client_register(self):
        self.client.username=self.username_entry.get()
        self.client.password=self.password_entry.get()
        self.client.send({'flag':'REG','username':self.client.username,'password':self.client.password})
        regis_data = self.client.receive()
        tk.messagebox.showinfo('register',message=regis_data['content'])

    def client_login(self):
        self.client.username=self.username_entry.get()
        self.client.password=self.password_entry.get()
        self.client.send({'flag':'LOGIN','username':self.client.username,'password':self.client.password})
        login_data = self.client.receive()
        if login_data['code']=='LOGIN_OK':
            tk.messagebox.showinfo('Login',message=login_data['content'])
            roomroot =tk.Tk()
            room = RoomMenu.RoomMenu(self.client,master=roomroot)
            self.master.withdraw()
            room.mainloop()
        else:
            tk.messagebox.showinfo('Login',message=login_data['content'])
            self.username_entry.delete(0,'end')
            self.password_entry.delete(0,'end')

