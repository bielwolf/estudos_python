import asyncio
import time

cursos = {
    "Python Avançado": {"vagas": 2, "inscritos": []},
    "Java para Iniciantes": {"vagas": 1, "inscritos": []},
    "Machine Learning": {"vagas": 0, "inscritos": []},
}
 
alunos = [
    {"nome": "Alice", "curso": "Python Avançado"},
    {"nome": "Bruno", "curso": "Python Avançado"},
    {"nome": "Carlos", "curso": "Java para Iniciantes"},
    {"nome": "Daniela", "curso": "Machine Learning"},
    {"nome": "Alice", "curso": "Python Avançado"},  
]

async def inscreve_aluno(aluno):
    curso_nome = aluno["curso"]
    nome_aluno = aluno["nome"]

    print(f"Inscrevendo {nome_aluno} no curso {curso_nome}")

    if curso_nome not in cursos:
        print(f"Erro! O curso {curso_nome} não existe.\n")
        return
    
    curso = cursos[curso_nome]

    if nome_aluno in curso ["inscritos"]:
        print(f'{nome_aluno} já está inscito no curso {curso_nome}! Inscrição rejeitada.\n')
        return
    if curso["vagas"] > 0:
        curso["inscritos"].append(nome_aluno)
        curso["vagas"] -= 1
        print(f"Inscriçã confirmada para {nome_aluno} no curso {curso_nome}")
    else:
        print(f"Turma lotada! {nome_aluno} não pôde se inscrever no curso {curso_nome}")

async def main():
    tarefas = [asyncio.create_task(inscreve_aluno(a)) for a in alunos]
    await asyncio.gather(*tarefas)
    print("Todas as inscrições foram processadas!\n")

asyncio.run(main())