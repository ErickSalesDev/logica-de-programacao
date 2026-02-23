nome = input("Nome: ")
conta_bloqueada = input(("A conta está bloqueada?: ")).strip().lower()


if conta_bloqueada == "sim":
    print("Pagamento negado. Conta bloqueada.")
else:
    limite_internacional = input("Possui limite internacional?: ").strip().lower()
    if limite_internacional == "não":
        print("Pagamento negado. Cliente sem limite internacional")
    else:
        saldo_reais = float(input("Saldo em reais: "))
        valor_dolar = float(input("Valor em dólar: "))
        cotacao = float(input("Cotação atual: "))

        valor_convertido = valor_dolar * cotacao
        
        if valor_convertido > saldo_reais:
          print("Pagamento negado. Saldo insuficiente")
        else:
            if valor_dolar <= 500:
                taxa = 0.01
            else:
                taxa = 0.03
            print("Valor convertido:", valor_convertido)
            print("Taxa: ", taxa * valor_convertido)
            print("Total cobrado: ", valor_convertido + taxa * valor_convertido)
            print("Pagamento aprovado!")
           
            novo_saldo = saldo_reais - (valor_convertido + taxa * valor_convertido)
            print("Novo saldo: ", novo_saldo)