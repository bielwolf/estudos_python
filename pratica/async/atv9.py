import asyncio

VELOCIDADE_DOWNLOAD = 5

arquivos = {
    "arquivo_1.txt": 30,
    "arquivo_2.txt": 45,
    "arquivo_3.txt": 20,
    "arquivo_4.txt": 10,
    "arquivo_5.txt": 50,
}

async def download(nome, tamanho):
    print(f'Iniciando download de {nome} (tamanho: {tamanho}MB)...')    
    baixado = 0
    segundos = 0

    while baixado < tamanho:
        await asyncio.sleep(1)
        baixado += VELOCIDADE_DOWNLOAD
        baixado = min(baixado, tamanho)
        segundos += 1
        print(f"[{segundos}s] {nome}: {baixado}MB baixados")
    print(f"{nome} concluído!\n")

async def main():
    tarefa = [asyncio.create_task(download(nome, tamanho)) for nome, tamanho in arquivos.items()]
    await asyncio.gather(*tarefa)
    print("\nTodos os downloads foam finalizados!")

asyncio.run(main())