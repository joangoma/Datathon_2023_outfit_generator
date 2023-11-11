from PIL import Image
from rembg import new_session, remove
import pandas as pd
import numpy as np

def get_pixel_matrix(image):
    pixel_data = list(image.getdata())
    width, height = image.size
    pixel_matrix = [pixel_data[i * width:(i + 1) * width] for i in range(height)]
    return pixel_matrix
rix

def get_rgb(input_path):
    n = len(input_path)
    no_back_path = input_path[:n-4] + "_nback.png"
    img = None
    try:  
        img = Image.open(no_back_path)
    except FileNotFoundError:
        in_file = Image.open(input_path)
        output = remove(in_file)
        output.save(no_back_path)
        img = output
    
    pixel_matrix = get_pixel_matrix(img)
    width,height = img.size
    suma = np.array([0,0,0,0], dtype=float)
    print(pixel_matrix[0][0])
    cnt = 0
    for i in range(height):
        for j in range(width):
            col = np.array(pixel_matrix[i][j])
            if np.all(abs(col) != np.array([0,0,0,0])):
                suma = suma + col
                cnt += 1
    print(suma/cnt)
    return suma/cnt

get_rgb("../dataset/images/2019_41075777_09.jpg")