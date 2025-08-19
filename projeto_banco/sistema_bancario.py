import time

mensagem='''
Olá, seja bem vindo ao banco.
Escolha a opção desejada:

\033[1;30m[S] - Sacar
[D] - Depositar
[E] - Extrato
[Q] - Sair\033[0m
==>
'''

saldo = 0.00
saque_realizado = 0
saque_diario = 3
limite_maximo = 500.00
extrato = ""

while True:
    print(mensagem)
    escolha = str (input("Digite aqui para prosseguir: ")).upper()

    if escolha == "S":
        if saque_realizado == saque_diario:
            print("❌ Seu limite de saque acabou.")
            continue
        valor_saque = float(input("Digite o valor a sacar (máximo R$500): "))

        if valor_saque <= 0:
            print("\033[1;31m❌ Valor inválido.\033[0m")
            continue
        elif valor_saque > limite_maximo:
            print("\033[1;31m❌ O valor máximo de saque é R$500.\033[0m")
            continue
        elif valor_saque > saldo:
            print("\033[1;31m❌ Saldo insuficiente.\033[0m")
            continue
        else:
            saldo -= valor_saque
            saque_realizado += 1
            time.sleep(1)
            extrato += f"Saque:\nR${valor_saque:.2f}\n"
            print(f"\033[1;32m✅ Saque realizado.\033[0m")
            print(f"Saldo atual: R${saldo:.2f}")
            print(f"Você possui {saque_diario-saque_realizado} saques diários")
                    

    elif escolha == "D":
        valor_deposito = float (input("Digite o valor a ser depositado: R$"))
        if valor_deposito <= 0:
            print("\033[1;31m❌Valor inválido.\033[0m")
        else:
            saldo += valor_deposito
            extrato += f"Depósito:\nR$ {valor_deposito:.2f}\n"
            print(f"Depósito concluído.")
            print(f"Quantia depositada:\nR${valor_deposito:.2f}\n")
    
    elif escolha == "E":
        print("\n========= EXTRATO =========")
        if extrato.strip():
            print(extrato.strip())
        else:
            print("Nenhuma movimentação.")
        print(f"Saldo Atual: R${saldo:.2f}")
        print("============================\n")

    elif escolha == "Q":
        print("✅ Saindo... Obrigado por usar nosso banco!")
        break

    else:
        print("\033[1;31m❌ Operação inválida. Tente novamente.\033[0m")