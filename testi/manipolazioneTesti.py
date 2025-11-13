import string # Importiamo 'string' per ottenere un elenco standard della punteggiatura
import sys    # Importiamo 'sys' per uscire in caso di errore
import csv
import matplotlib.pyplot as plt
import numpy as np

def contaLenWord(paragrafo):

    lunghezza = []
    for c in paragrafo:
        if len(c)>2:
            lunghezza.append(len(c))
    
    
    media = sum(lunghezza)/len(lunghezza)
    print(media)
    print
    return media


#funzione che genera grafici, non vengono ancora salvati
def grafico(dati,etichetta):

    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8  

    fig, ax = plt.subplots(1, 1)

    ax.plot(dati,color="blue", label="paragrafo")

    jls_extract_var = "_grafico.png"
    nome_img = etichetta + jls_extract_var
    plt.savefig(nome_img)

def analizza_testo(nome_file):
    """
    Legge un file di testo, analizza paragrafi (parole e punteggiatura)
    e salva i risultati in un file .csv con separatore ';'.
    """
    try:
        with open(nome_file, 'r', encoding='utf-8') as file:
            testo_completo = file.read()
    except FileNotFoundError:
        print(f"Errore: Il file '{nome_file}' non è stato trovato.")
        return
    except Exception as e:
        print(f"Si è verificato un errore durante la lettura del file: {e}")
        return

    if not testo_completo.strip():
        print("Il file è vuoto.")
        return

    # Definiamo il nome del file CSV di output
    # Es. "mio_testo.txt" -> "mio_testo_analisi.csv"
    nome_file_output = nome_file.replace('.txt', '_analisi.csv')

    # Definiamo la punteggiatura
    punteggiatura_da_contare = ",;:."

    # Dividiamo il testo in paragrafi
    paragrafi = testo_completo.split('\n')

    print(f"Analisi del file: {nome_file}\n")

    #definisco vettori nei quali salvare le informazioni da rendere a grafico
    parole =[]
    punt = []

    # Iniziamo a scrivere il file CSV
    try:
        # Apriamo il file CSV in modalità scrittura ('w')
        # newline='' è importante per la corretta gestione dei 'a capo' nel modulo CSV
        with open(nome_file_output, 'w', newline='', encoding='utf-8') as csv_file:
            
            # Creiamo un 'writer' (scrittore) CSV specificando il delimitatore
            csv_writer = csv.writer(csv_file, delimiter='-')
            
            # Scriviamo la riga di intestazione (Header)
            csv_writer.writerow(['Numero Paragrafo', 'Numero Parole', 'Conteggio Punteggiatura', 'media lunghezza parola'])
            
            print("Paragrafi analizzati:")
            
            # Iteriamo sui paragrafi. Usiamo un contatore separato
            # per numerare solo i paragrafi che contengono testo.
            numero_paragrafo_effettivo = 0
            
            for paragrafo in paragrafi:
                paragrafo_pulito = paragrafo.strip()

                # Contiamo solo se il paragrafo non è vuoto
                if paragrafo_pulito:
                    
                    # Incrementiamo il contatore dei paragrafi
                    numero_paragrafo_effettivo += 1
                    
                    # 1. Conteggio parole
                    lista_parole = paragrafo_pulito.split()
                    numero_parole = len(lista_parole)

                    parole.append(numero_parole)
                    # 2. Conteggio punteggiatura
                    numero_punteggiatura = 0
                    for carattere in paragrafo_pulito:
                        if carattere in punteggiatura_da_contare:
                            numero_punteggiatura += 1

                    punt.append(numero_punteggiatura)
                    # Scriviamo la riga di dati nel file CSV
                    
                    caratt_medio = contaLenWord(lista_parole)

                    csv_writer.writerow([numero_paragrafo_effettivo, numero_parole, numero_punteggiatura])
                    
                    # Stampiamo un feedback anche sul terminale
                    print(f"- Paragrafo {numero_paragrafo_effettivo}: {numero_parole} parole, {numero_punteggiatura} segni, le parole medie sono lunghe: {caratt_medio}")
                    
            
            grafico(parole, "numero_parole")
            grafico(punt, "numero_simboli")

            print(parole)
            print(punt)
            print(f"\nAnalisi completata!")
            print(f"Risultati salvati con successo nel file: {nome_file_output}")

    except Exception as e:
        print(f"Si è verificato un errore durante la scrittura del file CSV: {e}")

# --- Esecuzione del programma ---
if __name__ == "__main__":
    # Chiediamo all'utente il nome del file da analizzare
    nome_del_file = input("Inserisci il nome del file .txt da analizzare (es. mio_testo.txt): ")
    
    print(string.punctuation)
    print(type(string.punctuation))
    # Assicuriamoci che l'utente abbia inserito un nome
    if not nome_del_file:
        print("Nome file non valido.")
    elif not nome_del_file.endswith('.txt'):
        print("Per favore, inserisci un file con estensione .txt")
    else:
        analizza_testo(nome_del_file)
    