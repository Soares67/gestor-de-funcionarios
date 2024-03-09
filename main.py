import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import iconspath
import config

#Classe que controla o status do admin
class AdminStatus:
    def __init__(self):
        self.logged = False

    def login(self):
        self.logged = True

    def logout(self):
        self.logged = False

    def is_logged(self):
        return self.logged


#Janela de configurações
class ConfigEdge(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("300x300")
        self.title("Configurações")
        self.resizable(False, False)
        self.tema_atual = "#171717"
        self.configure(bg=self.tema_atual)  # Set background color
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
        tema.place(x=130, y=3)


    def mudar_tema(self):
        self.tema_atual = self.switch_var.get()
        self.configure(bg=self.tema_atual)
    

    def get_tema_atual(self):
        return self.switch_var.get()


#Janela de Login ADM
class AuthAdmin(tk.Toplevel):
    def __init__(self, parent, tema, admin_status):
        super().__init__(parent)
        self.admin_status = admin_status
        self.geometry("300x300")
        self.title("Admin Login")
        self.configure(bg='#0d9488')
        self.resizable(False, False)
        self.senha_oculta = True

        #Entry do usuário
        self.user_entry = ctk.CTkEntry(self,
                                   width=200,
                                   height=40,
                                   placeholder_text="Usuário",
                                   placeholder_text_color='#0d9488',
                                   font=("Arial", 14),
                                    border_width=2,
                                    border_color='white',
                                    corner_radius=20,
                                    fg_color="#171717",
                                    )
        self.user_entry.place(x=50, y=15)

        #Entry da senha
        self.senha_entry = ctk.CTkEntry(self,
                                width=200,
                                height=40,
                                font=("Arial", 14),
                                placeholder_text_color='#0d9488',
                                placeholder_text="Senha",
                                border_width=2,
                                border_color='white',
                                corner_radius=20,
                                fg_color="#171717",
                                show="*"
                                )
        self.senha_entry.place(x=50, y=90)

        #Botão de recuperar senha
        self.link_recover = ctk.CTkButton(self,
                                    text="Esqueceu sua senha?",
                                    font=("Arial", 13),
                                    fg_color="transparent",
                                    width=8,
                                    height=8,
                                    hover_color="#115e59",
                                    text_color="white",
                                    corner_radius=20
                                    )
        self.link_recover.place(x=55,y=140)

        #Botão de fazer login
        self.login_btn = ctk.CTkButton(self,
                                width=70,
                                height=40,
                                text="Login",
                                font=("Arial", 15),
                                command=lambda: self.autenticacao(),
                                border_width=2,
                                corner_radius=20,
                                fg_color="#171717",
                                border_color="white",
                                text_color="#0d9488",
                                hover_color='#115e59',
                                   )
        self.login_btn.place(x=110, y=200)

        #Botão de mostrar a senha   (São dois botões pois altera o ícone quando pressionado)
        self.show_pass_btn = ctk.CTkButton(self,
                                           text="",
                                           image=iconspath.CLOSED_EYE_ICON,
                                           width=10,
                                           height=10,
                                           corner_radius=50,
                                           fg_color="#171717",
                                           bg_color="#171717",
                                           hover_color="#115e59",
                                           command=self.show_hide
                                           )
        self.show_pass_btn.place(x=210, y=99)

        #Botão de ocultar a senha
        self.hide_pass_btn = ctk.CTkButton(self,
                                            text="",
                                            image=iconspath.EYE_ICON,
                                            width=10,
                                            height=10,
                                            corner_radius=50,
                                            fg_color="#171717",
                                            bg_color="#171717",
                                            hover_color="#115e59",
                                            command=self.show_hide
                                           )
        self.hide_pass_btn.place(x=210, y=99)

    
    # oculta/exibe a senha e altera os ícones
    def show_hide(self):
        if self.senha_oculta:
            self.senha_entry.configure(show="")
            self.hide_pass_btn.place_forget()
            self.show_pass_btn.place(x=210, y=99)
            self.senha_oculta = False
        else:
            self.senha_entry.configure(show="*")
            self.show_pass_btn.place_forget()
            self.hide_pass_btn.place(x=210, y=99)
            self.senha_oculta = True
    
    #Autentica os admins
    def autenticacao(self):
        if len(self.user_entry.get()) >= 5:
            if len(self.senha_entry.get()) >= 8:
                if config.auth_admin(self.user_entry.get(), self.senha_entry.get()):
                    messagebox.showinfo("hey", "Admin logado com sucesso")
                    self.admin_status.login()
                    self.destroy()
                else:
                    messagebox.showerror("Erro", "Login ou senha incorretos")
        else:
            messagebox.showwarning("Atenção", "O login deve possuir no mínimo 5 dígitos")



#Janela de funções ADM
class ADM(tk.Toplevel):
    def __init__(self, parent, tema, admin_status):
        super().__init__(parent)
        self.admin_status = admin_status
        self.title("ADM")
        self.geometry("300x300")


#Janela principal
class Gestor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x600")
        self.title("Gerenciamento")
        self.iconbitmap(r'icons\icons8-management-90.ico')
        self.resizable(False, False)
        self.tema_atual = "#171717"
        self.configure(bg=self.tema_atual)
        self.bar_status = 'reduced'
        self.admin_status = AdminStatus()
        
        # Fundo da barra lateral inicial
        self.sidebar_bg = ctk.CTkFrame(self,
                              fg_color='#0d9488',
                              width=55,
                              height=1000,
                              border_width=2,
                              border_color='#fde047'
                            )
        self.sidebar_bg.place(x=-2, y=-3)
        

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
        self.sidebar_btn.place(x=2, y=6)

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


        #Botão de Fechar a barra lateral
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

        #Botão admin (Autenticar/Ações)
        self.admin_btn = ctk.CTkButton(self.sidebar_bg,
                                       width=45,
                                       height=45,
                                       fg_color="transparent",
                                       hover_color="#115e59",
                                       text="",
                                       image=iconspath.ADMIN_ICON,
                                       command=self.admin_cmd
                                       )
        self.admin_btn.place(x=2, y=490)

        #Linha que separa as opções de admin/configurações das demais opções
        self.limitador = ctk.CTkFrame(self.sidebar_bg,
                                      width=30,
                                      height=3,
                                      fg_color="#fde047",
                                      corner_radius=20,
                                      )
        self.limitador.place(x=12,y=461)

        #Botão de feriados
        self.ferias_btn = ctk.CTkButton(self.sidebar_bg,
                                       width=45,
                                       height=45,
                                       fg_color="transparent",
                                       hover_color="#115e59",
                                       text="",
                                       image=iconspath.FERIAS_ICON,
                                       command=lambda: print("Férias")
                                       )
        self.ferias_btn.place(x=2, y=390)

        #Botão de Promover
        self.promover_btn = ctk.CTkButton(self.sidebar_bg,
                                       width=45,
                                       height=45,
                                       fg_color="transparent",
                                       hover_color="#115e59",
                                       text="",
                                       image=iconspath.PROMOVER_ICON,
                                       command=lambda: print("Promover")
                                       )
        self.promover_btn.place(x=2, y=326)

        #Botão de Horas extras
        self.hora_extra_btn = ctk.CTkButton(self.sidebar_bg,
                                       width=45,
                                       height=45,
                                       fg_color="transparent",
                                       hover_color="#115e59",
                                       text="",
                                       image=iconspath.HORA_EXTRA_ICON,
                                       command=lambda: print("Hora extra")
                                       )
        self.hora_extra_btn.place(x=2, y=262)

        #Botãode Relatórios
        self.relatorio_bt = ctk.CTkButton(self.sidebar_bg,
                                       width=45,
                                       height=45,
                                       fg_color="transparent",
                                       hover_color="#115e59",
                                       text="",
                                       image=iconspath.RELATORIO_ICON,
                                       command=lambda: print("Relatório")
                                       )
        self.relatorio_bt.place(x=2, y=198)

        #Botão de Folha de pagamento
        self.folha_pagamento_btn = ctk.CTkButton(self.sidebar_bg,
                                       width=45,
                                       height=45,
                                       fg_color="transparent",
                                       hover_color="#115e59",
                                       text="",
                                       image=iconspath.FOLHA_PAGAMENTO_ICON,
                                       command=lambda: print("Folha de pagamento")
                                       )
        self.folha_pagamento_btn.place(x=2, y=134)

        #Botão de cadastro
        self.cadastro_btn = ctk.CTkButton(self.sidebar_bg,
                                       width=45,
                                       height=45,
                                       fg_color="transparent",
                                       hover_color="#115e59",
                                       text="",
                                       image=iconspath.CADASTRO_ICON,
                                       command=lambda: print("Cadastrar")
                                       )
        self.cadastro_btn.place(x=2, y=70)


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
        self.admin_btn.place(x=55, y=553)
        self.limitador.configure(width=300, height=3)
        self.limitador.place(x=0,y=543)
    

    def reduce(self):
        self.sidebar_bg.configure(width=52)
        self.bar_status = "reduced"
        self.sidebar_btn.place(x=2, y=3)
        self.admin_btn.place(x=2, y=490)
        self.limitador.configure(width=30, height=3)
        self.limitador.place(x=12,y=461)
        


    def onclick(self):
        if self.bar_status == "reduced":
            self.expand()
        elif self.bar_status == "expanded":
            self.reduce()

    
    def open_auth_adm(self):
        auth = AuthAdmin(self, self.tema_atual, self.admin_status)
        auth.grab_set()

    def open_adm(self):
        adm = ADM(self, self.tema_atual, self.admin_status)
        adm.grab_set()

    def admin_cmd(self):
        if not self.admin_status.is_logged():
            self.open_auth_adm()
        else:
            self.open_adm()


if __name__ == "__main__":
    gestor = Gestor()
    gestor.mainloop()
