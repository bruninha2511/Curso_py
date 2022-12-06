
class Cartao:
    def __init__(self, nome, bandeira, limite, validade, cds):
        self.nome = nome
        self.bandeira = bandeira
        self.limite = limite
        self.validade = validade
        self.cds = cds

    def info (self):
        print(f'nome: {self.nome} ')
        print(f'bandeira: {self.bandeira} ')
        print(f'limite: {self.limite} ')
        print(f'validade: {self.validade} ')
        print(f'cds: {self.cds} ')
        print()

    def mlimite (self):
        print(f'O seu limite é de: {self.limite}')
    
    def comprar (self):
        Produto = input('Digite o que voce quer comprar: ')
        Preço = float(input('Digite o preço: '))
        if Preço > self.limite:
            print('Isso ultrapassa o seu limite')
        else:
            self.limite = self.limite - Preço





