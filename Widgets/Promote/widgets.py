import customtkinter as ctk


def promote_widgets(master):

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
                               command=lambda: print("Resultado")
                               )
    search_btn.place(x=243,y=187)

    # Frame onde é exibido a resposta da busca
    # res_frame = ctk.CTkFrame(searcher_frame,
    #                          width=683,
    #                          height=409,
    #                          fg_color="#CBCBCB",
    #                          border_width=4,
    #                          border_color="black"
    #                          )
    # res_frame.place(x=-4,y=280)

    # Frame das abas de ações
    tabs_frame = ctk.CTkFrame(master,
                                  width=674,
                                  height=669,
                                  fg_color="red",
                                  corner_radius=0
                                  )
    tabs_frame.place(x=674,y=50)