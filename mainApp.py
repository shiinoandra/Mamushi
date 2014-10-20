import tkinter as tk
import LoginClient
import RoomMenu
import Client

cl = Client.client()
cl.connect()
loginroot = tk.Tk()
loginCl = LoginClient.LoginClient(cl,master=loginroot)
#oom = RoomMenu.RoomMenu(cl,master=roomroot)
loginCl.mainloop()
#room.mainloop()
