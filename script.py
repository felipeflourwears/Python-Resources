import asyncio
from temi import Temi

async def connect_temi():
    temi = Temi('ws://10.39.228.73:8175')
    await temi.connect()
    await temi.speak(sentence='Hello!').run()

asyncio.get_event_loop().run_until_complete(connect_temi())
