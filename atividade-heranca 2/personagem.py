class Personagem: #super classe
    def __init__(self, nome, vida = 5 ):
        self._nome = nome
        self._vida = vida

    def info(self):
        print(f"O nome do personagem é {self._nome} e seu total de vida é {self._vida}")

    def atacar(self):
        print (f"CUIDADO! O personagem {self._nome} está atacando! ")

class Jogador(Personagem):
    def __init__(self, nome, raca, vida = 5):
        super().__init__(nome, vida)
        self._inventario = []
        self._raca = raca

    def info(self):
        print(f"A raça do persongem é: {self._raca}")

    def usarHabilidade(self, poder):
        print(f"Habilidade Ativada: {poder}")

    def coletarItem(self, item):
        self._inventario.append(item)  # append adiciona
        print(f"{item} foi adicionado ao inventário.")
        print(f"Itens coletados: {self._inventario} ")

class Monstro(Personagem):
    def __init__(self, nome, tipo, forca = 20, vida = 10):
         super().__init__(nome, vida)
         self._tipo = tipo
         self._forca = forca

    def defender(self):
        self._vida -= 1
        print(f"O {self._nome} está se defendendo, sua vida no momento é de {self._vida}")

    def exibirInformacoes(self):
        print(f"Nome do monstro: {self._nome}, Total de vida: {self._vida}, Tipo: {self._tipo}, Força: {self._forca} ")
    
    def invocarAliado(self, nomeAliado, tipoAliado, vidaAliado = 10, forcaAliado = 30):
        self._nomeAliado = nomeAliado
        self._TipoAliado = tipoAliado
        self._vidaAliado = vidaAliado
        self._forcaAliado = forcaAliado
        print(f"{self._nome} invocou o aliado: {self._nomeAliado}, Tipo: {self._TipoAliado}, Vida: {self._vidaAliado}, Força: {self._forcaAliado}")