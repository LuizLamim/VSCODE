import numpy as np
import matplotlib.pyplot as plt

def lorenz_derivadas(x, y, z, sigma=10.0, rho=28.0, beta=8.0/3.0):
    """
    Calcula as derivadas parciais do sistema de Lorenz.
    """
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return dx_dt, dy_dt, dz_dt

# Parâmetros da simulação
dt = 0.01          # Tamanho do passo de tempo
num_passos = 10000 # Número total de iterações 

# Inicialização dos arrays para armazenar as coordenadas
xs = np.empty(num_passos + 1)
ys = np.empty(num_passos + 1)
zs = np.empty(num_passos + 1)

# Valores iniciais (condição inicial ligeiramente fora da origem)
xs[0], ys[0], zs[0] = (0.0, 1.0, 1.05)

# Integração numérica usando o Método de Euler
for i in range(num_passos):
    dx, dy, dz = lorenz_derivadas(xs[i], ys[i], zs[i])
    
    xs[i + 1] = xs[i] + (dx * dt)
    ys[i + 1] = ys[i] + (dy * dt)
    zs[i + 1] = zs[i] + (dz * dt)

# Configuração e plotagem do gráfico 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

# Plota a linha contínua do atrator
ax.plot(xs, ys, zs, lw=0.5, color='teal')

# Configurações visuais do gráfico
ax.set_title("Atrator de Lorenz", fontsize=16)
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
ax.set_zlabel("Eixo Z")

# Exibe o gráfico na tela
plt.show()