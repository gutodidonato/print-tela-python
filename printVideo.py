import pyautogui 
import os
fotos = 0
pasta = input("Qual tipo de fotos deseja? ")
comprimento_imagem = 500
altura_imagem = 500
try:
    os.mkdir(pasta)
except:
    print("Diretório já existente!")

while (fotos <= 70):
    image = pyautogui.screenshot(region=(0,0, comprimento_imagem, altura_imagem))
    try:
        image.save(f"{pasta}/imagem{fotos}.png")
    except:
        print("Imagens já inicializadas nesta pasta! corrija o nome! ")
        break
    fotos+= 1
