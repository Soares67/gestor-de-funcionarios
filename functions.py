import messagebox as msg
import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from private import APP_KEY, MAIL


#Abre/Fecha um frame
def open_close_frame(botao, states):
        if states[botao.name][1] == "reduced":
            m_frame = states[botao.name][0]
            m_frame.configure(width=1380)
            states[botao.name][1] = "expanded"
            for i in states:
                if states[i][0] != m_frame and states[i][1] == "expanded":
                    states[i][0].configure(width=1)
                    states[i][1] = "reduced"
                else:
                    pass
        elif states[botao.name][1] == "expanded":
            m_frame = states[botao.name][0]
            m_frame.configure(width=1)
            states[botao.name][1] = "reduced"

#Verifica se duas senhas se coincidem     
def check(senha1, senha2):
    if senha1 == senha2:
        return True
    else:
        return False

#Verifica se as senhas tendem aos requisitos
def check_req(senha1, senha2):
    if len(senha1) >= 8 and len(senha2) >= 8:
        return True
    else:
        return False

#Verifica se um campo atende os requisitos
def check_field(field, min_len):
    if len(field) >= min_len:
        return True
    else:
        return False

def insert(where):
    text = """Nome: John Doe

E-mail: john@gmail.com

Último acesso: 21/03/2024 16:12:38"""
    where.delete("0.0", "end")
    where.insert("0.0", text)

def generate_token():
    """Gera um token único de redefinição de senha

    Returns:
        Código de 5 dígitos alfanumérico
    
    """
    return "".join(random.choices(string.ascii_letters.upper() + string.digits, k=5))

def send_mail(dest):
    # Configurações do servidor SMTP do Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Porta para conexão TLS
    sender_email = MAIL  # Seu e-mail do Gmail
    sender_password = APP_KEY   #senha do Gmail

    # Destinatário e corpo do e-mail
    recipient_email = dest
    subject = 'Redefinição de senha'
    body = f'<p>Seu código de redefinição de senha é: <b>{generate_token()}</b></p>'

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

send_mail()