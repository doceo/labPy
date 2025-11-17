import asyncio
import edge_tts

# ================= CONFIGURAZIONE =================

# Nome del file di testo da leggere
FILE_INPUT = "testo.txt"

# Nome del file audio che verrà creato
FILE_OUTPUT = "audiolibro.mp3"

# SCEGLI LA VOCE (Decommenta quella che vuoi usare)

# --- Opzione 1: VOCE MASCHILE (Diego) ---
VOCE = "it-IT-DiegoNeural"

# --- Opzione 2: VOCE FEMMINILE (Elsa) ---
# VOCE = "it-IT-ElsaNeural"

# --- Opzione 3: ALTRA VOCE FEMMINILE (Isabella) ---
# VOCE = "it-IT-IsabellaNeural"


# esistono altri timbri, puoi trovarli digitando nel terminale edge-tts --list-voices
# ==================================================

async def main():
    print(f"📖 Leggo il file: {FILE_INPUT}...")
    
    try:
        # Apertura del file di testo (encoding='utf-8' è fondamentale per gli accenti italiani)
        with open(FILE_INPUT, "r", encoding="utf-8") as f:
            contenuto = f.read()
        
        if not contenuto.strip():
            print("❌ Il file di testo è vuoto!")
            return

        print(f"🎙️ Generazione audio in corso con voce: {VOCE}...")
        
        # Creazione della comunicazione con il servizio TTS
        communicate = edge_tts.Communicate(contenuto, VOCE)
        
        # Salvataggio del file
        await communicate.save(FILE_OUTPUT)
        
        print(f"✅ Fatto! File salvato come: {FILE_OUTPUT}")

    except FileNotFoundError:
        print(f"❌ Errore: Non trovo il file '{FILE_INPUT}'. Assicurati che sia nella stessa cartella.")
    except Exception as e:
        print(f"❌ Si è verificato un errore: {e}")

if __name__ == "__main__":
    asyncio.run(main())