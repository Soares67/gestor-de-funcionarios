import customtkinter as ctk

def home_widgets(master):

    #Frame do cabeçalho
    header_frame = ctk.CTkFrame(master,
                                            width=1365,
                                            height=50,
                                            fg_color="#14b8a6",
                                            )
    header_frame.place(x=40, y=0)

    #Texto do cabeçalho
    lb1 = ctk.CTkLabel(header_frame,
                                    text="Funcionários",
                                    font=("Roboto", 30, "bold"),
                                    text_color="#171717"
                                    )
    lb1.place(x=620,y=7)

    #Frame das estatisticas
    stat_frame = ctk.CTkFrame(master,
                          width=455,
                          height=668,
                          fg_color="red"
                          )
    stat_frame.place(x=40,y=51)

    #Frame do gráfico de gêneros
    gen_frame = ctk.CTkFrame(master,
                             width=455,
                             height=333,
                             fg_color="green"
                             )
    gen_frame.place(x=494,y=51)

    #Frame do gráfico de idades
    age_frame = ctk.CTkFrame(master,
                             width=455,
                             height=333,
                             fg_color="blue"
                             )
    age_frame.place(x=494,y=385)

    #Frame do gráfico de áreas
    area_frame = ctk.CTkFrame(master,
                             width=455,
                             height=333,
                             fg_color="orange"
                             )
    area_frame.place(x=949,y=51)

    #Frame do gráfico de cargos
    pos_frame = ctk.CTkFrame(master,
                             width=455,
                             height=333,
                             fg_color="purple"
                             )
    pos_frame.place(x=949,y=385)

    #Botão de atualizar as informações
    ref_btn = ctk.CTkButton(header_frame,
                            text="Atualizar",
                            command=lambda: print("Atualizar"),
                            font=("Roboto", 16),
                            width=90,
                            height=35,
                            corner_radius=20,
                            border_width=2,
                            border_color="black"
                            )
    ref_btn.place(x=1200,y=8)