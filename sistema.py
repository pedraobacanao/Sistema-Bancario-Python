import banco_funcoes
tentativas=0
senha_salva=banco_funcoes.senha()
while True:
    login_salvo=banco_funcoes.login()
    if senha_salva!=login_salvo:
        print(f"Senha inválida, tentativas: {tentativas+1}")
        tentativas +=1
        if tentativas==3:
            break
    elif senha_salva==login_salvo:
        banco_funcoes.menu()
        acao=int(input("Digite sua ação: "))
        if acao==1:
            banco_funcoes.depositar()
        elif acao==2:
            banco_funcoes.sacar()
        elif acao==3:
            banco_funcoes.ver_saldo()
        elif acao==4:
            banco_funcoes.ver_historico()
        elif acao==5:
            sair=banco_funcoes.sair()
            if senha_salva==sair:
                print("Saindo...")
                break
            else:
                print("Senha incorreta")
                continue
        else:
            print("Ação inválida")
            
