from bisect import bisect
from datetime import datetime as dt
from PIL import Image
import os

# Zodiacal signs
signs = [(1, 20, "Cap"), (2, 18, "Aqu"), (3 , 20, "Pis"), (4, 20, "Ari"),
         (5, 21, "Tau"), (6, 21, "Gem"), (7, 22, "Can"), (8, 23, "Leo"),
         (9, 23, "Vir"), (10, 23, "Lib"), (11, 22, "Sco"), (12, 22, "Sag"),
         (12, 31, "Cap")]


# Gets zodiac sign from month & day of birth
def zodiac_sign(m, d):
    return signs[bisect(signs, (m, d))][2]


# Checks out if image is big enough (800x800)
def image_size_ok(foto):
    img = Image.open(foto)
    size = img.size
    if size[0] >= 800 and size[1] >= 800:
        return True
    else:
        return False


# Get Birthday from user. Validation is made
while True:
    geburtstag = input("Geburtstag Tag.Monat: ")
    try:
        birth = dt.strptime(geburtstag, "%d.%m").date()
    except ValueError:
        print("Datum ungültig")
        continue
    if zodiac_sign(birth.month, birth.day):
        break

sign = zodiac_sign(birth.month, birth.day)


# Get Filename of original picture, validation made
while True:
    foto = input("Foto: ")
    if os.path.isfile(foto):
        if image_size_ok(foto):
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
# Transparent image setting here
img2.putalpha(80)
img1_size = img1.size
img2_size = img2.size

# Pasting image here on upper right corner
img1.paste(img2, (img1_size[0]-img2_size[0], 0), img2)
# Saving result image on Hard Drive
img1.save("output.png")
# Show result image
img1.show()
