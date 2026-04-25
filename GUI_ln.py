import tkinter as tk
from tkinter import messagebox
import math

def calcular_ln():
    try:
        # Obtém o valor do campo de entrada
        valor_input = entry_numero.get()
        numero = float(valor_input)
        
        # O logaritmo natural só é definido para números estritamente positivos
        if numero <= 0:
            messagebox.showerror("Erro Matemático", "O valor deve ser maior que zero.")
            return
        
        # Calcula o ln (logaritmo na base e)
        resultado = math.log(numero)
        
        # Exibe o resultado formatado com 4 casas decimais
        label_resultado.config(text=f"Resultado (ln): {resultado:.4f}", fg="#00FF00")
        
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, insira um número válido.")