# -*- coding: utf-8 -*-
"""Imagenes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1W2YmTZ0epiJHzD7NUp63EbhqY0iQLjA-
"""

from PIL import Image

img = Image.open(requests.get('https://user-images.githubusercontent.com/84803283/119641631-c6905000-be11-11eb-821a-5e6483d54217.png', stream=True).raw)

pix_val = list(img.getdata())
print(pix_val)

from PIL import Image, ImageFilter
from numpy import asarray
import requests

#Abre la imagen
im = Image.open(requests.get('https://user-images.githubusercontent.com/84803283/120003052-4878a880-bfcd-11eb-8128-34597967ff38.png', stream=True).raw)
pix_val = list(im.getdata()) #Guarda los píxeles en una lista
#print(pix_val)

#Difumina la imagen
im2 = im.filter(ImageFilter.BoxBlur(1))
pix_val2 = list(im2.getdata()) #Guarda una lista con los píxeles difuminados
#print(pix_val2)

#Formato límite de los píxeles
tpx_r = (240,0,0)
tpx_g = (0,240,0)
tpx_b = (0,0,240)
tpx_w = (255,255,255)

#Contador de los píxeles de cada color
px_r = 0
px_g = 0
px_b = 0

#Lista que guarda las posiciones de cada píxel distinto
red = []
green = []
blue = []

#Compara el código de RGB para diferenciarlos
def cmp(a,b):
    return (a > b) - (a < b)

'''Separa de la lista de píxeles normales cada uno de los píxeles según si son
rojos, verdes o azules y los separa de los píxeles blancos. De esta forma, solo
se almacenan en las listas de arriba la posición de cada color'''
for i in range(len(pix_val)):

    if cmp(tpx_r, pix_val[i]) < 1 and cmp(tpx_w,pix_val[i]) != 0:
        px_r = px_r + 1
        red.append(i)

    elif cmp(tpx_g, pix_val[i]) < 1 and cmp(tpx_w,pix_val[i]) != 0:
        px_g = px_g + 1
        green.append(i)

    elif cmp(tpx_b, pix_val[i]) < 1 and cmp(tpx_w,pix_val[i]) != 0:
        px_b = px_b + 1
        blue.append(i)

#Como difumina con radio 1, coge los 8 pixeles de alrededor para difuminar
cte = 1/9

#Guarda todos los valores modificados de cada valor
red2 = []
green2 = []
blue2 = []

#Contador que guarda la cantidad de veces que llega un color
contador_rojo = 0
contador_verde = 0
contador_azul = 0


'''Va por la lista de píxeles modificados y se van separando según su color
definido por las listas de antes y se hacen los cálculos para calcular los vecinos
que tiene cada píxel'''
for i in range(len(pix_val2)):

    if i == red[contador_rojo] and contador_rojo < len(red) - 1:  #El -1 es para que se mantenga dentro del rango
        aux = list(pix_val2[i])
        aux[0] = aux[0] - cte
        red1 = aux
        auxr = []
        for j in range(len(red1)):
            auxr.append((9 * red1[j]) / 255)
        red2.append(auxr)
        contador_rojo = contador_rojo + 1

    elif i == green[contador_verde] and contador_verde < len(green) - 1:
        aux = list(pix_val2[i])
        aux[1] = aux[1] - cte
        green1 = aux
        auxg = []
        for j in range(len(green1)):
            auxg.append((9 * green1[j]) / 255)
        green2.append(auxg)
        contador_verde = contador_verde + 1

    elif i == blue[contador_azul] and contador_azul < len(blue) - 1:
        aux = list(pix_val2[i])
        aux[2] = aux[2] - cte
        blue1 = aux
        auxb = []
        for j in range(len(blue1)):
            auxb.append((9 * blue1[j]) / 255)
        blue2.append(auxb)
        contador_azul = contador_azul + 1


#Devuelven la media de todos los valores de los tres colores
Average_red = np.mean(red2, axis=0)
Average_green = np.mean(green2, axis=0)
Average_blue = np.mean(blue2, axis=0)

"""p_disperso:https://user-images.githubusercontent.com/84803283/120099740-1a15dd00-c135-11eb-81cf-ef75098461a4.png
p_solido: https://user-images.githubusercontent.com/84803283/120099754-2437db80-c135-11eb-91f5-aeb98aa45d68.png
p_tubular: https://user-images.githubusercontent.com/84803283/120099761-3154ca80-c135-11eb-9371-3193a001f796.png
p_trabecular: https://user-images.githubusercontent.com/84803283/120099769-3c0f5f80-c135-11eb-851d-2d9e77939c8e.png
p_noestructural: https://user-images.githubusercontent.com/84803283/120099777-45003100-c135-11eb-8db9-caa7c65000bf.png
"""