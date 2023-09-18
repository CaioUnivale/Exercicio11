class Veiculo:
    def __init__(self, cor, preco):
        self.cor = cor
        self.preco = preco
    
    def detalhes(self):
        return f"Cor: {self.cor}\nPreço: R${self.preco:.2f}"

class Carro(Veiculo):
    def __init__(self, cor, preco, numero_portas):
        super().__init__(cor, preco)
        self.numero_portas = numero_portas
    
    def detalhes(self):
        veiculo_detalhes = super().detalhes()
        return f"{veiculo_detalhes}\nNúmero de Portas: {self.numero_portas}"

class Bicicleta(Veiculo):
    def __init__(self, cor, preco, tipo):
        super().__init__(cor, preco)
        self.tipo = tipo
    
    def detalhes(self):
        veiculo_detalhes = super().detalhes()
        return f"{veiculo_detalhes}\nTipo: {self.tipo}"


carro = Carro(cor="Azul", preco=45000, numero_portas=4)
bicicleta = Bicicleta(cor="Verde", preco=1200, tipo="Montanha")

print("Detalhes do Carro:")
print(carro.detalhes())
print("\nDetalhes da Bicicleta:")
print(bicicleta.detalhes())