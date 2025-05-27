import sqlite3

def conectar():
    return sqlite3.connect("pizzaria.db")

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            telefone TEXT,
            sabor TEXT,
            tamanho TEXT,
            preco REAL
        )
    ''')
    conn.commit()
    conn.close()

def salvar_pedido(pedido):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pedidos (nome, telefone, sabor, tamanho, preco)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        pedido.cliente.nome,
        pedido.cliente.telefone,
        pedido.pizza.sabor,
        pedido.pizza.tamanho,
        pedido.pizza.preco
    ))
    conn.commit()
    conn.close()

def listar_pedidos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, telefone, sabor, tamanho, preco FROM pedidos")
    pedidos = cursor.fetchall()
    conn.close()
    return pedidos
