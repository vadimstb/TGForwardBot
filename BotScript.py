from telethon import TelegramClient, events

api_id = 22531523            # твой api_id
api_hash = "f4b55c3207ed993ad7063e276771f75e"     # твой api_hash

client = TelegramClient("forward_bot", api_id, api_hash)

SOURCE_CHANNEL = -1002743493594   # заменяй на свой канал
TARGET_CHANNEL = -1001944497734   # заменяй на свой канал

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    try:
        await client.forward_messages(TARGET_CHANNEL, event.message)
        print(f"✅ Переслано сообщение {event.message.id}")
    except Exception as e:
        print(f"⚠️ Ошибка: {e}")


print("🚀 Бот запущен...")
client.start()
client.run_until_disconnected()
