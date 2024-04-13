import customtkinter as ctk
from tkcalendar import DateEntry
from Icons.iconspath import EMPLOYEES_IMG

def register_widgets(master):
    
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
    
    name_entry = ctk.CTkEntry(main_frame,
                              width=365,
                              height=56,
                              placeholder_text="Nome completo",
                              font=("Arial", 16),
                              corner_radius=20,
                              )
    name_entry.place(x=55, y=117)

    bdt_entry = DateEntry(main_frame,
                          width=16,
                          year=2024,
                          month=4,
                          day=13
                          )
    bdt_entry.place(x=55,y=230)

    # gen_options

    # email_entry

    # area_entry

    # pos_entry

    # wag_entry

    # reg_btn


