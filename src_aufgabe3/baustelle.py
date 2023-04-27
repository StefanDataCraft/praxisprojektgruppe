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

"""
while True:
    geburtstag = input("Geburtstag Tag.Monat: ")
    try:
        birth = dt.strptime(geburtstag, "%d.%m").date()
    except ValueError:
        continue
    if zodiac_sign(birth.month, birth.day):
        break
"""
#sign = zodiac_sign(birth.month, birth.day)
sign = zodiac_sign(5, 19)

"""while True:
    foto = input("Foto: ")
    if os.path.isfile(foto):
        break
"""
foto = "b.jpg"
sign_image_path = "sign_images/"+sign+".jpg"

"""
#Read the two images
image1 = Image.open(foto)
image1.show()
image2 = Image.open(sign_image_path)
image2.show()
#resize, first image
image1 = image1.resize((426, 240))
image1_size = image1.size
image2_size = image2.size
new_image = Image.new('RGB', (2*image1_size[0], image1_size[1]), (250, 250, 250))
new_image.paste(image1, (0, 0))
new_image.paste(image2, (image1_size[0], 0))
new_image.save("merged_image.jpg", "JPEG")
new_image.show()
"""
img1 = Image.open(foto)
img2 = Image.open(sign_image_path)

img1_size = img1.size
img2_size = img2.size

print ("0 img1: "+str(img1_size[0]))
print ("1 img1: "+str(img1_size[1]))
print ("0 img2: "+str(img2_size[0]))
print ("1 img2: "+str(img2_size[1]))

# No transparency mask specified,
# simulating an raster overlay
img1.paste(img2, (img1_size[0]-img2_size[0], 0))

img1.show()