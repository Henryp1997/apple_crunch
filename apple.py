
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.fft import rfft, rfftfreq
import os

here = f'{os.path.dirname(os.path.realpath(__file__))}'

def separate_peaks(data):
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

    peak_data = [
        data[peaks[i] - 2500: peaks[i] + 2500] for i in peak_locs
    ]

    # plot data around peaks
    for j, arr in enumerate(peak_data):
        plt.plot(arr)
        plt.savefig(f'{here}/peaks/rg_c4_peak{j}.png')
    plt.close()

    return peak_data

samplerate, data = wavfile.read(f'{here}/recordings/rg_c4.wav')

peak_data = separate_peaks(data)

time = [i / samplerate for i in range(len(peak_data[0]))]

for i in peak_data:
    num_samples = len(i)
    yf = rfft(i)
    xf = rfftfreq(num_samples, 1 / samplerate)

    plt.plot(xf, np.abs(yf))
    plt.show()
