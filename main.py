import tkinter as tk
import customtkinter as ctk
import iconspath

class ConfigEdge(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("300x300")
        self.title("Configurações")
        self.resizable(False, False)
        self.tema_atual = "#171717"
        self.configure(bg=self.tema_atual)
        self.iconbitmap(r"icons\icons8-settings-256.ico")
        self.switch_var = ctk.StringVar(value="#171717")
        
        
        self.mudar_tema()
        tema = ctk.CTkSwitch(self,
                             text="",
                             command=self.mudar_tema,
                             variable=self.switch_var,
                             onvalue="#171717",
                             offvalue="#d4d4d4"
                             )
        tema.place(x=130,y=3)

    def mudar_tema(self):
        self.tema_atual = self.switch_var.get()
        self.configure(bg=self.tema_atual)
    

    def get_tema_atual(self):
        return self.switch_var.get()


class Gestor(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("1000x600")
        self.title("Gerenciamento")
        self.resizable(False, False)
        self.tema_atual = "#171717"
        self.configure(bg=self.tema_atual)
        self.bar_status = 'reduced'
        
        # Fundo da barra lateral inicial
        self.sidebar_bg = tk.Frame(self,
                              bg='#0d9488',
                              width=52,
                              height=1000)
        self.sidebar_bg.place(x=0, y=0)
        

        # Botão da barra lateral
        self.sidebar_btn = ctk.CTkButton(master=self.sidebar_bg,
                                    width=45,
                                    height=45,
                                    text="",
                                    image=iconspath.SIDEBAR_ICON,
                                    fg_color="transparent",
                                    hover_color="#115e59",
                                    command=self.onclick,
                                    )
        self.sidebar_btn.place(x=2, y=3)

        # Botão de configurações
        self.config_btn = ctk.CTkButton(master=self.sidebar_bg,
                                   width=45,
                                   height=45,
                                   text="",
                                   image=iconspath.SETTINGS_ICON,
                                   fg_color="transparent",
                                   hover_color="#115e59",
                                   command=self.open_config,
                                   )
        self.config_btn.place(x=2, y=553)


        self.close_sidebar = ctk.CTkButton(self.sidebar_bg,
                                           width=45,
                                           height=45,
                                           fg_color="transparent",
                                           hover_color="#115e59",
                                           text="",
                                           image=iconspath.CLOSE_ICON,
                                           command=self.onclick,
                                           )
        self.close_sidebar.place(x=250,y=4)



    def open_config(self):
        config = ConfigEdge(self)
        config.grab_set()

        def on_switch_change(*args):
            tema_atual_edge = config.get_tema_atual()
            self.tema_atual = tema_atual_edge
            self.configure(bg=self.tema_atual)
        config.switch_var.trace("w", on_switch_change)
    

    def expand(self):
        self.sidebar_bg.configure(width=300)
        self.bar_status = "expanded"
        self.sidebar_btn.place_forget()
    

    def reduce(self):
        self.sidebar_bg.configure(width=52)
        self.bar_status = "reduced"
        self.sidebar_btn.place(x=2, y=3)


    def onclick(self):
        if self.bar_status == "reduced":
            self.expand()
        elif self.bar_status == "expanded":
            self.reduce()

        
        
        



if __name__ == "__main__":
    gestor = Gestor()
    gestor.mainloop()
