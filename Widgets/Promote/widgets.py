import customtkinter as ctk


def promote_widgets(master):
    
    # Framedo cabeçalho
    header_frame = ctk.CTkFrame(master,
                                width=1356,
                                height=52,
                                fg_color="green",
                                border_width=3,
                                border_color="black"
                                )
    header_frame.place(x=-3,y=-2)

    # Frame do buscador
    searcher_frame = ctk.CTkFrame(master,
                                  width=674,
                                  height=668,
                                  fg_color="blue",
                                  corner_radius=0
                                  )
    searcher_frame.place(x=0,y=50)

    # Frame das abas de ações
    tabs_frame = ctk.CTkFrame(master,
                                  width=674,
                                  height=669,
                                  fg_color="red",
                                  corner_radius=0
                                  )
    tabs_frame.place(x=674,y=50)