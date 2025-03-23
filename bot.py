import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

bot = Bot("8019523204:AAGE2w0_H6sAjQ6ZVRd_6kq_3MXxleYLyhI")

dp = Dispatcher()

@dp.startup()
async def on_startup() -> None:
    await bot.delete_webhook(True)


@dp.message(Command("start"))
async def start(message: Message) -> None:
     await message.answer_invoice(        
         title="Доступ к функционалу",
         description="Оплатите 1 звезд и получите доступ к функционалу",
         payload="access_to_private",
         currency="XTR",
         prices=[LabeledPrice(label="XTR", amount=1)]  
     )


@dp.pre_checkout_query()
async def pre_check_query(event: PreCheckoutQuery) -> None:
    await event.answer(True)


@dp.message(F.successful_payment)
async def successful_payment(message: Message) -> None:
    await message.answer("Вы успешно оплатили✅")
    await bot.refund_star_payment(message.from_user.id, message.successful_payment.telegram_payment_charge_id)


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))