menu = """
[1]Depósito
[2]Saque
[3]Extrato
[4]Sair
=>
"""

saldo = float(0)
limite= 500
extrato = ""
numero_saque=0
LIMITE_SAQUE=3

while True:

    opcao = input(menu)

    if opcao == "1":
        deposit=float(input("Digite o valor do depósito: "))

        if deposit > 0:
            saldo = (saldo + deposit)
            print("Depósito realizado com sucesso")
            print('Saldo atual: R$', saldo)
            extrato += f"Depósito de R${deposit:.2f}\n"
        else:
            print("Valor inválido")
        


    elif opcao == "2":

        valor = float(input("Digite o valor do saque: "))

        saldo_excedido = valor > saldo

        limite_excedido = numero_saque >= LIMITE_SAQUE

        saque_excedido = numero_saques >= LIMITE_SAQUE

        if saldo_excedido:
            print("Saldo insuficiente")
        elif limite_excedido:
            print("Limite de saques excedido")
        elif saque_excedido:
            print("Limite de saques excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saque += 1
        else:
            print("Operação falhou,o valor informado é inválido")

    elif opcao =="3":
        
        print("\n ===================EXTRATO===================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n saldo: R$ {saldo:.2f}")
        print(" ============================================")


        


    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida")


