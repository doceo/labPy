import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import wget


# costruiscto un array associativo con le regioni e i suoi abitanti


def residenti():

    reg = pd.read_csv('Tutte_le_regioni.csv', sep = ';', header = 0, index_col= 'Codice regione', usecols=['Codice regione', 'Regione', 'Maschi + Femmine'])

    listRegioni = list(reg['Regione'])
    listPopolazione = list(reg['Maschi + Femmine'])

    popolSeries = pd.Series(listPopolazione, name= "Residenti per Regione", index = listRegioni)

    print(popolSeries)

    fig, axes = plt.subplots(1, figsize=(4,6))

    left, bottom, width, height = 0.1, 1.1, 0.8, 0.8  

    popolSeries.plot(ax = axes, kind = 'bar', title="Popolazione residente")

#    plt.show()

    return(popolSeries)

'''
normalizza prende in inputo:
 - dato INT
 - regione STRING
 - res PD.SERIES

'''

def normalizza(dato, regione, res):

    dato = dato/res[regione]*100000

    return dato
    
'''
estrapola riceve 2 valori in input:
- datoUno è la prima colonna da estrapolare
- datoDue è la seconda colonna da estrapolare
'''

def estrapola(datoUno, datoDue, res):

    #print(residenti)
    estrazione = pd.read_csv('somministrazioni-vaccini-latest.csv', sep = ',', header = 0, usecols=['data_somministrazione', datoUno, datoDue])

    print(res["Campania"])

    regioni = []

#    print(res)

    datiNorm = []

    for re in res.index:
        dfRegioni = estrazione.loc[estrazione[datoUno]==re]
        print(res[re])
        norm = dfRegioni[datoDue].apply(lambda x: x/res[re]*100000)
        print(norm)

        #valori.apply(lambda x : x/res[re]*100000)
        #print(valori)

        #regioni.append(valori)

    print(len(regioni))

  


'''
INIZIO DEL MAIN
'''
res = residenti()

estrapola("nome_area","prima_dose",res)


#grafici(ospedalizzazioni, 10, 2)
