import pandas as pd
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

# Percorsi
csv_file = 'link-foglio3.csv'  # cambia con il tuo file
output_dir = 'qrcodes'

# Crea la cartella se non esiste
os.makedirs(output_dir, exist_ok=True)

# Leggi il CSV
df = pd.read_csv(csv_file)

# Font per l'etichetta (puoi cambiare con un percorso a un .ttf se vuoi un font specifico)
try:
    font = ImageFont.truetype("arial.ttf", 53)
except:
    font = ImageFont.load_default()

# Genera QR code per ogni riga
for index, row in df.iterrows():
    link = row['link']
    label = row['etichetta']

    # Crea il QR code
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(link)
    qr.make(fit=True)
    img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Aggiungi l'etichetta sotto
    width, height = img_qr.size
    label_height = 70
    img_final = Image.new("RGB", (width, height + label_height), "white")
    img_final.paste(img_qr, (0, 0))

    draw = ImageDraw.Draw(img_final)
    #text_width  = draw.textsize(label, font=font)
    bbox = draw.textbbox((0, 0), label, font=font)
    text_width = bbox[2] - bbox[0]

    text_position = ((width - text_width) // 2, height )# + 10
    draw.text(text_position, label, fill="black", font=font)

    # Salva il file
    filename = f"{label.replace(' ', '_')}.png"
    img_final.save(os.path.join(output_dir, filename))

print("QR code generati con successo!")
