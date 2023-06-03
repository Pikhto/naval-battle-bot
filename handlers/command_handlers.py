from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from lexicon.lexicon_ru import SERVICE_REPORTS


router = Router()


@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/start` command
    """
    # Most event objects have aliases for API methods
    # that can be called in events' context
    # For example if you want to answer to incoming message
    # you can use `message.answer(...)` alias
    # and the target chat will be passed to
    # :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>")


@router.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    """
    This handler receive messages with `/help` command
    """
    await message.answer(f"<b>{SERVICE_REPORTS['in development']}</b>")


@router.message(Command("contacts"))
async def command_contacts_handler(message: Message) -> None:
    """
    This handler receive messages with `/contacts` command
    """
    await message.answer(f"<b>{SERVICE_REPORTS['in development']}</b>")
