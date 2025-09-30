import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import lfilter, freqz

# Leer archivo de señal
with open("D:/CICLO 2025- II/ISB/Lab Filtros Digitales/Laboratorio 7- Filtros FIR IIR/Señales EKG/apnea_10seg_toma1.txt", "r") as f:
    lineas = f.readlines()
datos = np.array([line.strip().split() for line in lineas if not line.startswith("#")], dtype=float)

ecg = datos[:, -1] * -1   # señal ECG
fs = 1000                 # frecuencia de muestreo
tiempo = np.arange(len(ecg)) / fs


#con worN definimos la resolucion
# Cargar coeficientes FIR - Hamming
h = pd.read_csv("FIR_hamming.csv", names=["h"])["h"].to_numpy()
w_ham, H_ham = freqz(h, worN=2048, fs=fs)
# Cargar coeficientes FIR - Hann
hann = pd.read_csv("FIR_hann.csv", names=["hann"])["hann"].to_numpy()
w_hann, H_hann = freqz(hann, worN=2048, fs=fs)
# Cargar coeficientes FIR - Blackman
blackm = pd.read_csv("FIR_blackman.csv", names=["blackm"])["blackm"].to_numpy()
w_blackm, H_blackm = freqz(blackm, worN=2048, fs=fs)


# Filtrar señal con el FIR Hamming 
ecg_filtrada = lfilter(h, 1.0, ecg)
# Filtrar señal con el FIR Hann
ecg_filtrada1 = lfilter(hann, 1.0, ecg)
# Filtrar señal con el FIR blackman
ecg_filtrada2 = lfilter(blackm, 1.0, ecg)


# Ploteo de señal cruda vs filtrada-HAMMING
plt.figure(figsize=(10, 4))
plt.subplot(2, 1, 1)
plt.plot(tiempo, ecg, 'gray', linewidth=0.7)
plt.title("ECG cruda")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.xlim(0, 15)
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(tiempo, ecg_filtrada, 'blue', linewidth=0.8)
plt.title("ECG filtrada con FIR (Hamming)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.xlim(0, 15)
plt.grid()
plt.tight_layout()
plt.show()


# Ploteo de señal cruda vs filtrada-Hann
plt.figure(figsize=(10, 4))
plt.subplot(2, 1, 1)
plt.plot(tiempo, ecg, 'gray', linewidth=0.7)
plt.title("ECG cruda")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.xlim(0, 15)
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(tiempo, ecg_filtrada1, 'blue', linewidth=0.8)
plt.title("ECG filtrada con FIR (Hann)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.xlim(0, 15)
plt.grid()
plt.tight_layout()
plt.show()


# Ploteo de señal cruda vs filtrada-Blackman
plt.figure(figsize=(10, 4))
plt.subplot(2, 1, 1)
plt.plot(tiempo, ecg, 'gray', linewidth=0.7)
plt.title("ECG cruda")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.xlim(0, 15)
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(tiempo, ecg_filtrada2, 'blue', linewidth=0.8)
plt.title("ECG filtrada con FIR (Blackman)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.xlim(0, 15)
plt.grid()
plt.tight_layout()
plt.show()

# Respuesta en frecuencia de los 3 enventanamientos
plt.figure(figsize=(10, 5))

plt.plot(w_ham, 20*np.log10(np.abs(H_ham)), 'b', label="Hamming")
plt.plot(w_hann, 20*np.log10(np.abs(H_hann)), 'r', label="Hann")
plt.plot(w_blackm, 20*np.log10(np.abs(H_blackm)), 'g', label="Blackman")

plt.title("Respuestas en Frecuencia de Filtros FIR")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud [dB]")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

#########################################################################33
#FILTROS IIR
#Butterworth
iir1 = pd.read_csv("D:/CICLO 2025- II/ISB/Lab Filtros Digitales/Laboratorio 7- Filtros FIR IIR/Señales EKG/IIR-butterworth.csv", header=None)
b1 = iir1[0].to_numpy()
a1 = iir1[1].to_numpy()
w1_iir, H1_iir = freqz(b1,a1, worN=8000)
#Chevyshev1
iir2 = pd.read_csv("D:/CICLO 2025- II/ISB/Lab Filtros Digitales/Laboratorio 7- Filtros FIR IIR/Señales EKG/IIR-CHEV1.csv", header=None)
b2 = iir2[0].to_numpy()
a2 = iir2[1].to_numpy()
w2_iir, H2_iir = freqz(b2,a2, worN=8000)

#Filtramos la señal
ecg_butter = lfilter(b1, a1, ecg)
ecg_chevy  = lfilter(b2, a2, ecg)


plt.figure(figsize=(10, 5))
# Butterworth
plt.subplot(2,1,1)
plt.plot(tiempo, ecg_butter, 'b')
plt.title("EEG filtrada - Butterworth")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.grid(True)
# Chebyshev1
plt.subplot(2,1,2)
plt.plot(tiempo, ecg_chevy, 'r')
plt.title("EEG filtrada - Chebyshev1")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.grid(True)
plt.tight_layout()
plt.show()

#Respuestas en frecuencia
plt.plot(w1_iir, 20*np.log10(np.abs(H1_iir)), 'b', label="IIR Filtro Butterworth")
plt.plot(w2_iir, 20*np.log10(np.abs(H2_iir)), 'r', label="IIR Filtro Chevyshev 1")

plt.title("Respuestas en Frecuencia de Filtros IIR")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud [dB]")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()




