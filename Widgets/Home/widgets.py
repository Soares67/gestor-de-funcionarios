import customtkinter as ctk

def home_widgets(master):

    #Frame do cabeçalho
    header_frame = ctk.CTkFrame(master,
                                            width=1366,
                                            height=52,
                                            fg_color="#0891b2",
                                            border_width=2,
                                            border_color="black"
                                            )
    header_frame.place(x=39, y=-2)

    #Texto do cabeçalho
    lb1 = ctk.CTkLabel(header_frame,
                                    text="Funcionários",
                                    font=("Roboto", 30, "bold"),
                                    text_color="white"
                                    )
    lb1.place(x=620,y=7)

    #Frame das estatisticas
    stat_frame = ctk.CTkFrame(master,
                          width=455,
                          height=668,
                          fg_color="red",
                          corner_radius=0
                          )
    stat_frame.place(x=40,y=50)

    #Frame do gráfico de gêneros
    gen_frame = ctk.CTkFrame(master,
                             width=456,
                             height=334,
                             fg_color="green",
                             corner_radius=0
                             )
    gen_frame.place(x=494,y=50)

    #Frame do gráfico de idades
    age_frame = ctk.CTkFrame(master,
                             width=456,
                             height=336,
                             fg_color="blue",
                             corner_radius=0
                             )
    age_frame.place(x=494,y=382)

    #Frame do gráfico de áreas
    area_frame = ctk.CTkFrame(master,
                             width=455,
                             height=334,
                             fg_color="orange",
                             corner_radius=0
                             )
    area_frame.place(x=949,y=50)

    #Frame do gráfico de cargos
    pos_frame = ctk.CTkFrame(master,
                             width=456,
                             height=336,
                             fg_color="purple",
                             corner_radius=0
                             )
    pos_frame.place(x=949,y=382)

    #Botão de atualizar as informações
    ref_btn = ctk.CTkButton(header_frame,
                            text="Atualizar",
                            command=lambda: print("Atualizar"),
                            font=("Roboto", 16, "bold"),
                            width=90,
                            height=35,
                            corner_radius=20,
                            border_width=2,
                            border_color="#FB9C8D",
                            fg_color="#171717"
                            )
    ref_btn.place(x=1200,y=8)