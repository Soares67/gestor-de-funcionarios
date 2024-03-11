from customtkinter import CTkImage
from PIL import Image
 

img = Image.open(r"icons\icons8-menu-250.png")
SIDEBAR_ICON = CTkImage(light_image=img, size=(32, 31))

img1 = Image.open(r'icons\icons8-settings-144.png')
SETTINGS_ICON = CTkImage(light_image=img1, size=(32, 31))

img2 =  Image.open(r'icons\icons8-close-250.png')
CLOSE_ICON = CTkImage(light_image=img2, size=(32, 31))

img3 = Image.open(r'icons\icons8-admin-90.png')
ADMIN_ICON = CTkImage(light_image=img3, size=(32, 31))

img4 = Image.open(r'icons\icons8-eye-90.png')
EYE_ICON = CTkImage(light_image=img4, size=(15, 15))

img5 = Image.open(r'icons\icons8-closed-eye-50.png')
CLOSED_EYE_ICON = CTkImage(light_image=img5, size=(15, 15))

img6 = Image.open(r'icons\icons8-payroll-64.png')
FOLHA_PAGAMENTO_ICON = CTkImage(light_image=img6, size=(32, 31))

img7 = Image.open(r'icons\icons8-calendar-96.png')
FERIAS_ICON = CTkImage(light_image=img7, size=(33, 32))

img8 = Image.open(r'icons\icons8-register-100.png')
CADASTRO_ICON = CTkImage(light_image=img8, size=(32, 31))

img9 = Image.open(r'icons\icons8-report-64.png')
RELATORIO_ICON = CTkImage(light_image=img9, size=(32, 31))

img10 = Image.open(r'icons\icons8-time-is-money-64.png')
HORA_EXTRA_ICON = CTkImage(light_image=img10, size=(32, 31))

img11 = Image.open(r'icons\icons8-graphic-64.png')
PROMOVER_ICON = CTkImage(light_image=img11, size=(32, 31))
