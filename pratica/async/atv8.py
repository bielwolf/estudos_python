import asyncio
import random
import time

async def temperatura():
    while True:
        await asyncio.sleep(2)
        temp = random.randint(20, 30)
        print(f'[{2}s] Temperatura: {temp}°C')

async def umidade():
    while True:
        await asyncio.sleep(3)
        umi = random.randint(50, 70)
        print(f'[{3}s] Umidade: {umi}%')

async def qlddoar():
    while True:
        await asyncio.sleep(5)
        ar = random.choice(["Boa", "Regular", "Ruim"])
        print(f'[{5}s] Qualidade do ar: {ar}')

async def main():
    await asyncio.gather(temperatura(), umidade(), qlddoar())

asyncio.run(main())