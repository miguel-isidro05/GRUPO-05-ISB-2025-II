import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import filtfilt, freqz

# Cargamos el archivo EMG
datos = np.loadtxt("D:/CICLO 2025- II/ISB/Lab Filtros Digitales/Laboratorio 7- Filtros FIR IIR/Señales EMG/leve1_biceps.txt", comments="#")
emg = datos[:, -1]
fs = 1000
tiempo = np.linspace(0, len(emg) / fs, len(emg))

# Coeficientes
chev1 = pd.read_csv("D:/CICLO 2025- II/ISB/Lab Filtros Digitales/Laboratorio 7- Filtros FIR IIR/Señales EMG/chev1.csv", header=None)
b_chev1, a_chev1 = chev1[0].to_numpy(), chev1[1].to_numpy()
chev2 = pd.read_csv("D:/CICLO 2025- II/ISB/Lab Filtros Digitales/Laboratorio 7- Filtros FIR IIR/Señales EMG/chev2.csv", header=None)
b_chev2, a_chev2 = chev2[0].to_numpy(), chev2[1].to_numpy()
bessel = pd.read_csv("D:/CICLO 2025- II/ISB/Lab Filtros Digitales/Laboratorio 7- Filtros FIR IIR/Señales EMG/bessel.csv", header=None)
b_bessel, a_bessel = bessel[0].to_numpy(), bessel[1].to_numpy()

# Filtrado usando filtfilt
emg_chev1 = filtfilt(b_chev1, a_chev1, emg)
emg_chev2 = filtfilt(b_chev2, a_chev2, emg)
emg_bessel = filtfilt(b_bessel, a_bessel, emg)

# Señal cruda
plt.figure(figsize=(10, 4))
plt.plot(tiempo, emg, color="#00008B", linewidth=0.4)
plt.title("Señal EMG cruda")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (uV)")
plt.grid()
plt.show()

# Señales filtradas
plt.figure(figsize=(12, 8))
plt.subplot(3,1,1)
plt.plot(tiempo, emg_chev1, 'r')
plt.title("EMG filtrada - Chebyshev1")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (uV)")
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(tiempo, emg_chev2, 'g')
plt.title("EMG filtrada - Chebyshev2")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (uV)")
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(tiempo, emg_bessel, 'b')
plt.title("EMG filtrada - Bessel")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (uV)")
plt.grid(True)

plt.tight_layout()
plt.show()

# Respuesta en frecuencia
w1, H1 = freqz(b_chev1, a_chev1, worN=8000)
w2, H2 = freqz(b_chev2, a_chev2, worN=8000)
w3, H3 = freqz(b_bessel, a_bessel, worN=8000)

freq1, freq2, freq3 = w1*fs/(2*np.pi), w2*fs/(2*np.pi), w3*fs/(2*np.pi)
eps = 1e-12

plt.figure(figsize=(10, 5))
plt.plot(freq1, 20*np.log10(np.abs(H1)+eps), 'r', label="Chebyshev1")
plt.plot(freq2, 20*np.log10(np.abs(H2)+eps), 'g', label="Chebyshev2")
plt.plot(freq3, 20*np.log10(np.abs(H3)+eps), 'b', label="Bessel")
plt.title("Respuesta en Frecuencia de Filtros EMG")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (dB)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
