import tkinter as tk
import Client
import threading
import tkinter.messagebox

class ChatRoom(threading.Thread):
    def __init__(self,client,name,master):
        threading.Thread.__init__(self)
        self.master=master
        self.room_name = name
        self.client= client
        self.createWidgets()
        master.protocol("WM_DELETE_WINDOW", self.quit_handler)

    def quit_handler(self):
        self.client.send({'flag':'QUIT_ROOM','room':self.room_name})
        self.master.destroy()

    def send_message(self):
        message = self.chat_entry.get(1.0,'end')
        self.chat_entry.delete(1.0,'end')
        self.client.send({'flag':'SEND', 'sender':self.client.username , 'receiver':self.room_name , 'content':message , 'type':'TEXT' });
        
    def run(self):
        self.master.mainloop()

    def createWidgets(self):    

        self.room_label = tk.Label(self.master, text="ROOM "+self.room_name)
        self.room_label.grid(row =0 , column =0 , columnspan=3,pady=10)
        #GUI ---frame chat list---
        self.chat_list_container = tk.Frame(self.master)
        self.chat_list_container.grid(row =1,column =0,columnspan=2,pady=10,padx=10)

        self.chat_list_label = tk.Label(self.chat_list_container,text="Chat :")
        self.chat_list_label.grid(row =0 , column =0, padx=5)
        
        self.chat_list = tk.Text(self.chat_list_container, height=31,width=55)
        self.chat_list.grid(row =1 , column =0 , )

        #GUI ---frame Online user---

        self.user_list_container = tk.Frame(self.master)
        self.user_list_container.grid(row =1,column =2,padx=(3,10),pady=10,rowspan=1)

        self.user_list_label = tk.Label(self.user_list_container,text="User di dalam Room :")
        self.user_list_label.grid(row =0 , column =0, padx=5, pady=0)
        
        self.user_list = tk.Listbox(self.user_list_container, height=25,width=20)
        self.user_list.grid(row =1 , column =0 , )

        #GUI --Chat Entry--

        self.chat_entry = tk.Text(self.master,width=42,height=4)
        self.chat_entry.grid(row = 2 , column=0 , pady=(3,15),padx=10)
        self.chat_btn = tk.Button(self.master, text="Send",height=3,width=10,command=self.send_message)
        self.chat_btn.grid(row = 2 , column =1 , padx= 2 , pady =3)

 
            

#root = tk.Tk()
#ChatRoom(Client.client() , "tes" , root)
#root.mainloop()
       
