# Segue exemplo da aplicação do módulo PyToneGen

from time import thread_time
from PyToneGen import toneGenerator

import random

random.seed(thread_time())

# Possíveis notas geradas pelo programa
notes = [130, 147, 165, 174, 196, 220, 246, 261, 294, 329, 349, 392, 440, 493]
noteNames = ["C3", "D3", "E3", "F3", "G3", "A3", "B3", "C4", "D4", "E4", "F4", "G4", "A4", "B4"]

# Duração das notas (em centenas de ms)
durations = [2, 4, 8, 16]

# Valores iniciais
currentNote = 100 * (int(random.random() * 10) % 7)
currentDuration = 4

# Loop de geração de músicas
while True:
    # Variações pequenas para consistência melódica
    currentNote += (int(random.random() * 10) % 5) - 3
    currentDuration += ((int(random.random() * 10)) % 4)

    # Seleção das notas e durações
    freq = notes[currentNote % notes.__len__()]
    duration = durations[currentDuration % durations.__len__()]

    print("\tFrequency: %s Hz (%s)\t| Duration: %s ms" %(freq, noteNames[currentNote % notes.__len__()], 100 * duration))
    toneGenerator.sine(freq, duration)