from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
import pandas as pd
import tkinter as tk
from ttkthemes import ThemedTk
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

        _hits = [item for item in self._completion_list if self.get().lower() in item.lower()]

        if _hits != self._hits:
            self._hit_index = 0
            self._hits = _hits

        if _hits:
            self._hit_index = (self._hit_index + delta) % len(_hits)
            self.delete(0, tk.END)
            self.insert(0, _hits[self._hit_index])
            self.select_range(self.position, tk.END)

    def _handle_keyrelease(self, event):
        if event.keysym == 'Return':
            self._update_options()
        elif event.keysym in ('BackSpace', 'Left', 'Right', 'Up', 'Down'):
            return

    def _update_options(self):
        typed_text = self.get().lower()
        filtered_values = [value for value in self._completion_list if typed_text in value.lower()]
        self['values'] = filtered_values
        self.event_generate('<Down>')

def update_options(event, combobox, values):
    if event.keysym in ('BackSpace', 'Left', 'Right', 'Up', 'Down'):
        return
    typed_text = combobox.get().lower()
    filtered_values = [value for value in values if typed_text in value.lower()]
    combobox['values'] = filtered_values
    combobox.event_generate('<Down>')

def open_dropdown(event):
    event.widget.event_generate('<Down>')

def abre_planilha_cadastro():
    caminho_planilha_cadastro = "C:\\Users\\kevin.maykel\\OneDrive - CITY INCORP LTDA\\Documentos\\Meus Projetos\\Ferramenta Comercialização\\Ferramenta-de-Comercializacao\\build_v2\\teste1.xlsx"
    open(caminho_planilha_cadastro)

def abre_planilha_excessao():
    caminho_planilha_excessao = "C:\\Users\\kevin.maykel\\OneDrive - CITY INCORP LTDA\\Documentos\\Meus Projetos\\Ferramenta Comercialização\\Ferramenta-de-Comercializacao\\build_v2\\teste2.xlsx"
    open(caminho_planilha_excessao)    

window = Tk()
window.geometry("900x600")
window.configure(bg = "#FAFAFA")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"\\192.168.100.3\dados city\Inovação e Sistemas\01-INOVACAO\02-DESENVOLVIMENTO\03-PRODUÇÃO\Ferramenta de Comercialização\build_v2\assets\frame0")
caminho = "\\192.168.100.3\\dados city\\Inovação e Sistemas\\01-INOVACAO\\02-DESENVOLVIMENTO\\03-PRODUÇÃO\\Ferramenta Comercialização"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

font_path = caminho + "\\fonts\\fonnts.com-Halyard_Micro_Regular.otf"
canvas = Canvas(
    window,
    bg = "#FAFAFA",
    height = 600,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

gerar_planilha = PhotoImage(
    file=relative_to_assets("button_1.png"))
gerar_planilha_botao = Button(
    image=gerar_planilha,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("gerar_planilha_botao clicked"),
    relief="flat"
)
gerar_planilha_botao.place(
    x=384.0,
    y=420.0,
    width=127.0,
    height=30.0
)

combostilo=ttk.Style()
combostilo.theme_create('combostyle', parent='clam',
                        settings={
                                'TCombobox':
                                    {'configure':
                                        {'selectbackground': '#E6E6E6',
                                        'fieldbackground': '#E6E6E6',
                                        'background': '#E6E6E6'}}}
                        )
combostilo.theme_use('combostyle')

# -------------------------------------- EMPREENDIMENTO --------------------------------------- #

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
    x=273.0,
    y=220.0,
    width=350.0,
    height=30.0,
)
"""canvas.create_rectangle(
    273.0,
    220.0,
    623.0,
    250.0,
    fill="#000000",
    outline="")"""
canvas.create_text(
    273.0,
    205.0,
    anchor="nw",
    text="Empreendimento",
    fill="#686D6D",
    font=("HalyardDisplay Regular", 10 * -1)
)

# --------------------------------------- MÊS ------------------------------------------------- #
combobox_meses = [ "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro" ]
combobox_mes = ttk.Combobox(canvas, values=combobox_meses)
combobox_mes.place(
    x=273.0,
    y=320.0,
    width=170.0,
    height=30.0
)
"""canvas.create_rectangle(
    273.0,
    320.0,
    443.0,
    350.0,
    fill="#E6E6E6",
    outline="")
"""
canvas.create_text(
    273.0,
    305.0,
    anchor="nw",
    text="Mês",
    fill="#686D6D",
    font=("HalyardDisplay Regular", 10 * -1)
)

# --------------------------------------- ANO ----------------------------------------------- #

combobox_anos = [2024, 2025, 2026, 2027, 2028, 2029, 2030]
combobox_ano = ttk.Combobox(canvas, values=combobox_anos)
combobox_ano.place(
    x=453.0,
    y=320.0,
    width=170.0,
    height=30.0
)
"""canvas.create_rectangle(
    453.0,
    320.0,
    623.0,
    350.0,
    fill="#E6E6E6",
    outline="")"""
canvas.create_text(
    453.0,
    305.0,
    anchor="nw",
    text="Ano",
    fill="#686D6D",
    font=("HalyardDisplay Regular", 10 * -1)
)

# ------------------------------------------------------------------------------------------- #

qr_code = PhotoImage(
    file=relative_to_assets("image_1.png"))
qr_code_imagem = canvas.create_image(
    850.0,
    550.0,
    image=qr_code
)
planilha_cadastro = PhotoImage(
    file=relative_to_assets("button_2.png"))
planilha_cadastro_botao = Button(
    image=planilha_cadastro,
    borderwidth=0,
    bg="#FAFAFA",
    highlightthickness=0,
    command= open("C:\\Users\\kevin.maykel\\OneDrive - CITY INCORP LTDA\\Documentos\\Meus Projetos\\Ferramenta Comercialização\\Ferramenta-de-Comercializacao\\build_v2\\teste1.xlsx"),
    relief="flat"
)
planilha_cadastro_botao.place(
    x=423.0,
    y=150.0,
    width=100.0,
    height=33.0
)

suporte_tecnico = PhotoImage(
    file=relative_to_assets("button_3.png"))
suporte_tecnico_botao = Button(
    image=suporte_tecnico,
    borderwidth=0,
    bg="#FAFAFA",
    highlightthickness=0,
    command=lambda: print("suporte_tecnico_botao clicked"),
    relief="flat"
)
suporte_tecnico_botao.place(
    x=820.0,
    y=501.0,
    width=60.0,
    height=16.0
)

planilha_excecao = PhotoImage(
    file=relative_to_assets("button_4.png"))
planilha_excecao_botao = Button(
    image=planilha_excecao,
    borderwidth=0,
    bg="#FAFAFA",
    highlightthickness=0,
    command= open("C:\\Users\\kevin.maykel\\OneDrive - CITY INCORP LTDA\\Documentos\\Meus Projetos\\Ferramenta Comercialização\\Ferramenta-de-Comercializacao\\build_v2\\teste1.xlsx"),
    relief="flat"
)
planilha_excecao_botao.place(
    x=526.0,
    y=150.0,
    width=100.0,
    height=33.0
)

canvas.create_text(
    65.0,
    32.0,
    anchor="nw",
    text="Ferramenta de Comercialização",
    fill="#686D6D",
    font=("HalyardMicro Regular", 15 * -1)
)
image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    39.0,
    44.0,
    image=image_image_2
)

window.resizable(False, False)
window.mainloop()
