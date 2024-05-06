import customtkinter as ctk

def overtime_widgets(master):

    # Frame das estatísticas
    stats_frame = ctk.CTkFrame(master,
                               width=482,
                               height=718,
                               fg_color="#FB9C8D",
                               corner_radius=0
    )
    stats_frame.place(x=0,y=0)

    # Label do título total
    title_total_lb = ctk.CTkLabel(stats_frame,
                            text="Total de horas extras",
                            font=("Roboto", 26, "bold"),
                            text_color="black"
                            )
    title_total_lb.place(x=96,y=37)

    # Label do total
    total_lb = ctk.CTkLabel(stats_frame,
                            width=200,
                            height=57,
                            text="112",
                            font=("Roboto", 28, "bold"),
                            text_color="black",
                            fg_color="white",
                            corner_radius=20
                            )
    total_lb.place(x=130,y=74)

    # Label do título da média
    title_avg_lb = ctk.CTkLabel(stats_frame,
                            text="Média por funcionário",
                            font=("Roboto", 26, "bold"),
                            text_color="black"
                            )
    title_avg_lb.place(x=95,y=200)

    # Label da média
    avg_lb = ctk.CTkLabel(stats_frame,
                            width=200,
                            height=57,
                            text="7",
                            font=("Roboto", 28, "bold"),
                            text_color="black",
                            fg_color="white",
                            corner_radius=20
                            )
    avg_lb.place(x=130,y=237)

    # Label do título do grafico
    title_chart_lb = ctk.CTkLabel(stats_frame,
                            text="Horas extras por área",
                            font=("Roboto", 26, "bold"),
                            text_color="black"
                            )
    title_chart_lb.place(x=95,y=363)

    # Gráfico

    # Frame do formulário
    form_frame = ctk.CTkFrame(master,
                              width=870,
                              height=718,
                              fg_color="white",
                              corner_radius=0
    )
    form_frame.place(x=482,y=0)

    # Label do cabeçalho

    # Entry do ID

    # Entry da data

    # Entry da quantidade

    # Dropdown do motivo

    # Botão de salvar