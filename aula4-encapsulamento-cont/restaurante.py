class Servico:
    def __init__(self, pedido = 0):
        self.__pedido = pedido #armazena numero de pedidos

    def novoPedido(self):
        self.__pedido += 1 #toda vez que é chamado adiciona 1 pedido

    def cancelarPedido(self):
        if self.__pedido > 0:
            self.__pedido -= 1  #decrementa
        else:
            print("Não tem pedido para cancelar")

    def exibirPedido(self):
        return self.__pedido
