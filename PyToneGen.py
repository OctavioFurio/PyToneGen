import pygame
import time
import math
import numpy

pygame.init()
pygame.mixer.pre_init(44100, 16)

def sine_x(amp, freq, time):
    return int(round(amp * math.sin(2 * math.pi * freq * time)))

class toneGenerator:
    def sine(freq, duration):
        soundVector = numpy.zeros((44100, 2), dtype = numpy.int16)
        amp = 2 ** (15) - 1

        for samples in range(int(round(44100))):
            t = float(samples) / 44100

            sineValue = sine_x(amp, freq, t)

            soundVector[samples][0] = soundVector[samples][1] = sineValue

        generatedSound = pygame.sndarray.make_sound(soundVector)
        generatedSound.play(loops = duration, maxtime = int(duration * 100))
        time.sleep(duration / 10)