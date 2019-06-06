import itertools
import json
import sys

bar_len  = 60

q1 = [1,2,3,4,5,11,12,13,14,15,21,22,23,24,25]
q2 = [6,7,8,9,10,16,17,18,19,20,26,27,28,29,30]
q3 = [31,32,33,34,35,41,42,43,44,45,51,52,53,54,55]
q4 = [36,37,38,39,40,46,47,48,49,50,56,57,58,59,60]

qd1 = 0
qd2 = 0
qd3 = 0
qd4 = 0

apostas = {}
apostas['apostas'] = []
multiplos = {}
multiplos['de'] = []

volante = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
# volante = [1,2,3,4,5,6]
c = list(itertools.combinations(volante, 6))
unq = set(c)
total_apostas = len(unq)
impares = 0
pares = 0
multiplo_de = 0
primos = 0
Fibonacci = [1, 2, 3, 5, 8, 13, 21, 34, 55]
Quadraticos = [1, 4, 9, 16, 25, 36, 49]


total_fibonacci = 0
total_quadraticos = 0

soma_das_dezenas = 0
soma_dos_digitos_das_dezenas = 0
i = 0

tot = 0

for aposta in unq:

    i = i + 1

    for d in aposta:
        if d % 2 != 0:
            impares += 1
        else:
            pares += 1
        soma_das_dezenas += d

        strdezena = str(d)
        for s in strdezena:
            soma_dos_digitos_das_dezenas += int(s)

    # inicio quadrante
        if d in q1:
            qd1 += 1 
        elif d in q2:
            qd2 += 1
        elif d in q3:
            qd3 += 1
        else:
            qd4 += 1

    # fim quadrante

    # inicio primos
    for d in aposta:
        if d > 2:
            for p in range(2,d):
                if (d % p == 0):
                    primos += 1

    # fim primos

    # inicio fibonacci
    for f in aposta:
        if f in Fibonacci:
            total_fibonacci += 1
    # fim fibonacci 

    #inicio quadratico
    for q in aposta:
        if q in Quadraticos:
            total_quadraticos += 1    

    #fim quadratico
   

    # inicio: parte que calcula os multiplos
    tot_m = 0
    for m in range(2,30):
        for d in aposta:
            if d % m == 0:
                tot_m += 1       
        multiplos['de'].append({m: tot_m})
        tot_m = 0
    # fim: parte que calcula os multiplos


    apostas['apostas'].append({
        'id': i, 'dezenas': aposta, 'dez_impares':impares, 'dez_pares': pares,'primos':primos,  'multiplos': multiplos['de'], 'fibonacci': total_fibonacci, 'quadraticos': total_quadraticos, 'soma_das_dezenas': soma_das_dezenas, 'soma_dos_digitos':soma_dos_digitos_das_dezenas, 'quadrante1': qd1,'quadrante2':qd2, 'quadrante3':qd3,'quadrante4':qd4 
    })
    impares = 0
    pares = 0
    primos = 0
    total_fibonacci = 0
    total_quadraticos = 0
    soma_das_dezenas = 0
    soma_dos_digitos_das_dezenas = 0
    qd1 = 0
    qd2 = 0
    qd3 = 0
    qd4 = 0    
    print (str(i) + " : " + str(aposta))
    print("multiplos: " + str(multiplos['de']))
    multiplos['de'] = []

    
    if tot >= 1000:
        break
    else:
        tot += 1

with open ('apostas.json', 'w') as outfile:
    json.dump(apostas, outfile)