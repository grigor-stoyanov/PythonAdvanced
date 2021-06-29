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


def regrid(event=None):
    width = frame.winfo_width()
    slaves = list(frame.grid_slaves())
    max_width = max(100, max(slave.winfo_width() for slave in slaves))
    max_row_size = width // max_width
    if max_row_size <= width // 100:
        return
    col = row = 0
    i = 0
    while slaves:
        if i % max_row_size == 0 and not i == 0:
            col = 0
            row += 4
        for j in range(4):
            slave = slaves.pop()
            slave.grid_forget()
            slave.grid(row=row + j, column=col)
        col += 1
        i += 1
