import tkinter as tk
from tkinter import ttk

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

def get_max_width(values):
    return max(len(value) for value in values)

def button1_action():
    print("Planilha Cadastro pressed")

def button2_action():
    print("Exceção pressed")

def button3_action():
    print("Gerar Tabela pressed")

def main():
    root = tk.Tk()
    root.title("Ferramenta Comercialização")

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

    combobox_opcoes = SearchableCombobox(root, width=max_width_opcoes)
    combobox_opcoes.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
    combobox_opcoes.set_completion_list(combobox_values)
    combobox_opcoes.bind('<Button-1>', open_dropdown)

    # Valores do Combobox para meses
    combobox_months = [ "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro" ]

    combobox_mes = SearchableCombobox(root)
    combobox_mes.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
    combobox_mes.set_completion_list(combobox_months)
    combobox_mes.bind('<Button-1>', open_dropdown)

    # Criação dos botões na lateral direita
    button1 = tk.Button(root, text="Planilha Cadastro", command=button1_action)
    button1.grid(row=0, column=2, padx=10, pady=5)

    button2 = tk.Button(root, text="Exceção", command=button2_action)
    button2.grid(row=1, column=2, padx=10, pady=5)

    button3 = tk.Button(root, text="Gerar Tabela", command=button3_action)
    button3.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()