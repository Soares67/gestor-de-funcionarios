from customtkinter import CTkImage
from PIL import Image

img = Image.open(r"icons\menu.png")
SIDEBAR_ICON = CTkImage(light_image=img, size=(32, 31))

img1 = Image.open(r'icons\icons8-settings-256.png')
SETTINGS_ICON = CTkImage(light_image=img1, size=(32, 31))