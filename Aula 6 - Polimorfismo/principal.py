from produto import Produto, Eletronico

prod1 = Produto(" Armário", 776.12)
eletron1 = Eletronico("Smartphone", 899, 200)

prod1.descrever()
prod1.calcularDesconto(30)

eletron1.descrever()
eletron1.calcularDesconto(30)