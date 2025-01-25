import colorgram

color_pal = []
colors = colorgram.extract('images.jpeg', 20)
for color in colors:
    rgb = color.rgb
    red = rgb.r
    green = rgb.g
    blue = rgb.b
    new_color = (red,green,blue)
    color_pal.append(new_color)


print(color_pal)

color_pal = [(199, 162, 100), (62, 91, 128), (140, 170, 192), (139, 90, 48), (219, 206, 119), (135, 27, 52), (32, 41, 67), (78, 16, 36), (149, 59, 85), (167, 154, 49), (187, 143, 162), (134, 183, 147), (46, 55, 100), (181, 95, 107), (56, 39, 27), (96, 118, 167)]


