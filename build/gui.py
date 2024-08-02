
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
import tkinter as tk
from PIL import ImageFont, Image, ImageDraw, ImageTk




class SearchableCombobox(ttk.Combobox):
    def set_completion_list(self, completion_list):
        self._completion_list = sorted(completion_list)
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind('<KeyRelease>', self._handle_keyrelease)
        self['values'] = self._completion_list

    def _autocomplete(self, delta=0):
        if delta:
            self.delete(self.position, tk.END)
        else:
            self.position = len(self.get())

        _hits = [item for item in self._completion_list if item.lower().startswith(self.get().lower())]

        if _hits != self._hits:
            self._hit_index = 0
            self._hits = _hits

        if _hits:
            self._hit_index = (self._hit_index + delta) % len(_hits)
            self.delete(0, tk.END)
            self.insert(0, _hits[self._hit_index])
            self.select_range(self.position, tk.END)

    def _handle_keyrelease(self, event):
        if event.keysym in ('BackSpace', 'Left', 'Right', 'Up', 'Down'):
            return
        if event.keysym == 'Return':
            self._hits = []
            return
        self._autocomplete()

def update_options(event, combobox, values):
    if event.keysym in ('BackSpace', 'Left', 'Right', 'Up', 'Down'):
        return
    typed_text = combobox.get().lower()
    filtered_values = [value for value in values if typed_text in value.lower()]
    combobox['values'] = filtered_values
    combobox.event_generate('<Down>')

def open_dropdown(event):
    event.widget.event_generate('<Down>')

caminho = "C:\\Users\\kevin.maykel\\OneDrive - CITY INCORP LTDA\\Documentos\\Meus Projetos\\Ferramenta Comercialização"

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path( caminho + r"\\build\\assets\\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("900x506")
window.configure(bg = "#FAFAFA")


font_path = caminho + "\\fonts\\fonnts.com-Halyard_Micro_Regular.otf"

canvas = Canvas(
    window,
    bg = "#FAFAFA",
    height = 900,
    width = 1600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    335.0,
    506.0,
    fill="#696D6D",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=554.0,
    y=335.0,
    width=127.0,
    height=30.0
)

# Valores do Combobox para meses
combobox_months = [ "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro" ]

combobox_mes = ttk.Combobox(canvas, values=combobox_months)
combobox_mes.bind('<Button-2>', open_dropdown)
combobox_mes.place(
    x=468.0,
    y=260.0,
    width=140.0,
    height=18.0
)

# Valores do Combobox para meses
combobox_ano_values = [ 2024, 2025, 2026, 2027, 2028, 2030 ]

combobox_ano = SearchableCombobox(canvas)
# combobox_ano.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
combobox_ano.set_completion_list(combobox_ano_values)
combobox_ano.bind('<Button-3>', open_dropdown)
combobox_ano.place(
    x=628.0,
    y=260.0,
    width=140.0,
    height=18.0
)

def get_max_width(values):
    return max(len(value) for value in values)
# Valores do Combobox para opções
combobox_values = [
    "26 | SPE CITY 02 T-55 EMPREENDIMENTOS LTDA", 
    "27 | SPE RESIDENCIAL CITY 04 OM EMPREENDIMENTOS LTDA", 
    "53 | SPE RESIDENCIAL CITY 12 OM AREIAO EMPREENDIMENTOS LTDA", 
    "55 | SPE RESIDENCIAL CITY 15 OM EMPREENDIMENTOS LTDA", 
    "52 | SPE RESIDENCIAL CITY 13 OM EMPREENDIMENTOS LTDA", 
    "47 | SPE RESIDENCIAL CITY 10 OM EMPREENDIMENTOS LTDA", 
    "13 | SPE CITY 01 PARANHOS EMPREENDIMENTOS LTDA"
]

max_width_opcoes = get_max_width(combobox_values)

combobox_opcoes = SearchableCombobox(canvas, width=max_width_opcoes)
# combobox_opcoes.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
combobox_opcoes.set_completion_list(combobox_values)
combobox_opcoes.bind('<Button-1>', open_dropdown)

combobox_opcoes.place(
    x=468.0,
    y=185.0,
    width=300.0,
    height=18.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=700.0,
    y=141.0,
    width=30.0,
    height=30.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=738.0,
    y=141.0,
    width=30.0,
    height=30.0
)



def draw_text(canvas, text, x, y, font_path, font_size, fill):
    # Crie uma imagem temporária para desenhar o texto
    image = Image.new('RGBA', (canvas.winfo_width(), canvas.winfo_height()), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Carregue a fonte personalizada
    font = ImageFont.truetype(font_path, font_size)

    # Desenhe o texto na imagem
    draw.text((x, y), text, font=font, fill=fill)

    # Converta a imagem para um formato compatível com Tkinter
    image_tk = ImageTk.PhotoImage(image)

    # Desenhe a imagem no canvas
    canvas.image = image_tk  # Mantenha a referência para evitar a coleta de lixo
    canvas.create_image(0, 0, anchor='nw', image=image_tk)

# Adicione um botão para desenhar o texto e o triângulo após o carregamento da janela
def draw_elements():
    draw_text(canvas, "Ferramenta de Comercialização", 65, 103, font_path, 14, "#FAFAFA")

    x_start = 20
    y_start = 20
    width = 58
    height = 68

    points = [x_start, y_start, x_start + width, y_start, x_start, y_start + height]

    # Criando o triângulo com a cor laranja
    canvas.create_polygon(points, fill="#FF8700", outline="")

window.after(100, draw_elements)

# window.resizable(False, False)
window.mainloop()