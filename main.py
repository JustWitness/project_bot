import asyncio
import logging
import aiogram
import aiohttp
from aiogram import Dispatcher, types
from pymongo import MongoClient

token = "6723888423:AAFpNWiK2HUYeFP1jMfo5zljxHUL5XPbwXk"
bot = aiogram.Bot(token=token)
password = "721DDunIUFyeHmPv"
connection = f"mongodb+srv://Admin:{password}@cluster0.ob0lvop.mongodb.net/"
client = MongoClient(connection)
db = client["test_database"]
collection = db["test_collection"]

dp = Dispatcher()


@dp.channel_post()
async def handle_channel_post(message: types.Message):
    post = {'companyName': "", 'image': 0, 'description': "", 'creationDate': ""}
    chat = await bot.get_chat(message.chat.id)
    post['companyName'] = chat.title
    if message.photo:
        response = await bot.get_file(message.photo[-1].file_id)
        photo_url = f'https://api.telegram.org/file/bot{token}/{response.file_path}'
        async with aiohttp.ClientSession() as session:
            async with session.get(photo_url) as response:
                image_data = await response.read()
        post['image'] = image_data
        if not message.caption == "":
            post['description'] = message.caption
        else:
            print(f"Message {message.id} from chat '{chat.title}' has just photo.")
    else:
        post['description'] = message.text
    post['creationDate'] = message.date
    collection.insert_one(post)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
