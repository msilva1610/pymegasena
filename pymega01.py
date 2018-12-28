import random
from random import randint
import time
import json, codecs

q1 = [1,2,3,4,5,11,12,13,14,15,21,22,23,24,25]
q2 = [6,7,8,9,10,16,17,18,19,20,26,27,28,29,30]
q3 = [31,32,33,34,35,41,42,43,44,45,51,52,53,54,55]
q4 = [36,37,38,39,40,46,47,48,49,50,56,57,58,59,60]

Os10MaisSorteados = [10,5,53,4,23,33,54,24,51,42,17,37,27,52,13,28,56,6,30,32,34,43,16,2,36,44,29,50,18]
Os10MaisAtrasados = [41,35,8,38,12,11,49,59,1,45,58,40,47,20,46,31,7,19,39,3,14,60,25,48,15,57,22,9,55,21,26]
todos = [1,2,3,4,5,11,12,13,14,15,21,22,23,24,25,6,7,8,9,10,16,17,18,19,20,26,27,28,29,30,31,32,33,34,35,41,42,43,44,45,51,52,53,54,55,36,37,38,39,40,46,47,48,49,50,56,57,58,59,60]

#Os10MaisSorteados = todos
#Os10MaisAtrasados = todos

numapostas = 30
dezenas = 7
apostas = []
concursos = {}
corteiguais = 4


def CarregaConcursos():
    with open('megasena.json') as json_file:
        data = json.load(json_file)
        d = data[0]
        # print(d)
        # print(d['Concurso'])
        r = []
        for item in range(len(data)):
            concursocod = data[item]['Concurso']
            dez01 = (data[item]['Dezena01'])
            dez02 = (data[item]['Dezena02'])
            dez03 = (data[item]['Dezena03'])
            dez04 = (data[item]['Dezena04'])
            dez05 = (data[item]['dezena05'])
            dez06 = (data[item]['Dezena06'])
            if concursocod <> '':
                dr = [int(dez01),int(dez02),int(dez03),int(dez04),int(dez05),int(dez06)]
                dr.sort()
                d = {int(concursocod):dr}
                concursos.update(d)

def ValidaDezenas():
    iguais = []
    retorno = True
    for concurso,dez in concursos.items():
        for d in dez:
            for i in apostas:
                if d == i:
                    iguais.append(d)
        if len(iguais) >= corteiguais:
            #print('Dezenas: {} saiu no concurso {}'.format(iguais,concurso))
            retorno = False
        del iguais[:]
    return retorno



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

def principal():
    Validado = False
    CarregaConcursos()
    for i in range(1, numapostas+1):
        time.sleep(7)
        apostar()
        apostas.sort()
        # print('minhas apostas {}: {}'.format(i, apostas))
        # ValidaDezenas()
        Validado = ValidaDezenas()
        if Validado:
            print('>>>> Aposta valida {}: {}'.format(i, apostas))
        del apostas[:]

principal()
