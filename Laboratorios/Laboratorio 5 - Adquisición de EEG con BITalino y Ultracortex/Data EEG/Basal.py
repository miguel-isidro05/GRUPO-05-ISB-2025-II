import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, iirnotch, welch

# Filtros
def filtro_pasabanda(senal, fs, frec_baja=0.5, frec_alta=40.0, orden=4):
    nyquist = 0.5 * fs
    bajo = frec_baja / nyquist
    alto = frec_alta / nyquist
    b, a = butter(orden, [bajo, alto], btype="band")
    return filtfilt(b, a, senal)

def filtro_notch(senal, fs, frec_notch=60.0, Q=30.0):
    nyquist = 0.5 * fs
    w0 = frec_notch / nyquist
    b, a = iirnotch(w0, Q)
    return filtfilt(b, a, senal)

# Cargamos los datos del archivo .txt de OpenSignals
datos = np.loadtxt("basal.txt", delimiter=None, comments="#")
eeg = datos[:, 5] #La señal se encuentra en ña 5 columna

fs = 1000  
t = np.arange(len(eeg)) / fs

#Señal filtrada
eeg_filtrado = filtro_pasabanda(eeg, fs, 0.5, 40)
eeg_filtrado = filtro_notch(eeg_filtrado, fs, 60)

#FFT
fft_vals_cruda = np.fft.rfft(eeg)
fft_freqs_cruda = np.fft.rfftfreq(len(eeg), 1/fs)
fft_db_cruda = 20*np.log10(np.maximum(np.abs(fft_vals_cruda),1e-12)/np.max(np.abs(fft_vals_cruda)))

# FFT filtrada
fft_vals_filt = np.fft.rfft(eeg_filtrado)
fft_freqs_filt = np.fft.rfftfreq(len(eeg_filtrado), 1/fs)
fft_db_filt = 20*np.log10(np.maximum(np.abs(fft_vals_filt),1e-12)/np.max(np.abs(fft_vals_filt)))

#PSD (Welch)
f_cruda, psd_cruda = welch(eeg, fs=fs, nperseg=fs*2)
f_filt, psd_filt = welch(eeg_filtrado, fs=fs, nperseg=fs*2)

bandas = {"Delta (0.5–4 Hz)": (0.5, 4),"Theta (4–8 Hz)": (4, 8),"Alfa (8–12 Hz)": (8, 12),"Beta (13–30 Hz)": (13, 30),"Gamma (30–40 Hz)": (30, 40)}

potencias_cruda = []
for low, high in bandas.values():
    idx = np.logical_and(f_cruda >= low, f_cruda <= high)
    potencia = np.trapezoid(psd_cruda[idx], f_cruda[idx])
    potencias_cruda.append(potencia)

potencias_filt = []
for low, high in bandas.values():
    idx = np.logical_and(f_filt >= low, f_filt <= high)
    potencia = np.trapezoid(psd_filt[idx], f_filt[idx])
    potencias_filt.append(potencia)


colores = ["#FF6F61","#6B5B95","#88B04B","#FFA500","#00BFFF"]

# Ploteos
plt.figure(figsize=(12, 10))
#SEÑAL CRUDA
plt.subplot(4,1,1)
plt.plot(t, eeg, color="darkblue")
plt.title("EEG cruda")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (uV)")
plt.xlim(0, 10)
plt.grid()
#FFT
plt.subplot(4,1,2)
plt.plot(fft_freqs_cruda, np.abs(fft_vals_cruda), color="darkorange")
plt.title("FFT - EEG cruda")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.xlim(0, 100)
plt.ylim(0, 750000)
plt.grid()
#FFT en dB
plt.subplot(4,1,3)
plt.plot(fft_freqs_cruda, fft_db_cruda, color="darkgreen")
plt.title("FFT en dB - EEG cruda")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (dB)")
plt.xlim(0, 100)
plt.grid()
#Welch
plt.subplot(4,1,4)
plt.semilogy(f_cruda, psd_cruda, color="blue")
plt.title("PSD (Welch) - EEG cruda")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("PSD (uV^2/Hz)")
plt.xlim(0, 50)
plt.grid()

plt.tight_layout()
plt.show()

#PSD
plt.figure(figsize=(8,4))
plt.bar(bandas.keys(), potencias_cruda, color=colores)
plt.title("Potencia por banda - EEG cruda")
plt.ylabel("Potencia (uV^2)")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.ylim(0, 1000)
plt.show()

#SEÑAL FILTRADA 
plt.figure(figsize=(12, 10))

plt.subplot(4,1,1)
plt.plot(t, eeg_filtrado, color="darkgreen")
plt.title("EEG filtrada (0.5–40 Hz + notch 60 Hz)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (uV)")
plt.xlim(0,10)
plt.grid()
#FFT
plt.subplot(4,1,2)
plt.plot(fft_freqs_filt, np.abs(fft_vals_filt), color="darkred")
plt.title("FFT - EEG filtrada")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.xlim(0, 100)
plt.ylim(0, 220000)
plt.grid()
#FFT en dB
plt.subplot(4,1,3)
plt.plot(fft_freqs_filt, fft_db_filt, color="purple")
plt.title("FFT en dB - EEG filtrada")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (dB)")
plt.xlim(0, 100)
plt.grid()
#WELCH
plt.subplot(4,1,4)
plt.semilogy(f_filt, psd_filt, color="red")
plt.title("PSD (Welch) - EEG filtrada")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("PSD (uV^2/Hz)")
plt.xlim(0, 50)
plt.grid()

plt.tight_layout()
plt.show()

#PSD 
plt.figure(figsize=(8,4))
plt.bar(bandas.keys(), potencias_filt, color=colores)
plt.title("Potencia por banda - EEG filtrada")
plt.ylabel("Potencia (uV^2)")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.ylim(0, 1000)
plt.show()

