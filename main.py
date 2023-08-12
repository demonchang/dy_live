import logging
import dy
import time

if __name__ == '__main__':
	LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
	logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
	with open('dy_url.txt') as dytxt:
		while True:
			line = dytxt.readline()
			if not line:
				time.sleep(2)
			else:
				with open('dy_url.txt', 'w') as dyurl :
					dyurl.write('')
				dy.parseLiveRoomUrl(line)
				break



