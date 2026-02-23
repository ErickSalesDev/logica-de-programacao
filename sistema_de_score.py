nome = input("Cliente: ")
salario = float(input("Salário: "))
score = float(input("Score: "))

if score < 300:
    print("Empréstimo negado. Score insuficiente.")
else:
    emprestimo = float(input("Valor do empréstimo: "))

    if score > 700:
        juros = 0.02
    else:
        juros = 0.05


    valor_com_juros = emprestimo + (emprestimo * juros)
    valor_total = valor_com_juros / 12
   
    if salario < valor_total:
        print("Empréstimo negado. Salário insuficiente para cobrir a parcela.")
    else:
        print("Cliente: ", nome)
        print("Empréstimo aprovado!")
        print("Juros:", juros * 100, "%")
        print("Valor da parcela mensal: R$", round(valor_total, 2))
