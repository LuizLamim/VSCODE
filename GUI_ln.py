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

# Configuração da Janela Principal
janela = tk.Tk()
janela.title("Calculadora de Logaritmo Natural")
janela.geometry("350x250")
janela.configure(bg="#2c3e50") # Cor de fundo elegante

# Estilização de Labels e Botões
font_estilo = ("Arial", 12, "bold")

label_instrucao = tk.Label(janela, text="Digite o número para calcular ln(x):", 
                           bg="#2c3e50", fg="white", font=font_estilo)
label_instrucao.pack(pady=20)

entry_numero = tk.Entry(janela, font=("Arial", 14), justify='center')
entry_numero.pack(pady=5)

botao_calcular = tk.Button(janela, text="Calcular ln", command=calcular_ln, 
                           bg="#3498db", fg="white", font=font_estilo, cursor="hand2")
botao_calcular.pack(pady=20)

label_resultado = tk.Label(janela, text="Resultado (ln): ---", 
                           bg="#2c3e50", fg="#ecf0f1", font=font_estilo)
label_resultado.pack(pady=10)

# Inicia o loop da interface
janela.mainloop()