equipe_a = {"planejar reunião", "revisar documento", "testar sistema"} 

equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"} 

lista_u = equipe_a.union(equipe_b)

tarefa = input("Digite a tarefa que deseja excluir: ").lower()

if tarefa in lista_u:
    lista_u.remove(tarefa)

print(f'Tarefas finais: {lista_u}')