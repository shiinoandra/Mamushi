import tkinter as tk
import Client
import ChatRoom
import threading
import tkinter.messagebox

class RoomMenu(tk.Frame):

    def __init__(self,client,master="none"):
        tk.Frame.__init__(self,master)
        self.client = client
        self.pack()
        self.createWidgets()
        self.chat_rooms={}
        rcv_thread = threading.Thread(target=self.receive)
        rcv_thread.start()

    def createWidgets(self):
        self.username_label = tk.Label(self,text = "Terlogin sebagai : " +self.client.username)
        self.username_label.grid(row = 0 , column =0 , padx=3,pady=20)
                
         #GUI ---frame room list---

        self.room_list_container = tk.Frame(self)
        self.room_list_container.grid(row =1,column =0 , columnspan=3,padx=5,pady=10)

        self.room_list_label = tk.Label(self.room_list_container,text="List Room :")
        self.room_list_label.grid(row =0 , column =0, padx=5, pady=5)
        
        self.room_list = tk.Listbox(self.room_list_container, height=20,width=40)
        self.room_list.grid(row =1 , column =0 , )

        #GUI ---frame Online user---

        self.user_list_container = tk.Frame(self)
        self.user_list_container.grid(row =1,column =4 , columnspan=3,padx=5,pady=10)

        self.user_list_label = tk.Label(self.user_list_container,text="Online User :")
        self.user_list_label.grid(row =0 , column =0, padx=5, pady=5)
        
        self.user_list = tk.Listbox(self.user_list_container, height=20,width=20)
        self.user_list.grid(row =1 , column =0 , )


        self.login_btn = tk.Button(self,text="Join Room",command = self.join_room)
        self.login_btn.grid(column =0 ,row=2,pady=10)

        self.reg_btn = tk.Button(self,text="Make Room",command=self.make_room)
        self.reg_btn.grid(column =1 , row=2 , pady=10)

    def receive(self):
        while 1:
            data = self.client.receive()
            if data['code'] == 'ROOM_LIST_OK':
                 list_room = data['content']
                 self.room_list.delete(0,'end')
                 for room in list_room:
                    self.room_list.insert('end',room)
            elif data['code'] == 'ONLINE_LIST_OK':
                list_online = data['content']
                self.user_list.delete(0,'end')
                for user in list_online:
                    self.user_list.insert('end',user)
            elif data['code'] == 'CREATE_ROOM_OK':
                tkinter.messagebox.showinfo(title="buat room" , message=data['content'])
            elif data['code'] == 'CREATE_ROOM_DUPE':
                tkinter.messagebox.showerror(title="buat room" , message=data['content'])
            elif data['code'] == 'JOIN_ROOM_OK':
                room_name = data['content']
                self.joined_room(room_name)
            elif data['code'] == 'ROOM_USER_LIST':
                list_user = data['content']
                self.chat_rooms[data['room']].user_list.delete(0,'end')
                for user in list_user:
                    self.chat_rooms[data['room']].user_list.insert('end',user)
            elif data['code'] == 'JOIN_ROOM_FAILED':
                tkinter.messagebox.showerror(title="buat room" , message=data['content'])

            elif data['code'] == 'MESSAGE':
                self.chat_rooms[data['room']].chat_list.insert('end',data['sender']+" : "+data['content'])
            #elif data['code'] == 'ROOM_QUITTED':
            #    for room in self.chat_rooms:
            #        if room.room_name == data['room']:
            #            alert('ahalo')
            #            chat_rooms.remove(room)
                
    def make_room(self):
        self.room_name=""
        self.room_entry_frame = tk.Toplevel()
        def get_entry():
            self.room_name = room_entry_input.get()
            self.room_entry_frame.destroy()
        room_entry_input = tk.Entry(self.room_entry_frame)
        room_entry_input.grid(column =0 , row=1,columnspan =3 ,padx=5,pady=10)
        room_entry_label = tk.Label(self.room_entry_frame,text="Masukkan Nama Room yang ingin dibuat")
        room_entry_label.grid(column =0 , row=0,padx=5,pady=10)
        room_entry_btn = tk.Button(self.room_entry_frame , text="OK" ,command=get_entry)
        room_entry_btn.grid(column = 0 , row =2 , padx = 5 , pady=5)
        self.room_entry_frame.wait_window()        

        self.client.send({'flag':'MAKE_ROOM', 'content':self.room_name})

    def join_room(self):
        room_name = self.room_list.selection_get()
        self.client.send({'flag':'JOIN_ROOM', 'content':room_name})

    def joined_room(self,name):
        chatroomroot =tk.Toplevel()
        chatroom = ChatRoom.ChatRoom(self.client,name,chatroomroot)
        self.chat_rooms[name]=chatroom
        
      




    #def get_list_room(self):
    #    self.client.send({'flag':'LIST_ROOM'})
    #    list_room = self.client.receive()['content']
    #    self.room_list.delete(0,'end')
    #    for room in list_room:
    #        self.user_list.insert('end',room)

    #def get_list_online(self):
    #    self.client.send({'flag':'LIST_ONLINE'})
    #    list_online = self.client.receive()['content']
    #    self.user_list.delete(0,'end')
    #    for user in list_online:
    #        self.user_list.insert('end',user)

           





