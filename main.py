import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import iconspath
import config
from CTkToolTip import *
import functions

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
        self.configure(bg=self.tema_atual)
        self.iconbitmap(r"icons\icons8-settings-256.ico")
        self.switch_var = ctk.StringVar(value="#171717")
        
        
        
        self.mudar_tema()

        #Switch que muda o tema
        self.tema = ctk.CTkSwitch(self,
                             text="",
                             command=self.mudar_tema,
                             variable=self.switch_var,
                             onvalue="#171717",
                             offvalue="#d4d4d4",
                             button_color="#0d9488",
                             button_hover_color="#115e59",
                             progress_color="#d4d4d4",
                             fg_color="#171717"
                             )
        self.tema.place(x=130, y=15)

        #Ícone modo escuro
        self.moon_icon = ctk.CTkLabel(self,
                                      text="",
                                      image=iconspath.MOON_ICON
                                      )
        self.moon_icon.place(x=173,y=8)

        #Ícone modo claro
        self.sun_icon = ctk.CTkLabel(self,
                                     text="",
                                     image=iconspath.SUN_ICON
                                     )
        self.sun_icon.place(x=93,y=9)


    def mudar_tema(self):
        self.tema_atual = self.switch_var.get()
        self.configure(bg=self.tema_atual)
    

    def get_tema_atual(self):
        return self.switch_var.get()

#Janela de Login ADM
class AuthAdmin(tk.Toplevel):
    def __init__(self, parent, admin_status):
        super().__init__(parent)
        self.admin_status = admin_status
        self.geometry("300x300")
        self.title("Admin Login")
        self.configure(bg='#0d9488')
        self.resizable(False, False)
        self.senha_oculta = True

        self.lb = ctk.CTkLabel(self,
                               text="Login",
                               text_color="black",
                               font=("Arial", 29)
                               )
        self.lb.place(x=112, y=10)

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
        self.user_entry.place(x=50, y=65)

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
        self.senha_entry.place(x=50, y=130)

        #Botão de recuperar senha
        self.link_recover = ctk.CTkButton(self,
                                    text="Esqueceu sua senha?",
                                    font=("Arial", 13),
                                    fg_color="transparent",
                                    width=8,
                                    height=8,
                                    hover_color="#115e59",
                                    text_color="white",
                                    corner_radius=20,
                                    command=lambda: self.open_recover()
                                    )
        self.link_recover.place(x=55,y=180)

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
        self.login_btn.place(x=110, y=240)

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
        self.show_pass_btn.place(x=210, y=139)

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
        self.hide_pass_btn.place(x=210, y=139)

    # oculta/exibe a senha e altera os ícones
    def show_hide(self):
        if self.senha_oculta:
            self.senha_entry.configure(show="")
            self.hide_pass_btn.place_forget()
            self.show_pass_btn.place(x=210, y=139)
            self.senha_oculta = False
        else:
            self.senha_entry.configure(show="*")
            self.show_pass_btn.place_forget()
            self.hide_pass_btn.place(x=210, y=139)
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
                messagebox.showwarning("Atenção", "A senha deve possuir no mínimo 8 dígitos")
        else:
            messagebox.showwarning("Atenção", "O login deve possuir no mínimo 5 dígitos")

    #Abre a janela de recuperação de senha
    def open_recover(self):
        recover_edge = RecoverEdge(self)
        recover_edge.grab_set()

#Janela para remover um administrador
class DeleteAdmin(tk.Toplevel):
     def __init__(self, parent):
        super().__init__(parent)
        self.geometry("384x410")
        self.title("Deletar Admin")
        self.configure(bg='#0d9488')
        self.resizable(False, False)
    
        self.lb = ctk.CTkLabel(self,
                    text="Deletar Administrador",
                    text_color="black",
                    fg_color="transparent",
                    font=("Arial", 23),
                    
                    )
        self.lb.place(x=90,y=10)

        self.user_entry = ctk.CTkEntry(self,
                            width=176,
                            height=40,
                            corner_radius=20,
                            border_width=2,
                            font=("Arial", 15),
                            border_color="white",
                            fg_color="#171717",
                            text_color="white",
                            placeholder_text_color="#0d9488",
                            placeholder_text="Usuário",
                            )
        self.user_entry.place(x=8,y=70)

        self.email_entry = ctk.CTkEntry(self,
                            width=176,
                            height=40,
                            corner_radius=20,
                            border_width=2,
                            font=("Arial", 15),
                            border_color="white",
                            fg_color="#171717",
                            text_color="white",
                            placeholder_text_color="#0d9488",
                            placeholder_text="E-mail",
                            )
        self.email_entry.place(x=200,y=70)

        self.search_btn = ctk.CTkButton(self,
                            width=30,
                            height=40,
                            text="Buscar",
                            command=lambda: functions.insert(self.info_txb),
                            border_width=2,
                            border_color="white",
                            corner_radius=20,
                            font=("Arial", 16),
                            fg_color='#171717',
                            text_color='#0d9488',
                            hover_color='#115e59',
                            anchor="center",
                            )
        self.search_btn.place(x=145,y=140)

        self.info_txb = ctk.CTkTextbox(self,
                                width=384,
                                height=130,
                                corner_radius=15,
                                border_width=1,
                                border_color='white',
                                text_color="white",
                                fg_color="#171717",
                                font=("Arial", 17),
                                activate_scrollbars=False,
                                wrap="none",
                                )
        self.info_txb.place(x=0,y=200)

        self.delete_btn = ctk.CTkButton(self,
                            width=30,
                            height=40,
                            text="Deletar",
                            command=lambda: print("Deletado"),
                            border_width=2,
                            border_color="#dc2626",
                            corner_radius=20,
                            font=("Arial", 16),
                            fg_color='#171717',
                            text_color='#dc2626',
                            hover_color='#115e59',
                            anchor="center",
                            )
        self.delete_btn.place(x=147,y=352)

#Janela de recuperação de senha (Enviar o código)
class RecoverEdge(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("300x280")
        self.title("Recuperar senha")
        self.configure(bg='#0d9488')
        self.resizable(False, False)

        self.lb = ctk.CTkLabel(self,
                               text="Recuperar senha",
                               text_color="black",
                               font=("Arial", 25)
                               )
        self.lb.place(x=52, y=10)

        #Entry do Email
        self.email_entry = ctk.CTkEntry(self,
                                   width=200,
                                   height=40,
                                   placeholder_text="Email",
                                   placeholder_text_color='#0d9488',
                                   font=("Arial", 14),
                                    border_width=2,
                                    border_color='white',
                                    corner_radius=20,
                                    fg_color="#171717",
                                    )
        self.email_entry.place(x=50, y=65)

        #Entry do usuário
        self.user_entry = ctk.CTkEntry(self,
                                width=200,
                                height=40,
                                font=("Arial", 14),
                                placeholder_text_color='#0d9488',
                                placeholder_text="Usuário",
                                border_width=2,
                                border_color='white',
                                corner_radius=20,
                                fg_color="#171717",
                                show="*"
                                )
        self.user_entry.place(x=50, y=130)

        #Botão de enviar o código
        self.send_btn = ctk.CTkButton(self,
                                width=70,
                                height=40,
                                text="Enviar",
                                font=("Arial", 15),
                                command=lambda: self.open_check(self.email_entry.get(), self.user_entry.get()),
                                border_width=2,
                                corner_radius=20,
                                fg_color="#171717",
                                border_color="white",
                                text_color="#0d9488",
                                hover_color='#115e59',
                                   )
        self.send_btn.place(x=109, y=220)

    #Envia o código de recuperação e abre a janela de checagem
    def open_check(self, email, user):
        if config.verify_email(email):
            if config.verify_user(email, user):
                config.recover_pass(email, user)
                messagebox.showinfo("Atenção", "Um código de verificação foi enviado para o e-mail inserido.")
                check_edge = CheckCodeEdge(self)
                check_edge.grab_set()
            else:
                messagebox.showerror("Erro", "O usuário não corresponde ao e-mail inserido.")
        else:
            messagebox.showerror("Erro", "E-mail não identificado.")


#Janela de verificação do código
class CheckCodeEdge(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("300x280")
        self.title("Recuperar senha")
        self.configure(bg='#0d9488')
        self.resizable(False, False)

#Janela de funções ADM
class ADM(tk.Toplevel):
    def __init__(self, parent, admin_status):
        super().__init__(parent)
        self.admin_status = admin_status
        self.title("Administrador")
        self.geometry("577x400")
        self.resizable(False, False)
        self.configure(bg="#0d9488")
        self.senha_oculta = True
        self.c_senha_oculta = True

        #Texto maior
        self.adm_lb = ctk.CTkLabel(self,
                      text="Administrador",
                      font=("Bold", 27),
                      text_color="black",
                      anchor="center",
                      )
        self.adm_lb.place(x=211, y=6)

        #texto menor
        self.cad_lb = ctk.CTkLabel(self,
                            text="Cadastrar ADM",
                            font=("Bold", 17),
                            text_color="black",
                            anchor="center",
                            )
        self.cad_lb.place(x=238, y=85)

        #Entry do nome
        self.nome_entry = ctk.CTkEntry(self,
                                width=176,
                                height=40,
                                corner_radius=20,
                                border_width=2,
                                border_color="white",
                                font=("Arial", 15),
                                fg_color="#171717",
                                text_color="white",
                                placeholder_text_color="#0d9488",
                                placeholder_text="Nome",
                                )
        self.nome_entry.place(x=4,y=130)

        #Entry do usuário
        self.user_entry = ctk.CTkEntry(self,
                                width=176,
                                height=40,
                                corner_radius=20,
                                border_width=2,
                                font=("Arial", 15),
                                border_color="white",
                                fg_color="#171717",
                                text_color="white",
                                placeholder_text_color="#0d9488",
                                placeholder_text="Usuário",
                                )
        self.user_entry.place(x=202,y=130)

        #Entry do email
        self.email_entry = ctk.CTkEntry(self,
                                width=176,
                                height=40,
                                corner_radius=20,
                                border_width=2,
                                border_color="white",
                                font=("Arial", 15),
                                fg_color="#171717",
                                text_color="white",
                                placeholder_text_color="#0d9488",
                                placeholder_text="Email",
                                )
        self.email_entry.place(x=397,y=130)

        #Entry da senha
        self.senha_entry = ctk.CTkEntry(self,
                                width=176,
                                height=40,
                                corner_radius=20,
                                border_width=2,
                                border_color="white",
                                font=("Arial", 15),
                                fg_color="#171717",
                                text_color="white",
                                placeholder_text_color="#0d9488",
                                placeholder_text="Senha",
                                show="*"
                                )
        self.senha_entry.place(x=99,y=215)

        #Entry de confirmação da senha
        self.c_senha_entry = ctk.CTkEntry(self,
                                width=176,
                                height=40,
                                corner_radius=20,
                                border_width=2,
                                border_color="white",
                                font=("Arial", 15),
                                fg_color="#171717",
                                text_color="white",
                                placeholder_text_color="#0d9488",
                                placeholder_text="Confirmar Senha",
                                show="*"
                                )
        self.c_senha_entry.place(x=315,y=215)

        #Botão de cadastrar
        self.cadastrar_btn = ctk.CTkButton(self,
                                    width=30,
                                    height=40,
                                    text="Cadastrar",
                                    command=lambda: self.onclick(
                                                                self.nome_entry.get(),
                                                                self.user_entry.get(),
                                                                self.email_entry.get(),
                                                                self.senha_entry.get(),
                                                                self.c_senha_entry.get(),
                                                                ),
                                    border_width=2,
                                    border_color="white",
                                    corner_radius=20,
                                    font=("Arial", 16),
                                    fg_color='#171717',
                                    text_color='#0d9488',
                                    hover_color='#115e59'
                                    )
        self.cadastrar_btn.place(x=238, y=300)

        #Botão de exibir a senha do entry da senha
        self.show_btn1 = ctk.CTkButton(self,
                                            text="",
                                            image=iconspath.CLOSED_EYE_ICON,
                                            width=10,
                                            height=10,
                                            corner_radius=50,
                                            fg_color="#171717",
                                            bg_color="#171717",
                                            hover_color="#115e59",
                                            command=self.show_hide_senha
                                           )
        self.show_btn1.place(x=234,y=224)

        #Botão de ocultar a senha do entry da senha
        self.hide_btn1 = ctk.CTkButton(self,
                                            text="",
                                            image=iconspath.EYE_ICON,
                                            width=10,
                                            height=10,
                                            corner_radius=50,
                                            fg_color="#171717",
                                            bg_color="#171717",
                                            hover_color="#115e59",
                                            command=self.show_hide_senha
                                            
                                            )
        self.hide_btn1.place(x=234,y=224)

        #Botão de exibir a senha do entry de confirmação de senha
        self.show_btn2 = ctk.CTkButton(self,
                                            text="",
                                            image=iconspath.CLOSED_EYE_ICON,
                                            width=10,
                                            height=10,
                                            corner_radius=50,
                                            fg_color="#171717",
                                            bg_color="#171717",
                                            hover_color="#115e59",
                                            command=self.show_hide_c_senha
                                            
                                            )
        self.show_btn2.place(x=450,y=224)

        #Botão de ocultar a senha do entry de confirmação de senha
        self.hide_btn2 = ctk.CTkButton(self,
                                            text="",
                                            image=iconspath.EYE_ICON,
                                            width=10,
                                            height=10,
                                            corner_radius=50,
                                            fg_color="#171717",
                                            bg_color="#171717",
                                            hover_color="#115e59",
                                            command=self.show_hide_c_senha
                                            
                                            )
        self.hide_btn2.place(x=450,y=224)

        #Botão para deletar um admin
        self.delete_admin = ctk.CTkButton(self,
                                          width=5,
                                          height=20,
                                          text="Deletar admin?",
                                          fg_color="transparent",
                                          text_color="white",
                                          font=("Arial", 13),
                                          command=lambda: self.deletar_admin(),
                                          hover_color='#115e59',
        )
        self.delete_admin.place(x=5, y=378)
    
    #Abre a janela de deletar admins
    def deletar_admin(self):
        deletar = DeleteAdmin(self)
        deletar.grab_set()

    #Exibe/Esconde a senha do entry da senha
    def show_hide_senha(self):
        if self.senha_oculta:
            self.senha_entry.configure(show="")
            self.hide_btn1.place_forget()
            self.show_btn1.place(x=234,y=224)
            self.senha_oculta = False
        else:
            self.senha_entry.configure(show="*")
            self.show_btn1.place_forget()
            self.hide_btn1.place(x=234,y=224)
            self.senha_oculta = True
        
    #Exibe/Esconde a senha do entry de confirmação de senha
    def show_hide_c_senha(self):
        if self.c_senha_oculta:
            self.c_senha_entry.configure(show="")
            self.hide_btn2.place_forget()
            self.show_btn2.place(x=450,y=224)
            self.c_senha_oculta = False
        else:
            self.c_senha_entry.configure(show="*")
            self.show_btn2.place_forget()
            self.hide_btn2.place(x=450,y=224)
            self.c_senha_oculta = True

    #Cadastra um novo Administrador
    def onclick(self, nome, usuario, email, senha1, senha2):
        if functions.check_field(usuario, 5):
            user = usuario
            if functions.check_req(senha1, senha2):
                if functions.check(senha1, senha2):
                    senha = senha2
                    try:
                        config.create_admin(nome, user, senha, email, config.timenow())
                        messagebox.showinfo("Hey", "Admin cadastrado com sucesso")
                        ### implementar a limpeza de todos os campos ao cadastrar
                    except:
                        messagebox.showwarning("Erro", "Não foi possível realizar o cadastro. Tente novamente")
                else:
                    messagebox.showerror("Erro", "As senhas não se coincidem")
            else:
                messagebox.showerror("Erro", "As senhas devem possuir no mínimo 8 dígitos")
            
        else:
            messagebox.showerror("Erro", f"O Usuário deve ter no mínimo 5 caracteres")

#Janela principal
class Gestor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1400x718")
        self.title("Gerenciamento")
        self.iconbitmap(r'icons\icons8-management-90.ico')
        self.tema_atual = "#171717"
        self.configure(bg=self.tema_atual)
        self.bar_status = "reduced"
        self.admin_status = AdminStatus()
        self.resizable(False, False)
        
        #Frame da opção de férias
        self.ferias_frame = ctk.CTkScrollableFrame(self,
                                         width=0,
                                         height=720,
                                         fg_color=self.tema_atual,
                                         scrollbar_button_color="#0d9488",
                                         scrollbar_button_hover_color="#115e59"
                                         )
        self.ferias_frame.place(x=0,y=0)

        #Frame da opção de Promover
        self.promover_frame = ctk.CTkScrollableFrame(self,
                                         width=0,
                                         height=720,
                                         fg_color=self.tema_atual,
                                         scrollbar_button_color="#0d9488",
                                         scrollbar_button_hover_color="#115e59"
                                         )
        self.promover_frame.place(x=0,y=0)

        #Frame da opção de Horas extras
        self.hora_extra_frame = ctk.CTkScrollableFrame(self,
                                         width=0,
                                         height=720,
                                         fg_color=self.tema_atual,
                                         scrollbar_button_color="#0d9488",
                                         scrollbar_button_hover_color="#115e59"
                                         )
        self.hora_extra_frame.place(x=0,y=0)

        #Frame da opção de Relatório
        self.relatorio_frame = ctk.CTkScrollableFrame(self,
                                         width=0,
                                         height=720,
                                         fg_color=self.tema_atual,
                                         scrollbar_button_color="#0d9488",
                                         scrollbar_button_hover_color="#115e59"
                                         )
        self.relatorio_frame.place(x=0,y=0)

        #Frame da opção de Folha de pagamento
        self.folha_pagamento_frame = ctk.CTkScrollableFrame(self,
                                         width=0,
                                         height=720,
                                         fg_color=self.tema_atual,
                                         scrollbar_button_color="#0d9488",
                                         scrollbar_button_hover_color="#115e59"
                                         )
        self.folha_pagamento_frame.place(x=0,y=0)

        #Frame da opção de Cadastrar
        self.cadastrar_frame = ctk.CTkScrollableFrame(self,
                                         width=0,
                                         height=720,
                                         fg_color=self.tema_atual,
                                         scrollbar_button_color="#0d9488",
                                         scrollbar_button_hover_color="#115e59"
                                         )
        self.cadastrar_frame.place(x=0,y=0)

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
        self.config_btn.place(x=2, y=675)
        self.tooltip8 = CTkToolTip(self.config_btn, "Configurações", delay=0.1)

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
        self.admin_btn.place(x=2, y=600)
        self.tooltip7 = CTkToolTip(self.admin_btn, "Administrador", delay=0.1)

        #Linha que separa as opções de admin/configurações das demais opções
        self.limitador = ctk.CTkFrame(self.sidebar_bg,
                                      width=30,
                                      height=3,
                                      fg_color="#fde047",
                                      corner_radius=20,
                                      )
        self.limitador.place(x=12,y=561)

        #Botão de ferias
        self.ferias_btn = ctk.CTkButton(self.sidebar_bg,
                                       width=45,
                                       height=45,
                                       fg_color="transparent",
                                       hover_color="#115e59",
                                       text="",
                                       image=iconspath.FERIAS_ICON,
                                       command=lambda: functions.open_close_frame(self.ferias_btn, self.states)
                                       )
        self.ferias_btn.place(x=2, y=475)
        self.ferias_btn.name = "ferias"
        self.tooltip6 = CTkToolTip(self.ferias_btn, "Férias", delay=0.1)

        #Botão de Promover
        self.promover_btn = ctk.CTkButton(self.sidebar_bg,
                                       width=45,
                                       height=45,
                                       fg_color="transparent",
                                       hover_color="#115e59",
                                       text="",
                                       image=iconspath.PROMOVER_ICON,
                                       command=lambda: functions.open_close_frame(self.promover_btn, self.states)
                                       )
        self.promover_btn.place(x=2, y=398)
        self.promover_btn.name = "promover"
        self.tooltip5 = CTkToolTip(self.promover_btn, "Promover", delay=0.1)

        #Botão de Horas extras
        self.hora_extra_btn = ctk.CTkButton(self.sidebar_bg,
                                       width=45,
                                       height=45,
                                       fg_color="transparent",
                                       hover_color="#115e59",
                                       text="",
                                       image=iconspath.HORA_EXTRA_ICON,
                                       command=lambda: functions.open_close_frame(self.hora_extra_btn, self.states)
                                       )
        self.hora_extra_btn.place(x=2, y=316)
        self.hora_extra_btn.name = "hora extra"
        self.tooltip4 = CTkToolTip(self.hora_extra_btn, "Horas Extras", delay=0.1)

        #Botãode Relatórios
        self.relatorio_btn = ctk.CTkButton(self.sidebar_bg,
                                       width=45,
                                       height=45,
                                       fg_color="transparent",
                                       hover_color="#115e59",
                                       text="",
                                       image=iconspath.RELATORIO_ICON,
                                       command=lambda: functions.open_close_frame(self.relatorio_btn, self.states)
                                       )
        self.relatorio_btn.place(x=2, y=232)
        self.relatorio_btn.name = "relatorio"
        self.tooltip3 = CTkToolTip(self.relatorio_btn, "Relatório", delay=0.1)

        #Botão de Folha de pagamento
        self.folha_pagamento_btn = ctk.CTkButton(self.sidebar_bg,
                                       width=45,
                                       height=45,
                                       fg_color="transparent",
                                       hover_color="#115e59",
                                       text="",
                                       image=iconspath.FOLHA_PAGAMENTO_ICON,
                                       command=lambda: functions.open_close_frame(self.folha_pagamento_btn, self.states)
                                       )
        self.folha_pagamento_btn.place(x=2, y=154)
        self.folha_pagamento_btn.name = "folha pagamento"
        self.tooltip2 = CTkToolTip(self.folha_pagamento_btn, "Folha de Pagamento", delay=0.1)

        #Botão de cadastro
        self.cadastro_btn = ctk.CTkButton(self.sidebar_bg,
                                       width=45,
                                       height=45,
                                       fg_color="transparent",
                                       hover_color="#115e59",
                                       text="",
                                       image=iconspath.CADASTRO_ICON,
                                       command=lambda: functions.open_close_frame(self.cadastro_btn, self.states)
                                       )
        self.cadastro_btn.place(x=2, y=76)
        self.cadastro_btn.name = "cadastrar"
        self.tooltip1 = CTkToolTip(self.cadastro_btn, "Cadastrar", delay=0.1)

        #Controlador dos frames
        self.states = {
            "ferias": [self.ferias_frame, "reduced"],
            "promover": [self.promover_frame, "reduced"],
            "hora extra": [self.hora_extra_frame, "reduced"],
            "relatorio": [self.relatorio_frame, "reduced"],
            "folha pagamento": [self.folha_pagamento_frame, "reduced"],
            "cadastrar": [self.cadastrar_frame, "reduced"]

        }
            
    #Abre a janela de configurações
    def open_config(self):
        config = ConfigEdge(self)
        config.grab_set()

        #Define o tema que será a´licado nas demais janelas
        def on_switch_change(*args):
            tema_atual_edge = config.get_tema_atual()
            self.tema_atual = tema_atual_edge
            self.configure(bg=self.tema_atual)
            self.ferias_frame.configure(fg_color=self.tema_atual)
            self.promover_frame.configure(fg_color=self.tema_atual)
            self.hora_extra_frame.configure(fg_color=self.tema_atual)
            self.relatorio_frame.configure(fg_color=self.tema_atual)
            self.folha_pagamento_frame.configure(fg_color=self.tema_atual)
            self.cadastrar_frame.configure(fg_color=self.tema_atual)
        config.switch_var.trace("w", on_switch_change)  #Aplica o tema que foi definido
        
    #Recua/Expande a barra lateral
    def onclick(self):
        if self.bar_status == "reduced":
            self.sidebar_bg.configure(width=300)
            self.bar_status = "expanded"
            self.sidebar_btn.place_forget()
            self.admin_btn.place(x=70, y=675)
            self.limitador.configure(width=300, height=3)
            self.limitador.place(x=0,y=650)

        elif self.bar_status == "expanded":
            self.sidebar_bg.configure(width=55)
            self.bar_status = "reduced"
            self.sidebar_btn.place(x=2, y=3)
            self.admin_btn.place(x=2, y=600)
            self.limitador.configure(width=30, height=3)
            self.limitador.place(x=12,y=561)
  
    #Abre a janela de adm (Se estiver logado), se não estiver, abre a janela de autenticação
    def admin_cmd(self):
        if not self.admin_status.is_logged():
            auth = AuthAdmin(self, self.admin_status)
            auth.grab_set()
        else:
            adm = ADM(self, self.admin_status)
            adm.grab_set()


if __name__ == "__main__":
    gestor = Gestor()
    gestor.mainloop()
