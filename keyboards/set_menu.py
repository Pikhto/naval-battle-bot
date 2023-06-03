from aiogram import Bot
from aiogram.types.bot_command import BotCommand
from lexicon.lexicon_ru import COMMANDS_RU


async def set_main_menu(bot: Bot):
    """
    Function to customize the bot menu
    """
    main_menu_commands = (
        BotCommand(command=command,
                   description=description)
        for command, description in COMMANDS_RU.items()
        )

    await bot.set_my_commands(main_menu_commands)
