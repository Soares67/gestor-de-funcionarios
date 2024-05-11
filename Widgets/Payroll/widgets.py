import customtkinter as ctk

def payroll_widgets(master):


    # Frame do cabeçalho
    header_frame = ctk.CTkFrame(master,
                                width=1360,
                                height=53,
                                fg_color="blue",
                                corner_radius=0,
                                border_width=3,
                                border_color="black"
                                )
    header_frame.place(x=-5,y=-3)

    # Texto do cabeçalho
    lb1 = ctk.CTkLabel(header_frame,
                       text="Folha de Pagamento",
                       font=("Roboto", 30, "bold"),
                       text_color="black"
                       )
    lb1.place(x=540, y=9)


    # Frame do total
    total_frame = ctk.CTkFrame(master,
                               width=336,
                               height=255,
                               fg_color="#FB9C8D",
                               corner_radius=0
                               )
    total_frame.place(x=0,y=50)

    # Texto do total
    lb2 = ctk.CTkLabel(total_frame,
                       text="Total Folha de Pagamento",
                       font=("Roboto", 26, "bold"),
                       text_color="black"
                       )
    lb2.place(x=2, y=19)

    # Campo do total
    total_payroll_field = ctk.CTkLabel(total_frame,
                       text="R$ 152.675,00",
                       font=("Roboto", 26, "bold"),
                       text_color="black",
                       width=180,
                       height=70,
                       fg_color="white",
                       corner_radius=20
                       )
    total_payroll_field.place(x=53, y=80)


    

    # Frame do total férias
    total1_frame = ctk.CTkFrame(master,
                               width=336,
                               height=255,
                               fg_color="green",
                               corner_radius=0
                               )
    total1_frame.place(x=335,y=50)

    # Texto do total férias
    lb3 = ctk.CTkLabel(total1_frame,
                       text="Total Férias",
                       font=("Roboto", 26, "bold"),
                       text_color="black"
                       )
    lb3.place(x=90, y=19)

    # Campo do total férias
    total_vac_field = ctk.CTkLabel(total1_frame,
                       text="R$ 19.246,00",
                       font=("Roboto", 26, "bold"),
                       text_color="black",
                       width=180,
                       height=70,
                       fg_color="white",
                       corner_radius=20
                       )
    total_vac_field.place(x=53, y=80)


    # Frame do total por área
    total2_frame = ctk.CTkFrame(master,
                               width=690,
                               height=255,
                               fg_color="pink",
                               corner_radius=0
                               )
    total2_frame.place(x=672,y=50)

    # Texto do total de salários por área
    lb4 = ctk.CTkLabel(total2_frame,
                       text="Total de Salários por Área",
                       font=("Roboto", 26, "bold"),
                       text_color="black"
                       )
    lb4.place(x=170, y=9)


    # Frame do salário bruto por funcionário
    total3_frame = ctk.CTkFrame(master,
                               width=1360,
                               height=413,
                               fg_color="yellow",
                               corner_radius=0
                               )
    total3_frame.place(x=0,y=305)

    # Texto do total de salários por área
    lb5 = ctk.CTkLabel(total3_frame,
                       text="Salário Bruto por Funcionário",
                       font=("Roboto", 26, "bold"),
                       text_color="black"
                       )
    lb5.place(x=487, y=9)
