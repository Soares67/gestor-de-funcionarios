import tkinter as tk
import customtkinter as ctk
import iconspath

class ConfigEdge(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("300x300")
        self.title("Configurações")
        self.resizable(False, False)
        self.configure(bg="")
        self.iconbitmap(r"icons\icons8-settings-256.ico")
        self.tema_atual = "#0d9488"
        

        tema = ctk.CTkSwitch(self,
                             onvalue="#282424",
                             offvalue="#d4d4d8",
                             ).pack()


class Gestor(tk.Tk):

    def __init__(self, config):
        super().__init__()
        self.geometry("1000x600")
        self.title("Gerenciamento")
        self.resizable(False, False)
        self.tema_atual = config.tema_atual
        self.configure(bg=self.tema_atual)
        
        # Fundo da barra lateral inicial
        sidebar_bg = tk.Frame(self,
                              bg=self.tema_atual,
                              width=52,
                              height=1000)
        sidebar_bg.place(x=0, y=0)

        # Botão da barra lateral
        sidebar_btn = ctk.CTkButton(master=sidebar_bg,
                                    width=45,
                                    height=45,
                                    text="",
                                    image=iconspath.SIDEBAR_ICON,
                                    fg_color="transparent",
                                    hover_color="#115e59")
        sidebar_btn.place(x=2, y=3)

        # Botão de configurações
        config_btn = ctk.CTkButton(master=sidebar_bg,
                                   width=45,
                                   height=45,
                                   text="",
                                   image=iconspath.SETTINGS_ICON,
                                   fg_color="transparent",
                                   hover_color="#115e59",
                                   command=self.open_config,
                                   )
        config_btn.place(x=2, y=553)


    def open_config(self):
        config = ConfigEdge(self)
        config.grab_set()

if __name__ == "__main__":
    gestor = Gestor()
    gestor.mainloop()
