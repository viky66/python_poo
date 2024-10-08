from personagem import Personagem, Jogador, Monstro

print("-"*50)

p1 = Personagem("Vorath", 5)
p1.info()
p1.atacar()

print("-"*50)

elfo = Jogador("Vorath", "Elfo")
elfo.info()
elfo.usarHabilidade("Visão Noturna")
elfo.coletarItem("Armadura")

print("-"*50)


m1 = Monstro("Zyphor", "Vampiro")
m1.exibirInformacoes()
m1.invocarAliado("P4perback", "Esqueleto")
m1.defender()

