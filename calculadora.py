def calculadora():
    print("--- Calculadora Simples ---")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    escolha = input("\nEscolha a operação (1/2/3/4): ")

    if escolha in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, digite apenas números válidos.")
            return

        if escolha == '1':
            print(f"\nResultado: {num1} + {num2} = {num1 + num2}")
        elif escolha == '2':
            print(f"\nResultado: {num1} - {num2} = {num1 - num2}")
        elif escolha == '3':
            print(f"\nResultado: {num1} * {num2} = {num1 * num2}")
        elif escolha == '4':
            if num2 != 0:
                print(f"\nResultado: {num1} / {num2} = {num1 / num2}")
            else:
                print("\nErro: Divisão por zero não é permitida.")
    else:
        print("\nEscolha inválida. Tente novamente.")

if __name__ == "__main__":
    calculadora()