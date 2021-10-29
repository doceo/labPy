
'''
Il seguente script verifica l'esistenza di una stringa all'interno di un file

str -> contiene la stringa da cercare
it -> il nome del file all'interno del quale cercare riga per riga
'''

str= "pop"  # nel caso di ruzzle, str deve contenere l'attributo di istanza
it = 'words.italian.txt' # è possibile aggiungere tante variabili quanti file di lingua si posseggono

f = open(it, 'r')
line = f.readline()

for line in f:  # per ogni riga del file vengono eseguite le righe di codice che seguono
#    print(str) 
    if str == line[:-1]:  #bisogna eliminare l'ultimo carattere dalla parola contenuta nella riga del file
        print("vero")
