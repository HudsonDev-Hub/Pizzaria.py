class Pedido:
    def __init__(self, cliente_id):
        self._cliente_id = cliente_id
        self._data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._itens = []
        self._total = 0.0
        self._endereco = input("Informe o endereço de entrega: ")

    def adicionar_item(self, pizza_id, sabor, preco, quantidade):
        self._itens.append((pizza_id, sabor, preco, quantidade))
        self._total += preco * quantidade

    def calcular_total_com_frete(self):
        frete = 8.0 if self.total_pizzas() >= 2 else 0.0
        return self._total + frete

    def total_pizzas(self):
        return sum(qtd for _, _, _, qtd in self._itens)

    def exibir_resumo(self):
        print("\n🧾 Resumo do Pedido:")
        for _, sabor, preco, qtd in self._itens:
            print(f"  - {qtd}x {sabor} (R${preco:.2f})")
        print(f"🏠 Endereço de entrega: {self._endereco}")
        print(f"📦 Total com frete: R${self.calcular_total_com_frete():.2f}")
