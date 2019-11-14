import json
import asyncio
from channels.consumer import AsyncConsumer

class CTFConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept"
        })
        await self.send({
            "type": "websocket.send",
            "text": "Websockets are amazing. Here is your flag{onetrust}",
        })

        await self.send({
            "type": "websocket.close"
        })

    async def websocket_receive(self, event):
        pass
    async def websocket_disconnect(self, event):
        pass
