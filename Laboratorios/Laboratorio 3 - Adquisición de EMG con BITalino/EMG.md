# LABORATORIO 3: Uso de BITalino para EMG


### Introducción


### Objetivos específicos de la práctica


### Materiales y equipos

|  **Materiales**  | **Detalles** | **Cantidad** |
|:------------:|:---------------:|:---------------:|
|  Kit BITalino   | (R)EVOLUTION   | 1 |
|   Laptop |  | 1 |
|   Electrodos |  | 1 |

### Procedimiento


### Resultados

### Referencias


#FUERZA 1

import numpy as np
import matplotlib.pyplot as plt


# Cargar el archivo, sin contar el encabezado del archivo que empieza con '#'
datos = np.loadtxt("fuerza1_biceps.txt", comments="#")
#Obtenemos la seál EMG que está en la última posición  -1
emg = datos[:, -1]
fs=1000 #frecuencia de muestreo 
tiempo=np.linspace(0, len(emg) / fs, len(emg))

plt.figure(figsize=(10,4))
plt.plot(tiempo, emg, color="purple", linewidth=0.4)
plt.title("Señal EMG desde OpenSignals")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (uV)")
plt.grid()
plt.show()


