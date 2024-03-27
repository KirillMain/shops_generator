from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def tt_photo_gen(i: int):
    """ generate an image fo tt post

    :param i: indes of photo
    :return: image ready to post
    """
    back = Image.new(mode="RGB", size=(1080, 1920))

    fronteground = Image.open(f"C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\data\\parser\\item_photo{i}.png")
    img_width, img_height = fronteground.size
    fronteground = fronteground.crop(((img_width - 1000) // 2,
                         (img_height - 1000) // 2,
                         (img_width + 1000) // 2,
                         (img_height + 1000) // 2))
    back.paste(fronteground, (40, 480))

    # price = Image.open(f"C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\data\\parser\\history1.png")
    # price = price.resize([i*5 for i in price.size])
    # back.paste(price, (400, 1550))

    draw = ImageDraw.Draw(back)
    font = ImageFont.truetype("C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\pil_\\ofont.ru_Letov.ttf", 70)
    draw.text((540, 250), "Артикулы в тг:", (255, 255, 255), font, align='center', anchor="mm")
    draw.text((540, 350), "shmot_est", (255, 255, 255), font, align='center', anchor="mm")
    draw.text((540, 1600), "5 500 P", (255, 255, 255), font, align='left', anchor="mm")

    back.save(f"C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\data\\tt_post\\res{i}.png")

