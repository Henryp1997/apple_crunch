
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.fft import rfft, rfftfreq
import os
import glob

here = f'{os.path.dirname(os.path.realpath(__file__))}'

def separate_peaks(data, recording):
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
        plt.savefig(f'{here}/peak_plots/{recording.strip(".wav")}_peak{j}.png')
        plt.close()
    
    plt.plot(data)
    plt.savefig(f'{here}/waveforms/{recording.strip(".wav")}_full.png')
    plt.close()

    return peak_data

############
for recording in glob.glob(f'{here}/recordings/*.wav'):
    recording = recording.split("recordings\\")[1]
    samplerate, data = wavfile.read(f'{here}/recordings/{recording}')

    peak_data = separate_peaks(data, recording)

    # time = [i / samplerate for i in range(len(peak_data[0]))]

    for j, i in enumerate(peak_data):
        num_samples = len(i)
        yf = rfft(i)
        xf = rfftfreq(num_samples, 1 / samplerate)

        for k, val in enumerate(xf):
            if val > 4000:
                break
        
        x_plot, y_plot = xf[:k], np.abs(yf)[:k]

        plt.plot(x_plot, y_plot)
        plt.savefig(f'{here}/frequency_plots/{recording.strip(".wav")}_freq{j}.png')
        plt.close()
        # plt.show()
