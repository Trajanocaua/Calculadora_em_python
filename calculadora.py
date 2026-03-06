print("=== Calculadora Simples ===")

while True:
    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print("\nEscolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    operacao = input("Digite o número da operação: ")

    if operacao == "1":
        print("Resultado:", num1 + num2)

    elif operacao == "2":
        print("Resultado:", num1 - num2)

    elif operacao == "3":
        print("Resultado:", num1 * num2)

    elif operacao == "4":
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Erro: divisão por zero!")

    elif operacao == "0":
        print("Encerrando calculadora...")
        break

    else:
        print("Operação inválida.")
