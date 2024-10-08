from restaurante import Servico
servico1 = Servico(20)
    
#métodos
print("Quantidade de pedidos: ", servico1.exibirPedido())
servico1.novoPedido()

print("Quantidade de pedidos após novo pedido: ", servico1.exibirPedido())
servico1.cancelarPedido()

print("Quantidade de pedidos após cancelamento: ", servico1.exibirPedido())
servico1.cancelarPedido()