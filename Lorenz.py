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