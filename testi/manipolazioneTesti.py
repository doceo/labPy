import string # Importiamo 'string' per ottenere un elenco standard della punteggiatura
import sys    # Importiamo 'sys' per uscire in caso di errore

def analizza_testo(nome_file):
    """
    Legge un file di testo, lo divide in paragrafi (basati su linee vuote)
    e conta parole e punteggiatura per ciascun paragrafo.
    """
    try:
        # Apriamo il file in lettura ('r') con codifica 'utf-8'
        # 'with' gestisce automaticamente la chiusura del file
        with open(nome_file, 'r', encoding='utf-8') as file:
            testo_completo = file.read()

    except FileNotFoundError:
        print(f"Errore: Il file '{nome_file}' non è stato trovato.")
        return
    except Exception as e:
        print(f"Si è verificato un errore durante la lettura del file: {e}")
        return

    # Se il testo è vuoto, usciamo
    if not testo_completo.strip():
        print("Il file è vuoto.")
        return

    # Definiamo la punteggiatura che vogliamo contare
    # Usiamo string.punctuation che è un elenco standard
    # Esempio: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    punteggiatura_da_contare = ",.:;"

    # Dividiamo il testo in paragrafi.
    # L'assunzione è che i paragrafi siano separati da una o più linee vuote ('\n\n').
    paragrafi = testo_completo.split('\n')

    print(f"Analisi del file: {nome_file}\n")
    
    # Iteriamo su ogni paragrafo trovato
    # usiamo enumerate per avere un contatore (partendo da 1)
    for i, paragrafo in enumerate(paragrafi, 1):
        
        # Puliamo il paragrafo da eventuali spazi/righe vuote all'inizio o alla fine
        paragrafo_pulito = paragrafo.strip()

        # Se il paragrafo pulito non è vuoto (evita di contare linee vuote multiple)
        if paragrafo_pulito:
            
            # 1. Conteggio parole
            # Dividiamo il paragrafo in base agli spazi bianchi (spazi, tab, a capo)
            lista_parole = paragrafo_pulito.split()
            numero_parole = len(lista_parole)

            # 2. Conteggio punteggiatura
            numero_punteggiatura = 0
            for carattere in paragrafo_pulito:
                if carattere in punteggiatura_da_contare:
                    numero_punteggiatura += 1

            # Stampa dei risultati per questo paragrafo
            print(f"--- Paragrafo {i} ---")
            
            # Stampa un'anteprima del paragrafo (i primi 80 caratteri)
            anteprima = (paragrafo_pulito[:80] + '...') if len(paragrafo_pulito) > 80 else paragrafo_pulito
            print(f"Anteprima: \"{anteprima.replace(chr(10), ' ')}\"") # Sostituisce eventuali a capo interni
            
            print(f"Numero di parole: {numero_parole}")
            print(f"Numero di segni di punteggiatura: {numero_punteggiatura}\n")

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