from gtts import *
from playsound import *
text="Goddamn, its my birthday Everybody love me"
sp=gTTS(text)
sp.save("myfile.mp3")
for i in range(3):
    playsound("myfile.mp3")
