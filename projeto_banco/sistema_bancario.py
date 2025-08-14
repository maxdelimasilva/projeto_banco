mensagem='''
Olá, seja bem vindo ao banco.
Escolha a opção desejada:

\033[1;30m[1] - Sacar
[2] - Depositar
[3] - Extrato
[4] - Sair\033[0m

'''

while True:
    print(mensagem)
    try:
        escolha = float (input("DIgite aqui para prosseguir: "))
    except ValueError:
        print("Valor inválido.Tente novamente.")
        continue

    if escolha == 1:
        sacar = float (input("Digite a quantia a ser sacada: R$"))
        if sacar == 0:
            print("Saldo insuficiente.")
        elif sacar -=
    
    elif escolha == 2:
        depositar = float (input("Digite o valor a ser depositado: R$"))
        print(f"Saque concluído.")
        print(f"Quantia depositada:{depositar:.2f}")