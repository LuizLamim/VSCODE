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