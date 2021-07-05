import time
import random
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetAllStickersRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID

first_day = "第 1 日"
no_body = '冇人死'
trigger = "揼"
msg = "希望你既離去有價值"
reply = ["邊位"]

if __name__ == '__main__':

    # Create the client and connect
    # use sequential_updates=True to respond to messages one at a time
    client = TelegramClient(name, api_id, api_hash)

    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
     
      if event.is_private: #reply in private
          if event.message.media.document.id == 2781732661285100615:
            await event.respond("斷你") 
      if event.is_group: #reply in group
        #print(event,event.chat_id)
        if event.chat_id == -1001210202420 or event.chat_id == -1001425821503:  #reply in group_id
         from_ = await event.client.get_entity(event.from_id)  # this lookup will be cached by telethon
         print(from_.first_name,from_.last_name,event.message.text,event.from_id)
         text = str(event.message.message)
         if text.find(trigger) != -1:
            await event.respond(random.choice(reply)) #if contain word then reply
         if event.from_id == 618096097 or event.from_id == 1029642148:
          if text.find(first_day) != -1:
           if text.find(no_body) == -1:
            time.sleep(1)
            await event.reply(msg)
         if event.message.media.document.id == 2781732661285100615:
            await event.respond("斷你")
            #return  
    print(time.asctime(), '-', 'Auto-replying...')
    client.start()
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')
