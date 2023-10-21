from PIL import Image

def vassiviere():
    s: int = 0
    x: float
    y: float

    image = Image.open("vassiviere.png")
    (largeur, longueur) = image.size

    for x in range(largeur) :
        for y in range(longueur) :

            px = image.getpixel((x, y))

            bleu = (156, 192, 249)

            if px == bleu :
                s = s + 1
                image.putpixel((x,y), (255, 0, 0))

    image.show()
    return s / (123**2)


print(vassiviere())