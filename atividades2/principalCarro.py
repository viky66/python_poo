from carro import Carro

carro1 = Carro("BWM", "BMW. X1.", 2015, 200.00)
carro1.exibirDetalhes()

dias = 5
total = carro1.calcularPrecoAluguel(dias)
print(f"O total de {dias} dias será: R$ {total:}")

carro2 = Carro("Chevrolet", "Equinox 2024", 2010, 400.00)
carro2.exibirDetalhes()

dias = 10
total = carro2.calcularPrecoAluguel(dias)
print(f"O total de {dias} dias será: R$ {total:}")