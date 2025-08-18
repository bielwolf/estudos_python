notas = list(map(float, input('Digite as notas dos alunos separapados por vigulas: ').split(', ')))

media = sum(notas) / len(notas)

print(f'Média final da turma: {media}')