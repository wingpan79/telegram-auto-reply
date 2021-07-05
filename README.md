
# telegram-auto-reply

A simple telegram bot using Python script(telethon) when trigger specific word will auto replying telegram message.Able to reply in specific group or private chat

## How to use

Install Python
https://www.python.org/downloads/

Install telethon
https://docs.telethon.dev/en/latest/basic/installation.html

Get Telegram API Key
got to https://my.telegram.org and go to API development tools

copy your name,api_id,api_hash from App configuration and replace it in auto-reply.py:

```python
client = TelegramClient(name, api_id, api_hash)
```

When someone send the trigger message will auto-reply.
```python
trigger = "揼"
```

Auto-reply message.
```python
reply = ["邊位"]
```

Specific group list.
```python
group_id = [-1001210202420, -1001425821503] #group id list
```
get the group id.

```python
print(event,event.chat_id)
```

Run auto-reply.py

inspired by https://gist.github.com/yi-jiayu/acc31fbad5a25f746430428ce4d62c28

