from bisect import bisect
from datetime import datetime as dt
from PIL import Image
import os

signs = [(1,20,"Cap"), (2,18,"Aqu"), (3,20,"Pis"), (4,20,"Ari"),
         (5,21,"Tau"), (6,21,"Gem"), (7,22,"Can"), (8,23,"Leo"),
         (9,23,"Vir"), (10,23,"Lib"), (11,22,"Sco"), (12,22,"Sag"),
         (12,31,"Cap")]


def zodiac_sign(m,d):
    return signs[bisect(signs,(m,d))][2]

def image_size_ok(foto):
    img1 = Image.open(foto)
    size = img1.size
    if size[0] >= 800 and size[1] >= 800:
        return True
    else:
        return False

while True:
    geburtstag = input("Geburtstag Tag.Monat: ")
    try:
        birth = dt.strptime(geburtstag, "%d.%m").date()
    except ValueError:
        continue
    if zodiac_sign(birth.month, birth.day):
        break

sign = zodiac_sign(birth.month, birth.day)

while True:
    foto = input("Foto: ")
    if os.path.isfile(foto):
        if (image_size_ok(foto)):
            break
        else:
            print("Datei zu klein")
    else:
        print("Datei ist nicht zu finden")

sign_image_path = "sign_images/"+sign+".jpg"

img = Image.open(sign_image_path)
img = img.convert("RGBA")

img1 = Image.open(foto)
img2 = Image.open(sign_image_path)
img2 = img2.convert('L')
img2.putalpha(230)
img1_size = img1.size
img2_size = img2.size

# No transparency mask specified,
# simulating an raster overlay
img1.paste(img2, (img1_size[0]-img2_size[0], 0), img2)
img1.save("output.png")
img1.show()
