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
                    "Database=gerenciador.db")
            conexao = pyodbc.connect(dados_conexao)

            cursor = conexao.cursor()
            cursor.execute("UPDATE admins SET [Codigo Temporario] = ? WHERE Email = ? AND Usuario = ?", (code, email, user))
            cursor.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False

    if create_code():
        send_mail()
