from celular import Celular

# Criação de dois objetos Celular com números e planos diferentes
cliente1 = Celular(numero="123456789", plano="pré-pago")
cliente2 = Celular(numero="987654321", plano="pós-pago")

# Recarregar saldo para o cliente 1 (pré-pago)
cliente1.recarregar(50)

# Recarregar saldo para o cliente 2 (pós-pago) - não será aplicado
cliente2.recarregar(30)

# Fazer chamada de 10 minutos com o cliente 1 (pré-pago)
cliente1.fazerChamada(10)

# Fazer chamada de 5 minutos com o cliente 2 (pós-pago)
cliente2.fazerChamada(5)

# Exibir os dados após as chamadas
cliente1.exibirDados()
cliente2.exibirDados()
