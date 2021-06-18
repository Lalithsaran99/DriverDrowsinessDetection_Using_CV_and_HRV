from pulsesensor import Pulsesensor
import time
import pygame
import threading
p = Pulsesensor()
p.startAsyncBPM()



try:
    while True:
        bpm = p.BPM
        if bpm <= 72.3 or bpm <= 90.7 or bpm == 81.5:
            pygame.mixer.init()
            pygame.mixer.music.load("alarm.wav")
            pygame.mixer.music.play()
            print("BPM: %d" % bpm)
            print("Drowsiness Detected")
        elif bpm > 0:
            print("BPM: %d" % bpm)
        elif bpm == 0:
            print("No Heartbeat found")
        time.sleep(1)
except:
    p.stopAsyncBPM()
