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


codigo = int(input("Informe o código do funcionário: "))

sql = "DELETE FROM funcionario  WHERE codigo = ?"

campos = (codigo,) #é preciso colocar uma virgula depois do item para configurar que temos um atupla, caso contrário não será aceito uma tupla válida.

consulta.execute(sql, campos)

conexao.commit()

print(consulta.rowcount, " linhas(s) deletada(s) com sucesso.")

conexao.close()
