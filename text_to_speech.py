#=====BY SANJANA=====
from gtts import gTTS
import pygame #playing the sound

def sound_setup():
    pygame.mixer.init()

def tts(gottentext):
    #the actual text to speech
    sound = gTTS(text=gottentext[0],lang=gottentext[1],slow=False)
    
    #save sound temporarily so it can be played later
    sound.save('temp_sound.mp3')

    #play sound
    pygame.mixer.music.load("temp_sound.mp3")
    pygame.mixer.music.play()
