import asyncio
import time
import math

numeros = [5, 3, 7, 4, 6]

async def fatorial(n):
    await asyncio.sleep(n)
    print(f'Fatorial de {n} = {math.factorial(n)}')
    
async def main():
    tarefas = [asyncio.create_task(fatorial(n)) for n in numeros]
    await asyncio.gather(*tarefas)

asyncio.run(main())