import asyncio
import time

async def download(tempo):
    print('Iniciando download...')
    await asyncio.sleep(tempo)
    print('Download concluído')

async def analise(tempo):
    print('Iniciando análise de dados...')
    await asyncio.sleep(tempo)
    print('Análise de dados concluídas!')

async def main():
    await asyncio.gather(
        download(2),
        analise(3)
    )
asyncio.run(main())