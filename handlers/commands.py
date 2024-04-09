from aiogram import Router
from aiogram.types import Message, InputMediaPhoto, FSInputFile
from aiogram.filters import Command, CommandObject, CommandStart

from filters.is_admin import IsAdmin

from parsers.wb_parser import wb_parser
from generators.tt_gen import tt_photo_gen
from generators.first_gen import first_photo_gen
from generators.video import video_gen


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
    """
    :param message:
    :param command: txt (for first photo), url, url, ...
    :return:
    """
    if isinstance(command.args, int):
        return await message.answer("tu kto takoi syka")

    args = command.args.split(" ")

    first_photo_gen(args[0])

    urls = args[1:]
    res_tg = tg_post(urls, text='💜 WILDBERRIES 💜\n')
    video_gen(len(urls), duration=2)

    await message.answer_media_group(media=res_tg[0])
    await message.answer(text=res_tg[2], parse_mode="MarkdownV2")
    await message.answer_media_group(media=res_tg[1])
    await message.answer_video(FSInputFile(f"C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\data\\tt_post\\movie.mp4"))


def tg_post(urls, text: str):
    """ Create txt and media group for post in tg group

    :param urls: list of links to photos
    :param text: name of shop
    :return: mediafiles for group, text for group,
    """

    src_back = FSInputFile(f"C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\data\\tt_post\\back_res.png")
    mediatt = [InputMediaPhoto(media=src_back)]
    mediatg = []
    txt = text
    count = 0
    for url in urls:
        arr = wb_parser(url, index=count)

        price = arr[0]
        txt += f"{count + 1}\. [Цена: {price}]({url})\n"

        src_tg = arr[1]
        mediatg.append(InputMediaPhoto(media=src_tg))

        tt_photo_gen(count, price)
        src_tt = FSInputFile(f"C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\data\\tt_post\\res{count}.png")
        mediatt.append(InputMediaPhoto(media=src_tt))

        count += 1

    return mediatg, mediatt, txt



