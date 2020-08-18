usersoc = []

async def chatting(scope,receive,send):
    while True :
        event = await receive()
        #handshake
        if event['type'] == "websocket.connect":
            usersoc.append(send)
            await send({
                'type': 'websocket.accept'
            })
        elif event['type'] == 'websocket.disconnet':
            usersoc.remove(send)
            break
        elif event['type'] == 'websocket.receive':
            msg = event['text']
            for soc in usersoc:
                await soc({
                    'type':'websocket.send',
                    'text':msg,
                })
        else :
            pass
