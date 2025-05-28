import paho.mqtt.client as mqtt
import time

# Configurazione MQTT
MQTT_BROKER = "io.adafruit.com"  # O il tuo broker privato (es: "mqtt.eclipseprojects.io")
MQTT_PORT = 1883
MQTT_USER = "tuo_username_adafruit"  # Lascia vuoto se non richiesto
MQTT_PASSWORD = "tua_api_key_adafruit"  # Lascia vuoto se non richiesto
MQTT_TOPIC = "tuo_username_adafruit/feeds/nome_feed"  # Formato Adafruit: <username>/feeds/<feedname>

# Callback per la connessione
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connesso al broker MQTT!")
    else:
        print(f"Errore di connessione: Codice {rc}")

# Crea un client MQTT
client = mqtt.Client()
client.on_connect = on_connect

# Autenticazione (se richiesta)
if MQTT_USER and MQTT_PASSWORD:
    client.username_pw_set(MQTT_USER, MQTT_PASSWORD)

# Connessione al broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Pubblica un messaggio
try:
    while True:
        message = "Ciao Mondo!"
        client.publish(MQTT_TOPIC, message)
        print(f"Inviato: {message}")
        time.sleep(5)  # Invia ogni 5 secondi
except KeyboardInterrupt:
    print("\nScript interrotto")
    client.disconnect()
MQTT_BROKER = "io.adafruit.com"
MQTT_PORT = 1883
MQTT_USER = "tuo_username_adafruit"  # Il tuo username su Adafruit
MQTT_PASSWORD = "aio_tua_api_key"  # La tua chiave API (Adafruit IO)
MQTT_TOPIC = f"{MQTT_USER}/feeds/test"  # Topic nel formato: <username>/feeds/<feedname>
