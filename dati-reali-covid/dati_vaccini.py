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

    plt.show()

    return(popolSeries)


'''
estrapola riceve 2 valori in input:
- datoUno è la prima colonna da estrapolare
- datoDue è la seconda colonna da estrapolare
'''


def estrapola(datoUno, datoDue):

    #print(residenti)
    estrazione = pd.read_csv('somministrazioni-vaccini-latest.csv', sep = ',', header = 0, usecols=['data_somministrazione', datoUno, datoDue])

    #print(estrazione.head())

    res = residenti()
  
    regioni = []

#    print(res)

    for re in res:
        valori = pd.DataFrame(estrazione.loc[estrazione[datoDue]==re])
        print(re)
        #regioni.append()




'''
RIFERIMENTI
iterare un DF
http://www.antoiovi.com/python/python-pandas/pandas-dataframe/casi-d-uso-ed-esempi/python-pandas-dataframe-operazioni-frequenti#TOC-Iterare-un-dataframe-per-righe-:

https://qastack.it/programming/17071871/how-to-select-rows-from-a-dataframe-based-on-column-values

'''


'''
INIZIO DEL MAIN
'''


re = residenti()

#estrapola("nome_area","prima_dose")


#grafici(ospedalizzazioni, 10, 2)
