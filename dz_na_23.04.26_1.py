import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, ifft, fftshift, ifftshift, fftfreq
'''
выводы:
нотч имба и не контрится, он почти не портит файл
бэнд- и хайпасс дают эффект "приглушенности"
а лоупасс дает что-то не совсем описуемое, но искажение очевидно
'''
# ---------- Настраиваемые параметры (коэффициенты "испорченности") ----------
lowpass_cutoff = 1000  # частота среза для ФНЧ (Гц)
highpass_cutoff = 1000  # частота среза для ФВЧ (Гц)
bandpass_low = 500  # нижняя граница полосового фильтра (Гц)
bandpass_high = 2000  # верхняя граница полосового фильтра (Гц)
notch_freq = 1000  # центральная частота режекторного фильтра (Гц)
notch_width = 50  # ширина режекторной полосы (Гц)

# Общий коэффициент усиления (можно менять, чтобы сделать сигнал тише/громче)
amplify = 1.0  # 1.0 — без изменения

# -------------------------------------------------------------------------

sample_rate, data = wavfile.read('sample-6s.wav')
if data.ndim > 1:
    data = data[:, 0]
signal = data.astype(float)
n = len(signal)


def apply_filter_in_freq(signal, sample_rate, mask_func):
    n = len(signal)
    spectrum = fft(signal)
    spectrum_shifted = fftshift(spectrum)
    freqs = fftfreq(n, 1 / sample_rate)
    freqs_shifted = fftshift(freqs)
    mask = mask_func(freqs_shifted)
    filtered_spectrum_shifted = spectrum_shifted * mask
    filtered_spectrum = ifftshift(filtered_spectrum_shifted)
    filtered_signal = np.real(ifft(filtered_spectrum))
    return filtered_signal


# Функции масок (используют глобальные переменные)
def lowpass_mask(freqs):
    return np.where(np.abs(freqs) <= lowpass_cutoff, 1, 0)


def highpass_mask(freqs):
    return np.where(np.abs(freqs) >= highpass_cutoff, 1, 0)


def bandpass_mask(freqs):
    return np.where((np.abs(freqs) >= bandpass_low) & (np.abs(freqs) <= bandpass_high), 1, 0)


def notch_mask(freqs):
    return np.where((np.abs(freqs) < notch_freq - notch_width) | (np.abs(freqs) > notch_freq + notch_width), 1, 0)


# Список фильтров (имя, функция, имя файла)
filters = [
    ('Low-pass', lowpass_mask, 'filtered_lowpass.wav'),
    ('High-pass', highpass_mask, 'filtered_highpass.wav'),
    ('Band-pass', bandpass_mask, 'filtered_bandpass.wav'),
    ('Notch', notch_mask, 'filtered_notch.wav')
]

# Построение графиков и сохранение файлов
plt.figure(figsize=(12, 10))

# Исходный сигнал
plt.subplot(3, 2, 1)
time = np.arange(n) / sample_rate
plt.plot(time, signal)
plt.title('Исходный сигнал (время)')
plt.xlabel('Время, с')
plt.ylabel('Амплитуда')

# Спектр исходного сигнала
spectrum = fft(signal)
spectrum_shifted = fftshift(spectrum)
freqs = fftfreq(n, 1 / sample_rate)
freqs_shifted = fftshift(freqs)
magnitude = np.abs(spectrum_shifted)
plt.subplot(3, 2, 2)
plt.semilogy(freqs_shifted, magnitude)
plt.title('Амплитудный спектр')
plt.xlabel('Частота, Гц')
plt.ylabel('|FFT|')
plt.xlim(0, sample_rate / 2)

# Обработка каждого фильтра
filtered_signals = []
for i, (name, mask_func, outfile) in enumerate(filters):
    filtered = apply_filter_in_freq(signal, sample_rate, mask_func)
    # Применяем дополнительное масштабирование (коэффициент "испорченности")
    filtered = filtered * amplify
    filtered_signals.append(filtered)

    # Сохраняем в WAV (нормализуем к int16, если нужно)
    # Для предотвращения клиппирования ограничиваем диапазон
    max_val = np.max(np.abs(filtered))
    if max_val > 0:
        filtered_norm = filtered / max_val * 32767
    else:
        filtered_norm = filtered
    wavfile.write(outfile, sample_rate, filtered_norm.astype(np.int16))

    # Отображаем фрагмент (0.1 секунды)
    plt.subplot(3, 2, 3 + i)
    time_short = time[:int(0.1 * sample_rate)]
    sig_short = filtered[:int(0.1 * sample_rate)]
    plt.plot(time_short, sig_short)
    mse = np.mean((signal - filtered) ** 2)
    plt.title(f'{name}\nMSE = {mse:.4f}')
    plt.xlabel('Время, с')
    plt.ylabel('Амплитуда')

plt.tight_layout()
plt.show()

print("Обработка завершена. Созданы файлы:")
for _, _, outfile in filters:
    print(f"  {outfile}")