#Menu interativo

from reserva import Reserva
from verifica import verifica

def menu():
    acao = '0'
    lista_dados = []
    while acao != 5:
        print()
        print('======LABORATÓRIOS-INFORMÁTICA======')
        print('Escolha uma ação: \n1. Reservar \n2. Consultar Laboratório \n3. Listar \n4. Remover Reserva \n5. Salvar e Sair')
        acao = input('Ação: ')
        print('--------------------------------------------')

        if acao == '1':
            a = Reserva()
            a.nomeprof = input('Digite o nome do professor: ')
            a.matriculaprof = int(input('Digite a matrícula: '))
            a.labsala = int(input('Digite o laboratório desejado: LAB'))
            a.data = input('Informe a data desejada: (d/m) ')
            r = verifica(a.labsala, a.data, lista_dados)
            if r == True:
                lista_dados.append(a)
            else:
                print()
                print('O laboratório já está reservado! Selecione outro LAB.')                
           
        elif acao == '2':
            labsala = int(input('Digite o laboratório desejado: LAB'))
            data = input('Informe a data desejada: (d/m)')
            r = verifica(labsala, data, lista_dados)
            if r == False:
                print()
                print('O laboratório já está reservado!')
            else:
                print()
                print('O laboratório está disponível!')

        elif acao == '3':
            for x in lista_dados:
                    print(f'Professor(a): {x.nomeprof} \nMatrícula: {x.matriculaprof}')
                    print(f'Laboratório Reservado: LAB{x.labsala} na data: {x.data}')
                    print('--------------------------------------------')

        elif acao == '4':
            apagar_sala = int(input('Digite o Laboratório a ser desoupado: LAB'))
            apagar_data = input('Digite a data da reserva: (d/m) ')
            print('')
            i = 0
            while i < len(lista_dados):
                if apagar_sala == lista_dados[i].labsala and apagar_data == lista_dados[i].data:
                    print(f'A reserva do professor(a): {lista_dados[i].nomeprof} removida com sucesso!')
                    lista_dados.pop(i)
                    break
                i = i + 1

        elif acao == '5':
            arq = open('registros.txt', 'w')
            for x in lista_dados:
                s = str(x.nomeprof) + ' - ' + str(x.matriculaprof) + ' - ' + 'LAB' + str(x.labsala) + ' - ' + str(x.data)
                arq.write(s)
            arq.close()
            print('             -SISTEMA-ENCERRADO-')
            print('--------------------------------------------')
            break
