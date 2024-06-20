def calculadora():
    while True:
        # Exibe o menu de operações
        print("\nEscolha a operação:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        # Solicita a escolha da operação ao usuário
        escolha = input("Digite o número da operação desejada: ")

        # Verifica se a escolha é válida
        if escolha == '5':
            print("Encerrando a calculadora.")
            break
        elif escolha not in ['1', '2', '3', '4']:
            print("Escolha inválida. Por favor, digite um número de 1 a 5.")
            continue

        # Solicita os dois números ao usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Realiza a operação escolhida e exibe o resultado
        if escolha == '1':
            resultado = num1 + num2
            print(f"\nResultado: {num1} + {num2} = {resultado}")
        elif escolha == '2':
            resultado = num1 - num2
            print(f"\nResultado: {num1} - {num2} = {resultado}")
        elif escolha == '3':
            resultado = num1 * num2
            print(f"\nResultado: {num1} * {num2} = {resultado}")
        elif escolha == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"\nResultado: {num1} / {num2} = {resultado}")
            else:
                print("Erro: divisão por zero.")

# Executa a calculadora
calculadora()

