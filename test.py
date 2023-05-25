import asyncio
from temi import Temi

async def connect_temi():
    temi = Temi('ws://10.39.228.73:5555')
    await temi.connect()
    print("Conectado a TEMI")

    # Aquí puedes realizar acciones con TEMI, como moverlo, mostrar mensajes, etc.

    await temi.disconnect()
    print("Desconectado de TEMI")

asyncio.get_event_loop().run_until_complete(connect_temi())
