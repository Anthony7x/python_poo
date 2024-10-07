from conta import Conta

minhaConta = Conta(321, "Jefferson de Costa", 200000, 1000)

minhaConta.relatorio()

minhaConta.setLimite(2500)
minhaConta.relatorio()

print(f"O seu limite atual é de {minhaConta.getLimite()}")

minhaConta.depositar(500)
minhaConta.relatorio()

minhaConta.sacar(100)
minhaConta.relatorio()