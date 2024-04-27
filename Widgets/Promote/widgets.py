import customtkinter as ctk
import private
from Icons.iconspath import PROMOTED_ICON

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
    tabs.add("Editar")
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