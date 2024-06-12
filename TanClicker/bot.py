import asyncio

from aiogram import Router, Bot, Dispatcher
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder

def webapp_bilder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
          text="let`s Click", wed_app=WebAppInfo(
                url="https://demon341.github.io/Click/"
          )
    )
    return builder.as_markup()

router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
        await message.reply(
              "Hello",
              reply_markup=webapp_bilder()             
                            )


async def main():
      bot = Bot("7428983062:AAEUEMgmzKn15M2aYLOaS7a6MadKg2UzKqQ", parse_mode=ParseMode.HTML)

      dp =Dispatcher()
      dp.include_router(router)


      await bot.delete_webhook(True)
      await dp.start_polling(bot)








if __name__ == "__main__":
    asyncio.run(main())
