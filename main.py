def obter_notas():
    notas = []
    for i in range(5):
        while True:
            try:
                nota = float(input(f"Digite a nota {i+1} (0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Por favor, insira um número válido.")
    return notas

def calcular_media(notas):
    return sum(notas) / len(notas)

def main():
    alunos = []
    aprovados = []

    while True:
        for i in range(30):
            nome = input(f"Digite o nome do aluno {i+1}: ")
            notas = obter_notas()
            media = calcular_media(notas)
            aprovado = media >= 7
            alunos.append({'nome': nome, 'media': media, 'aprovado': aprovado})
            if aprovado:
                aprovados.append(nome)
        
        print("\nLista de Alunos:")
        for aluno in alunos:
            status = "Aprovado" if aluno['aprovado'] else "Reprovado"
            print(f"Nome: {aluno['nome']}, Média: {aluno['media']:.2f}, Status: {status}")

        print("\nAlunos Aprovados:")
        for nome in aprovados:
            print(nome)

        # Menu para inserir mais alunos ou encerrar o programa
        while True:
            opcao = input("\nDeseja inserir mais alunos ou encerrar o programa? (inserir/encerrar): ").strip().lower()
            if opcao == 'inserir':
                break
            elif opcao == 'encerrar':
                print("Programa encerrado.")
                return
            else:
                print("Opção inválida. Por favor, escolha 'inserir' ou 'encerrar'.")

if __name__ == "__main__":
    main()
