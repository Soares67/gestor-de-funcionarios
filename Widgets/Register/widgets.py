import customtkinter as ctk

def register_widgets(master):
    
    img_frame = ctk.CTkFrame(master,
                             fg_color="#FFE8C6",
                             width=400,
                             height=300
                             )
    img_frame.place(x=0,y=0)

    list_frame = ctk.CTkFrame(master,
                              fg_color="#CBC2FF",
                              width=400,
                              height=418
                              )
    list_frame.place(x=0,y=300)

    main_frame = ctk.CTkFrame(master,
                              fg_color="#CAFFC6",
                              width=948,
                              height=718
                              )
    main_frame.place(x=400,y=0)

    list_header_frame = ctk.CTkFrame(list_frame,
                                     fg_color="#FFFBA2",
                                     width=400,
                                     height=50
                                    )
    list_header_frame.place(x=0,y=0)