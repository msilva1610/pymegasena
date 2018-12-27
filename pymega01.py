import random
from random import randint
import time
q1 = [1,2,3,4,5,11,12,13,14,15,21,22,23,24,25]
q2 = [6,7,8,9,10,16,17,18,19,20,26,27,28,29,30]
q3 = [31,32,33,34,35,41,42,43,44,45,51,52,53,54,55]
q4 = [36,37,38,39,40,46,47,48,49,50,56,57,58,59,60]
Os10MaisSorteados = [10,5,53,4,23,33,54,24,51,42]
Os10MaisAtrasados = [55,42,26,7,25,21,47,53,23,32]

numapostas = 10
dezenas = 7
apostas = []
# passos
# 

def sorteiaSobra(sobrou):
    for i in range(1, sobrou+1):
        SorteadoAtrasado = [1,2]
        r = random.choice(SorteadoAtrasado)
        if r == 1:
            while True:
                dezena = random.choice(Os10MaisSorteados)
                if dezena not in apostas:
                    apostas.append(dezena)
                    break 
        else:
            while True:
                dezena = random.choice(Os10MaisAtrasados)
                if dezena not in apostas:
                    apostas.append(dezena)
                    break 

def fazquadrantes():
    quadrantes = ["q1","q2","q3","q4",]
    for i in quadrantes:  
        if i == 'q1':
            q = q1
        elif i == 'q2':
            q = q2
        elif i == 'q3':
            q = q3
        else:
            q = q4
        while True:
            dezena = random.choice(q)
            if dezena not in apostas:
                apostas.append(dezena)
                break 

def apostar():
    Quadrantes = divmod(dezenas,4)[0]
    sobrou = divmod(dezenas,4)[1]

    for i in range(1,Quadrantes+1):
        fazquadrantes()
    
    sorteiaSobra(sobrou)

    #print('dezenas sorteadas: {}'.format(aposta))

def principal():
    for i in range(1, numapostas+1):
        time.sleep(5)
        apostar()
        apostas.sort()
        print('minhas apostas {}: {}'.format(i, apostas))
        del apostas[:]

principal()
