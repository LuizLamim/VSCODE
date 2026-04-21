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

# 2. Criação dos Elementos (Widgets)
# Título
label_titulo = tk.Label(root, text="Descubra X% de um valor", font=("Arial", 12, "bold"))
label_titulo.pack(pady=10)

# Campo do Valor Total
label_valor = tk.Label(root, text="Valor Total:")
label_valor.pack()
entry_valor = tk.Entry(root, justify="center")
entry_valor.pack(pady=5)

# Campo da Porcentagem
label_porcentagem = tk.Label(root, text="Porcentagem (%):")
label_porcentagem.pack()
entry_porcentagem = tk.Entry(root, justify="center")
entry_porcentagem.pack(pady=5)

# Botão Calcular
btn_calcular = tk.Button(root, text="Calcular", command=calcular_porcentagem, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_calcular.pack(pady=15)

# Label para exibir o resultado final
label_resultado = tk.Label(root, text="Resultado: ", font=("Arial", 12, "bold"), fg="blue")
label_resultado.pack()