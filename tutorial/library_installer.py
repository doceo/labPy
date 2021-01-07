# Luca Patruno - IIE 2020/2021


from os import system, path
from sys import platform, executable
#Importo le librerie
assert platform  in ['darwin', 'win32', 'cygwin']
directory = path.dirname(executable)
#Controllo la cartella di installazione di Python
print("Benvenuto!")
while True:
    while True:
        #Chiedo se si deve installare o disinstallare una libreria
        choice = input("\n-Premi 1 per installare una libreia\n-Premi 2 per disinstallare una libreria\n--> ")
        if choice in [1,2,"1","2"]:
            #Se la risposta dell'utente è valida rompo il ciclo
            break
        else:
            #Altrimenti avverto l'utente e ricomincio il ciclo
            print("Valore non valido\nI valori validi sono solo 1 e 2")
    #Controllo se il sistema operativo è MacOS o Windows, diversamente da errore
    libreria = input("Come si chiama la tua libreria?  --> ")
    #Chiedo il nome della libreria da installare
    if choice in [1,"1"]:
        #A seconda della scelta dell'utente il comando sarà di installare o disinstallare la libreria
        command = "install"
    else:
        command = "uninstall -y"   
        #-y indica che non verrà chiesta la conferma per disinstallare la libreria
        
    if platform  in ['win32', 'cygwin']:
        system(f"cd {directory}\\Scripts && pip {command} {libreria}")
        #Se la piattaforma è Windows lo slash è \, si usa doppio da sintassi di python
    else:
        system(f"cd {directory}/Scripts && pip {command} {libreria}")
        #Se la piattaforma è MacOS lo slash è /
    #Grazie al terminale vado nella cartella Scripts di Python e installo\disinstallo la libreria
    input("\n\n\n-Premi invio per riutilizzare il programma o premi ctrl + c per terminarne  l'esecuzione  ")
    #Se viene premuto invio il ciclo si ripete, se l'utente preme ctrl+c il programma verrà chiuso dall'errore KeyboardInterrupt
