def cadastrar_usuario():
    username = input("Digite o nome de usuário para cadastro: ")
    if username in usuarios:
        print("Usuário já existe!")
        return None  
    senha = input("Digite sua senha: ")
    email = input("Digite seu email: ")
    is_admin = input("O usuário é admin? (s/n): ").lower() == 's'
    if is_admin:
        mcs_inicial = 200000  
    else:
        mcs_inicial = 2500
    usuarios[username] = {
        "senha": senha, 
        "email": email, 
        "admin": is_admin, 
        "saldo_compras": [], 
        "MCs": mcs_inicial, 
        "carrinho": {}
    }
    print("Cadastro realizado com sucesso!")
    return login()

def login():
    username = input("Digite o nome de usuário: ")
    if username not in usuarios:
        print("Usuário não encontrado!")
        return None  
    senha = input("Digite sua senha: ")
    if usuarios[username]["senha"] == senha:
        print(f"Bem-vindo, {username}!")
        return {"username" : username, **usuarios[username]}  
    else:
        print("Senha incorreta!")
        return None

usuarios = {
    "admin": {
        "senha": "admin123", 
        "email": "admin@example.com", 
        "admin": True, 
        "saldo_compras": [], 
        "MCs": 0, 
        "carrinho": {}
    },
    "user1": {
        "senha": "userpass", 
        "email": "user1@example.com", 
        "admin": False, 
        "saldo_compras": [], 
        "MCs": 0, 
        "carrinho": {}
    }
}
