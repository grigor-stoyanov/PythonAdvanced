import json
import os

from canvas import tk, frame
from products import render_shop
from tools import clear_screen, popup_message


def render_main_view():
    clear_screen()
    tk.Button(frame, text='Login', command=lambda: render_login()
              , bg='green', fg='yellow', font='16', width='10').grid(row='0', column='0', padx=200, pady=250)
    tk.Button(frame, text='Register', command=lambda: render_registration(),
              bg='red', fg='cyan', font='16', width='10').grid(row='0', column='1', padx=0, pady=250)


# TODO remember login functionality
def render_login():
    clear_screen()
    tk.Label(frame, text='Username:').grid(row=0, column=0)
    username = tk.Entry(frame)
    username.grid(row=0, column=1)
    tk.Label(frame, text='Password:').grid(row=1, column=0)
    password = tk.Entry(frame, show='*')
    password.grid(row=1, column=1)

    def on_click():
        with open(os.path.join('db', 'user_credentials.txt'), 'r') as file:
            for line in file:
                user = json.loads(line)
                if user['Username'] == username.get() and user['Password'] == password.get():
                    render_shop()
                else:
                    tk.Label(text='Invalid Username/Password', fg='red', bg='gray').grid(row=3, columnspan=2)

    tk.Button(frame, text='Enter', command=on_click).grid(row=2, column=0)
    tk.Button(frame, text='Back', command=lambda: render_main_view()).grid(row=2, column=1)


def render_registration():
    clear_screen()
    user_data = [
        (tk.Label(frame, text='First Name'), tk.Entry(frame)),
        (tk.Label(frame, text='Last Name'), tk.Entry(frame)),
        (tk.Label(frame, text='Username'), tk.Entry(frame)),
        (tk.Label(frame, text='Password'), tk.Entry(frame, show='*')),
    ]
    for idx, (label, text_input) in enumerate(user_data):
        label.grid(row=idx, column=0)
        text_input.grid(row=idx, column=1)

    def on_click():
        register(**{user_atr.cget("text"): data.get() for (user_atr, data) in user_data})

    tk.Button(frame, text='Submit', command=on_click).grid(row=len(user_data), column=0)
    tk.Button(frame, text='Back', command=lambda: render_main_view()).grid(row=len(user_data), column=1)


# TODO add validations to all fields, update grid positions and css
def register(**data):
    with open(os.path.join('db', 'user_credentials.txt'), 'r') as file:
        for line in file:
            if json.loads(line).get('Username') == data['Username']:
                return popup_message('User already exists!')
    with open(os.path.join('db', 'users.txt'), 'a+') as file1, \
            open(os.path.join('db', 'user_credentials.txt'), 'a+') as file2:
        data['products'] = []
        json.dump(data, file1)
        file1.write('\n')
        credentials = {'Username': data['Username'], 'Password': data['Password']}
        json.dump(credentials, file2)
        file2.write('\n')
    render_login()
    return popup_message('Successful Registration!')
