class Pessoa:
    def __init__(self):
        self.__nome = None
        self.__cpf = None
        self.__telefone = None

    def __str__(self):
        return self.__nome, self.__cpf, self.__telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone


class Agenda:

    def __init__(self):
        self.__agenda = []

    def armanezar_pessoa(self, pessoa):
        self.__agenda.append([pessoa.nome, pessoa.cpf, pessoa.telefone])
        print(pessoa.__str__())
        print('Dados Salvos \n')

    def remover_pessoa(self, pessoa):
        print(f'\nRemomento pessoa do indice {pessoa}')
        print(self.__agenda[pessoa])
        del(self.__agenda[pessoa])
        print('Dados removidos')

    def buscar_pessoa(self, dado):
        print('Buscando pessoa \n')
        print(f'Dado informado : {dado}')
        for i in range(len(self.__agenda)):
            if self.__agenda[i][1] == dado or self.__agenda[i][2] == dado:
                return print(f'Posição {i} \n')

    def imprimir_agenda(self):
        print('\n Agenda \n')
        for i in range(len(self.__agenda)):
            print(self.__agenda[i])
        print('Fim agenda \n')

    def imprimir_pessoa(self, pessoa):
        print(f'A pessoa do indice {pessoa} é :')
        print(self.__agenda[pessoa])


agenda = Agenda()

joao = Pessoa()
joao.nome = 'Joao'
joao.cpf = '1111111111'
joao.telefone = '99999999'

maria = Pessoa()
maria.nome = 'Maria'
maria.cpf = '2222222222'
maria.telefone = '888888888'

pedro = Pessoa()
pedro.nome = 'Pedro'
pedro.cpf = '33333333333'
pedro.telefone = '777777777'

agenda.armanezar_pessoa(joao)
agenda.armanezar_pessoa(maria)
agenda.armanezar_pessoa(pedro)

agenda.buscar_pessoa('33333333333')

agenda.imprimir_agenda()

agenda.imprimir_pessoa(2)

agenda.remover_pessoa(2)
