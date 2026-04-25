import numpy as np
import matplotlib.pyplot as plt

# Define o intervalo de valores para x (ex: de -5 até 5, com 100 pontos)
x = np.linspace(-5, 5, 100)

# Calcula a função exponencial e^x para cada valor de x
y = np.exp(x)

# Cria a figura e plota os dados
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='y = e^x', color='blue', linewidth=2)

# Adiciona título e rótulos aos eixos
plt.title('Gráfico da Função Exponencial (e^x)')
plt.xlabel('x')
plt.ylabel('f(x)')

# Adiciona uma grade para facilitar a visualização
plt.grid(True, linestyle='--', alpha=0.7)

# Destaca os eixos x=0 e y=0
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Mostra a legenda
plt.legend()

# Exibe o gráfico na tela
plt.show()