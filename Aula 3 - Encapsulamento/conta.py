class Conta:
    def __init__(self, numero, titular, saldo, limite):
        #Quando colocamos 2 underlines antes do atributo, indicamos que esse atributo está com a visibilidade  "privada", o contrário significa que está público
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def relatorio(self):
        print(f"Olá {self.__titular} seu saldo atual é R$ {self.__saldo} e o seu atual limite é R${self.__limite}")

    def getLimite(self):
        return self.__limite
    
    def setLimite(self, valor):
        if valor < 0 :
            print("Informe um valor válido: ")
        else:
            self.__limite = valor

    def depositar(self, valor):
        if valor <= 0:
            print("Informe um valor positivo")
        else:
            self.__saldo = self.__saldo + valor
    def sacar(self, valor):
        if valor <= 0 or valor > self.__saldo:
            print("Saldo insuficiente ou valor negativo soilicitado")
        else:
            self.__saldo -= valor