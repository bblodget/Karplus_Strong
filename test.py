#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import time


def synthesize(sampling_speed, wavetable, n_samples, atten):
    """Synthesizes a new waveform from an existing wavetable."""
    samples = []
    current_sample = 0
    while len(samples) < n_samples:
        current_sample += sampling_speed
        current_sample = current_sample % wavetable.size
        samples.append(wavetable[current_sample])
        current_sample += 1
    return np.array(samples) * atten

# Create the wave table
fs = 8000

# Duration
duration_s = 3.0

# Attenuation
atten = 0.3

t = np.linspace(0, 1, num=fs)
wavetable = np.sin(np.sin(2 * np.pi * t))

# Create samples
sample1 = synthesize(220, wavetable, duration_s * fs, atten)
sample2 = synthesize(440, wavetable, duration_s * fs, atten)

# Play the waveform out the speakers
sd.play(sample2, fs)
time.sleep(duration_s)
sd.stop()



