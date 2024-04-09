import random

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def first_photo_gen(txt: str):
    text = txt.replace('\p', ' ').replace('\\n', '\n')
    i = random.randint(1, 6)
    back = Image.open(f"C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\data\\backs\\back{i}.jpg")
    img = back.resize((1080, 1920))

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\generators\\Lora-Regular.ttf", 150)
    draw.text((540, 600), text, (255, 255, 255), font, align='center', anchor="mm")

    img.save(f"C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\data\\tt_post\\back_res.png")
