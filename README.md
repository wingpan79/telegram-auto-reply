
# telegram-auto-reply

A simple telegram bot using Python script(telethon) when trigger specific word will auto replying telegram message.Able to reply in specific group or private chat

## How to use

Get Telegram API Key
got to https://my.telegram.org and go to API development tools

copy your name,api_id,api_hash from App configuration and replace it in auto-reply.py:

```python
client = TelegramClient(name, api_id, api_hash)
```
Install Python
https://www.python.org/downloads/

Install telethon
https://docs.telethon.dev/en/latest/basic/installation.html

## Usage

when someone send the trigger message will auto-reply. change to what you like
```python
trigger = "揼"
```

Auto-reply message. change to what you like

```python
reply = ["邊位"]
```

