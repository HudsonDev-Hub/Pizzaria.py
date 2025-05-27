import tkinter as tk
from tkinter import ttk, messagebox, font
from cliente import Cliente
from pizza import Pizza
from pedido import Pedido
import database

def fazer_pedido(nome_entry, telefone_entry, sabor_cb, tamanho_cb, pedidos_listbox):
    nome = nome_entry.get()
    telefone = telefone_entry.get()
    sabor = sabor_cb.get()
    tamanho = tamanho_cb.get()

    precos = {"Pequena": 20.0, "Média": 30.0, "Grande": 40.0}

    if not nome or not telefone or not sabor or not tamanho:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
        return

    cliente = Cliente(nome, telefone)
    pizza = Pizza(sabor, tamanho, precos[tamanho])
    pedido = Pedido(cliente, pizza)

    try:
        database.salvar_pedido(pedido)
        pedidos_listbox.insert(tk.END, str(pedido))
        nome_entry.delete(0, tk.END)
        telefone_entry.delete(0, tk.END)
        sabor_cb.set('')
        tamanho_cb.set('')
        messagebox.showinfo("Sucesso", "Pedido registrado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao registrar pedido:\n{e}")

def criar_gui():
    # Janela principal
    window = tk.Tk()
    window.title("Sistema da Pizzaria 🍕")
    window.geometry("600x550")
    window.configure(bg="#fdf6e3")  # Cor de fundo

    # Fontes personalizadas
    titulo_font = font.Font(family="Helvetica", size=18, weight="bold")
    label_font = font.Font(family="Arial", size=11)
    entry_font = font.Font(family="Arial", size=10)

    # Título
    titulo = tk.Label(window, text="Pizzaria Delícia 🍕", font=titulo_font, bg="#fdf6e3", fg="#d9480f")
    titulo.pack(pady=15)

    # Frame de formulário
    form_frame = tk.Frame(window, bg="#fdf6e3")
    form_frame.pack(pady=10)

    # Nome
    tk.Label(form_frame, text="Nome:", font=label_font, bg="#fdf6e3").grid(row=0, column=0, sticky='e', padx=10, pady=5)
    nome_entry = tk.Entry(form_frame, font=entry_font, width=30)
    nome_entry.grid(row=0, column=1, pady=5)

    # Telefone
    tk.Label(form_frame, text="Telefone:", font=label_font, bg="#fdf6e3").grid(row=1, column=0, sticky='e', padx=10, pady=5)
    telefone_entry = tk.Entry(form_frame, font=entry_font, width=30)
    telefone_entry.grid(row=1, column=1, pady=5)

    # Sabor
    tk.Label(form_frame, text="Sabor da Pizza:", font=label_font, bg="#fdf6e3").grid(row=2, column=0, sticky='e', padx=10, pady=5)
    sabores = ["Calabresa", "Mussarela", "Frango com Catupiry", "Quatro Queijos"]
    sabor_cb = ttk.Combobox(form_frame, values=sabores, state="readonly", width=28, font=entry_font)
    sabor_cb.grid(row=2, column=1, pady=5)

    # Tamanho
    tk.Label(form_frame, text="Tamanho:", font=label_font, bg="#fdf6e3").grid(row=3, column=0, sticky='e', padx=10, pady=5)
    tamanhos = ["Pequena", "Média", "Grande"]
    tamanho_cb = ttk.Combobox(form_frame, values=tamanhos, state="readonly", width=28, font=entry_font)
    tamanho_cb.grid(row=3, column=1, pady=5)

    # Botão de envio
    btn_style = {
        "font": ("Arial", 11, "bold"),
        "bg": "#d9480f",
        "fg": "white",
        "activebackground": "#b03a0d",
        "activeforeground": "white",
        "bd": 0,
        "width": 20,
        "cursor": "hand2"
    }

    cadastrar_btn = tk.Button(window, text="Fazer Pedido", command=lambda: fazer_pedido(
        nome_entry, telefone_entry, sabor_cb, tamanho_cb, pedidos_listbox
    ), **btn_style)
    cadastrar_btn.pack(pady=10)

    # Lista de pedidos
    tk.Label(window, text="Pedidos Realizados:", font=label_font, bg="#fdf6e3").pack()
    pedidos_listbox = tk.Listbox(window, width=70, font=("Courier New", 10))
    pedidos_listbox.pack(pady=10)

    for p in database.listar_pedidos():
        pedidos_listbox.insert(tk.END, f"{p[0]} - {p[3]} {p[2]} - R${p[4]:.2f}")

    window.mainloop()
