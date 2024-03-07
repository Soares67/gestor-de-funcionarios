import pyodbc

def create(nome, data_nascimento, email, cargo, salario, data_admissao, status_emprego):
    #Cria a conexão
    dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                "Server=localhost;"
                "Database=db_funcionarios.db")
    conexao = pyodbc.connect(dados_conexao)

    cursor = conexao.cursor()

    cursor.execute(f"""
INSERT INTO funcionarios ('Nome', 'Data de Nascimento', 'Email', 'Cargo', 'Salario', 'Data Admissao', 'Status de emprego')
VALUES
("{nome}", "{data_nascimento}", "{email}", "{cargo}", {salario}, "{data_admissao}", "{status_emprego}")
""")

    cursor.commit()

    cursor.close()


def read(nome=None):
    #Define o tipo da busca
    if nome is None:
        busca = f"SELECT * FROM funcionarios"
    elif nome is not None:
        busca = f"SELECT * FROM funcionarios Where [Nome] = '{nome}'"

    #Cria a conexão
    dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                "Server=localhost;"
                "Database=db_funcionarios.db")
    conexao = pyodbc.connect(dados_conexao)

    cursor = conexao.cursor()

    cursor.execute(busca)

    dados = cursor.fetchall()
    cursor.close()
    return dados


print(read("Santt"))
