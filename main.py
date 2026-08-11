@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Salom! Botga xush kelibsiz 👋")
