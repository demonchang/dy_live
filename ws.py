import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://localhost:2375") as websocket:
        await websocket.send("https://live.douyin.com/269909523264")
        recv_msg = await websocket.recv()
        print(recv_msg)

asyncio.run(hello())