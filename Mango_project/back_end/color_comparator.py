def rgb_to_hsv(rgb:list[int])->list[int]:
    r, g, b = [x / 255.0 for x in rgb]
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df / mx) * 100
    v = mx * 100
    return h, s, v

def color_relationship(color1:list[int], color2:list[int])->str:
    h1, s1, v1 = rgb_to_hsv(color1)
    h2, s2, v2 = rgb_to_hsv(color2)

    # Check for monochromatic relationship
    if abs(h1 - h2) < 30 and abs(s1 - s2) < 10:
        return "Monochromatic"

    # Check for analogous relationship
    if abs(h1 - h2) < 30 and abs(s1 - s2) < 25:
        return "Analogous"

    # Check for complementary relationship
    if abs(h1 - h2) > 160:
        return "Complementary"

    return "No relationship"

def comparator(colors1, colors2):
    dic = dict()
    dic["Monochromatic"] = 0
    dic["Analogous"] = 0
    dic["Complementary"] = 0
    dic["No relationship"] = 0

    for color1:colors1:
        for color2:colors2:
            dic[color_relationship(color1, color2)] += 1


