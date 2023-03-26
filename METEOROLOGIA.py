from random import randint

semanas = []
semana = []
somasemana = []
contador = soma2 = 0
for c in range(0, 28):
    temperatura = randint(15, 38)
    semana.append(temperatura)
    contador += 1
    if contador == 7:
        semanas.append(semana[:])
        soma1 = sum(semana)
        somasemana.append(soma1)
        semana.clear()
        contador = 0
        soma2 += soma1
maior = menor = semanas[0][0]
media = soma2/28
semanasalta = []
semanamaisalta = []
dias7 = 0
quantsemanas = 0 
for s in semanas:
    quantsemanas += 1
    for dia in s:
        if dia > maior:
            maior = dia
        if dia < menor:
            menor = dia
        if dia > media:
            dias7 += 1
    if dias7 >= 3:
        num = quantsemanas - 1 
        semanasalta.append(num)
    dias7 = 0
acimadamedia = len(semanasalta)
print('='*50)
print('{:^50}'.format('METEOROLOGIA DO MÊS'))
print(f'Semanas com temperaturas acima da média do mês: ')
if semanasalta != 0:
    for c in range(0, acimadamedia):
        print(f'Semana {semanasalta[c]+1}: {semanas[semanasalta[c]]}')
else:
    print('Não foram encontrados semanas com a temperatura acima da média em pelo menos três dias.')
print(f'A temperatura mínima foi de \033[36m{menor}\033[m°C')
print(f'A temperatura máxima foi de \033[31m{maior}\033[m°C')
print('='*50)
print('Histograma da semana com a temperatura mais quente: ')
if semanasalta != 0:
    for t in semanas[semanasalta[0]]:
        print('{}'.format('▉'*t))