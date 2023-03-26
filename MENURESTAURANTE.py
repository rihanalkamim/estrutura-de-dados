from time import sleep
import os

#MENU DE COMIDAS
comidas = {'macarronada':30, 'feijoada':20, 'estrogonofe':25, 'moqueca':15, 'baiaodedois':10}
#TODOS OS PRATOS QUE O CLIENTE ESCOLHER
todospratos = []
#APENAS PARA SER UMA PONTE PARA AS ESCOLHAS DO CLIENTE
pratos = []
#TOTAL DO DIA
fechamentocaixa = []
#QUANTIDADE DE CLIENTES
totalclientes = 1
# PARTE RELACIONADA APENAS A ENTRADA DE DADOS E APRESENTAÇÃO DO MENU
while True:
    while True:
        print('-'*50)
        print('{:^50}'.format('MENU'))
        print('-'*50, end = '')
        print('''
        1) Macarronada - R$30,00
        2) Feijoada - R$20,00
        3) Estrogonofe - R$25,00
        4) Moqueca - R$15,00
        5) Baião de Dois - R$10,00
        ''')
        escolha = int(input('Escolha qual a comida deseja: '))
        if escolha < 1 or escolha > 5:
            while True:
                escolha = int(input('Tente Novamente: '))
                if escolha < 1 or escolha > 5:
                    print('', end = '')
                else:
                    break
        quantidade = int(input('Escolha quantos pratos deste você deseja: '))
        pratos.append(escolha)
        pratos.append(quantidade)
        todospratos.append(pratos[:])
        pratos.clear()
        sair = input('Você deseja mais algum tipo de comida?[S/N]\n').strip().upper()[0]
        if sair in 'N':
            print('\033[31mSAINDO DO MENU\033[m ...')
            sleep(1)
            break
        elif sair in 'S':
            print('Escolha o próximo prato ...')
            sleep(1.5)
            print('\033c', end = '')
        else:
            print('Tente novamente ...')
            sair = input('Você deseja mais algum tipo de comida?[S/N]\n').strip().upper()[0]

#PARTE DE ANÁLISE E MANIPULAÇÃO DOS DADOS DE ENTRADA

#PARA CONTAR SABER EM QUE POSIÇÃO ESTÁ A CONTAGEM
    contador = 0
#PARA PERCORRER NO DICIONARIO
    contadordict = 0
#PARA O VALOR TOTAL
    valortotal = 0
    for comida in todospratos:
        for prato in comida:
            if contador % 2 == 0:
                for selecionacomida in comidas.keys():
                    if prato - 1 == contadordict:
                        valordoprato = comidas[selecionacomida]
                    contadordict+= 1
                contadordict = 0
            else:
                valorestimado = valordoprato*prato
            contador += 1
        valortotal += valorestimado
    fechamentocaixa.append(valortotal)
    print(f'O VALOR TOTAL CONSUMIDO PELO CLIENTE FOI DE R${float(valortotal):.2f}')
    clientes = input('Possui mais algum cliente no momento?[S/N]\n').strip().upper()[0]
    if clientes in 'N':
        break
    elif clientes in 'S':
        print('Perfeito!!!')
        sleep(1)
        os.system('cls')
        totalclientes+=1
        todospratos.clear()
    else:
        while True:
            if clientes != 'S' or clientes != 'N':
                clientes = input('Digite novamente = ').strip().upper()[0]
            if clientes == 'S':
                print('Perfeito!!!')
                break
            elif clientes == 'N':
                break
        if clientes == 'N':
            break
os.system('cls')
valordocaixa = sum(fechamentocaixa)
print(f'''
{'-'*50}
{'FECHAMENTO DE CAIXA':^50}
{'-'*50}
TOTAL DE CLIENTES: {totalclientes}
VALOR TOTAL DO CAIXA DIÁRIO: R${float(valordocaixa):.2f}
''')