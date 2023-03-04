import json
from channels.generic.websocket import AsyncWebsocketConsumer 
from asgiref.sync import async_to_sync
from time import sleep
class ChatConsumer(AsyncWebsocketConsumer):
    count = 0
    patti = 1
    async def connect(self):
        print("==================")
        await self.accept()
        # ChatConsumer.count = ChatConsumer.count +1
        await self.channel_layer.group_add("chat", self.channel_name)
         
        ChatConsumer.count =  ChatConsumer.count+1
        await self.channel_layer.group_send(
            'chat',
            {
                "type": "chat.message", 
                "message": ChatConsumer.count,
            }
        )
    async def disconnect(self, close_code):
        ChatConsumer.count =  ChatConsumer.count-1
        await self.channel_layer.group_send(
            'chat',
            {
                "type": "chat.message", 
                "message": ChatConsumer.count,
            }
        )
    # Receive message from WebSocket
    async def receive(self, text_data):
        print(text_data)
         
        await self.channel_layer.group_send(
            'chat',
            {
                'type':'send.msg',
                'msg': text_data
            }
            )


    async def send_msg(self,event):
        print(event['msg'])
        await self.send(json.dumps({'msg':event['msg'],'list':json.dumps(event['mas'])}))


    async def sendrandom_list(self,event):
        await self.send(json.dumps(event['mas']))


    async def chat_message(self, event):
         
        await self.send(json.dumps({'msg':"hhhhhhhhh"}))
         


