import tkinter as tk
from tkinter import messagebox

def calcular_porcentagem():
    try:
        # Pega os valores digitados e substitui vírgula por ponto (para aceitar decimais)
        valor_total = float(entry_valor.get().replace(',', '.'))
        porcentagem = float(entry_porcentagem.get().replace(',', '.'))
        
        # Realiza o cálculo da porcentagem
        resultado = (porcentagem / 100) * valor_total
        
        # Atualiza a label de resultado
        label_resultado.config(text=f"Resultado: {resultado:.2f}")
        
    except ValueError:
        # Mostra um erro se o usuário digitar letras ou símbolos inválidos
        messagebox.showerror("Erro de Entrada", "Por favor, insira apenas números válidos.")

# 1. Configuração da Janela Principal
root = tk.Tk()
root.title("Calculadora de Porcentagem")
root.geometry("300x250")
root.resizable(False, False) # Impede que a janela seja redimensionada