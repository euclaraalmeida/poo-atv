import random

class Cartas:
    

    def __init__(self):
        self.baralho = [] 

        self.carta = [
            "ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valete", "dama", "rei"
        ]


        self.naipe = ['PAUS','OURO','ESPADAS','COPAS']

        
    
    def relacionar(self,baralho):
        for naipe in self.naipe:
            for carta in self.carta:
                self.baralho.append((f"{carta} de {naipe}"))

        for naipe in self.naipe:
            for carta in self.carta:
                print(f" {baralho:4}", end=", ")  # Mostra a relação carta-naipe
            print()

 

Baralho = Cartas()
Baralho.relacionar(Baralho)

'''class Baralho(Cartas):

    
    def convertando(self):
        super().__init__()
        self.itens = list(self.cartas.items())

    def embaralhar(self):
        random.shuffle(self.itens)
        dicionario_embaralhado = dict(self.itens)
        return dicionario_embaralhado

baralho = Baralho()


dicionario_embaralhado = baralho.embaralhar()


print(dicionario_embaralhado)'''

 