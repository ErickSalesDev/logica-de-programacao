nome = input("Nome: ")
conta_bloquada = input("A sua conta está bloqueada?: ")


if conta_bloquada == "sim":
    print("Resultado: Saque negado. Conta bloqueada.")
else:
   saldo_atual = float(input("Saldo atual: "))
   valor_do_saque = float(input("Valor do saque: "))
   if valor_do_saque < saldo_atual:
      novo_saldo = saldo_atual - valor_do_saque
      print("Resultado: Saque aprovado! Seu novo saldo é", novo_saldo) 
   else:
      print("Saque negado. Saldo insuficiente.")
