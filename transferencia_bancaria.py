nome = input("Nome: ")
saldo = float(input("Saldo atual: "))
seguranca = input("A sua conta está bloqueada?: ")

if seguranca == "sim":
    print("Transferência negada. Conta bloqueada")
else:
    valor = float(input("Valor da transferência: "))
    if valor > saldo:
        print("Transferência negada. Saldo insuficiente")
    else:
       if valor > 5000:
          senha = (input("Senha: "))
          if senha == "4321":
            novo_saldo = saldo - valor
            print("Transferência aprovada!")
            print("Novo saldo:", novo_saldo)
          else:
            print("Transferência negada. Senha incorreta.")
       else:
            novo_saldo = saldo - valor
            print("Transferência aprovada!")
            print("Novo saldo:", novo_saldo)