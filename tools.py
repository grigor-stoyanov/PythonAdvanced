from canvas import frame, tk


def clear_screen():
    for ele in frame.grid_slaves():
        ele.destroy()


def popup_message(popup_type):
    popup_window = tk.Toplevel()
    popup_window.grab_set()
    popup_window.title('message')
    popup_window.config(bg='grey')
    popup_window.geometry('200x150')
    tk.Label(popup_window, text=popup_type).grid(row=0, column=0)
    tk.Button(popup_window, bg='red', fg='green', text='OK', command=popup_window.destroy).grid(row=1, column=0)
