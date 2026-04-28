import tkinter as tk
from tkinter import messagebox

def calcular_juros():
    try:
        # Resgatando os valores dos campos de entrada
        principal = float(entry_principal.get())
        taxa = float(entry_taxa.get()) / 100
        tempo = float(entry_tempo.get())
        
        # Fórmula de Juros Compostos: M = P * (1 + i)^t
        montante = principal * (1 + taxa) ** tempo
        juros = montante - principal
        
        # Atualizando o resultado na tela
        label_resultado_valor.config(text=f"R$ {montante:.2f}", fg="#2ecc71")
        label_juros_valor.config(text=f"R$ {juros:.2f}", fg="#e67e22")
        
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, insira apenas números válidos.")

# Configuração da Janela Principal
janela = tk.Tk()
janela.title("Calculadora de Juros Compostos")
janela.geometry("350x450")
janela.configure(padx=20, pady=20)

# Estilização Simples
fonte_label = ("Arial", 10, "bold")
fonte_entry = ("Arial", 10)