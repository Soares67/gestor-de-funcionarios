import bcrypt
import pyodbc
from datetime import datetime
import pytz
import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from private import APP_KEY, MAIL


#Todos as funções dos CRUDs necessários para o sistema


#Cria um usuário
def create_user(nome, data_nascimento, genero, email, area, cargo, salario, data_admissao, status_emprego):
    """Cadastra um funcionário no banco de dados

    Args:
        nome (str): Nome do funcionário
        data_nascimento (str): Data de nascimento do funcionario no formato DD/MM/AAAA
        genero (str): Gênero do funcionário, podendo ser (Masculino/Feminino/Outros)
        email (str): Email do funcionário
        area (str): Área de atuação do funcionário
        cargo (str): Cargo do funcionário
        salario (int/float): Salário do funcionário
        data_admissao (str): Data de admissão do funcionário no formato DD/MM/AAAA H:M:S
        status_emprego (str): Status de emprego do funcionário (empregado/afastado/aposentado)
    """
    #Cria a conexão
    dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                "Server=localhost;"
                r"Database=DB\gerenciador.db")
    conexao = pyodbc.connect(dados_conexao)

    cursor = conexao.cursor()

    cursor.execute(f"""
INSERT INTO funcionarios ('Nome', 'Data Nascimento', 'Genero', 'Email', 'Area', 'Cargo', 'Salario', 'Data Admissao', 'Status Emprego')
VALUES
("{nome}", "{data_nascimento}", "{genero}", "{email}", "{area}", "{cargo}", {salario}, "{data_admissao}", "{status_emprego}")
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
                r"Database=DB\gerenciador.db")
    conexao = pyodbc.connect(dados_conexao)

    cursor = conexao.cursor()

    cursor.execute(busca)

    dados = cursor.fetchall()
    cursor.close()
    return dados

#Cria um admin
def create_admin(nome, user, senha, email, ultimo_acesso):
    """Cadastra um administrador no banco de dados

    Args:
        nome (str): Nome do administrador
        user (str): Nome de usuário do administrador (Usado para fazer login)
        senha (str): Senha do administrador
        email (str): E-mail do administrador
        ultimo_acesso (str): último acesso do administrador no formato DD/MM/AAAA H:M:S
    """
    #Cria a conexão
    dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                "Server=localhost;"
                r"Database=DB\gerenciador.db")
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
                r"Database=DB\gerenciador.db")
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
                r"Database=DB\gerenciador.db")
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

#Criptografa uma determinada senha
def hash_password(password):
    """Criptografa a senha determinada

    Args:
        password (str): Senha que será criptografada
    
    Returns:
        Senha criptografada
    
    """
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')

#Pega data e hora atuais
def timenow():
    """Pega a data e hora atuais

    Returns:
        data e hora formatados
    """
    fuso_br = pytz.timezone("America/Sao_Paulo")
    return datetime.now(fuso_br).strftime("%d/%m/%Y %H:%M:%S")

#Cria um código de recuperação, atribui ao BD e envia por e-mail
def recover_pass(email, user):
    code = "".join(random.choices(string.ascii_letters.upper() + string.digits, k=5))  # Cria o código de recuperação
    def send_mail():
        # Configurações do servidor SMTP do Gmail
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # Porta para conexão TLS
        sender_email = MAIL  # Seu e-mail do Gmail
        sender_password = APP_KEY   #senha do Gmail

        # Destinatário e corpo do e-mail
        recipient_email = email
        subject = 'Redefinição de senha'
        body = f'<p>Seu código de redefinição de senha é: <b>{code}</b></p>'

        # Criar mensagem
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'html'))

        # Conectar ao servidor SMTP do Gmail e enviar e-mail
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Habilitar TLS
            server.login(sender_email, sender_password)
            text = message.as_string()
            server.sendmail(sender_email, recipient_email, text)
            print('E-mail enviado com sucesso!')
        except Exception as e:
            print(f'Erro ao enviar e-mail: {str(e)}')
        finally:
            server.quit()  # Encerrar conexão com o servidor SMTP

    def create_code():
        try:
            dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                    "Server=localhost;"
                    r"Database=DB\gerenciador.db")
            conexao = pyodbc.connect(dados_conexao)

            cursor = conexao.cursor()
            cursor.execute("UPDATE admins SET [Codigo Temporario] = ? WHERE Email = ? AND Usuario = ?", (code, email, user))
            cursor.commit()
            cursor.close()
            conexao.close()
            return True
        except Exception as e:
            print(e)
            return False

    if create_code():
        send_mail()

#Verifica se um email está no BD
def verify_email(email):
    #Conexão com o banco de dados
    dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                "Server=localhost;"
                r"Database=DB\gerenciador.db")
    conexao = pyodbc.connect(dados_conexao)

    cursor = conexao.cursor()

    cursor.execute(f"SELECT Email FROM admins WHERE Email = ?", (email))
    resultado = cursor.fetchone()  #Resultado da busca
    cursor.close()
    conexao.close()

    if resultado is not None:
        return True
    else:
        return False

#Verifica se o usuário corresponde ao email inserido
def verify_user(email, user):
    #Conexão com o banco de dados
    dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                "Server=localhost;"
                r"Database=DB\gerenciador.db")
    conexao = pyodbc.connect(dados_conexao)

    cursor = conexao.cursor()

    cursor.execute(f"SELECT Usuario FROM admins WHERE Email = ? AND Usuario = ?", (email, user))
    resultado = cursor.fetchval()  #Resultado da busca
    cursor.close()
    conexao.close()

    if resultado is not None:
        return True
    else:
        return False

#Verifica se o código inserido corresponde ao recebido por email
def verify_code(email, user, entry_code):
    #Conexão com o banco de dados
    dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                "Server=localhost;"
                r"Database=DB\gerenciador.db")
    conexao = pyodbc.connect(dados_conexao)

    cursor = conexao.cursor()

    cursor.execute(f"SELECT [Codigo Temporario] FROM admins WHERE Email = ? AND Usuario = ?", (email, user))
    resultado = cursor.fetchval()  #Resultado da busca
    cursor.close()

    if entry_code == resultado:
        return True
    else:
        return False

#Redefine a senha de admin
def update_pass(email, user, nova_senha):
    try:
        #Conexão com o banco de dados
        dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                    "Server=localhost;"
                    r"Database=DB\gerenciador.db")
        conexao = pyodbc.connect(dados_conexao)

        cursor = conexao.cursor()

        cursor.execute("UPDATE admins SET Senha = ? WHERE Email = ? AND Usuario = ?", (hash_password(nova_senha), email, user))

        cursor.commit()

        cursor.close()
        conexao.close()
        return True
    except Exception as e:
        print(e)
        return False

#Atualiza a data e hora do ultimo acesso do administrador
def update_last_access(login, senha):
    dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                    "Server=localhost;"
                    r"Database=DB\gerenciador.db")
    conexao = pyodbc.connect(dados_conexao)

    cursor = conexao.cursor()
    cursor.execute("UPDATE admins SET [Ultimo Acesso] = ? WHERE Usuario = ? or Email = ? AND Senha = ?", (timenow(), login, login, hash_password(senha)))
    cursor.commit()
    cursor.close()
    conexao.close()

#Pega as informações de um administrador
def get_admin_info(user, email):
     #Conexão com o banco de dados
    dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                "Server=localhost;"
                r"Database=DB\gerenciador.db")
    conexao = pyodbc.connect(dados_conexao)

    cursor = conexao.cursor()

    cursor.execute(f"SELECT Nome, Email, [Ultimo Acesso] FROM admins WHERE Usuario = ? AND Email = ?", (user, email))
    resultado = cursor.fetchall()  #Resultado da busca
    cursor.close()
    conexao.close()
    texto = f"""Nome: {resultado[0][0]}

E-mail: {resultado[0][1]}

Último acesso: {resultado[0][2]}"""
    return texto

#Exclui um administrador
def delete_admin(user, email):
    dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                "Server=localhost;"
                r"Database=DB\gerenciador.db")
    conexao = pyodbc.connect(dados_conexao)

    cursor = conexao.cursor()
    cursor.execute("DELETE FROM admins WHERE Usuario = ? AND Email = ?", (user, email))

    cursor.commit()

    if cursor.rowcount > 0:
        cursor.close() 
        conexao.close()
        return True
    else:
        cursor.close() 
        conexao.close()
        return False

#Exclui o código temporário do BD
def del_code(email, user):
    dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                "Server=localhost;"
                r"Database=DB\gerenciador.db")
    conexao = pyodbc.connect(dados_conexao)

    cursor = conexao.cursor()
    cursor.execute("UPDATE admins SET [Codigo Temporario] = NULL WHERE Email = ? AND Usuario = ?", (email, user))

    cursor.commit()
    cursor.close()
    conexao.close()

def get_funcionarios():
    #Conexão com o banco de dados
    dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                "Server=localhost;"
                r"Database=DB\gerenciador.db")
    conexao = pyodbc.connect(dados_conexao)

    cursor = conexao.cursor()

    cursor.execute(f"SELECT Nome FROM funcionarios")
    resultado = cursor.fetchall()  #Resultado da busca
    cursor.close()
    conexao.close()
    return [resultado[i][0] for i, row in enumerate(resultado)]
