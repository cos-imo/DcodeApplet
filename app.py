import customtkinter
from PIL import Image as PILImage
from tkinter import *
from tkinter.ttk import *
import core

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("decoder")
        self.geometry("400x150")
        self.grid_columnconfigure((0, 1), weight=1)

        self.result = "result"
        self.data = "data"
        self.format = ""

        self.core = core.Core()

        self.optionmenu_values = self.core.optionmenu_values
        self.function_mapping = self.core.function_mapping

        self.copy_image = customtkinter.CTkImage(PILImage.open(r"assets/copy.png/"))

        self.init_display()

    def init_display(self):
        self.optionmenu = customtkinter.CTkOptionMenu(self, values=self.optionmenu_values, command=self.set_format)
        self.optionmenu.grid(row=0, column=0, padx=0, pady=0, sticky="ew", columnspan=2)
        self.optionmenu.set(self.optionmenu_values[0])

        self.entry = customtkinter.CTkEntry(self, placeholder_text="input")
        self.entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew", columnspan=2)

        self.label = customtkinter.CTkLabel(self, text=self.data, fg_color="transparent")
        self.label.grid(row=2, column=1, padx=0, pady=0, sticky="ew", columnspan=2)

        self.button = customtkinter.CTkButton(self, text="",fg_color="transparent", image=self.copy_image, width=20, command=self.save_to_clipboard)
        self.button.grid(row=2, column=2, padx=0, pady=0, sticky="ew", columnspan=2)

        self.button = customtkinter.CTkButton(self, text="decoder", command=self.decode)
        self.button.grid(row=3, column=1, padx=0, pady=0, sticky="ew", columnspan=2)

    def set_format(self, selected_option):
        self.format = selected_option

    def decode(self):
        to_map = self.optionmenu.get()
        self.set_format(to_map)
        self.data = self.entry.get()

        func = self.function_mapping[self.format]
        self.result = func(self.data)

        self.update_result_dispay()

    def update_result_dispay(self):
        self.label.configure(text=self.result)

    def save_to_clipboard(self):
        self.clipboard_clear()
        self.clipboard_append(self.result)

app = App()
app.mainloop()
