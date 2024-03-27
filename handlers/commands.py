from aiogram import Router
from aiogram.types import Message, InputMediaPhoto, FSInputFile
from aiogram.filters import Command, CommandObject, CommandStart

from filters.filter import IsAdmin

from parsers.wb_parser import parse
from pil_.tt_gen import tt_photo_gen


router = Router()
router.message.filter(
    IsAdmin()
)


@router.message(CommandStart())
async def start(message: Message):
    await message.answer('А в Африке реки вот такой ширины,\n'
                         'А в Африке горы вот такой вышины!')


@router.message(Command('get'))
async def get_wb(message: Message, command: CommandObject):
    if isinstance(command.args, int):
        return await message.answer("tu kto takoi syka")

    urls = command.args.split(" ")
    print(urls)

    mediatg_txt_mediatt = generate_tg_post(urls)

    await message.answer_media_group(media=mediatg_txt_mediatt[0])
    await message.answer(text=mediatg_txt_mediatt[1], parse_mode="MarkdownV2")
    await message.answer_media_group(media=mediatg_txt_mediatt[2])


def generate_tg_post(urls):
    """ Create txt and media group for post in tg group

    :param urls: list of links to photos
    :return: text for group, mediafiles for group
    """

    mediatg = []
    mediatt = []
    txt = '💜 WILDBERRIES 💜\n'
    count = 0
    for url in urls:
        arr = parse(url, index=count)

        price = arr[0]
        txt += f"{count + 1}\. [Цена: {price}]({url})\n"

        src_tg = arr[1]
        mediatg.append(InputMediaPhoto(media=src_tg))

        tt_photo_gen(count)
        src_tt = FSInputFile(f"C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\data\\tt_post\\res{count}.png")
        mediatt.append(InputMediaPhoto(media=src_tt))

        count += 1

    return mediatg, txt, mediatt



