import random
from random import randint
import time
q1 = [1,2,3,4,5,11,12,13,14,15,21,22,23,24,25]
q2 = [6,7,8,9,10,16,17,18,19,20,26,27,28,29,30]
q3 = [31,32,33,34,35,41,42,43,44,45,51,52,53,54,55]
q4 = [36,37,38,39,40,46,47,48,49,50,56,57,58,59,60]

listajogos = []

n = 10

def geraapostas():
    apostas = []
    apostas.append(random.choice(q1))
    apostas.append(random.choice(q2))
    apostas.append(random.choice(q3))
    apostas.append(random.choice(q4))

    for i in range(10):
        a1 = randint(1,60)
        if a1 not in apostas:
            apostas.append(a1)
            break

    for i in range(10):
        a2 = randint(1,60)
        if a2 not in apostas:
            apostas.append(a2)
            break
    #print(apostas)
    listajogos.append(apostas)
    apostas.clear
for i in range(n):
    time.sleep(0.2)
    geraapostas()

for i in range(len(listajogos)):    
    print(listajogos[i])
