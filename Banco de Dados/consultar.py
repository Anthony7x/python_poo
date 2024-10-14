import sqlite3

#Passo 1 - Conexão com o banco
conexao = sqlite3.connect('departamento.db')

#Passo 2 - Verificar se a tabela existe ou não
tabela = """
    CREATE TABLE IF NOT EXISTS funcionario(
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    salario FLOAT,
    cargo VARCHAR(100)
);
"""
#Passo 3 - Acessar o objeto cursor() da biblioteca sqlite3, para manipular dados do banco
consulta = conexao.cursor()

#Passo 4 - Executar o comando de criação da tabela
consulta.execute(tabela)

#Passo 5 - Criando comando SQL para consultar os dados na tabela
sql = "SELECT * FROM funcionario"

#Passo 6 - Executar o comando sql 
consulta.execute(sql)

print(consulta.rowcount, "linha(s) inseridas com sucesso")

#Passo 7 - Exibir dados da tabela
resultado  = consulta.fetchall() #fetchall() irá trazer todos os registros que existem na tabela do banco de dados

for itens in resultado:
    print(f"Código: {itens[0]}, Nome: {itens[1]}")

#Passo 10 - Encerrar a conexão
conexao.close()
