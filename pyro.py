from pyrogram import Client

api_id = 5972952
api_hash = "74536bd24d8ad4d2e51445d07c41b0bb"
while True:
    with Client("vinesh_1981", api_id, api_hash) as app:
        app.send_message("vinesh1981", "Greetings from **Pyrogram**!")