
## https://pypi.org/project/gTTS/
## https://pypi.org/project/playsound/
from gtts import gTTS

from playsound import playsound 

# decido cosa dovrà dire

TEXT = "Un saluto da Stephen Hawking"

#  è possibile anche modificar ela velocità, provate a cambiare parametri
#  tts = gTTS(text=TEXT, lang="it", slow=True)


tts = gTTS(text=TEXT, lang="it")

# salvo un mp3 con l'audio
tts.save("ciaoSH.mp3")
playsound("ciaoSH.mp3")