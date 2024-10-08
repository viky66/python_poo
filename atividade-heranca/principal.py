from animal import Animal, Mamifero, Reptil

cavalo = Animal("Spirit", 7)
cachorro = Mamifero("Taffy", 2)
lagarto = Reptil("Pascal", 4)

print("-"*50)
cavalo.exibirInfo()
cavalo.som("Neigh!")
print("-"*50)

cachorro.exibirInfo()
cachorro.som("Auau!")
cachorro.alimentarFilhotes()
print("-"*50)

lagarto.exibirInfo()
lagarto.som("Hiss!")
lagarto.mudarPele()