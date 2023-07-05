def changeDF(data, dfDict):
    newDict = dict()
    for k,v in dfDict.items():
        if str(type(v)) == "<class 'str'>":
            if v != '':
                if k == 'GENERO':
                    sub = list()
                    for y in list(data[v]):
                        if y == 'Masculino' or y == 'Femenino':
                            sub.append(y)
                        else:
                            sub.append('Otro')
                    newDict[k] = sub
                else:
                    newDict[k] = list(data[v])
            else:
                newDict[k] = list()
        else:
            lista = [str(i) for i in list(data[v[0]])]
            for j in range(1, len(v), 1):
                row = list(data[v[j]])
                for x in range(0, len(row), 1):
                    lista[x] += str(row[x])
            newDict[k] = [k.replace('nan', '') for k in lista]
    return newDict