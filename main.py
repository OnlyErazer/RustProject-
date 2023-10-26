import asyncio
from rustplus import RustSocket
from time import sleep
socket = RustSocket("178.32.14.213", "27121", 76561198287107482, 260895708)

async def flicker():
    await socket.turn_on_smart_switch(169239485)
    sleep(1/3)
    await socket.turn_on_smart_switch(169239414)
    sleep(1/3)
    await socket.turn_on_smart_switch(169239573)
    sleep(1/3)
    await socket.turn_off_smart_switch(169239485)
    await socket.turn_off_smart_switch(169239414)
    await socket.turn_off_smart_switch(169239573)

async def main():

    await socket.connect()

    await flicker()

    await socket.disconnect()

if __name__ == "__main__":
    asyncio.run(main())