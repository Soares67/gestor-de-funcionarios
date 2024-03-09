from customtkinter import CTkImage
from PIL import Image, ImageOps



img = Image.open(r"icons\menu.png")
SIDEBAR_ICON = CTkImage(light_image=img, size=(32, 31))

img1 = Image.open(r'icons\icons8-settings-256.png')
SETTINGS_ICON = CTkImage(light_image=img1, size=(32, 31))

img2 =  Image.open(r'icons\icons8-close-250.png')
CLOSE_ICON = CTkImage(light_image=img2, size=(32, 31))

img3 = Image.open(r'icons\icons8-admin-90.png')
ADMIN_ICON = CTkImage(light_image=img3, size=(32, 31))

img4 = Image.open(r'icons\icons8-eye-90.png')
EYE_ICON = CTkImage(light_image=img4, size=(15, 15))

img5 = Image.open(r'icons\icons8-closed-eye-50.png')
CLOSED_EYE_ICON = CTkImage(light_image=img5, size=(15, 15))