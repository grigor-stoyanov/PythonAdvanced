import json
import os

from PIL import Image, ImageTk

from canvas import tk, ttk, frame
from tools import clear_screen, regrid,mouse_wheel


# TODO add shopping update functionality
# TODO add products as admin and form for adding product data make adding new data dynamic
# TODO description text editor
# TODO drag and drop to shopping cart
def render_shop():
    clear_screen()
    canvas = tk.Canvas(height=frame.winfo_height(), width=frame.winfo_width(), borderwidth=0, bg='gray')
    frame2 = tk.Frame(canvas, bg='gray')
    scrollbar = ttk.Scrollbar(orient='vertical', command=canvas.yview)
    scrollbar.pack(side='right', fill='y', expand=False)
    canvas.pack(side='left', fill='both', expand=True)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.create_window((0, 0), window=frame2, anchor='nw', tags='frame')
    with open(os.path.join('db', 'products.txt')) as file:
        current_row = current_col = 0
        row_size = (frame.winfo_width() // 100) - 1
        for idx, line in enumerate(file):
            product = json.loads(line)
            if idx % row_size == 0 and not idx == 0:
                current_row += 4
                current_col = 0
            tk.Label(frame2, text=product['name']).grid(row=current_row, column=current_col)
            image = Image.open(os.path.join('db', 'images', product['img_path'])).resize((100, 100))
            tk_image = ImageTk.PhotoImage(image)
            lbl = tk.Label(frame2, image=tk_image)
            lbl.image = tk_image
            lbl.grid(row=current_row + 1, column=current_col)
            tk.Label(frame2, text=product['count']).grid(row=current_row + 2, column=current_col)
            tk.Button(frame2, text=f'buy {product["id"]}').grid(row=current_row + 3, column=current_col)
            current_col += 1
    # with Windows OS
    frame.bind("<MouseWheel>", lambda event: mouse_wheel(canvas,event))
    # with Linux OS
    frame.bind("<Button-4>", lambda event: mouse_wheel(canvas,event))
    frame.bind("<Button-5>", lambda event: mouse_wheel(canvas,event))
    frame.bind('<Configure>', lambda event: regrid(frame2, event))
