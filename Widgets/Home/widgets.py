import customtkinter as ctk
from Icons.iconspath import REFRESH_ICON

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
                          fg_color="#FB9C8D",
                          corner_radius=0
                          )
    stat_frame.place(x=40,y=50)

    # Título da quantidade de  funcionários
    qtde_emp_title = ctk.CTkLabel(stat_frame,
                                   text="Quantidade de Funcionários",
                                   font=("Roboto", 26, "bold"),
                    text_color="black",
    )
    qtde_emp_title.place(x=53,y=40)

    # Label da quantidade de funcionários
    qtde_emp = ctk.CTkLabel(stat_frame,
                            text="200",
                            font=("Roboto", 28, "bold"),
                            width=309,
                            height=66,
                            text_color="black",
                            fg_color="#e4e4e7",
                            corner_radius=20
                            )
    qtde_emp.place(x=77,y=80)

    # Título do salário médio bruto
    sal_mean_title = ctk.CTkLabel(stat_frame,
                                  text="Salário Médio Bruto",
                                  font=("Roboto", 26, "bold"),
                    text_color="black"

                                  )
    sal_mean_title.place(x=110,y=196)

    # Label do salário médio bruto
    val_sal_mean = ctk.CTkLabel(stat_frame,
                            text="3.200,00",
                            font=("Roboto", 28, "bold"),
                            width=309,
                            height=66,
                            text_color="black",
                            fg_color="#e4e4e7",
                            corner_radius=20
                            )
    val_sal_mean.place(x=77,y=236)

    # Título do maior salário
    max_sal_title = ctk.CTkLabel(stat_frame,
                                 text="Maior Salário",
                                 font=("Roboto", 26, "bold"),
                    text_color="black"
                                 )
    max_sal_title.place(x=150,y=352)

    # Label do maior salário
    max_sal_val = ctk.CTkLabel(stat_frame,
                            text="6.500,00",
                            font=("Roboto", 28, "bold"),
                            width=309,
                            height=66,
                            text_color="black",
                            fg_color="#e4e4e7",
                            corner_radius=20
                            )
    max_sal_val.place(x=77,y=392)

    # Título do menor salário
    min_sal_title = ctk.CTkLabel(stat_frame,
                    text="Menor Salário",
                    font=("Roboto", 26, "bold"),
                    text_color="black"
                    )
    min_sal_title.place(x=150,y=508)

    # Label do menor salário
    min_sal_val = ctk.CTkLabel(stat_frame,
                            text="1.300,00",
                            font=("Roboto", 28, "bold"),
                            width=309,
                            height=66,
                            text_color="black",
                            fg_color="#e4e4e7",
                            corner_radius=20
                            )
    min_sal_val.place(x=77,y=548)

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
                             width=1404,
                             height=336,
                             fg_color="blue",
                             corner_radius=0
                             )
    age_frame.place(x=494,y=382)

    #Frame do gráfico de áreas
    area_frame = ctk.CTkFrame(master,
                             width=455,
                             height=334,
                             fg_color="red",
                             corner_radius=0
                             )
    area_frame.place(x=949,y=50)

    #Botão de atualizar as informações
    ref_btn = ctk.CTkButton(header_frame,
                            text="",
                            image=REFRESH_ICON,
                            command=lambda: print("Atualizar"),
                            corner_radius=20,
                            width=20,
                            height=20,
                            fg_color="transparent",
                            border_color="white",
                            border_width=2,
                            hover_color="#155e75"
    )
    ref_btn.place(x=1200,y=7)

    # Delimitadores

    stats_del = ctk.CTkFrame(master,
                             width=2,
                             height=668,
                             fg_color="black"
                             )
    stats_del.place(x=494,y=50)

    age_del = ctk.CTkFrame(master,
                             width=1404,
                             height=2,
                             fg_color="black"
                             )
    age_del.place(x=494,y=382)

    gen_del = ctk.CTkFrame(master,
                             width=2,
                             height=334,
                             fg_color="black"
                             )
    gen_del.place(x=949,y=50)