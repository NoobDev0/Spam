from pyrogram import Client
from .__init__.py import API_HASH, APP_ID

api_id = APP_ID
api_hash = API_HASH 
while True:
    with Client("vinesh_1981", api_id, api_hash) as app:
        app.send_message("vinesh1981", "Greetings from **Pyrogram**!")
