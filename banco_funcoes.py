saldo=0
historico=[]

def senha():
    senha_criar = int(input("Crie sua senha: "))
    if len(str(senha_criar)) < 4:
        print("Senha invalida")
    else:
        print("Senha criada")
        return senha_criar

def login():
    print("Faça login")
    login=int(input("Digite sua senha: "))
    return login

def menu():
    print("---BANCO---")
    print("[1] DEPOSITAR ")
    print("[2] SACAR ")
    print("[3] VER SALDO ")
    print("[4] VER HISTÓRICO ")
    print("[5] SAIR ") 

def ver_saldo():
    global saldo
    print("Ver saldo selecionado")
    print(f"O saldo atual é de: {saldo}")

def depositar():
    global saldo
    print("Deposito selecionado")
    valor_deposito=float(input("Insira o valor a ser depositado: "))
    if valor_deposito <= 0:
        print("Valor invalido")
    else:
        saldo += valor_deposito
        historico.append(f"Depósito: {valor_deposito}")
        print(f"O valor de: {valor_deposito} foi depositado, operação salva no histórico")

def sacar():
    global saldo
    print("Saque selecionado: ")
    valor_saque=float(input("Insira o valor a ser sacado: "))
    if valor_saque <= 0:
        print("Valor invalido")
    elif valor_saque > saldo:
        print("Saque maior que o saldo")
    else:
        saldo -= valor_saque
        historico.append(f"Saque: {valor_saque}")
        print(f"O valor de: {valor_saque} foi retirado, operação salva no histórico")

def ver_historico():
    print("Ver histórico selecionado")
    if len(historico)==0:
        print("Nenhuma operação registrada")
    else:
        for operacao in historico:
            print(operacao)

def sair():
    print("Sair selecionado")
    sair_sis=int(input("Digite a senha para sair"))
    return sair_sis
                  
