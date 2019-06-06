import itertools
import json
import sys

bar_len  = 60


apostas = {}
apostas['apostas'] = []
multiplos = {}
multiplos['de'] = []

# volante = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]

#volante = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
volante = [1,2,3,4,5,6]
c = list(itertools.combinations(volante, 3))
unq = set(c)
total_apostas = len(unq)
impares = 0
pares = 0
multiplo_de = 0

i = 0
for aposta in unq:
    i = i + 1

    for d in aposta:
        if d % 2 != 0:
            impares += 1
        else:
            pares += 1

    # inicio: parte que calcula os multiplos
    tot_m = 0
    for m in range(2,4):
        for d in aposta:
            if d % m == 0:
                tot_m += 1       
        multiplos['de'].append({m: tot_m})
        tot_m = 0
    # fim: parte que calcula os multiplos
    apostas['apostas'].append({
        'id': i, 'dezenas': aposta, 'dez_impares':impares, 'dez_pares': pares, 'multiplos': multiplos['de']
    })
    impares = 0
    pares = 0
    print (str(i) + " : " + str(aposta))
    print("multiplos: " + str(multiplos['de']))
    multiplos['de'] = []

with open ('apostas.json', 'w') as outfile:
    json.dump(apostas, outfile)