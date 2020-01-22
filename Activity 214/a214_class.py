import tkinter as tk
import string 
from passlib.hash import pbkdf2_sha256

users = {}

root = tk.Tk()
root.geometry('600x400')
root.title('Login Practice')

user_label = tk.Label(root, text='Username: ')
user_label.pack()
user_entry = tk.Entry(root,)
user_entry.pack(pady = 5)

password_label = tk.Label(root, text='Password: ')
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack(pady = 5)

def handle_login():
    if check_users():
        print('Username: ', user_entry.get())
        print('Password: ', password_entry.get())
        result_label.config(text='Successfully logged-in')
    else:
        result_label.config(text='invalid login')

def handle_sign_up():
    if is_valid_password(password_entry.get()):
        if user_entry.get() not in users:
            store_users()
            result_label.config(text='That is Valid')
        else:
            result_label.config(text='Username has already been taken')
    else:
        result_label.config(text='That is Invalid')
    print(users)

def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for pass_char in password_entry.get():
        if pass_char.isupper():
            has_upper = True
    for pass_char in password_entry.get():
        if pass_char.islower():
            has_lower = True
    for pass_char in password_entry.get():
        if pass_char in string.punctuation:
            has_special = True
    for pass_char in password_entry.get():
        if pass_char.isdigit():
            has_digit = True

    return has_digit and has_lower and has_special and has_upper

def store_users():
    hash = pbkdf2_sha256.hash(password_entry.get())
    users[user_entry.get()] = hash

def check_users():
    if user_entry.get() in users:
        if pbkdf2_sha256.verify(users[user_entry.get()],hash):
            return True
        else:
            return False

submit = tk.Button(root, text='login', command=handle_login)
submit.pack(pady = 5)

sign_up = tk.Button(root, text='sign up', command=handle_sign_up)
sign_up.pack(pady = 10)

result_label = tk.Label(root, text='Result: ')
result_label.pack(pady = 20)

root.mainloop()