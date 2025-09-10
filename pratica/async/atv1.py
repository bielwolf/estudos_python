import asyncio
import time

async def temporizador():
    print(f'Iniciando temporizador...')
    await asyncio.sleep(3)
    print(f'Tempo finalizado após 3 segundos!')

asyncio.run(temporizador())