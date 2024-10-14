import sqlite3

#Passo 1 - Estabelecendo a conexão
conexao = sqlite3.connect('departamento.db')

#Passo - Acessar o banco de dados
consulta = conexao.cursor()

#Passo 3 - Criar a tabela
tabela = """
    CREATE TABLE IF NOT EXISTS funcionario(
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    salario FLOAT,
    cargo VARCHAR(100)
);
"""
#Passo 4 - Executar o comando para criação da tabela
consulta.execute(tabela)

#Passo 5 - Criação de novas informações para atualizar o banco
nome = input("Informe o novo nome do funcionário: ")
codigo = int(input("Informe o código do funcionário: "))

sql = "UPDATE funcionario SET nome = ? WHERE codigo = ?"

campos = (nome, codigo)

consulta.execute(sql, campos)

conexao.commit()

print(consulta.rowcount, " linhas(s) atualizada(s) com sucesso.")

conexao.close()
