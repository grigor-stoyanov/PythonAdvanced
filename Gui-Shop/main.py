from authenticate import render_main_view
from canvas import frame

if __name__ == '__main__':
    render_main_view()
    frame.update_idletasks()
    frame.mainloop()
