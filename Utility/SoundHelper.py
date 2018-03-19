import pygame
import time

class SoundHelper:
   
   def SetInitial():
      pygame.mixer.init()
   
   def PlaySound(argName):
      _sound = pygame.mixer.Sound(argName)
      _sound.play()

   # play the sound file for 10 seconds and then stop it
   mysound.play()
   time.sleep(20)

   def PlayAlarmSound():
      SoundHelper.PlaySound("src\\Sound\\AlarmSlow")