import time
import random
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetAllStickersRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID

trigger = "揼"
reply = ["邊位"]
group_id = [-1001210202420, -1001425821503]  # group id list
if __name__ == '__main__':
    # Create the client and connect
    # use sequential_updates=True to respond to messages one at a time
    client = TelegramClient(name, api_id, api_hash)

    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        if event.is_private:
            await event.reply(random.choice(reply))  # reply in private
        if event.is_group:  # reply in group
            # print(event,event.chat_id)
            if event.chat_id in group_id:
                # this lookup will be cached by telethon
                from_ = await event.client.get_entity(event.from_id)
                if from_.bot == False: #ignore bot msg
                    return
                print(from_.first_name, from_.last_name,
                      event.message.text, event.from_id)
                text = str(event.message.message)
                if text.find(trigger) != -1:
                    # if contain word then reply
                    await event.reply(random.choice(reply))
    print(time.asctime(), '-', 'Auto-replying...')
    client.start()
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')
