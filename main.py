import customtkinter as ctk


root = ctk.CTk()
root.geometry("1000x600")
root.title("Gerenciamento")


bar_i = ctk.CTkFrame(master=root,
                     bg_color="red",
                     fg_color="red",
                     width=100,
                     height=1000
                     )
bar_i.place(x=0,y=0)











root.mainloop()