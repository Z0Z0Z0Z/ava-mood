import os
import telethon as th

app_id = "1150077"
app_hash = "162842e9d791c876a61d1791047d7971"
session_name = "login"
print(app_hash)
client = th.TelegramClient(session_name, api_id=app_id, api_hash=app_hash)
client.start()
for i in range(1, 100):
	client.send_message('@mi_xxx', 'Hello! Message num: {} '.format(i))
