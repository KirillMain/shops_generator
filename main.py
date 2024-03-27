import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from handlers import commands
# from handlers.admin import a_commands, a_faq, a_appeal
# from data import database as db

from config_reader import config


async def main():
    bot = Bot(config.bot_token.get_secret_value(), default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()

    dp.include_routers(  # 1 в импорте - последний в инклуде этом, иначе он не считает хз поч
        commands.router
    )

    await bot.delete_webhook(drop_pending_updates=True)  # проупскает накопленные входящие
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())