import logging
import dy
import asyncio
import time
import websockets

async def echo(websocket, path):
	#fetch msg
	async for message in websocket:
		#print(message)
		if message.find('live.douyin.com') > 0:
			with open('dy_url.txt', 'w') as dyurl :
				dyurl.write(message)
		else:
			with open('dy.txt','r') as f:
				while True:
					line = f.readline()
					if not line:
						with open('dy.txt', 'w') as dyurl :
							dyurl.write('')
						break
					else:
						await websocket.send(line)

async def main():
	# start a websocket server
	async with websockets.serve(echo, "localhost", 2375):
		await asyncio.Future()  # run forever


if __name__ == '__main__':
	asyncio.run(main())
