import messagebox as msg



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

#Insere um texto em uma textbox
def insert(where):
    """Insere um texto em um textbox

    Args:
        where (Textbox): Campo em que o texto será inserido
    """
    text = """Nome: John Doe

E-mail: john@gmail.com

Último acesso: 21/03/2024 16:12:38"""
    where.delete("0.0", "end")
    where.insert("0.0", text)
