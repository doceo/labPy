'''
TRY-EXCEPT

Struttura
try:
    ... # Blocco di codice che può generare errori
except ValueError:
    print('Valore inserito non valido!')
except ZeroDivisionError:
    print('Divisione per zero')
except:
    print('Altro tipo di errore')
else:  # dopo tutte le clausole except
    print('Nessun errore') # se non ci sono errori
finally:
    print('Fine') # Eseguita anche in caso di errore

'''

Raggio = -1.0
while Raggio < 0:
    try:
	        Raggio = float(input("Inserire il Raggio "))
    except:
        print ("Inserimento non valido !!!")
        Raggio = -1.0
    else:
        if Raggio < 0:
            print ("Raggio NON puo` essere negativo!")
	
Area = Raggio * Raggio * 3.14159265
print('Area', Area, sep=' = ')
