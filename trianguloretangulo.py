import math

def calcular_triangulo():
    print("--- Calculadora de Triângulo Retângulo ---")
    print("O que você deseja fornecer?")
    print("1. Os dois catetos")
    print("2. A hipotenusa e um cateto")
    
    opcao = input("Escolha a opção (1 ou 2): ")

    try:
        if opcao == '1':
            a = float(input("Digite o valor do primeiro cateto: "))
            b = float(input("Digite o valor do segundo cateto: "))
            
            # Cálculo da hipotenusa: c = sqrt(a² + b²)
            c = math.sqrt(a**2 + b**2)
            area = (a * b) / 2
            
            print(f"\nResultados:")
            print(f"- Hipotenusa: {c:.2f}")
            print(f"- Área: {area:.2f}")
            print(f"- Perímetro: {a + b + c:.2f}")

        elif opcao == '2':
            c = float(input("Digite o valor da hipotenusa: "))
            a = float(input("Digite o valor do cateto conhecido: "))
            
            if c <= a:
                print("Erro: A hipotenusa deve ser maior que o cateto!")
                return

            # Cálculo do outro cateto: b = sqrt(c² - a²)
            b = math.sqrt(c**2 - a**2)
            area = (a * b) / 2
            
            print(f"\nResultados:")
            print(f"- Outro cateto: {b:.2f}")
            print(f"- Área: {area:.2f}")
            print(f"- Perímetro: {a + b + c:.2f}")
        
        else:
            print("Opção inválida!")

