
#colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

def multiply_color(color, factor):
    r, g, b = color
    return int(r * factor), int(g * factor), int(b * factor)