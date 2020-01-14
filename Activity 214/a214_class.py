import tkinter as tk

uppercase = 'Q W E R T Y U I O P A S D F G H J K L Z  X C V B N M'
lowercase = 'q w e r t y u i o p a s d f g h j k l z x c v b n m'
special = '` - = [ ] \ ; , . / ~ ! @ # $ % ^ & * ( ) _ + { ` ¡ ™ £ ¢ ∞ § ¶ • ª º – ≠ “ ‘ « … æ ≤ ≥ ÷ ` ⁄ € ‹ › ﬁ ﬂ ‡ ° · ‚ — ± ” ’ » Ú Æ ¯ ˘ ¿ '
digit = '1 2 3 4 5 6 7 8 9 0'

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
    validation = False

    upper_num = 0
    lower_num = 0
    digit_num = 0
    special_num = 0

    for pass_char in password_entry.get():
            for upper_char in uppercase.split():
                if pass_char == upper_char:
                    upper_num += 1
    for pass_char in password_entry.get():
            for lower_char in lowercase.split():
                if pass_char == lower_char:
                    lower_num += 1
    for pass_char in password_entry.get():
            for special_char in special.split():
                if pass_char == special_char:
                    special_num += 1
    for pass_char in password_entry.get():
            for digit_char in digit.split():
                if pass_char == digit_char:
                    digit_num += 1

    if len(password_entry.get()) < 8:
        print('missing 8 characters')
        validation = False
    elif upper_num < 1:
        validation = False
        print('missing capital letter')
    elif lower_num < 1:
        validation = False
        print('missing lowercase letter')
    elif special_num < 1:
        validation = False
        print('missing special character')
    elif digit_num < 1:
        validation = False
        print('missing digit')
    else:
        validation = True
    if validation == True:
        print('Username: ', user_entry.get())
        print('Password: ', password_entry.get())

submit = tk.Button(root, text='login', command=handle_login)
submit.pack(pady = 5)

root.mainloop()