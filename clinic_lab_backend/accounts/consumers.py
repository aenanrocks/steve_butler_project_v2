import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # This is called when the WebSocket connection is opened
        self.user = self.scope['user']
        if self.user.is_authenticated:
            self.group_name = f"user_{self.user.id}"
            await self.channel_layer.group_add(self.group_name, self.channel_name)
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        # This is called when the WebSocket connection is closed
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        # Called when a message is received from the WebSocket
        data = json.loads(text_data)
        await self.send(text_data=json.dumps({
            'message': data['message']
        }))

    async def send_notification(self, event):
        # Called to send a notification to the WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))