import asyncio
import random

jogos = [
    {"id": 1, "times": ("Flamengo", "Palmeiras")},
    {"id": 2, "times": ("São Paulo", "Corinthians")},
    {"id": 3, "times": ("Grêmio", "Internacional")},
]
 
RESULTADOS = ["Vitória do Time A", "Vitória do Time B", "Empate"]

async def apostafeitas(jogo, futuro):
    tempo = random.randint(2, 8)
    indice = jogo["id"]
    time_a, time_b = jogo["times"]

    print(f"Apostando no jogo {indice}: {time_a} x {time_b}...")
    await asyncio.sleep(tempo)

    print(f"Aposta no jogo {indice}: {time_a} x {time_b} registrada! Aguardando resultado...")

    escolha = random.choice(RESULTADOS)
    futuro.set_result(escolha)

    print(f"Aposta do jogo {indice}: {time_a} x {time_b} - {escolha}")

async def main():
    futuro = [asyncio.Future() for _ in jogos]
    tarefas = [asyncio.create_task(apostafeitas(jogos[i], futuro[i])) for i in range(len(jogos))]
    await asyncio.gather(*tarefas)

    print('\nTodos os resultadso foram revelados!\n')

asyncio.run(main())