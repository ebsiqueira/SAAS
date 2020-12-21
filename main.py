#################################################
# Autor: Eduardo Borges Siqueira                #
# Data: 21/12/2020                              #
# Versão 1.0                                    #
# Modelo de subsistema para caixas eletrônicos  #
#################################################

#################################################
# Sistema hipotético para controle de notas em  #
# caixas eletrônicos. Caso fosse ser utilizado, #
# os prints e inputs seriam substituidos pelas  #
# devidas entradas e saídas de dados indicadas. #
#################################################

# Import da classe Atm, localizada em atm.py
from atm import Atm 

# Criação de um "Caixa Eletrônico"
atm = Atm()

# Controle do Menu
controleMenu = True

# Saldo de Conta fictício para testes de execução
saldoConta = 9999

while(controleMenu):
    menu = int(input('\n1. Abastecer\n2. Sacar\n3. Consultar\n4. Sair\n> '))

    # Abastecimento do caixa
    if(menu == 1):
        nota = int(input("\nCédula que será inserida: "))
        quantidade = int(input('Quantidade de cédulas: '))
        atm.abastece(nota, quantidade)

    # Saque de dinheiro
    elif(menu == 2):
        valor = int(input('\nDigite o valor a ser sacado: '))
        if(valor <= saldoConta):
            valorSacado = atm.saque(valor)
            saldoConta -= valorSacado
        else:
            print('Saque rejeitado! O seu saldo é insuficiente.')

    # Consulta de cédulas
    elif(menu == 3):
        atm.get_cedulas()

    # Sair do programa
    elif(menu == 4):
        controleMenu = False

    # Opção inválida do menu
    else:
        print('Digito inválido! Tente novamente.')