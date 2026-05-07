import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, ifft, fftshift, ifftshift, fftfreq

sample_rate, data = wavfile.read('sample-6s.wav')
if data.ndim > 1:
    data = data[:, 0]
signal = data.astype(float)
n = len(signal)

def apply_filter_in_freq(signal, sample_rate, mask_func):
    n = len(signal)
    spectrum = fft(signal)
    spectrum_shifted = fftshift(spectrum)
    freqs = fftfreq(n, 1/sample_rate)
    freqs_shifted = fftshift(freqs)
    mask = mask_func(freqs_shifted)
    filtered_spectrum_shifted = spectrum_shifted * mask
    filtered_spectrum = ifftshift(filtered_spectrum_shifted)
    filtered_signal = np.real(ifft(filtered_spectrum))
    return filtered_signal

plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
time = np.arange(n) / sample_rate
plt.plot(time, signal)
plt.title('Исходный сигнал (время)')
plt.xlabel('Время, с')
plt.ylabel('Амплитуда')
spectrum = fft(signal)
spectrum_shifted = fftshift(spectrum)
freqs = fftfreq(n, 1/sample_rate)
freqs_shifted = fftshift(freqs)
magnitude = np.abs(spectrum_shifted)

plt.subplot(3, 2, 2)
plt.semilogy(freqs_shifted, magnitude)
plt.title('Амплитудный спектр')
plt.xlabel('Частота, Гц')
plt.ylabel('|FFT|')
plt.xlim(0, sample_rate/2)

def lowpass_mask(freqs, cutoff=1000):return np.where(np.abs(freqs) <= cutoff, 1, 0)
def highpass_mask(freqs, cutoff=1000):return np.where(np.abs(freqs) >= cutoff, 1, 0)
def bandpass_mask(freqs, low=500, high=2000):return np.where((np.abs(freqs) >= low) & (np.abs(freqs) <= high), 1, 0)
def notch_mask(freqs, notch_freq=1000, width=50):return np.where((np.abs(freqs) < notch_freq - width) | (np.abs(freqs) > notch_freq + width), 1, 0)

filters = [
    ('Low-pass (1000 Hz)', lowpass_mask, {'cutoff': 1000}),
    ('High-pass (1000 Hz)', highpass_mask, {'cutoff': 1000}),
    ('Band-pass (500–2000 Hz)', bandpass_mask, {'low': 500, 'high': 2000}),
    ('Notch (1000 Hz)', notch_mask, {'notch_freq': 1000, 'width': 50})
]

plt.subplot(3, 2, 3)
for i, (name, mask_func, kwargs) in enumerate(filters):
    filtered = apply_filter_in_freq(signal, sample_rate, lambda f: mask_func(f, **kwargs))
    mse = np.mean((signal - filtered)**2)
    plt.subplot(3, 2, 3 + i)
    time_short = time[:int(0.1 * sample_rate)]
    sig_short = filtered[:int(0.1 * sample_rate)]
    plt.plot(time_short, sig_short)
    plt.title(f'{name}\nMSE = {mse:.4f}')
    plt.xlabel('Время, с')
    plt.ylabel('Амплитуда')

plt.tight_layout()
plt.show()
wavfile.write('filtered_lowpass.wav', sample_rate, filtered.astype(np.int16))