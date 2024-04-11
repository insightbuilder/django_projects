#!/usr/bin/env python
# The file needs to be in the django server folder
# sys.path.append("D:\\gitFolders\\django_projects\\streamdjango")

import asyncio
import sys
import os
sys.path.append("D:\\gitFolders\\django_projects\\streamdjango")
os.environ['DJANGO_SETTINGS_MODULE'] = "streamdjango.settings"
print(sys.path)
import django
import websockets


django.setup()

from sesame.utils import get_user
from websockets.frames import CloseCode

# Execute the below in seperate django-admin shell only. (Not python shell, it wont work)
# import sys
# sys.path.append("D:\\gitFolders\\django_projects\\streamdjango")    
# import django  
# django.setup()
# from django.contrib.auth import get_user_model
# User = get_user_model()
# user = User.objects.get(username="useradmin")
# from sesame.utils import get_token
# user    
# get_token(user)

# websocket = new WebSocket("ws://localhost:8888/");
# websocket.onopen = (event) => websocket.send("<your token>");
# websocket.onmessage = (event) => console.log(event.data);

async def handler(websocket):
    sesame = await websocket.recv()
    user = await asyncio.to_thread(get_user, sesame)  # this will get the user based on the token extracted from cmd prompt.
    if user is None:
        await websocket.close(CloseCode.INTERNAL_ERROR, "authentication failed")
        return

    await websocket.send(f"Hello {user}!")


async def main():
    async with websockets.serve(handler, "localhost", 8888):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())