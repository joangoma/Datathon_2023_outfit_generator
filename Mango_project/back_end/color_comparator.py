import numpy as np


def color_relationship(color1:list[int], color2:list[int])->str:
    
    # Check for monochromatic relationship
    eucl_dist = sum((color1-color2)**2)
    if (eucl_dist < 10000):
        return "Monochromatic"
    # Check for complementary relationship

    return "Complementary"

def comparator(colors1, colors2):
    """Colors1 són els fixos i colors2 no són fixos dona 
    la relació de grup entre 
     """
    dic = dict()
    keys = ["Monochromatic", "Complementary" ]
    for k in keys:
        dic[k] = 0
    for color1 in colors1:
        for color2 in colors2:
            rel = color_relationship(color1, color2)
            dic[rel] += 1
    if(len(color1) > 1):
        dic[color_relationship(color1[0], color1[1])]
    if dic["No relationship"] != 0:
        return "No relationship"
    elif dic["Complementary"] != 0:
        return "Complementary"
    else:
        return "Monochromatic"
 


print(color_relationship(np.array([10,10,10]),np.array([10,12,11])))

