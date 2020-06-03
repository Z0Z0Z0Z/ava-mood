import os
import telethon as th

app_id = os.getenv('app_id')
app_hash = os.getenv('app_hash')
session_name = "login.session"
client = th.TelegramClient(session_name, app_id, app_hash)
client.start()

for i in range(1, 100):
	client.send_message('@mi_xxx', 'Hello! Message num: {} '.format(i))
