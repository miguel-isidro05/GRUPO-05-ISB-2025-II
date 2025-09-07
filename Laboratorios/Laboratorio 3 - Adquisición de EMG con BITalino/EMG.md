# LABORATORIO 3: Uso de BITalino para EMG


### Introducción
La electromiografía (EMG) es una prueba diagnóstica que evalúa el estado y salud de los músculos así como de los nervios que los controlan [1].
En una prueba EMG se analizan las señales eléctricas que emiten los músculos cuando están en reposo y en movimiento. Gracias a estas evaluaciones se puede detectar si existe una afección o transtorno muscular [2].
Durante la contracción muscular, ya sea en reposo en un músculo normal o anormal, el sistema nervioso envía impulsos eléctricos a través de las neuronas motoras las cuales activan las fibras musculares generando un potencial de acción muscular que produce la contracción[3]. De este modo las pruebas de EMG proporcionan datos sobre los impulsos nerviosos y las reacciones de las fibras musculares.

Para obtener dichas señales fisiológicas se hace uso del BITalino, un dispositivo que permite la recolección de datos biomédicos. Este equipo cuenta con sensores diseñados para la obtención de EDA, ECG, EEG y EMG. Además, cuenta con el software OpenSignals (r)evolution para visualizar en tiempo real las señales adquiridas, almacenarlas y exportarlas para un posterior análisis. 


### Objetivos específicos de la práctica
* Familiarizarse con el hardware y software del BITalino para el procesamiento de señales EMG.
* Registrar señales EMG en reposo y contracción en diferentes grupos musculares.
* Aplicar filtros y procesamiento a las señales obtenidas del software para mejorar la calidad.
* Analizar e interpretar las señales obtenidas.


### Materiales y equipos

|  **Materiales**  | **Detalles** | **Cantidad** |
|:------------:|:---------------:|:---------------:|
|  Kit BITalino   | (R)EVOLUTION   | 1 |
|   Laptop | Software OpenSignals | 1 |
|   Electrodos |  | 3 |

### Procedimiento


### Resultados

### Referencias
[1]
[2]
[3]

<<<<<<< HEAD
=======

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


>>>>>>> 6616ee31046ed1120ed4c53d722effb6a9966ba1
