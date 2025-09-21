# **LABORATORIO 5: Adquisicion de señales EEG con BITalino y Ultracortex**

## **Tabla de contenidos**

1. [Introducción](#id1)
2. [Objetivos de la práctica](#id2)
3. [Materiales e instrumentos](#id3)
4. [Metodologia](#id4)\
5. [Descripción de las señales](#id7)\
6. [Discusión](#id5)\
7. [Referencias](#id9)

## **1. Introducción** <a name="id1"></a>
La electroencefalografía (EEG) es una técnica no invasiva que permite registrar la actividad eléctrica del cerebro mediante electrodos colocados en el cuero cabelludo. Esta actividad se organiza en diferentes ritmos u ondas cerebrales, clasificados según su frecuencia y asociados a distintos estados fisiológicos y cognitivos [1,2]. Las ondas delta (0–4 Hz) predominan durante el sueño profundo y se relacionan con procesos de descanso y recuperación. Las ondas theta (4–8 Hz) se vinculan a estados de somnolencia y a la memoria de trabajo. Las ondas alfa (8–12 Hz) aparecen en condiciones de reposo y relajación, especialmente con los ojos cerrados, y se asocian a la atención y la meditación. Por su parte, las ondas beta (12–25 Hz) reflejan estados de alerta, concentración activa y control motor. Finalmente, las ondas gamma (>25 Hz) se relacionan con el procesamiento cognitivo rápido, la memoria y la resolución de problemas [2,3]. En este laboratorio se busca registrar y analizar señales EEG en diferentes condiciones: reposo, fijación de la mirada en un punto, resolución de preguntas cognitivas y exposición a estímulos auditivos, tanto de música de preferencia personal como de sonidos modulados en frecuencias características de ondas alfa y beta. Estas variaciones permiten identificar cómo el cerebro responde a distintos estados de atención, relajación o activación, así como reconocer la predominancia de determinadas bandas de frecuencia en cada escenario.
<p align="center"> <img src="https://i.pinimg.com/736x/18/18/8f/18188fdb48dd3a434b2b5e0472f7bcc3.jpg" alt="Ondas cerebrales EEG" width="450"><br> <em>Figura 1. Representación de ondas cerebrales.</em> </p>

## **Electroencefalograma** <a name="id2"></a> 

En el registro electroencefalográfico, los electrodos se distribuyen siguiendo el sistema internacional 10-20, que asigna nombres según la región cerebral: frontopolar (Fp), frontal (F), central (C), temporal (T), parietal (P) y occipital (O). Para diferenciar la lateralidad, se emplean números: los impares (1, 3, 5, 7) corresponden al hemisferio izquierdo, mientras que los pares (2, 4, 6, 8) se colocan en el hemisferio derecho [4]. 

<p align="center"> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSr1ZnUnIs5k6OW3BSKt5xHgdYpOe-XpAUKQw&s" alt="Ondas cerebrales EEG" width="450"><br> <em>Figura 2.Representación de la posición electrodos en el cuero cabelludo</em> </p>

## **2. Objetivos de la práctica** <a name="id2"></a>
- Registrar la señal EEG de un integrante del grupo durante la exposición a diferentes estímulos.
- Configurar de manera adecuada el dispositivo BiTalino.
- Representar gráficamente las señales EEG utilizando el software OpenSignals (r)evolution.
- Interpretar y analizar los datos obtenidos a partir del registro.
  
## **3. Materiales e instrumentos** <a name="id3"></a>
| Materiales                                   | Cantidad | Imagen                          |
|----------------------------------------------|----------|---------------------------------|
| Batería 3.7V                                 | 1        | ![bateria](https://github.com/user-attachments/assets/25fe9643-a7fa-4bd9-85ad-e1ce78a926ab) |
| Software OpenSignals                         | 1        | ![opensignals](https://github.com/user-attachments/assets/270de790-173f-42fc-9960-5b12a7fff042) |
| Electrodos de superficie descartables        | 3        | ![electrodos (1)](https://github.com/user-attachments/assets/2e58ad27-7c4a-4336-9fdf-fe54129be397) |
| Cable de los 3 electrodos                    | 1        | ![cable](https://github.com/user-attachments/assets/2d397e32-3ec4-4982-91fe-0d6855e3aec0) |
| Kit BITalino                                 | 1        | ![bitalino](https://github.com/user-attachments/assets/a60c127f-27c2-4a03-b852-454d23f54163) |
| Laptop                                       | 1        | ![laptop](https://github.com/user-attachments/assets/c1394461-1a65-41fc-b6f4-8d8ae5b3b37b) |


## Descripción de materiales: 
-**Batería 3.7V:** Fuente de alimentación portátil para el funcionamiento del kit BiTalino.
- **Software OpenSignals:** Herramienta utilizada para la adquisición y visualización de las señales EEG.
- **Software OpenBCI:** Programa de apoyo para la configuración y análisis de registros neurofisiológicos.
- **Electrodos de superficie descartables:** Dispositivos que permiten captar la actividad eléctrica cerebral de manera no invasiva.
- **Cable de los 3 electrodos:** Conector necesario para enlazar los electrodos con el sistema de registro.
- **Kit BiTalino:** Plataforma biomédica empleada para la adquisición de señales EEG y otros biosignales.
- **UltraCortex:** Casco con electrodos secos que facilita la colocación en posiciones específicas del sistema 10-20.
- **Laptop:** Equipo de cómputo utilizado para ejecutar el software de registro, almacenamiento y análisis de datos.

## **4. Metodología:** <a name="id4"></a> 

Para la adquisición de las señales EEG se utilizó un protocolo basado en la exposición del participante a diferentes condiciones experimentales, con el fin de observar variaciones en la actividad cerebral según la tarea realizada. El procedimiento se desarrolló en un ambiente controlado, con el sujeto en posición cómoda y utilizando electrodos de superficie conectados al sistema BiTalino y visualización en el software OpenSignals.  

### Secuencia de registro  

1. **Reposo:** El participante permaneció en reposo absoluto durante 30 segundos.  
2. **Fijación visual:** Se solicitó al sujeto mantener la vista fija en un punto durante 2 minutos.  
3. **Ojos cerrados:** El participante cerró los ojos durante 30 segundos, permitiendo registrar la aparición de ondas alfa típicas en este estado.  
4. **Tarea cognitiva:** Se aplicó un ejercicio de cálculo mental consistente en restar en secuencia el número 7 a partir de 100, durante 1 minuto.  
5. **Artefactos controlados:**  
   - **Parpadeo voluntario:** el sujeto parpadeó cada 2 segundos durante 1 minuto (repetido 3 veces).  
   - **Masticación:** el participante simuló masticar durante 1 minuto (repetido 3 veces).  
6. **Estimulación auditiva:**  
   - **Música instrumental aleatoria:** se expuso al participante a fragmentos de música instrumental relajante, dado que este tipo de estímulos favorece la modulación de ondas alfa y reduce interferencias externas en el EEG [1].  
   - **Ondas alfa y beta:** se reprodujeron sonidos modulados en frecuencias características de las bandas alfa (8–12 Hz) y beta (12–25 Hz), para analizar la respuesta cerebral inducida por dichas frecuencias.  
7. **Preguntas complejas:** Finalmente, se formularon preguntas de dificultad elevada durante 2 minutos, con el fin de inducir estados de concentración asociados a un aumento en la actividad beta.

   
### Adquisición de datos: Durante la práctica se registraron señales de EEG en un sujeto voluntario en diferentes condiciones fisiológicas. En total se realizaron las siguientes tomas:

**1. Reposo**  
| **Toma en reposo** |
|:------------------:|
| <video src="" controls></video> |

---

**2. Mirada fija**  
| **Toma 1** | **Toma 2** | **Toma 3** |
|:----------:|:----------:|:----------:|
| <video src="" controls></video> | <video src="" controls></video> | <video src="" controls></video> |

---

**3. Mirada sin luz**  
| **Toma 1** | **Toma 2** | **Toma 3** |
|:----------:|:----------:|:----------:|
| <video src="" controls></video> | <video src="" controls></video> | <video src="" controls></video> |

---

**4. Parpadeo cada 2s**  
| **Toma 1** | **Toma 2** | **Toma 3** |
|:----------:|:----------:|:----------:|
| <video src="" controls></video> | <video src="" controls></video> | <video src="" controls></video> |

---

**5. Resta**  
| **Toma 1** |
|:----------:|
| <video src="" controls></video> |

---

**6. Escuchar música**  
| **Toma 1** | **Toma 2** | **Toma 3** |
|:----------:|:----------:|:----------:|
| <video src="" controls></video> | <video src="" controls></video> | <video src="" controls></video> |




## **6. Procesamiento de datos** <a name="id3"></a>
Para los resultados haremos uso del archivo "CodigosEEG_BITalino.ipynb" que se encuentra en el mismo folder. El cual contiene todos los codigos hechos para la visualización de las gráficas de las señales adquiridas. Asi como su respectivo filtrado y análisis de frecuencia.

### a) Importar Librerías  <a name="importar-librerías"></a>
Se importan las librerías a utilizar para graficar las señales.
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, iirnotch
```
### b) Cargar archivos  <a name="cargar-archivos"></a>
Se cargan los archivos .txt que contienen las señales obtenidas del software OpenSignals.
```python
datos = np.loadtxt("resta1.txt", delimiter=None, comments="#")
eeg = datos[:, 5] #La señal se encuentra en ña 5 columna

fs = 1000  
t = np.arange(len(eeg)) / fs
```

### c) Aplicación de filtros <a name="aplicación-de-filtros"></a>
La señal EEG refleja la suma de potenciales postsinápticos de grandes poblaciones neuronales y se caracteriza por ser compleja, dinámica y de baja amplitud, con componentes que se distribuyen principalmente en un rango de frecuencias entre 1 y 30 Hz.
- **Pasa-banda (0.5 Hz-40Hz):** Este rango permite preservar las oscilaciones cerebrales de interés (δ, θ, α, β y parte de γ), mientras se atenúan artefactos de baja frecuencia (movimientos, sudoración y derivas lentas de electrodos) y de alta frecuencia (actividad muscular e interferencia electromagnética). De este modo, se mejora la relación señal-ruido y se garantiza que los análisis en dominios de tiempo y frecuencia se centren en la actividad cerebral relevante [a].
- **Filtro Notch:** Reduce la interferencia de la red eléctrica.

### d) Ploteo de las señales <a name="visualización"></a>
Se realizó el ploteo de las señales crudas y filtradas, así como de sus respectivos FFT en amplitud y dB, análisis Welch y PSD.

### **6.1 Reposo Basal**
| Tipo                 | Señal original | Señal filtrada    |                    
|-------------------------|----------|---------------------------------|
| Ploteo  |<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/281ffe63-96a8-4f1d-8b95-10686ee2fe39" />|<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/ed8e6096-4a77-4723-9070-149d1a21e637" />|
|  PSD |<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/80605c2e-6d2d-40ba-a8d7-2f49e684fce4" />|<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/7446e9aa-e553-467b-b54c-30860c86c17d" />|


### **6.2 Mirada fija**
Toma 1
| Tipo                 | Señal original | Señal filtrada    |                    
|-------------------------|----------|---------------------------------|
|Ploteo   |<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/0239a2de-9eb4-4a01-80f5-cb1fd3ea0f85" />|<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/d689ff01-9394-403a-a4a7-2cda1466a7b2" />|
|  PSD |<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/51dfc68f-9656-415a-85f3-ace495a03344" />|<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/c2f1790d-b787-4042-b985-a0770d214208" />|


Toma 2
| Tipo                 | Señal original | Señal filtrada    |                    
|-------------------------|----------|---------------------------------|
|Ploteo   |<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/8b261407-03c6-4881-b6ab-f7d19f87b3bf" />|<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/1a39d999-d1e6-4996-b3b7-369474b94ff5" />|
|  PSD |<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/9fa0ecc4-2784-4762-a7d5-c70eaef8f64d" />|<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/c53a9e5c-02fc-4deb-8167-734808f47e92" />|


### **6.3 Ojos Cerrados (sin luz)**
Toma 1
| Tipo                 | Señal original | Señal filtrada    |                    
|-------------------------|----------|---------------------------------|
|Ploteo   |<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/8f79b291-c95d-47bf-81a7-da17ebaa55a4" />|<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/09a4811f-152f-4c5b-942a-671f5cda6120" />|
|  PSD |<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/22e53037-c21d-4021-a830-2a27e79713cd" />|<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/eaceff78-a42a-4173-abcf-733620ce32e0" />|

Toma 2
| Tipo                 | Señal original | Señal filtrada    |                    
|-------------------------|----------|---------------------------------|
|Ploteo   |<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/63191e59-b3fe-4a74-bf9d-242ad1a786d5" />|<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/b2bb8f5a-fafd-4ec1-b63d-3c41e253581d" />|
|  PSD |<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/4bfd704b-0d44-42df-ad5b-465c3dbdfcce" />|<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/cfc5ee5a-75a9-4d9b-bc9b-391742245ba0" />|


### **6.4 Parpadeo cada 2 segundos**
Toma 1
| Tipo                 | Señal original | Señal filtrada    |                    
|-------------------------|----------|---------------------------------|
|Ploteo   |<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/28d5a92b-c238-4200-9b27-3853f5fd7fa8" />|<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/651a937b-3868-49ad-a85c-bb04dbd2b22d" />|
|  PSD |<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/c4967867-017a-4389-b0a5-371ea8b0f58b" />|<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/78dbddfa-836b-4129-be68-74ca7bcc7258" />|

Toma 2
| Tipo                 | Señal original | Señal filtrada    |                    
|-------------------------|----------|---------------------------------|
|Ploteo  |<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/37f073a3-50c7-4f18-add5-f13c3a538660" />|<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/6e31a7d2-0194-459a-9347-b0b49523bddb" />|
|  PSD | <img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/19eddb2e-94be-4da3-9fc3-c7a41bc12570" />|<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/9f8ad1d4-2ebb-4221-b711-b6bff1a2e097" />|


### **6.5 Resta**
| Tipo                 | Señal original | Señal filtrada    |                    
|-------------------------|----------|---------------------------------|
|Ploteo   |<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/642246ae-05b1-4388-a700-e31171ca08a6" />|<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/d4e4a759-5235-4d8e-b0d3-1e4bc1f20967" />|
|  PSD |<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/2d664e24-4e9c-4685-8b4b-6b01907ac4b7" />|<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/1a2a082c-49a1-4790-8a63-79ca471c9d16" />|



### **6.6 Actividad libre: Escuchar música**
Toma 1: Escuchando ondas alfa
| Tipo                 | Señal original | Señal filtrada    |                    
|-------------------------|----------|---------------------------------|
|Ploteo   |<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/b4addf7a-fdd2-413c-816d-fd6636f27b82" />|<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/423242a5-416a-4b99-baac-20980e192441" />|
|  PSD |<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/0a17bb66-35c4-4342-80f2-14162cf00311" />|<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/181acbfe-3b96-4658-a66e-2ad502340e1a" />|

Toma 2: Escuchando ondas beta
| Tipo                 | Señal original | Señal filtrada    |                    
|-------------------------|----------|---------------------------------|
|Ploteo   |<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/2e3bb86a-a762-40a8-9da6-7656a57258fc" /> |<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/9c1810bb-2b71-4bc7-994e-2837ba8407fd" />|
|  PSD |<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/d346b40b-8b85-47e7-9353-19759146dfa1" />|<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/e536bd95-b4c1-4fac-b2d3-67c5b003e8ac" />|

Toma 3: Escuchando una canción
| Tipo                 | Señal original | Señal filtrada    |                    
|-------------------------|----------|---------------------------------|
|Ploteo   |<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/4462ccbf-0b23-44ff-adeb-f248f3a21087" />|<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/be30095e-1cf5-41fa-9565-0bceb86dafba" />|
|  PSD |<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/10f9933f-adc8-487f-b267-e3f3190e0a8b" />|<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/f20a10f4-bb61-4264-8917-f224956e3cff" />|


### **6.7 Respondiendo a preguntas**
| Tipo                 | Señal original | Señal filtrada    |                    
|-------------------------|----------|---------------------------------|
|Ploteo   |<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/13c15156-7e66-40c4-bbfe-3a8d64e32d07" />|<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/27643f03-dff7-4478-8c1a-c95108c3d1b3" />|
|  PSD | <img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/d93761b9-8009-4a7e-9d40-affa5239f66e" />|<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/73bcca58-c799-4dbc-9d35-53cad39f7c18" />|


## **7. Discusión y resultados** <a name="id3"></a>
El análisis de PSD (Power Spectral Density) mediante el método de Welch se emplea para complementar la información obtenida de la FFT. Mientras que la FFT permite identificar la composición espectral de la señal en un rango de frecuencias, su estimación puede verse afectada por el ruido y la variabilidad de segmentos cortos de EEG. En cambio, el método de Welch divide la señal en ventanas solapadas, aplica una función de suavizado y luego promedia los espectros parciales, lo que reduce la varianza de la estimación y proporciona un espectro de potencia más estable y confiable. De esta manera se obtiene tanto una caracterización espectral detallada como una estimación robusta de la potencia en cada banda cerebral (δ, θ, α, β, γ).
- **Reposo:** En la gráfica de PSD se observa que tanto en la señal cruda como filtrada, la banda delta presenta mayor potencia, seguida de beta y theta. Lo ideal sería que al estar en reposo la banda theta presente mayor potencia ya que está asociada a la somnolencia ligera y relajación, no obstante se ve mayor potencia en delta y beta, la cual está relacionada con estados de alerta y tensión mental, lo que indica que la persona evaluada mantenía un nivel de tensión mental a pesar del intento de mantener la calma. Por parte de la banda gamma, se ve reducida considerablemente ya que es clave en la atención de tareas complejas  donde se involucra el razonamiento; resultado esperado ya que el voluntario se encontraba en reposo.
- **Mirada Fija:** En ambas tomas se observa que predomina la potencia en las bandas theta,beta y alfa respectivamente. El predominio de theta  puede indicar cierto nivel de fatiga, somnolencia o baja activación, podría deberse a artefactos relacionados con el parpadeo o el movimiento ocular. La banda beta está asociada a procesos de atención y concentración, que son necesarios para mantener la mirada fija sin distraerse mientras que la presencia de alfa en menor medida es coherente ya que esta banda normalmente predomina con ojos cerrados y se reduce cuando el sujeto abre los ojos o dirige su atención a estímulos visuales, fenómeno conocido como bloqueo alfa o desincronización alfa.
- **Ojos cerrados (sin luz):** En ambas tomas predominan en orden las bandas theta, beta y alfa. El resultado difiere a lo esperado ya que la banda que debería presentar mayor potencia debería ser la alfa, relacionada a la relajación y desconexión visual; esto podría deberse a que el sujeto no alcanzó un nivel de calma sficiente además de presentar ruidos musculares o eléctricos, lo que explicaría la presencia de las bandas beta y theta.
- **Parpadeo cada 2 segundos:** El parpadeo voluntario es un estímulo motor simple que suele generar actividad de corta duración y, en general, no altera de forma significativa la distribución de bandas. El predominio de theta podría indicar que el sujeto experimentó desconexión atencional o somnolencia, incluso durante la tarea. Beta en segundo lugar refleja la activación motora y sensorial asociada al parpadeo, mientras que la alfa en tercer lugar confirma que no se consolidó un estado de relajación estable durante la tarea. Este comportamiento puede deberse tanto a factores individuales (cansancio, falta de concentración) como a la presencia de artefactos musculares u oculares que enmascararon la actividad típica.
- **Resta desde 100 a 0:** Durante esta tarea cognitiva, el sujeto restó 7 desde el 100 al 0. El análisis espectral mostró predominio de theta, beta y alfa, mientras que  gamma se mantuvo mucho menor en comparación con las demás bandas. Beta está asociada al esfuerzo mental y a la concentración, así como  gamma, vinculada al procesamiento cognitivo de alto nivel y la integración de información. Sin embargo, en este caso el predominio de la theta podría reflejar fatiga mental o distracción, lo que difiere con lo esperado. La baja expresión de alfa es coherente, ya que la tarea demanda atención sostenida y evita estados de relajación. En cuanto a la gamma, su marcada reducción puede indicar que el sujeto no alcanzó un nivel elevado de procesamiento cortical sincronizado, ya sea por la dificultad de la tarea,o por la presencia de ruido, hipótesis comprobada ya que el sujeto mencionó que le costó hacer las restas sucesivas.
- **Actividad libre-Escuchar música:** Durante esta actividad se reprodujeron videos que contenían ondas alfa, beta y una canción de libre elección por parte del evaluador. El resultado de las bandas fue el mismo en las 3 situaciones, predominó theta por poco sobre beta. Esta similitud de potencia puede deberse a que la música activa procecsos emocionales que generan relajo (banda theta) a la par de que requiere atención y procesamiento cognitivo (banda beta). La combinación de ambos refleja cómo el cerebro responde de manera integrada al estímulo musical favoreciendo un estado de relajación y manteniendo la atención e interpretación del estímulo. Además, se evidenció un ligero incremento en la banda gamma, lo que resulta coherente, ya que la música suele activar la sincronización cortical asociada con la integración multisensorial y la experiencia emocional.
- **Respondiendo preguntas:** Las preguntas que se realizaron fueron de complejidad media, por lo que el resultado esperado era el predominio de la banda gamma; sin embargo la potencia fue baja en comparación al resto de bandas. Esto puede deberse a que la demanda cognitiva no fue lo suficientemente elevada como para activar con fuerza esta banda, o a que el sujeto procesó la tarea de manera más superficial explicada por la ausencia de integración cortical más profunda. El mantenimiento del predominio en theta refleja carga mental o somnolencia.

## **8. Referencias** <a name="id3"></a>
