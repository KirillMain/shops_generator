from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def tt_photo_gen(i: int, price: int):
    """ generate an image fo tt post

    :param i: indes of photo
    :param price:
    :return: image ready to post
    """
    img = Image.new(mode="RGB", size=(1080, 1920))

    # photo of product
    fronteground = Image.open(f"C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\data\\parser\\item_photo{i}.png")
    img_width, img_height = fronteground.size
    fronteground = fronteground.crop(((img_width - 1000) // 2,
                         (img_height - 1000) // 2,
                         (img_width + 1000) // 2,
                         (img_height + 1000) // 2))
    img.paste(fronteground, (40, 480))

    # price history
    # price = Image.open(f"C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\data\\parser\\history1.png")
    # price = price.resize([i*5 for i in price.size])
    # back.paste(price, (400, 1550))

    # adding text on img
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\generators\\Lora-Regular.ttf", 70)
    # main info
    draw.text((540, 250), "Артикулы в тг:", (255, 255, 255), font, align='center', anchor="mm")
    draw.text((540, 350), "shmot_est", (255, 255, 255), font, align='center', anchor="mm")
    # price
    draw.text((540, 1600), f'{price}', (255, 255, 255), font, align='center', anchor="mm")

    img.save(f"C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\data\\tt_post\\res{i}.png")

