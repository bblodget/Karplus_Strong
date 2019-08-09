#!/usr/bin/env python

import numpy as np
import sounddevice as sd
import time
from scipy.io.wavfile import write


#Samples per second
sps = 44100

# Frequency / pitch of sine wave
freq_hz = 440.0

# Duration
duration_s = 3.0

# Attenuation so sound is reasonable
atten = 0.3

# NumPy magic
each_sample_number = np.arange(duration_s * sps)
waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sps)
waveform_quiet = waveform * atten

# Play waveform out the speakers
sd.play(waveform_quiet, sps)
time.sleep(duration_s)
sd.stop()

#waveform_integers = np.int16(waveform_quiet * 32767)
#write('sine_wave.wav', sps, waveform_integers)


