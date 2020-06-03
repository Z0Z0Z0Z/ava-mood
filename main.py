import os
import telethon as th

app_id = os.getenv('app_id')
app_hash = os.getenv('app_hash')
session_name = "login"
print(app_hash)
client = th.TelegramClient(session_name, app_id, app_hash)
client.send_code_request('+380931684539')
client.start()
for i in range(1, 100):
	client.send_message('@mi_xxx', 'Hello! Message num: {} '.format(i))
