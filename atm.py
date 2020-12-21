# Função universal para o cálculo da quantidade de cédulas
def calculaCedulas(self, valor, valorCedula, saque):
    if(valor >= valorCedula):
        for i in range(int(valor/valorCedula)):
            if(self.cedulas[valorCedula] != 0):
                saque[valorCedula] += 1
                self.cedulas[valorCedula] -= 1
                valor -= valorCedula
    return valor
        

class Atm:
    # Construtor
    def __init__(self):
        # Dicionário com as cédulas permitidas
        self.cedulas = {100: 0, 50: 0, 20: 0, 10: 0}

    # Carrega com cédulas o caixa eletrônico
    def abastece(self, nota, quantidade):
        existe = False
        for cedula in self.cedulas.keys():
            if(cedula == nota):
                existe = True
        if(existe):
            self.cedulas[nota] += quantidade
            print('{} cédulas de R${} foram adicionadas!'.format(quantidade, nota))
        else:
            print('Valor de cédula inválido!')

    # Descarrega cédulas do caixa eletrônico
    def saque(self, valor):
        saque = {100: 0, 50: 0, 20: 0, 10: 0} # Vetor auxiliar que conterá as cédulas para o saque
        
        # Como python somente trabalha com cópias de valores em funções, é necessário varivável auxíliar
        valorSaque = valor
        for valorCedula in self.cedulas:
            valorSaque = calculaCedulas(self, valorSaque, valorCedula, saque)
            if(valorSaque == 0): # Sai do laço caso já tenha conseguido cédulas suficientes
                break
        
        # Saque não conseguiu ser concluído
        if(valorSaque != 0):
            print('Saque REJEITADO! O caixa eletrônico não possui cédulas suficientes.')
            return 0
        
        # Sáida das cédulas sacadas
        print('Saque APROVADO! As notas emitidas foram:')
        for valores in saque:
            if(saque[valores] != 0):
                print('{} notas de R${}'.format(saque[valores], valores))
        return valor
   
    # Retorna a quantidade de cédulas
    def get_cedulas(self):
        print('\nCédulas em estoque:')
        for valores in self.cedulas:
            print('{} notas de R${}'.format(self.cedulas[valores], valores))