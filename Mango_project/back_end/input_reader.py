import pandas as pd
import numpy as np
outfit_data = pd.read_csv("../dataset/outfit_data.csv")
product_data = pd.read_csv("../dataset/product_data.csv")


with open("./Query/outfit_data.txt","w") as filename:
    ids = outfit_data["cod_outfit"].unique()
    j = 0
    n = len(outfit_data["cod_outfit"])
    filename.write(str(n))
    filename.write("\n")
    for i in ids:
        filename.write(str(i))
        filename.write(" ")
        while(j<n and outfit_data["cod_outfit"][j] == i):
            filename.write(outfit_data["cod_modelo_color"][j])
            j+=1
            filename.write(" ")
        filename.write("\n")

with open("./Query/product_data.txt","w") as filename:
    keys = np.array(product_data.keys()).take([0,2,4,5,8,9])
    n = len(product_data["cod_modelo_color"])
    filename.write(str(n))
    filename.write("\n")
    for i in range(n):
        for k in keys:
            filename.write(product_data[k][i])
            filename.write("\n")

    