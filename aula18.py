import random


class Carta:
    """Representa a alegria do povo brasileiro."""

    def __init__(self, naipe=0, rank=1):
        self.naipe = naipe
        self.rank = rank

    nomes_dos_naipes = ('Paus', 'Copas', 'Espada', 'Ouro')
    nomes_dos_ranks = (
        None,
        'Às',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        'Valete',
        'Dama',
        'Rei',
    )

    def __str__(self) -> str:
        return f'{Carta.nomes_dos_ranks[self.rank]} de {Carta.nomes_dos_naipes[self.naipe]}'

    def __lt__(self, other):
        if self.rank == other.rank:
            return Carta.nomes_dos_naipes.index(
                self.naipe
            ) > Carta.nomes_dos_naipes.index(other.naipe)
        return self.rank < other.rank

    def __gt__(self, other):
        if self.rank == other.rank:  # se as cartas forem iguais
            return Carta.nomes_dos_naipes.index(  # verifica a importancia do naipe e retorna
                self.naipe
            ) < Carta.nomes_dos_naipes.index(
                other.naipe
            )
        return self.rank > other.rank  # se não, retorna se é maior ou não


class Baralho:
    def __init__(self) -> None:
        self.cartas = list()
        for naipe in range(4):
            for vlr_da_carta in range(1, 14):
                carta = Carta(naipe, vlr_da_carta)
                self.cartas.append(carta)

    def __str__(self) -> str:
        lista_de_cartas = []
        for carta in self.cartas:
            lista_de_cartas.append(str(carta))
        return '\n'.join(lista_de_cartas)

    def tirar_carta(self):
        return self.cartas.pop()

    def adicionar_carta(self, carta):
        self.cartas.append(carta)

    def misturar_cartas(self):
        random.shuffle(self.cartas)

    def pegar_cartas(self, mao, numero):
        for _ in range(numero):
            self.misturar_cartas()
            mao.adicionar_carta(self.tirar_carta())

    def sortear_tombo(self, mao, manilha):
        self.pegar_cartas(mao, 1)

    def deal_hands(self, mao, numeromaos, numerocartas):
        listademaos = list()
        listadecartas = list()
        for _ in range(numeromaos):
            listadecartas.append(self.pegar_cartas(mao, numerocartas))
        listademaos.append(listadecartas)

    def coringas(self, mao):
        pass


class Mao(Baralho):
    def __init__(self, nome):
        self.cartas = []
        self.nome = nome


truco_ladrao = Baralho()

mao_de_baralho = Mao('Truco ladrão')

tombo = Mao('vaisifude')

truco_ladrao.sortear_tombo(tombo, 1)

truco_ladrao.deal_hands(mao_de_baralho, 4, 3)

print('=====================================')

print(mao_de_baralho)
