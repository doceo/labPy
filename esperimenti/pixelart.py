# 1. Importiamo lo strumento per le immagini
from PIL import Image

# 2. Definiamo le dimensioni della nostra immagine (in pixel)
larghezza_img = 10 # Larghezza di 10 pixel
altezza_img = 10  # Altezza di 10 pixel

# 3. Definiamo alcuni colori che vogliamo usare (come tuple RGB)
colore_sfondo = (255, 255, 255) # Bianco
colore_rosso = (255, 0, 0)      # Rosso
colore_blu = (0, 0, 255)        # Blu

# 4. Creiamo una nuova immagine vuota con le nostre dimensioni e colore di sfondo
# 'RGB' indica che usiamo il modello di colore RGB
immagine = Image.new('RGB', (larghezza_img, altezza_img), colore_sfondo)

# 5. Mettiamo un pixel! Usiamo putpixel(coordinate, colore)
# Le coordinate sono (x, y) partendo da (0,0) in alto a sinistra
immagine.putpixel((1, 1), colore_rosso)  # Mette un pixel rosso a x=1, y=1
immagine.putpixel((3, 5), colore_blu)    # Mette un pixel blu a x=3, y=5
immagine.putpixel((4, 5), colore_blu)    # Mette un altro pixel blu accanto

# (Opzionale, se la classe segue bene: introdurre un piccolo ciclo for)
# Disegniamo una linea verde da (0,8) a (9,8)
# colore_verde = (0, 255, 0)
# for x in range(larghezza_img): # x va da 0 a 9
#    immagine.putpixel((x, 8), colore_verde)

# 6. Salviamo l'immagine in un file
nome_file = "mia_prima_pixelart.png"
immagine.save(nome_file)

# 7. Messaggio per confermare
print(f"Immagine salvata come {nome_file}!")

# (Opzionale) Mostra l'immagine creata aprendo il file .png
# immagine.show() # Questo apre l'immagine con il visualizzatore predefinito