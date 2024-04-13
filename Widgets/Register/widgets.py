import customtkinter as ctk
from Icons.iconspath import EMPLOYEES_IMG

employees = [
    "John Smith", "Emily Brown", "Benjamin Johnson", "Isabella Garcia", "William Davis",
    "Sophia Rodriguez", "Michael Williams", "Olivia Miller", "James Jones", "Jane Martinez",
    "Benjamin Johnson", "Olivia Davis", "Michael Williams", "Emily Garcia", "William Miller",
    "Isabella Brown", "Sophia Smith", "Benjamin Martinez", "John Jones", "Emily Garcia",
    "Olivia Johnson", "James Miller", "Michael Smith", "Benjamin Davis", "Emily Martinez",
    "John Rodriguez", "James Williams", "Olivia Smith", "William Johnson", "Isabella Jones",
    "John Brown", "Benjamin Garcia", "Olivia Martinez", "James Rodriguez", "Sophia Davis",
    "Emily Miller", "Isabella Johnson", "John Smith", "Michael Martinez", "Sophia Johnson",
    "William Davis", "Benjamin Rodriguez", "Olivia Brown", "James Williams", "John Jones",
    "Isabella Garcia", "Michael Martinez", "Sophia Johnson", "Emily Davis", "William Rodriguez",
    "Olivia Smith", "Benjamin Miller", "James Brown", "Isabella Jones", "John Martinez",
    "Michael Williams", "Sophia Garcia", "William Smith", "Emily Brown", "Benjamin Davis",
    "Olivia Rodriguez", "James Johnson", "John Miller", "Isabella Smith", "Michael Garcia",
    "Sophia Martinez", "William Brown", "Emily Jones", "Benjamin Williams", "Olivia Davis",
    "James Johnson", "John Rodriguez", "Isabella Miller", "Michael Smith", "Sophia Martinez",
    "William Jones", "Emily Brown", "Benjamin Garcia", "Olivia Williams", "James Davis",
    "John Johnson", "Isabella Smith", "Michael Brown", "Sophia Miller", "William Martinez",
    "Emily Garcia", "Benjamin Johnson", "Olivia Rodriguez", "James Jones", "John Williams",
    "Isabella Davis", "Michael Johnson", "Sophia Smith", "William Brown", "Emily Miller",
    "Benjamin Martinez", "Olivia Garcia", "James Rodriguez", "John Jones", "Isabella Williams"
]

def onclick(var):
    if var == "A-Z":
        print("Alfabética")
    elif var == "Z-A":
        print("Reverso")
    print(var)


def register_widgets(master):

    # Control Var
    actual_filter = None

    def list_employees(list, frame):
        for i in list:
            name = ctk.CTkLabel(frame, font=("Arial", 16, "bold"), text_color="black", text=i)
            name.pack()

    
    # Frame da imagem
    img_frame = ctk.CTkFrame(master,
                             fg_color="#FFE8C6",
                             width=400,
                             height=300,
                             
                             )
    img_frame.place(x=0,y=0)

    # Imagem
    image_lb = ctk.CTkLabel(img_frame,
                            text="",
                            image=EMPLOYEES_IMG
                            )
    image_lb.place(x=15,y=20)

    # Frame da lista de funcionários
    list_frame = ctk.CTkFrame(master,
                              fg_color="#CBC2FF",
                              width=400,
                              height=418
                              )
    list_frame.place(x=0,y=300)

    # Frame do cabeçalho da lista de funcionários
    list_header_frame = ctk.CTkFrame(list_frame,
                                     fg_color="#FFFBA2",
                                     width=400,
                                     height=50
                                    )
    list_header_frame.place(x=0,y=0)

    # Cabeçalho da lista de funcionários
    list_header = ctk.CTkLabel(list_header_frame,
                               text="Funcionários",
                               font=("Arial", 26, "bold"),
                               text_color="black"
                               )
    list_header.place(x=15,y=12)

    # Filtro de ordem dos funcionários
    search_filter = ctk.CTkComboBox(list_header_frame,
                                    width=120,
                                    height=48,
                                    values=["A-Z", "Z-A"],
                                    font=("Arial", 13, "bold"),
                                    dropdown_font=("Arial", 13, "bold"),
                                    corner_radius=20,
                                    variable=actual_filter,
                                    command=lambda actual_filter: onclick(actual_filter)
                                    )
    search_filter.set("Filtrar")
    search_filter.place(x=280,y=1)

    # Lista de funcionários
    emp_list = ctk.CTkScrollableFrame(list_frame,
                                      width=400,
                                      height=418,
                                      fg_color="white"
                                      )
    emp_list.place(x=0,y=50)

    # Frame principal
    main_frame = ctk.CTkFrame(master,
                              fg_color="#CAFFC6",
                              width=948,
                              height=718
                              )
    main_frame.place(x=400,y=0)

    # Título do frame principal
    title = ctk.CTkLabel(main_frame,
                         text="Registrar Funcionário",
                         font=("Arial", 30, "bold"),
                         text_color="black"
                         )
    title.place(x=331,y=29)
    
    # Entry do nome
    name_entry = ctk.CTkEntry(main_frame,
                              width=365,
                              height=56,
                              placeholder_text="Nome completo",
                              font=("Arial", 16, "bold"),
                              corner_radius=20,
                              )
    name_entry.place(x=55, y=117)

    # Entry da data de nascimento
    bdt_entry = ctk.CTkEntry(main_frame,
                              width=365,
                              height=56,
                              placeholder_text="Data de nascimento",
                              font=("Arial", 16, "bold"),
                              corner_radius=20,
                              )
    bdt_entry.place(x=55,y=230)

    # Opções de gênero
    gen_options = ctk.CTkComboBox(main_frame,
                                  width=365,
                                  height=56,
                                  values=["Masculino", "Feminino", "Outros"],
                                  font=("Arial", 16, "bold"),
                                  dropdown_font=("Arial", 16, "bold"),
                                  corner_radius=20
                                  )
    gen_options.set("Gênero")
    gen_options.place(x=55,y=343)

    # Entry do email
    email_entry = ctk.CTkEntry(main_frame,
                              width=365,
                              height=56,
                              placeholder_text="E-mail",
                              font=("Arial", 16, "bold"),
                              corner_radius=20,
                              )
    email_entry.place(x=55, y=456)

    # Entry da área
    area_entry = ctk.CTkEntry(main_frame,
                              width=365,
                              height=56,
                              placeholder_text="Área",
                              font=("Arial", 16, "bold"),
                              corner_radius=20,
                              )
    area_entry.place(x=524, y=174)

    # Entry do cargo
    pos_entry = ctk.CTkEntry(main_frame,
                              width=365,
                              height=56,
                              placeholder_text="Cargo",
                              font=("Arial", 16, "bold"),
                              corner_radius=20,
                              )
    pos_entry.place(x=524, y=287)

    # Entry do salário
    wag_entry = ctk.CTkEntry(main_frame,
                              width=365,
                              height=56,
                              placeholder_text="Salário",
                              font=("Arial", 16, "bold"),
                              corner_radius=20,
                              )
    wag_entry.place(x=524, y=400)

    # botão de cadastrar
    reg_btn = ctk.CTkButton(main_frame,
                            width=170,
                            height=56,
                            text="Cadastrar",
                            font=("Arial", 20, "bold"),
                            corner_radius=20
                            )
    reg_btn.place(x=387,y=610)

    list_employees(employees, emp_list)

