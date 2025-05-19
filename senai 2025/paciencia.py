#Aula 03/02

class Nipe:
    def __init__(self, nome, simbolo, cor):
        self.nome = nome
        self.simbolo = simbolo
        self.cor = cor

class Carta:
    def __init__(self, nipe, nome, valor):
        self.nipe = nipe
        self.nome = nome
        self.valor = valor

    def imprimir(self):
        print(f"{self.nome} de {self.nipe.nome} ({self.nipe.simbolo}) - Valor: {self.valor}")

class Pilha:
    def __init__(self, nome):
        self.nome = nome
        self.cartas = []

    def adicionar(self, carta):
        """Adiciona uma carta à pilha"""
        self.cartas.append(carta)

    def remover(self):
        """Remove a última carta da pilha e retorna ela"""
        if self.cartas:
            return self.cartas.pop()
        return None

    def imprimir_pilha(self):
        """Mostra as cartas da pilha"""
        print(f"\n{self.nome}:")
        if self.cartas:
            for carta in self.cartas:
                carta.imprimir()
        else:
            print("(Vazia)")


copas = Nipe("Copas", "♥", "vermelho")
ouro = Nipe("Ouros", "♦", "vermelho")
paus = Nipe("Paus", "♣", "preto")
espadas = Nipe("Espadas", "♠", "preto")


nomes_cartas = ["Ás", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Valete", "Dama", "Rei"]
baralho = [Carta(nipe, nomes_cartas[i], i + 1) for nipe in [copas, ouro, paus, espadas] for i in range(13)]


pilha1 = Pilha("Pilha 1")
pilha2 = Pilha("Pilha 2")


pilha1.adicionar(baralho[0]) 
pilha1.adicionar(baralho[1])  
pilha2.adicionar(baralho[13]) 


carta_movida = pilha1.remover()
if carta_movida:
    pilha2.adicionar(carta_movida)
    print(f"\n✅Carta movida com sucesso: {carta_movida.nome} de {carta_movida.nipe.nome} ({carta_movida.nipe.simbolo})")
else:
    print("\n❌ Não foi possível mover a carta: Pilha vazia!")


carta_movida2 = pilha1.remover()
if carta_movida2:
    pilha2.adicionar(carta_movida2)
    print(f"\nCarta movida com sucesso: {carta_movida2.nome} de {carta_movida2.nipe.nome} ({carta_movida2.nipe.simbolo})")
else:
    print("\n Não foi possível mover a carta: Pilha vazia!")


pilha1.imprimir_pilha()
pilha2.imprimir_pilha()
