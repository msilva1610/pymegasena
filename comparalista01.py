lista1 = [20,40,9,11,32,50,53]

concursos = {'100':[2,4,9,10,31,53,55],'102':[1,4,9,11,32,51,54]}
iguais = []
for concurso,dezenas in concursos.items():
    print('concurso: {}'.format(concurso))
    del iguais[:]
    dezs = dezenas
    print(dezs)
    # for item in dezs:
    #     for i in lista1:
    #         if item == i:
    #             iguais.append(item)
    # if len(iguais) > 2:
    #     print('iguais: {}'.format(iguais))
    # del iguais[:]