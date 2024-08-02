import tkinter as tk
from tkinter import ttk

class SearchableCombobox(ttk.Combobox):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self._completion_list = []
        self._hits = []
        self._hit_index = 0

        self.bind('<KeyRelease>', self.on_keyrelease)
        self.bind('<FocusIn>', self.on_focusin)
        self.bind('<FocusOut>', self.on_focusout)

    def set_completion_list(self, completion_list):
        self._completion_list = sorted(completion_list)
        self._hits = self._completion_list
        self._hit_index = 0

    def autocomplete(self, delta=0):
        if delta:
            pattern = self.get().lower()
            self._hits = [item for item in self._completion_list if pattern in item.lower()]
            self._hit_index = 0
            if self._hits:
                self._hits.sort()
                self.set(self._hits[0])
                self._hit_index = 0
                self._hit_index = min(self._hit_index, len(self._hits) - 1)
                self._hit_index = 0
                self._hits_len = len(self._hits)
            else:
                self._hit_index = -1
        else:
            self._hits = self._completion_list

    def on_keyrelease(self, event):
        if event.keysym in ('BackSpace', 'Left', 'Right', 'Up', 'Down', 'Shift_R', 'Shift_L', 'Tab', 'Return'):
            return
        self.autocomplete()

    def on_focusin(self, event):
        self.autocomplete()

    def on_focusout(self, event):
        self._hits = self._completion_list

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('300x200')

    combo = SearchableCombobox(root)
    combo.set_completion_list([
        "Apple",
        "Banana",
        "Cherry",
        "Date",
        "Date 2",
        "Date 2 2",
        "Elderberry",
        "Fig",
        "Grape",
        "Honeydew"
    ])
    combo.pack(padx=10, pady=10)
    combo.set_completion_list([
        "Apple",
        "Banana",
        "Cherry",
        "Date",
        "Date 2",
        "Date 2 2",
        "Elderberry",
        "Fig",
        "Grape",
        "Honeydew"
    ])

    root.mainloop()
