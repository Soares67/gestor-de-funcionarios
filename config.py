import bcrypt
import pyodbc
from datetime import datetime
import pytz


#Todos as funções dos CRUDs necessários para o sistema


#Cria um usuário
def create_user(nome, data_nascimento, email, cargo, salario, data_admissao, status_emprego):
    #Cria a conexão
    dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                "Server=localhost;"
                "Database=gerenciador.db")
    conexao = pyodbc.connect(dados_conexao)

    cursor = conexao.cursor()

    cursor.execute(f"""
INSERT INTO funcionarios ('Nome', 'Data de Nascimento', 'Email', 'Cargo', 'Salario', 'Data Admissao', 'Status de emprego')
VALUES
("{nome}", "{data_nascimento}", "{email}", "{cargo}", {salario}, "{data_admissao}", "{status_emprego}")
""")

    cursor.commit()

    cursor.close()

#Lê o banco de dados
def read_user(nome=None):
    #Define o tipo da busca
    if nome is None:
        busca = f"SELECT * FROM funcionarios"
    elif nome is not None:
        busca = f"SELECT * FROM funcionarios Where [Nome] = '{nome}'"

    #Cria a conexão
    dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                "Server=localhost;"
                "Database=gerenciador.db")
    conexao = pyodbc.connect(dados_conexao)

    cursor = conexao.cursor()

    cursor.execute(busca)

    dados = cursor.fetchall()
    cursor.close()
    return dados

#Cria um admin
def create_admin(nome, user, senha, email, ultimo_acesso):
    #Cria a conexão
    dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                "Server=localhost;"
                "Database=gerenciador.db")
    conexao = pyodbc.connect(dados_conexao)

    cursor = conexao.cursor()

    cursor.execute(f"""
INSERT INTO admins ('Nome', 'Usuario', 'Senha', 'Email', 'Ultimo Acesso')
VALUES
("{nome}", "{user}", "{hash_password(senha)}", "{email}", "{ultimo_acesso}")
""")

    cursor.commit()

    cursor.close()

#Deleta um admin
def delete_admin(user, email):

    #Cria a conexão
    dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                "Server=localhost;"
                "Database=gerenciador.db")
    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM admins WHERE Usuario = ? AND Email = ?", (user, email))

    cursor.commit()
    cursor.close()

#Autentica um admin
def auth_admin(login, password):

    #Conexão com o banco de dados
    dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                "Server=localhost;"
                "Database=gerenciador.db")
    conexao = pyodbc.connect(dados_conexao)

    cursor = conexao.cursor()

    cursor.execute(f"SELECT Senha FROM admins WHERE Usuario = ? OR Email = ?", (login, login))
    resultado = cursor.fetchone()  #Resultado da busca
    cursor.close()

    #Checagem dos dados
    def autenticar():
        if resultado:
            senha = resultado.Senha
            if bcrypt.checkpw(password.encode("utf-8"), senha.encode("utf-8")):
                return True
        return False
    
    #Autenticação
    if autenticar():
        return True
    else:
        return False


def hash_password(password):
    """Criptografa a senha determinada

    Args:
        password (str): Senha que será criptografada
    
    Returns:
        Senha criptografada
    
    """
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')


def timenow():
    """Pega a data e hora atuais

    Returns:
        data e hora formatados
    """
    fuso_br = pytz.timezone("America/Sao_Paulo")
    return datetime.now(fuso_br).strftime("%d/%m/%Y %H:%M:%S")

