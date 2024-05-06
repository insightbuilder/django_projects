import json
from channels.generic.websocket import AsyncWebsocketConsumer 
from asgiref.sync import async_to_sync


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name,
                                           self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def receive(self, text_data):
        text_json = json.loads(text_data)
        # print(text_json)
        message = text_json['message']
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message",
                                   "message": message}
        )
        # self.send(text_data=json.dumps({"message": message}))

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({"message": message}))
