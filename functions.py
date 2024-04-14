import messagebox as msg
import config
import string


#Abre/Fecha um frame
def open_close_frame(botao, states):
    """Expande/Encolhe um frame
    
    Args:
        botao (tk.Button): Botão que fará a ação
        states (dict): dicionário com o formato: {tk.Frame: "epanded/reduced"}
    """
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
    """Checa se duas senhas se coincidem
    
    Args:
        senha1 (str): Primeira senha
        senha2 (str): Segunda senha
    
    Returns:
        bool
    """
    if senha1 == senha2:
        return True
    else:
        return False

#Verifica se as senhas atendem aos requisitos
def check_req(senha1, senha2):
    """Checa se duas senhas possuem no mínimo 8 dígitos
    
    Args:
        senha1 (str): Primeira senha
        senha2 (str): Seguinda senha

    Returns:
        bool
    """
    if len(senha1) >= 8 and len(senha2) >= 8:
        return True
    else:
        return False

#Verifica se um campo atende os requisitos
def check_field(field, min_len):
    """Checa se um campo possui a qtde mínima de dígitos
    
    Args:
        field (tkinter.Entry): Campo que será checado
        min_len (int): Quantidade mínima de caracteres
    
    Returns:
        bool
    """
    if len(field) >= min_len:
        return True
    else:
        return False

# Checa um campo de nomes
def check_name(name):
    """Verifica se um nome está em um formato válido.

    Args:
        name (str): O nome a ser verificado.

    Returns:
        bool: True se o nome estiver em um formato válido, False caso contrário.
    """
    if name:  # Não pode estar em branco
        if len(name.strip()) >= 5:  # No mínimo 5 dígitos
            if len(name.split()) >= 2:  # No mínimo 2 palavras (deve ser composto)
                return True
            else:
               msg.showwarning("Erro", "O nome deve ter pelo menos duas palavras.")
               return False
        else:
            msg.showwarning("Erro", "O nome deve ter no mínimo 5 caracteres.")
            return False
    else:
        msg.showwarning("Erro", "O nome não pode estar em branco.")
        return False
            
# Checa um campo de datas com regras específicas
def check_date(date):
    """Verifica se a data fornecida está no formato válido (DD/MM/AAAA) e se está dentro dos limites permitidos.

    Args:
        date (str): A data no formato DD/MM/AAAA a ser verificada.

    Returns:
        bool: True se a data estiver no formato válido e dentro dos limites permitidos, False caso contrário.
    """
    if date:  # Não pode estar em branco
        if len(date.split("/")) == 3:  # DD/MM/AAAA
            if date.count("/") == 2:  # 2 barras
                if len(date.split("/")[0]) == 2:  # Dois dígitos no dia
                    if len(date.split("/")[1]) == 2:  # Dois dígitos no mês
                        if len(date.split("/")[2]) == 4:  # Quatro dígitos no ano
                            if int(date.split("/")[0]) <= 31:  # Dia deve ser no máximo 31
                                if int(date.split("/")[1]) == 2 and int(date.split("/")[0]) <= 29 or int(date.split("/")[0]) <= 28:  # Fevereiro
                                    if int(date.split("/")[1]) <= 12:  # Mês deve ser no máximo 12
                                        if int(date.split("/")[2]) >= int(config.timenow()[6:10]) - 70:  # funcionário deve ter no máximo 70 anos
                                            return True
                                        else:
                                            msg.showwarning("Erro", "A idade máxima é de 70 anos")
                                            return False
                                    else:
                                        msg.showwarning("Erro", "O mês deve ser no máximo 12")
                                        return False
                                else:
                                    msg.showwarning("Erro", "Data inválida para fevereiro")
                                    return False
                            else:
                                msg.showwarning("Erro", "O dia deve ser no máximo 31")
                                return False
                        else:
                            msg.showwarning("Erro", "O ano deve ter 4 dígitos")
                            return False
                    else:
                        msg.showwarning("Erro", "O mês deve ter 2 dígitos")
                        return False
                else:
                    msg.showwarning("Erro", "O dia deve ter 2 dígitos")
                    return False
            else:
                msg.showwarning("Erro", "Data deve estar no formato DD/MM/AAAA")
                return False
        else:
            msg.showwarning("Erro", "Data deve estar no formato DD/MM/AAAA")
            return False
    else:
        msg.showwarning("Erro", "O campo deve estar preenchido")
        return False


def check_email(email):
    SERVERS = [
    "gmail.com",
    "outlook.com",
    "yahoo.com",
    "icloud.com",
    "aol.com",
    "hotmail.com"
]
    if email:  # Não pode estar em branco
        if len(email) >= 15:  # No mínimo 15 dígitos
            if email.endswith(".com"):
                # Verifica se a local part do email é válida
                for i in email.split("@")[0]:
                    if i in string.ascii_lowercase or i in string.ascii_uppercase or i in string.digits or i == ".":
                        pass
                    else:
                        msg.showwarning("Erro", "O email digitado possui dígitos inválidos")
                        return False
                # Verifica se o servidor do email é válido
                valido = False  # Variável de controle
                for server in SERVERS:
                    if server in email:
                        valido = True
                        break
                if valido:
                    return True
                else:
                    msg.showwarning("Erro", "O servidor do email é inválido")
                    return False
                
            else:
                msg.showwarning("Erro", "O email deve terminar com (.com)")
                return False
        else:
            msg.showwarning("Erro", "O email deve ter no mínimo 15 dígitos")
            return False
    else:
        msg.showwarning("Erro", "O email não pode estar em branco")
        return False




email = "santtdev@gmail.com"
check_email(email=email)