from PIL import Image
from random import random

inputImgPath = 'IMG_8700.jpg'
outputImgPath = 'out.jpg'

def filter_image(path, shifts=list()):
    if len(shifts) == 0:
        shifts = [random() for _ in range(9)] #to insert random values in shifts list
    
    im = Image.open(path) #get the image object
    photo = list(im.getdata()) #get the pixels of the image in a list
    filtered = list() #empty list

    for pixel in photo:
        # print(pixel)
        r, g, b = pixel #giving the value of pixel in r, g, b
        new_r = ((r*shifts[0]) + (g*shifts[1]) + (b*shifts[2]))
        new_g = ((r*shifts[3]) + (g*shifts[4]) + (b*shifts[5]))
        new_b = ((r*shifts[6]) + (g*shifts[7]) + (b*shifts[8]))
        filtered.append((int(new_r), int(new_g), int(new_b)))
    
    im.putdata(filtered)
    im.save(outputImgPath)
    print(shifts)

filter_image(inputImgPath)