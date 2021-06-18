import tkinter as tk


def create_app():
    window = tk.Tk()
    window.title('Desktop Shop')
    window.geometry('800x600')
    window.config(bg='gray')
    return window


frame = create_app()
