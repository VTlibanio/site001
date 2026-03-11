import tkinter as tk
from tkinter import messagebox

# Função que calcula e exibe os resultados
def calcular_compras():
    global valorestotais, menorpreco, cont, barato, produtos

    # Nome do produto
    produto = nome_produto.get().strip().upper()

    if produto == '':
        messagebox.showwarning("Campo Produto", "Por favor, digite o nome do produto.")
        return

    # Validação do valor
    try:
        valor = float(valor_produto.get())
    except ValueError:
        messagebox.showerror("Valor Inválido", "Por favor, digite um número válido para o valor do produto.")
        return

    cont += 1

    # Verifica o produto mais barato
    if cont == 1 or valor < menorpreco:
        menorpreco = valor
        barato = produto

    # Atualiza as variáveis de total e lista de produtos
    valorestotais += valor
    produtos += produto + ', '

    # Pergunta se o usuário deseja continuar
    escolha = escolha_var.get().strip().upper()

    if escolha not in ['S', 'N', 'SIM', 'NAO', 'sim', 'nao']:
        messagebox.showwarning("Escolha Inválida", "Por favor, digite 'S' ou 'N'.")
        return

    if escolha in ['N', 'NAO', 'nao']:
        # Exibe o resumo
        messagebox.showinfo("Resumo", f"Valor total das compras: R$ {valorestotais:.2f}\n"
                                      f"Produtos comprados: {produtos.rstrip(', ')}\n"
                                      f"Produto mais barato: {barato} (R$ {menorpreco:.2f})")
        # Reseta o formulário
        resetar_campos()
    else:
        # Limpa os campos para a próxima entrada
        nome_produto.delete(0, tk.END)
        valor_produto.delete(0, tk.END)

# Função para resetar os campos após o resumo
def resetar_campos():
    global valorestotais, menorpreco, cont, barato, produtos

    # Reseta as variáveis
    valorestotais = menorpreco = cont = 0
    barato = ''
    produtos = ''

    # Limpa os campos
    nome_produto.delete(0, tk.END)
    valor_produto.delete(0, tk.END)
    escolha_var.delete(0, tk.END)

# Criando a janela principal da interface gráfica
root = tk.Tk()
root.title("Controle de Compras")
root.geometry("400x300")

# Título
titulo = tk.Label(root, text="Cadastro de Compras", font=("Arial", 16))
titulo.pack(pady=10)

# Campo para nome do produto
label_produto = tk.Label(root, text="Digite o nome do produto:")
label_produto.pack()
nome_produto = tk.Entry(root, width=40)
nome_produto.pack(pady=5)

# Campo para valor do produto
label_valor = tk.Label(root, text="Digite o valor do produto (R$):")
label_valor.pack()
valor_produto = tk.Entry(root, width=40)
valor_produto.pack(pady=5)

# Campo para escolher se deseja continuar
label_escolha = tk.Label(root, text="Deseja continuar? (S/N):")
label_escolha.pack()
escolha_var = tk.Entry(root, width=40)
escolha_var.pack(pady=5)

# Botão para calcular e mostrar o resumo
botao_calcular = tk.Button(root, text="Finalizar Compras", command=calcular_compras)
botao_calcular.pack(pady=20)

# Inicializa as variáveis globais
valorestotais = 0
menorpreco = float('inf')  # Inicializa com valor muito alto
cont = 0
barato = ''
produtos = ''

# Rodando a interface gráfica
root.mainloop()
