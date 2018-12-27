import json, codecs

with open('megasena.json') as json_file:
    data = json.load(json_file)
    d = data[0]
    # print(d)
    # print(d['Concurso'])
    concursos = {}
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
