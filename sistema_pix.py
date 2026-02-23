nome = input("nome: ")
conta_bloqueada = input("A conta está bloqueada?: ")

if conta_bloqueada == "sim":
    print("Pagamento negado. Conta bloqueada")
else:
    saldo = float(input("Saldo: "))
    chave_pix = str(input("chave pix: "))
    if len(chave_pix) < 11:
        print("Pagamento negado. Chave pix inválida ( menos de 11 dígitos)")
    else:
        valor = float(input("Valor: "))
        if valor > saldo:
            print("Saldo insuficiente")
        else:
            novo_saldo = saldo - valor
            horário = int(input("Horário atual: "))
            if (horário >= 22 or horário < 6) and valor > 1000:
                print("Pagamento negado. Pix noturno limitado a R$ 1.000,00")
            else:
                print("Pagamento aprovado, o seu novo saldo é:", novo_saldo)