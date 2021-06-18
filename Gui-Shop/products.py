import json
import os
from PIL import Image, ImageTk

from tools import clear_screen
from canvas import tk

ROW_SIZE = 3


# TODO  pages or infinite scroll, add shopping update functionality, dynamic image positioning
# TODO add products as admin and form for adding product data make adding new data dynamic
def render_shop():
    clear_screen()
    with open(os.path.join('db', 'products.txt')) as file:
        current_row = current_col = 0
        for idx, line in enumerate(file):
            product = json.loads(line)
            if idx % ROW_SIZE == 0 and not idx == 0:
                current_row += 4
                current_col = 0
            tk.Label(text=product['name']).grid(row=current_row, column=current_col)
            image = Image.open(os.path.join('db', 'images', product['img_path'])).resize((100, 100))
            tk_image = ImageTk.PhotoImage(image)
            lbl = tk.Label(image=tk_image)
            lbl.image = tk_image
            lbl.grid(row=current_row + 1, column=current_col)
            tk.Label(text=product['count']).grid(row=current_row + 2, column=current_col)
            tk.Button(text=f'buy {product["id"]}').grid(row=current_row + 3, column=current_col)
            current_col += 1
