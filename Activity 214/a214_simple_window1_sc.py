import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("300x200")
root.wm_title('Authorization')

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid()

lbl_username = tk.Label(frame_login, text='Username:',font = "Courier")
lbl_username.grid(row = 1, column = 1)

lbl_password = tk.Label(frame_login,text="Password:",font = "Courier")
lbl_password.grid(row = 3, column = 1)

ent_username = tk.Entry(frame_login, bd = 3)
ent_username.grid(row = 2, column = 1)

ent_password = tk.Entry(frame_login, bd = 3)
ent_password.grid(row = 4, column = 1)

root.mainloop()