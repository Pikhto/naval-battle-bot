import asyncio

from aiogram import Bot, Dispatcher, Router
from handlers import command_handlers, user_handlers
from config_data.config import load_config
from keyboards.set_menu import set_main_menu

# Bot token can be obtained via https://t.me/BotFather
config = load_config()
TOKEN = config.tg_bot.token

# All handlers should be attached to the Router (or Dispatcher)
router = Router()


async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)
    dp.include_router(command_handlers.router)
    dp.include_router(user_handlers.router)

    # Initialize Bot instance with a default parse mode which will be passed
    # to all API calls
    bot = Bot(TOKEN, parse_mode="HTML")
    # setting up the Menu button
    await set_main_menu(bot)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
