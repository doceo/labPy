# per installare le librerie serve:
# pip install edge-tts asyncio

import asyncio
import edge_tts

# Testo da leggere
TESTO = "Ciao! Questa è una prova di sintesi vocale neurale. Sento che la mia voce è molto più umana rispetto ai vecchi robot."

# Voce: it-IT-DiegoNeural o it-IT-ElsaNeural sono ottime scelte italiane
VOCE = "it-IT-DiegoNeural"
OUTPUT_FILE = "audio_naturale.mp3"

async def main():
    # Creazione dell'oggetto per la comunicazione
    communicate = edge_tts.Communicate(TESTO, VOCE)
    
    # Salvataggio del file audio
    await communicate.save(OUTPUT_FILE)
    print(f"Fatto! Audio salvato in '{OUTPUT_FILE}'")

if __name__ == "__main__":
    asyncio.run(main())