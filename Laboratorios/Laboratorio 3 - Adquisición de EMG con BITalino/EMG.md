# **LABORATORIO 3: Uso de BITalino para EMG**

## **Tabla de contenidos**

1. [Introducción](#id1)
2. [Objetivos específicos de la práctica](#id2)
3. [Materiales y equipos](#id3)
4. [Procedimiento](#id4)\
     4.1. [EMG - Biceps Braquial](#id5)\
     4.2. [EMG - Triceps](#id6)
5. [Resultados](#id7)
6. [Análisis y discusión](#id8)
7. [Referencias](#id9)

## **1. Introducción** <a name="id1"></a>
La electromiografía (EMG) es una prueba diagnóstica que evalúa el estado y salud de los músculos así como de los nervios que los controlan [1].
En una prueba EMG se analizan las señales eléctricas que emiten los músculos cuando están en reposo y en movimiento. Gracias a estas evaluaciones se puede detectar si existe una afección o transtorno muscular [2].
Durante la contracción muscular, ya sea en reposo en un músculo normal o anormal, el sistema nervioso envía impulsos eléctricos a través de las neuronas motoras las cuales activan las fibras musculares generando un potencial de acción muscular que produce la contracción[3]. De este modo las pruebas de EMG proporcionan datos sobre los impulsos nerviosos y las reacciones de las fibras musculares.

<img width="486" height="294" alt="image" src="https://github.com/user-attachments/assets/62238343-b1b6-4886-ab35-aeaaddf7090f" />

***Fig 1**. Registro electromiografico [4].*

Para obtener dichas señales fisiológicas se hace uso del BITalino, un dispositivo que permite la recolección de datos biomédicos. Este equipo cuenta con sensores diseñados para la obtención de EDA, ECG, EEG y EMG. Además, cuenta con el software OpenSignals (r)evolution para visualizar en tiempo real las señales adquiridas, almacenarlas y exportarlas para un posterior análisis. 


## **2. Objetivos específicos de la práctica** <a name="id2"></a>
* Familiarizarse con el hardware y software del BITalino para el procesamiento de señales EMG.
* Registrar señales EMG en reposo y contracción en diferentes grupos musculares.
* Aplicar filtros y procesamiento a las señales obtenidas del software para mejorar la calidad.
* Analizar e interpretar las señales obtenidas.


## **3. Materiales y equipos** <a name="id3"></a>

| Materiales                                   | Cantidad | Imagen                          |
|----------------------------------------------|----------|---------------------------------|
| Batería 3.7V                                 | 1        | ![bateria](https://github.com/user-attachments/assets/25fe9643-a7fa-4bd9-85ad-e1ce78a926ab) |
| Software OpenSignals                         | 1        | ![opensignals](https://github.com/user-attachments/assets/270de790-173f-42fc-9960-5b12a7fff042) |
| Electrodos de superficie descartables        | 3        | ![electrodos (1)](https://github.com/user-attachments/assets/2e58ad27-7c4a-4336-9fdf-fe54129be397) |
| Cable de los 3 electrodos                    | 1        | ![cable](https://github.com/user-attachments/assets/2d397e32-3ec4-4982-91fe-0d6855e3aec0) |
| Kit BITalino                                 | 1        | ![bitalino](https://github.com/user-attachments/assets/a60c127f-27c2-4a03-b852-454d23f54163) |
| Laptop                                       | 1        | ![laptop](https://github.com/user-attachments/assets/c1394461-1a65-41fc-b6f4-8d8ae5b3b37b) |

## **4. Procedimiento** <a name="id4"></a>
1. Se debe seleccionar el músculo a evaluar y limpiar la zona. De ser posible seleccionar una zona sin vellos para mejorar la impedancia de los electródos.
2. Colocar 2 electrodos (Positivo y Negativo) en el músculo objetivo y un tercer electrodo de referencia sobre una región electricamente muerta. En el presente laboratorio se eligio poner el electrodo en la cresta hiliaca (hueso de la cadera).
3. Sincronizar mediante protocolo Bluetooth el BITalino y la computadora con el software previamente instalado
4. Realizar las mediciones con el software de 3 diferentes ejercicios para cada músculo: en reposo, fuerza leve sin oposición y fuerza con oposición.

### **4.1. Configuración de electrodos** <a name="id20"></a>
Configuración de registro bipolar diferencial en EMG de superficie



### **4.2. EMG - Biceps Braquial** <a name="id5"></a>
La ubicación más recomendada para la colocación de electrodos en el bíceps braquial es sobre el vientre muscular, específicamente entre la zona de inervación y el tendón distal, ya que esta localización mejora la estabilidad de la señal y reduce el ruido en el registro electromiográfico [5]. En investigaciones recientes, se ha demostrado que registrar en esta franja permite obtener señales más estables y con menor interferencia de músculos vecinos en comparación con ubicaciones cercanas al tendón o en los bordes del músculo [6]. Para garantizar la calidad de la señal, se sugiere mantener una separación entre electrodos de aproximadamente 20 mm, lo cual equilibra la amplitud y disminuye el riesgo de contaminación de la actividad de otros músculos. Además, los electrodos deben colocarse alineados en dirección a las fibras musculares, ya que una orientación transversal u oblicua puede atenuar la propagación de los potenciales de acción.

<img width="641" height="550" alt="image" src="https://github.com/user-attachments/assets/3b785460-04fd-43c8-9163-934d44616a94" />

***Fig. X.** Puntos de ubicación de electrodos [6]*

A continuación, presentamos el material audiovisual del EMG en entranamiento con el biceps braquial:

<div align="center">
 
|  **Biceps en reposo**  | **Biceps sin oposición** | **Biceps con oposición** |
|:----------------------:|:------------------------:|:------------------------:|
| <video src="https://github.com/user-attachments/assets/a20d28f2-9160-462d-9f0d-921bce4582ed"></video> | <video src="https://github.com/user-attachments/assets/e34ea912-98a3-4a99-8bbd-69a006e5b189"></video> | <video src="https://github.com/user-attachments/assets/582a7d62-79ef-40fb-a2c3-521d561ef5de"></video> |

</div>


### **4.3. EMG - Triceps** <a name="id6"></a>
En la literatura más reciente sobre electromiografía de superficie (EMG), se ha señalado la importancia de mantener protocolos estandarizados de colocación de electrodos en músculos como el bíceps y el tríceps. Un estudio publicado en 2025 destacó que, aunque las recomendaciones clásicas como las del proyecto SENIAM siguen siendo la base de la práctica actual, el foco de los nuevos trabajos está puesto en la integridad de los datos y la consistencia de los registros, más que en proponer cambios sustanciales en la ubicación de los electrodos [7]. Esto implica que la posición en el vientre muscular del tríceps continúa siendo válida, siempre y cuando se respete una correcta orientación y separación de los electrodos.
Del mismo modo, otra revisión también de 2025, aunque centrada en el tríceps sural, ofrece conclusiones relevantes que pueden extrapolarse al tríceps braquial. Este trabajo subraya la necesidad de reducir el crosstalk o interferencia de músculos adyacentes, así como de minimizar la variabilidad espacial en los registros EMG. Para lograrlo, recomienda mantener los electrodos alineados con las fibras musculares y situarlos en el vientre del músculo, lo que asegura un registro más selectivo y confiable [8].

<img width="654" height="476" alt="image" src="https://github.com/user-attachments/assets/581a91c7-ce45-4b64-a8a4-f2987a88e074" />

***Fig. X.** Ubicación de electrodos para la realización de ejercicios [3]*

A continuación, presentamos el material audiovisual del EMG en entranamiento con el triceps:

<div align="center">
 
|  **Triceps en reposo**  | **Triceps sin oposición** | **Triceps con oposición** |
|:----------------------:|:------------------------:|:------------------------:|
| <video src="https://github.com/user-attachments/assets/122f538e-1267-4ab4-ba6d-a0584519151f" controls></video> | <video src="https://github.com/user-attachments/assets/5412d4e4-d70a-40e8-b306-6c804fc63fcb" controls></video> | <video src="https://github.com/user-attachments/assets/dc13e13e-e735-4437-a025-f35a0cd603c7" controls></video> |

</div>




## **5. Resultados** <a name="id7"></a>

Para los resultados haremos uso del archivo "CodigosEMG.ipynb" que se encuentra en el mismo folder. El cual contiene todos los codigos hechos para la visualización de las gráficas de las señales adquiridas. Asi como su respectivo filtrado y análisis de frecuencia.

### **5.1. Procesamiento y visualización de gráficas con python**
### a) Importar librerias
Importamos las librerias a utilizar que son comunes para el codigo de cada señal graficada.
```python
import numpy as np
import matplotlib.pyplot as plt
import neurokit2 as nk
from scipy.signal import butter, filtfilt
```
### b) Cargar el archivo
Cargamos el archivo .txt según la ruta en la que este almacenada en el ordenador local (Se muestra el ejemplo para la señal del músculo Biceps Braquial en reposo)
```python
ruta = r"D:\IB PUCP - UPCH 2022\7mo Semestre\Introducción a las Señales Biomédicas\Lab 3 - Adquisicion EMG\pythoooooon\Biceps\Reposo\reposo1_biceps.txt"
datos = np.loadtxt(ruta, comments="#")
emg = datos[:, -1]  # señal EMG en la última columna
```
### c) Definimos variables de la señal para la visualización
```python
fs = 1000  # frecuencia de muestreo
tiempo = np.linspace(0, len(emg) / fs, len(emg))
```
### d) Graficamos la señal original
```python
plt.figure(figsize=(10, 4))
plt.plot(tiempo, emg, color="#00008B", linewidth=0.4)
plt.title("Señal EMG cruda")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (uV)")
plt.grid()
plt.show()
```
### e) Filtramos la señal
```python
#Función filtro pasa-banda
def filtro_pasabanda(señal, f_muestreo, frec_baja=20.0, frec_alta=450.0, orden=4):
    nyquist = 0.5 * f_muestreo  
    bajo = frec_baja / nyquist
    alto = frec_alta / nyquist
    b, a = butter(orden, [bajo, alto], btype="band")
    return filtfilt(b, a, señal)
# Aplicar el filtro pasa-banda
emg_filtrada = filtro_pasabanda(emg, fs)
```
### f) Graficamos la señal filtrada
```python
plt.figure(figsize=(10, 4))
plt.plot(tiempo, emg_filtrada, color="#006400", linewidth=0.4)
plt.title("Señal EMG con filtro pasa-banda (20–450 Hz)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (uV)")
plt.grid()
plt.show()
```
### **5.2. EMG - Biceps Braquial**
| Entrenamiento                                   | Señal original | Señal filtrada                         |
|----------------------------------------------|----------|---------------------------------|
| Reposo                              | <img width="867" height="391" alt="image" src="https://github.com/user-attachments/assets/c16b9bc8-bdce-4fcc-9b4e-b33b1bd82a2a" />| <img width="847" height="391" alt="image" src="https://github.com/user-attachments/assets/b9769556-36ce-4faf-9fad-55ae2ef1dd7e" /> |
| Movimiento leve sin oposición                        | <img width="850" height="391" alt="image" src="https://github.com/user-attachments/assets/1d1b1b80-523d-46ac-918b-7e19b1e89abb" /> | <img width="853" height="391" alt="image" src="https://github.com/user-attachments/assets/2513ad6d-c603-49da-af74-559656b3eeae" /> |
| Movimiento acelerado       | <img width="850" height="391" alt="image" src="https://github.com/user-attachments/assets/ab4ae997-9c47-49a4-9402-0260dc1e01c1" />        | <img width="862" height="391" alt="image" src="https://github.com/user-attachments/assets/9aa04e88-00ff-4c14-98a7-cc5472db8d07" /> |
| Movimiento fuerte con oposición                   | <img width="859" height="391" alt="image" src="https://github.com/user-attachments/assets/c204fa2b-b28d-4d90-b56a-a35dd35ffcdc" />       | <img width="862" height="391" alt="image" src="https://github.com/user-attachments/assets/989336a7-0473-4f46-bf8f-6259bf8d8ff8" />|

### 5.3. EMG - Triceps
| Entrenamiento                                   | Señal original | Señal filtrada                         |
|----------------------------------------------|----------|---------------------------------|
| Reposo                              | <img width="850" height="391" alt="image" src="https://github.com/user-attachments/assets/8676c769-ad5d-4631-9343-7881bbf88504" /> | <img width="853" height="391" alt="image" src="https://github.com/user-attachments/assets/5b390bc0-006f-4f8d-8d59-d11abfa55797" /> |
| Movimiento leve sin oposición                        | <img width="850" height="391" alt="image" src="https://github.com/user-attachments/assets/b9d306f2-59c4-4a3e-9159-d60378883d1a" /> | <img width="853" height="391" alt="image" src="https://github.com/user-attachments/assets/d690bf7d-f351-428c-ba18-119ffb22c6a9" /> |
| Movimiento acelerado       | <img width="859" height="391" alt="image" src="https://github.com/user-attachments/assets/a97481da-37c2-4b32-b61d-0e9313cfd1f1" /> | <img width="862" height="391" alt="image" src="https://github.com/user-attachments/assets/f35858c7-14c3-4e0c-9362-41c60bbf696e" /> |
| Movimiento fuerte con oposición                   | <img width="850" height="391" alt="image" src="https://github.com/user-attachments/assets/5b7c9897-2e83-4b18-9700-099d2cd50754" /> | <img width="862" height="391" alt="image" src="https://github.com/user-attachments/assets/1e16657f-b5b2-4e3b-8c0a-a6034a05b19b" /> |


## **6. Análisis y discusión** <a name="id8"></a>
### **6.1. Análisis del EMG - Biceps Braquial** <a name="id8"></a>

### **6.2. Análisis del EMG - Triceps** <a name="id8"></a>

## **7. Referencias** <a name="id9"></a>
[1] M. B. I. Raez, M. S. Hussain y F. Mohd-Yasin, “Techniques of EMG signal analysis: detection, processing, classification and applications,” Biological Procedures Online, vol. 8, pp. 115–145, ene. 2006, PMCID: PMC1455479.

[2] Cleveland Clinic, “EMG (Electromyography),” Cleveland Clinic Health Library, última revisión el 2 de marzo de 2023. Disponible en: my.clevelandclinic.org/health/diagnostics/4825-emg-electromyography

[3] Ahmet Kocyigit, Nehal Shah, Angeliki Chorti y Kim Jackson, “Electromyogram,” Physiopedia, ed. Ahmet Kocyigit, fecha de publicación o revisión no disponible, disponible en: Physiopedia.com/Electromyogram

[4] mDurance Solutions S.L., “¿Qué es la electromiografía de superficie o EMG?,” Blog de mDurance, 25 de julio de 2019. Disponible en: mdurance.com/blog/que-es-la-electromiografia-de-superficie/

[5]  N. R. Prasad, N. Burhan, and A. H. Abdullah, "Prediction of biceps muscle electromyogram signal using a NARX neural network," Journal of Healthcare Engineering, vol. 2021, Article ID 9928763, pp. 1–9, Apr. 2021. [Online]. Available: https://pmc.ncbi.nlm.nih.gov/articles/PMC8085855/

[6]  Y. Zhou, L. Wang, H. Chen, and X. Li, "Surface electromyography electrode placement between innervation zone and tendon: implications for signal quality," Sensors, vol. 23, no. 9, p. 46590, May 2023. [Online]. Available: https://pmc.ncbi.nlm.nih.gov/articles/PMC10246590/

[7] F. Martínez-Cabrera, J. López, and M. Torres, "Normalization protocols for EMG of biceps and triceps: ensuring data integrity in neuromuscular research," Sensors, vol. 25, no. 9, p. 2668, May 2025. [Online]. Available: https://www.mdpi.com/1424-8220/25/9/2668

[8]  B. Shuman et al., “Assessment of common electrode placement methods for surface EMG recordings of the triceps surae muscles,” Journal of Electromyography Applications, preprint, 2025. [Online]. Available: https://www.researchgate.net/publication/393277200_Assessment_of_Common_Electrode_Placement_Methods_for_Surface_Electromyography_Recordings_of_the_Triceps_Surae_Muscles
