from gtts import gTTS

from playsound import playsound

audio = 'skst.mp3'
language = 'en'
saddam = input("Enter Text which you want to convert into mp3 :\n")
sp = gTTS(text = saddam,lang= language,slow=False)

sp.save(audio)
playsound(audio)
