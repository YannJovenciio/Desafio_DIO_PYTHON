contas=[]
def menu():
    menu = """
    ===================BANCO===================
    [1]Depósito
    [2]Saque
    [3]Extrato
    [4]Nova conta
    [5]Listar contas
    [6]Novo usuario
    [7]Sair
    =>
    """
    return input(menu)

def Deposito_bancario(deposito,saldo,extrato):
    
    if deposito > 0:
         saldo = (saldo + deposito)
         print("Depósito realizado com sucesso")
         print("saldo atual: R$", saldo)
         extrato += f"Depósito de R${deposito:.2f}\n"
    else:
         print("Valor inválido")
    return saldo, extrato

def Saque_bancario(*, saque,saldo,numero_saque,extrato,limites_saques,limite):

    saldo_excedido = saque > saldo
    limite_excedido = saque > limite
    saque_excedido = numero_saque >= limites_saques
    if saldo_excedido:
        print("Saldo insuficiente")
    elif limite_excedido:
        print("Limite de saques excedido")
    elif saque_excedido:
        print("Limite de saques excedido")
    elif saque > 0:
        saldo -= saque
        extrato += f"Saque: R${saque:.2f}\n"
        numero_saque += 1
        print("\nSaque realizado com sucesso! ===")
    else:
        print("Operação falhou, o valor informado é inválido")

    return saldo, extrato
    
def Extrato_bancario(saldo, /,*, extrato):
    
    print("\n ===================EXTRATO===================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n saldo: R$ {saldo:.2f}")
    print(" ============================================")

def Criar_usuario(Lista_usuarios):

    cpf=input("Digite seu CPF:  ")
    usuario= filtrar_usuario(cpf,Lista_usuarios)

    if usuario:
        print("Usuário já cadastrado")
        return
    
    Nome=input("Digite seu nome:  ")
    DataN=input("Digite sua data de nascimento:  ")
    Endereco=input("Digite seu logradouro,Bairro,cidade,sigla estado:  ")
        
    Lista_usuarios.append({"nome": Nome, "data_nascimento": DataN, "cpf": cpf, "endereco": Endereco})
    
    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf,Lista_usuarios):
    usuarios_filtrados = [usuario for usuario in Lista_usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
def criar_conta(agencia,numero_conta,Lista_usuarios):
    cpf=input("Digite seu CPF:  ")
    usuario=filtrar_usuario(cpf,Lista_usuarios)

    if usuario:
        print("Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n Usuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    
    for conta in contas:
        print("=" * 50)
        print(f"Agência: {conta['agencia']}")
        print(f"Número da Conta: {conta['numero_conta']}")
        print(f"Titular: {conta['usuario']['nome']}")
        print(f"CPF: {conta['usuario']['cpf']}")
        print(f"Endereço: {conta['usuario']['endereco']}")
        print("=" * 50)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    Lista_usuarios = []
    
    


    while True:
        opcao = menu()
        if opcao == "1":
            deposito = float(input("Digite o valor do depósito: "))
            saldo, extrato = Deposito_bancario(deposito, saldo, extrato)

        elif opcao == "2":
            saque = float(input("Digite o valor do saque: "))

            saldo,extrato = Saque_bancario(
                saque=saque,
                saldo=saldo,
                numero_saque=numero_saques,
                extrato=extrato,
                limites_saques=LIMITE_SAQUES,
                limite=limite,
            )

        elif opcao =="3":
            Extrato_bancario(saldo, extrato=extrato)

        elif opcao == "4":
            numero_conta = len(contas)+1
            conta=criar_conta(AGENCIA,numero_conta,Lista_usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            Criar_usuario(Lista_usuarios)

        elif opcao == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida")



main()