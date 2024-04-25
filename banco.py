menu = " menu ".center(30, '#')
menu =f"""


{menu}
    [d] depositar
    [s] sacar
    [e] extrato
    [q] Sair
: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0

LIMITE_SAQUES = 3


while True:
    opcao = input(menu)

    if opcao.lower() == "d":
        valor = float(input("Informe o valor do deposito: "))
       
        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f}\n"
        else:
           print("Operação falhou! o valor informar é invalido")
           
    elif opcao.lower() == "s":
        if numero_saques >= 3 :
            print("Você atingiu o limite números de saque.")
            continue
        
        valor = float(input("Informe o valor do saque: "))
        if not valor > 0:
            print ("Se tu querer depositar escolha a opção correta :/")
        elif valor > limite:
            print (f"Você não pode realizar saques acima de R$ {limite:.2f}.")
        
        elif valor > saldo:
            print("Você não tem essa grana para sacar")
        else:
            saldo -= valor
            numero_saques += 1
            extrato +=f"Saque R$ {valor:.2f}\n"
            print(f"Você sacou R$ {valor:.2f}\n")
            
    elif opcao.lower() == "e":
        print( " Extrato bancário ".center(30,'#'))
        print(extrato)
        print(f""" *** Saldo atual: {saldo:.2f} """)
        
    elif opcao.lower() == "q":
        print("""
            Obrigado por utilizar o banco python.
            Até breve! """)
        break
    
    else:
        print("Opçõa invalida!")
        