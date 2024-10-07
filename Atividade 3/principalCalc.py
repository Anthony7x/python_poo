from calculadora import Calculadora

print(f"\nCALCULADORA 3000\n")
print(f"Informe dois números para verificar o resultado de suas 5 operações\n")

num1 = float(input("Informe o número 1: "))
num2 = float(input("Informe o número 2: "))

contagem = Calculadora(num1, num2)

contagem.montante()
contagem.abatimento()
contagem.proliferacao()
contagem.desmembramento()
contagem.aprimoramento()

valor = int(input(f"\nInforme um valor para verificar se é par ou ímpar: "))
contagem.verificaParImpar(valor)


class Celular:
    def __init__(self, numero, plano = "pré-pago" , saldo = 0, valorMinuto = 1.50):
        self.__numero = numero
        self.__plano = plano
        self.__saldo = saldo
        self.__valorMinuto = valorMinuto

    #Métodos usados para conseguir valores para os atributos privados
    def get_numero(self):
        return  self.__numero

   
    def set_plano(self, novo_plano):
        if novo_plano in ["pré-pago", "pós-pago"]:
            self.__plano = novo_plano
        else:
            print("Plano inválido. Escolha entre 'pré-pago' ou 'pós-pago'.")
        
    
    def get_saldo(self):
        return self.__saldo
    
     #Método para recarregar créditos (aplicável apenas para o plano pré-pago
    def recarregar(self,valor):
        if self.__plano == "pré-pago":
            self.__saldo += valor
        else:
            print("Recarga não disponível para planos pós-pagos.")

    #Mostra se a chamada será ou não efetuada dependendo do plano escolhido
    def fazerChamada(self,duracao_minutos):
        chamada = self.__valorMinuto * duracao_minutos
        if self.__plano == "pré-pago":
            if chamada > self.__saldo:
                print("Saldo insuficiente")
            else:
                print(f"Seu saldo atual é de {self.__saldo - chamada}")
        elif self.__plano == "pós-pago":
            print(f"No final do mês o valor total a pagar será de R${chamada - self.__saldo}")

    #exibe os dados do usuário
    def exibirDados(self):
        print(f"{self.__plano}: Você tem R${self.__saldo} válidos no número {self.__numero}")
