def medianotas():
    try:
        numerodealunos = int(input("Digite o número de alunos: "))
        numerodenotas = int(input("Digite o número de notas: "))
        notas = []
        aluno = []        
        for i in range(numerodealunos):
            aluno.append(input(f"Digite o nome do aluno {i+1}: "))
            notas_aluno = []  # Reiniciar a lista de notas para cada aluno
            for j in range(numerodenotas):
                nota = float(input(f"Digite a nota {j+1} de {aluno[i]}: "))
                notas_aluno.append(nota)
            notas.append(notas_aluno)  # Adicionar as notas deste aluno à lista geral

        for i in range(numerodealunos):
            soma = sum(notas[i])
            media_aluno = soma / numerodenotas
            if media_aluno >= 7:
                print(f"O aluno {aluno[i]} foi aprovado com média {media_aluno:.2f}")
            else:
                print(f"O aluno {aluno[i]} foi reprovado com média {media_aluno:.2f}")
                
    except ValueError:
        print("Valor inválido. Por favor, digite um número válido.")
        return None

medianotas()
