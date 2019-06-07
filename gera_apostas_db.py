import itertools
import json
import sys
import datetime

from pymongo import MongoClient
import json

serverMongo = MongoClient('192.168.0.20', 27017)
dbApostas = serverMongo['apostas']
col_apostasmegasena = dbApostas['apostasmegasena']

apostas = {}
apostas['apostas'] = []

volante = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]

print('Gerando lista completa: {}'.format(datetime.datetime.now()))

c = list(itertools.combinations(volante, 6))

print('gerando lista unica: {}'.format(datetime.datetime.now()))

unq = set(c)
# total_apostas = len(unq)

i = 0
print('Loop na lista unica iniciado ...: {}'.format(datetime.datetime.now()))
for aposta in unq:
    i += 1
    novaaposta = {'_id': i, 'dezenas': aposta}
    id_inset = col_apostasmegasena.insert_one(novaaposta).inserted_id
    print('Aposta salva: {} - {}'.format(id_inset, datetime.datetime.now()))

print('Terminou: {}'.format(datetime.datetime.now()))
