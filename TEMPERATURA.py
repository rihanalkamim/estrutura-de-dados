def fahrenheit(celsius):
    fah = (celsius*1.8)+32
    return fah 

def avaliacao(temperatura1:tuple, temperatura2:tuple):
    if temperatura1[1] != temperatura2[1]:
        if temperatura1[1] in 'Cc':
            fahrentemperatura1 = fahrenheit(temperatura1[0])
            maior = fahrentemperatura1
        else:
            maior = temperatura1[0]
        if temperatura2[1] in 'Cc':
            fahrentemperatura2 = fahrenheit(temperatura2[0])
        if fahrentemperatura2 > maior or temperatura2[0] > maior:
            maior = fahrentemperatura2
        return '{:.2f}°F'.format(maior)
    else:
        maior = temperatura1[0]
        if maior > temperatura2[0]:
            maior = temperatura2[0]
        return '{:.2f}°{}'.format(maior, temperatura1[1])

print('-'*40)
print('{:^40}'.format('ANÁLISE DE TEMPERATURAS'))
print('-'*40)
grau1 = float(input('Digite a primeira temperatura: '))
while True:
    escala1 = str(input('Digite a escala da primeira temperatura: ')).split()[0]
    if escala1 in 'FfCc':
        break
temperatura1 = (grau1, escala1)
grau2 = float(input('Digite a segunda temperatura: '))
while True:
    escala2 = input('Digite a escala da primeira temperatura: ').split()[0]
    if escala2 in 'FfCc':
        break
temperatura2 = (grau2, escala2)
print('A maior temperatura é \033[31m{}\033[m'.format(avaliacao(temperatura1, temperatura2)))