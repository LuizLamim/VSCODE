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

# --- Campos de Entrada ---
tk.Label(janela, text="Capital Inicial (R$):", font=fonte_label).pack(pady=5)
entry_principal = tk.Entry(janela, font=fonte_entry)
entry_principal.pack(pady=5)

tk.Label(janela, text="Taxa de Juros (% ao período):", font=fonte_label).pack(pady=5)
entry_taxa = tk.Entry(janela, font=fonte_entry)
entry_taxa.pack(pady=5)

tk.Label(janela, text="Período (meses/anos):", font=fonte_label).pack(pady=5)
entry_tempo = tk.Entry(janela, font=fonte_entry)
entry_tempo.pack(pady=5)

# --- Botão de Calcular ---
btn_calcular = tk.Button(janela, text="CALCULAR", command=calcular_juros, 
                         bg="#3498db", fg="white", font=fonte_label, 
                         cursor="hand2", relief="flat", width=20)
btn_calcular.pack(pady=20)

# --- Resultados ---
tk.Label(janela, text="Montante Total:", font=fonte_label).pack()
label_resultado_valor = tk.Label(janela, text="R$ 0.00", font=("Arial", 12, "bold"))
label_resultado_valor.pack(pady=5)

tk.Label(janela, text="Total em Juros:", font=fonte_label).pack()
label_juros_valor = tk.Label(janela, text="R$ 0.00", font=("Arial", 12, "bold"))
label_juros_valor.pack(pady=5)

janela.mainloop()