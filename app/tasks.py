from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import random
from time import sleep

channel_layer = get_channel_layer()

@shared_task
def add():
    sleep(5)
    x = [0,1,2,3,4,5,6,7,8,9]
    random.shuffle(x)
    print(x)
    async_to_sync(channel_layer.group_send)(
            'chat',
            {
                'type':'send.msg',
                'msg':  str(random.randint(0, 10)) ,
                'mas':x
            }
            )
    
     

    print("hello........dd")