nome = input("cliente: ")
idade = int(input("idade: "))

if idade < 18:
    responsavel = input("Tem responsável?: ")
    if responsavel == "não":
        print("Conta negada")
    else:
        cpf = str(input("cpf: "))
        if len(cpf) < 11:
            print("Conta negada. Cpf inválido")
        else:
            renda_mensal = float(input("Renda mensal: "))
            if renda_mensal < 500:
                print("Conta junivel poupança aprovada. responsável necessário")
            else:
                print("Conta junivel corrente aprovada. responsável necessário")
            
else:
    cpf = str(input("cpf: "))
    if len(cpf) < 11:
        print("Conta negada. Cpf inválido")
    else:
        renda_mensal = float(input("Renda mensal: "))
        if renda_mensal < 500:
            print("Conta poupança aprovada")
        else:
            print("Conta corrente aprovada")