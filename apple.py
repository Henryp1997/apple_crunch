
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
from scipy.io import wavfile

samplerate, data = wavfile.read('0004_c2.wav')

peaks = []
for i, val in enumerate(data):
    if data[i] > 5000:
        peaks.append(i)

peak_locs = []
for i, val in enumerate(peaks):
    try:
        if peaks[i+1] > val + 5000:
            peak_locs.append(i)
    except:
        peak_locs.append(i)
        pass

for i in peak_locs:
    plt.plot(data[peaks[i]-2500:peaks[i]+2500])
    plt.savefig(f'test{i}.png')
    plt.show()

