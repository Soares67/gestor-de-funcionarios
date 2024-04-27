import customtkinter as ctk
import private
from Icons.iconspath import PROMOTED_ICON, FIRED_ICON

def promote_widgets(master):

    def insert_text():
        res_txb.insert(0.0, private.data)

    # Função que configura os botôes das abas
    def configure_seg_button(buttons: dict):
        for item in buttons:
            buttons[item].configure(width=50)  # Aumenta a largura
            buttons[item].configure(height=40)  # Aumenta a altura
            buttons[item].configure(font=("Roboto", 15, "bold"))  # Muda a fonte e o tamanho do texto
            buttons[item].configure(border_width=1)  # Adiciona uma borda
            buttons[item].configure(border_color="white")  # Muda a cor da borda

    # Remove o texto guia
    def remove_placeholder(event):
        if obs.get("0.0", "end") == "Observações / Comentários\n":
            obs.delete("0.0", "end")

    # Adiciona o texto guia
    def place_placeholder(event):
        if len(obs.get("0.0", "end")) < 2:
            obs.insert("0.0", "Observações / Comentários")

    # Frame do cabeçalho
    header_frame = ctk.CTkFrame(master,
                                width=1356,
                                height=52,
                                fg_color="green",
                                border_width=3,
                                border_color="black"
                                )
    header_frame.place(x=-3,y=-2)

    # Texto do cabeçalho
    header_text = ctk.CTkLabel(header_frame,
                               text="Promover / Demitir Funcionário",
                               font=("Roboto", 30, "bold"),
                               text_color="white"
                               )
    header_text.place(x=474,y=9)

    # Frame do buscador
    searcher_frame = ctk.CTkFrame(master,
                                  width=674,
                                  height=668,
                                  fg_color="blue",
                                  corner_radius=0
                                  )
    searcher_frame.place(x=0,y=50)
    
    # Texto do buscador
    lb1 = ctk.CTkLabel(searcher_frame,
                       text="Buscar Funcionário",
                       font=("Roboto", 30, "bold"),
                       text_color="black",
                       )
    lb1.place(x=195,y=35)

    # Entry do buscador
    searcher_entry = ctk.CTkEntry(searcher_frame,
                                  width=432,
                                  height=60,
                                  placeholder_text="Nome/Email",
                                  corner_radius=20,
                                  font=("Arial", 16, "bold")
                                  )
    searcher_entry.place(x=119,y=90)

    # botão de buscar
    search_btn = ctk.CTkButton(searcher_frame,
                               width=150,
                               height=50,
                               text="Buscar",
                               font=("Arial", 16, "bold"),
                               corner_radius=20,
                               border_width=2,
                               border_color="white",
                               command=lambda: insert_text()
                               )
    search_btn.place(x=243,y=187)

    # TextBox onde é exibido o resultado da busca
    res_txb = ctk.CTkTextbox(searcher_frame,
                             width=680,
                             height=400,
                             activate_scrollbars=False,
                             font=("Arial", 19, "bold"),
                             text_color="black",
                             fg_color="gray",
                             )
    res_txb.place(x=0,y=280)

    # Frame das abas de ações
    tabs_frame = ctk.CTkFrame(master,
                                  width=674,
                                  height=669,
                                  fg_color="red",
                                  corner_radius=0
                                  )
    tabs_frame.place(x=674,y=50)

    # Abas de opções
    tabs = ctk.CTkTabview(tabs_frame,
                          width=674,
                          height=673,
                          )
    tabs.place(x=0,y=0)
    
    # Abas
    tabs.add("Promover")
    tabs.add("Demitir")
    configure_seg_button(tabs._segmented_button._buttons_dict)

    # Frame da imagem da aba promover
    img_promote_frame = ctk.CTkFrame(tabs.tab("Promover"),
                                     width=342,
                                     height=342,
                                     fg_color="red"
                                     )
    img_promote_frame.place(x=0,y=10)

    # Imagem
    img_promoted = ctk.CTkLabel(tabs.tab("Promover"),
                                text="",
                                image=PROMOTED_ICON
                                )
    img_promoted.place(x=0,y=10)

    # Entry do novo cargo
    new_pos_entry = ctk.CTkEntry(tabs.tab("Promover"),
                                 width=280,
                                 height=50,
                                 placeholder_text="Novo cargo",
                                 corner_radius=20,
                                 font=("Roboto", 16, "bold")
                                 )
    new_pos_entry.place(x=364,y=39)

    # Entry do novo salário
    new_sal_entry = ctk.CTkEntry(tabs.tab("Promover"),
                                 width=280,
                                 height=50,
                                 placeholder_text="Novo salário",
                                 corner_radius=20,
                                 font=("Roboto", 16, "bold")
                                 )
    new_sal_entry.place(x=364,y=163)

    # Opções de motivo
    opts = ctk.CTkComboBox(tabs.tab("Promover"),
                            width=280,
                            height=50,
                            corner_radius=20,
                            values=["Desempenho excepcional",
                                    "Conclusão de treinamento ou certificação",
                                    "Tempo de serviço",
                                    "Aquisição de novas habilidades",
                                    "Liderança e iniciativa",
                                    "Excelência no atendimento ao cliente",
                                    "Outros (especifique)"
                                    ],
                            font=("Roboto", 16, "bold"),
                            dropdown_font=("Roboto", 16, "bold"),
                           )
    opts.set("Motivo")
    opts.place(x=364,y=288)

    # Botão de salvar
    save_btn = ctk.CTkButton(tabs.tab("Promover"),
                             width=150,
                             height=50,
                             corner_radius=20,
                             font=("Roboto", 16, "bold"),
                             text="Salvar",

                             )
    save_btn.place(x=288,y=465)


    # Frame da imagem da aba demitir
    img_fire_frame = ctk.CTkFrame(tabs.tab("Demitir"),
                                     width=342,
                                     height=342,
                                     fg_color="red"
                                     )
    img_fire_frame.place(x=0,y=10)

    # Imagem
    fired_img = ctk.CTkLabel(tabs.tab("Demitir"),
                             text="",
                             image=FIRED_ICON
                             )
    fired_img.place(x=0,y=10)

    # Opções de motivo
    opts2 = ctk.CTkComboBox(tabs.tab("Demitir"),
                            width=280,
                            height=50,
                            corner_radius=20,
                            values=["Pedido de demissão voluntária",
                                    "Desempenho insatisfatório",
                                    "Violação das políticas da empresa",
                                    "Abandono de emprego",
                                    "Conclusão de contrato ou projeto",
                                    "Redução de quadro de funcionários",
                                    "Má conduta",
                                    "Aposentadoria",
                                    "Incompatibilidade com a cultura da empresa",
                                    "Razões pessoais",
                                    "Outros (especifique)"
                                    ],
                            font=("Roboto", 16, "bold"),
                            dropdown_font=("Roboto", 16, "bold"),
                            border_width=3
                           )
    opts2.set("Motivo")
    opts2.place(x=364,y=43)

    # Campo de observações e comentários extras
    obs = ctk.CTkTextbox(tabs.tab("Demitir"),
                         width=280,
                         height=215,
                         font=("Roboto", 16, "bold"),
                         border_width=3
                         )
    obs.insert("0.0", "Observações / Comentários")
    obs.place(x=364,y=139)
    obs.bind("<FocusIn>", remove_placeholder)
    obs.bind("<FocusOut>", place_placeholder)

    # Botão de salvar
    save_btn2 = ctk.CTkButton(tabs.tab("Demitir"),
                             width=150,
                             height=50,
                             corner_radius=20,
                             font=("Roboto", 16, "bold"),
                             text="Salvar",

                             )
    save_btn2.place(x=288,y=465)