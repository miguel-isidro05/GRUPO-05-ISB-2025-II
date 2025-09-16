# LABORATORIO 4: – ADQUISICIÓN DE ECG

## Tabla de contenidos 
1. [Introducción](#introducción)
2. [Señal ECG](#señal-ecg)
3. [Objetivos del Laboratorio](#objetivos-del-laboratorio)  
4. [Materiales](#materiales)  
5. [Metodología](#metodología)
   - [Preparación inicial](#preparación-inicial)
   - [Colocación de electrodos](#colocación-de-electrodos)
   - [Configuración del sistema](#configuración-del-sistema)
   - [Adquisición de datos](#adquisición-de-datos)
6. [Procesamiento de datos](#procesamiento-de-datos)  
   - [a) Importar Librerías](#importar-librerías)  
   - [b) Cargar archivos](#cargar-archivos)
   - [c) Aplicación de filtros](#aplicación-de-filtros)  
   - [d) Ploteo de las señales](#visualización) 
7. [Resultados y limitaciones](#resultados-y-limitaciones)  
8. [Referencias](#referencias)  

---

## 1. Introducción <a name="introducción"></a>
El electrocardiograma (ECG) es una herramienta fundamental en el ámbito biomédico, ya que permite registrar la actividad eléctrica del corazón de manera no invasiva. Su análisis facilita la detección de alteraciones en el ritmo y la conducción cardiaca, así como la evaluación del estado fisiológico del paciente en diferentes condiciones, como reposo o actividad física.[1]

Los resultados de un electrocardiograma pueden ayudar a diagnosticar:

- Arritmia
- Miocardiopatía
- Enfermedad de las arterias coronarias
- Ataque cardiaco
- Insuficiencia cardiaca
- Enfermedades de las válvulas del corazón
- Defectos cardiacos congénitos

## 2. Señal ECG <a name="señal-ecg"></a>
<p align="center">
  <img src="https://cdn.rohde-schwarz.com/pws/application/cards/3607_3180/capturing-small-ecg-signals-medical-applications_ac_3607-3180-92_01.1_w1280_hX.png" 
       alt="Registro de señales de ECG" 
       width="450"><br>
  <em>Figura 1. Registro de señales de ECG (Rohde & Schwarz, Aplicaciones médicas).</em>
</p>

| Segmento      | Descripción                                                                 |
|---------------|------------------------------------------------------------------------------|
| **Onda P**    | Indica la activación eléctrica de las aurículas previo al paso al ventrículo.|
| **Intervalo PR** | Tiempo que tarda el impulso en propagarse desde las aurículas hasta los ventrículos.|
| **Complejo QRS** | Señal que refleja la contracción eléctrica de los ventrículos.             |
| **Intervalo QT** | Periodo que abarca desde la activación ventricular hasta su recuperación completa.|
| **Segmento ST** | Marca la fase en la que el ventrículo está totalmente despolarizado.       |
| **Onda T**    | Representa el proceso de recuperación de la actividad eléctrica ventricular. |
| **Onda U**    | Se asocia con la recuperación tardía de fibras especializadas o miocitos.    |

## Electrocardiograma  

El ECG clínico estándar se registra con 12 derivaciones, que permiten observar la actividad eléctrica cardíaca desde distintos planos. Estas derivaciones se obtienen a partir de electrodos ubicados en las extremidades y en la región torácica. De ellas, seis corresponden al plano frontal (derivaciones I, II, III, aVR, aVL y aVF) y las otras seis al plano horizontal (precordiales V1 a V6). Esta disposición brinda una visión completa del proceso de despolarización y repolarización del corazón.[2]

<p align="center">
  <img src="https://fisiologia.facmed.unam.mx/wp-content/uploads/2021/11/UTII-2B-img-Vectores-de-despo-ventri.jpg" 
       alt="Electrocardiograma y derivaciones" 
       width="450"><br>
  <em>Figura 2. Electrocardiograma y derivaciones (UNAM, Fisiología).</em>
</p>

## 3. Objetivos del Laboratorio <a name="objetivos-del-laboratorio"></a>
- Configurar adecuadamente el sistema BiTalino para la adquisición de señales cardíacas.

- Registrar y visualizar una señal de ECG en condiciones controladas usando el software OpenSignals.

- Reconocer las ondas principales (P, QRS y T) dentro del registro electrocardiográfico.

- Analizar los cambios en la señal de ECG bajo diferentes condiciones fisiológicas (reposo, apnea breve y actividad física).

## 4. Materiales <a name="materiales"></a>
| Materiales                                   | Cantidad | Imagen                          |
|----------------------------------------------|----------|---------------------------------|
| Batería 3.7V                                 | 1        | ![bateria](https://github.com/user-attachments/assets/25fe9643-a7fa-4bd9-85ad-e1ce78a926ab) |
| Software OpenSignals                         | 1        | ![opensignals](https://github.com/user-attachments/assets/270de790-173f-42fc-9960-5b12a7fff042) |
| Electrodos de superficie descartables        | 3        | ![electrodos (1)](https://github.com/user-attachments/assets/2e58ad27-7c4a-4336-9fdf-fe54129be397) |
| Cable de los 3 electrodos                    | 1        | ![cable](https://github.com/user-attachments/assets/2d397e32-3ec4-4982-91fe-0d6855e3aec0) |
| Kit BITalino                                 | 1        | ![bitalino](https://github.com/user-attachments/assets/a60c127f-27c2-4a03-b852-454d23f54163) |
| Laptop                                       | 1        | ![laptop](https://github.com/user-attachments/assets/c1394461-1a65-41fc-b6f4-8d8ae5b3b37b) |

## 5. Metodología <a name="metodología"></a>
Para la adquisición de la señal de ECG utilizando el kit **BiTalino** y el software **OpenSignals**, se siguió el siguiente procedimiento:  

### Preparación inicial: <a name="preparación-inicial"></a>
   - Conexión de los electrodos desechables al cable de 3 derivaciones y colocación en la piel según la configuración estándar de ECG.  
   - Encendido del dispositivo BiTalino y vinculación por Bluetooth con la laptop mediante el software OpenSignals.  
   - Verificación de la señal registrada para asegurar calidad y ausencia de ruidos excesivos.

### Colocación de los electrodos: <a name="colocación-de-electrodos"></a>
Para obtener una señal de ECG de buena calidad, la ubicación correcta de los electrodos es fundamental. A continuación, se presentan dos referencias que explican la posición estándar y los efectos de colocar mal los electrodos:  

   **a. LITFL – ECG Lead Positioning** [3]
   Según la guía clínica de *Life in the Fast Lane (LITFL)*, los electrodos deben colocarse en puntos anatómicos bien definidos para asegurar registros confiables. En el caso de las derivaciones precordiales:  
   - **V1 y V2**: 4.º espacio intercostal, a la derecha e izquierda del esternón.  
   - **V4**: 5.º espacio intercostal en la línea medio clavicular.  
   - **V3**: entre V2 y V4.  
   - **V5 y V6**: en la misma altura que V4, pero en la línea axilar anterior y media.  

   <p align="center">
     <img src="https://litfl.com/wp-content/uploads/2018/08/Chest-external-landmarks-in-ECG-placament.png" 
          alt="Posición de electrodos precordiales" 
          width="400"><br>
     <em>Figura 3. Posición estándar de electrodos precordiales (LITFL).</em>
   </p>  

   **b. Tung, R. T. et al., 2021 – Electrocardiographic Limb Leads Placement and Its Effect on ECG Interpretation** [4]
   Este artículo científico analiza el impacto de la colocación de los electrodos de las extremidades en la interpretación del ECG. Explica que mover los electrodos de los brazos o piernas a posiciones no convencionales (por ejemplo, más arriba en el torso) puede cambiar el eje eléctrico aparente del corazón, alterar el segmento ST o incluso simular un infarto inexistente.  

   El estudio concluye que las derivaciones de miembros deben colocarse de forma simétrica en las extremidades (RA, LA, LL y RL), ya que su reposicionamiento sin seguir estándares puede generar errores clínicos serios. Por ello, recomienda seguir las guías internacionales para asegurar lecturas correctas.  

   <p align="center">
     <img src="https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8010/8415387/0b20e08ada27/14-229f3.jpg" 
          alt="Colocación de electrodos en extremidades" 
          width="400"><br>
     <em>Figura 4. Colocación de electrodos en extremidades (Tung et al., 2021).</em>
   </p>  
   
### Configuración del sistema: <a name="configuración-del-sistema"></a>
- Se instaló el software **OpenSignals** en la laptop para establecer la comunicación con el kit BiTalino.  
- Se activó la conectividad **Bluetooth** de la computadora y se emparejó con el dispositivo BiTalino utilizando el código predeterminado.  
- En el software, se seleccionó el canal correspondiente al **sensor de ECG** y se ajustaron los parámetros de muestreo (frecuencia de adquisición y duración de la señal).  
- Se verificó la correcta recepción de la señal en tiempo real antes de iniciar la adquisición formal.  

### Adquisición de datos; <a name="adquisición-de-datos"></a>
Durante la práctica se registraron señales de ECG en un sujeto voluntario en diferentes condiciones fisiológicas. En total se realizaron las siguientes tomas:  

**1. Reposo**  
   - 1 registro inicial con el sujeto en reposo y en calma.
     
<div align="center">

| **Toma en reposo** |
|:----------------------:|
| <video src="https://github.com/user-attachments/assets/2e581bb9-ceae-4bbf-82a4-4913a6c3245a" controls></video> |

</div>


**2. Respiracion**

<div align="center">
 
| **Toma 1** | **Toma 2** | **Toma 3** |
|:-----------------------:|:--------------------------:|:--------------------------:|
| <video src="https://github.com/user-attachments/assets/ecc5c4b2-8733-4968-9329-2e7f5ea2533f" controls></video> | <video src="https://github.com/user-attachments/assets/40c5edc6-781a-4698-807f-5a9b1ae9d326" controls></video> | <video src="https://github.com/user-attachments/assets/f7e2701a-3f41-422c-91ae-466e512d350b" controls></video> |

</div>

**3. Actividad Fisica**

<div align="center">

| **Pectoral sin oposición** |
|:---------------------------:|
| <video src="https://github.com/user-attachments/assets/22de795a-6e0c-4749-be6b-432d3a4b73ff" controls></video> |

</div>


     

## 6. Procesamiento de datos <a name="procesamiento-de-datos"></a>
Para los resultados haremos uso del archivo "CodigosECG.ipynb" que se encuentra en el mismo folder. El cual contiene todos los codigos hechos para la visualización de las gráficas de las señales adquiridas. Asi como su respectivo filtrado y análisis de frecuencia.

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
#Abrimos el archivo sin incluir las filas que inician con"#"
with open("reposo1.txt", "r") as f:
    lineas = f.readlines()

datos_limpios = [line.strip().split() for line in lineas if not line.startswith("#")]
datos = np.array(datos_limpios, dtype=float)
```

### c) Aplicación de filtros <a name="aplicación-de-filtros"></a>
El ECG es una señal bioeléctrica débil, muy suceptible al ruido de diversas fuentes, tanto internas como externas (al cuerpo del paciente). Los movimientos, las señales eléctricas de otros músculos, la mala conexión de electrodos pueden generar una lectura de ECG borrosa, por lo que es necesario aplicar un filtrado para mitigar esa interferencia[5]. Para este laboratorio se aplicaron los siguientes filtros:
- **Pasa-banda (0.5 Hz-40 Hz):** Filtrado suave para entornos ruidosos. Se usa principalmente para detectar la frecuencia cardiaca[6].
- **Filtro Notch:** Reduce la interferencia de la red eléctrica.
Gracias a este proceso de filtrado se logró resaltar mejor las ondas características del ECG, especialmente el complejo QRS y las ondas P y T.
<p align="center">
<img width="1226" height="458" alt="image" src="https://github.com/user-attachments/assets/6de69508-ae97-4735-96c8-4afbec3bcf4a" />
<em>Figura 5. Señales ECG con  intervalos y segmentos .</em>
</p>

### d) Ploteo de las señales <a name="visualización"></a>
Se realizó el ploteo de las señales crudas y filtradas, así como de sus respectivos FFT en amplitud y dB.

### 6.1 Reposo Basal 
| Tipo                 | Señal original | Señal filtrada    |                    
|-------------------------|----------|---------------------------------|
|Ploteo   |<img width="1176" height="393" alt="image" src="https://github.com/user-attachments/assets/b2c2dca0-7358-46a5-aa63-d6ce0e82821d" />| <img width="1176" height="393" alt="image" src="https://github.com/user-attachments/assets/39f6cdd8-1efd-4e27-b2c4-591c0947b314" />|
|  FFT  |<img width="890" height="393" alt="image" src="https://github.com/user-attachments/assets/bbd23322-c2ed-42d3-a326-d5831dd23b1b" />| <img width="890" height="393" alt="image" src="https://github.com/user-attachments/assets/783de173-f79f-4697-a5a2-5a9d56381e62" />|
|  FFT [dB]    |<img width="875" height="393" alt="image" src="https://github.com/user-attachments/assets/9b18516b-4030-44d6-bf95-e41b87800e3f" />| <img width="875" height="393" alt="image" src="https://github.com/user-attachments/assets/77f01de9-a001-482e-bf06-a2213c149ce3" />|

### 6.2 Mantenimiento de la respiracion por 10 segundos

**Toma 1:**
| Tipo                 | Señal original | Señal filtrada                         |
|-------------------------|----------|---------------------------------|
|Ploteo  |<img width="1181" height="393" alt="image" src="https://github.com/user-attachments/assets/e6f90235-bfc6-4cf1-937f-dd2064d9f32d" />|<img width="1181" height="393" alt="image" src="https://github.com/user-attachments/assets/46e23738-7fe3-4ea2-90ab-fede75e82290" />|
| FFT    |<img width="890" height="393" alt="image" src="https://github.com/user-attachments/assets/e25e1ef1-6bc0-4085-9969-1b48682d8b38" />| <img width="890" height="393" alt="image" src="https://github.com/user-attachments/assets/95174037-8dc7-4e58-a64f-1e0705a40add" />|
|  FFT [dB]    |<img width="875" height="393" alt="image" src="https://github.com/user-attachments/assets/4478e1f3-8077-4925-8150-8e3f2ec0502b" />| <img width="875" height="393" alt="image" src="https://github.com/user-attachments/assets/c4ea490d-836e-4337-85dc-2bc5826e72b3" /> |

**Toma 2:**
| Tipo                 | Señal original | Señal filtrada                         |
|-------------------------|----------|---------------------------------|
|Ploteo  | <img width="1181" height="393" alt="image" src="https://github.com/user-attachments/assets/133ee2e6-3d0c-49bc-b48b-367ece025ded" />|<img width="1181" height="393" alt="image" src="https://github.com/user-attachments/assets/09a252a1-3959-40be-bc9a-c24b6efad8cf" />|
| FFT    |<img width="890" height="393" alt="image" src="https://github.com/user-attachments/assets/b4f3533f-bf81-41a5-8950-318bcce70978" />|<img width="890" height="393" alt="image" src="https://github.com/user-attachments/assets/40d73983-a147-4585-a7f9-0cc015ec6ca3" />|
|  FFT [dB] | <img width="875" height="393" alt="image" src="https://github.com/user-attachments/assets/75f320db-90cb-4e0f-86ce-446040a534ca" />|<img width="875" height="393" alt="image" src="https://github.com/user-attachments/assets/579310e4-d6b1-4fd4-ab3e-85db13bc43db" />|

**Toma 3:**
| Tipo                 | Señal original | Señal filtrada                         |
|-------------------------|----------|---------------------------------|
| Ploteo |<img width="1181" height="393" alt="image" src="https://github.com/user-attachments/assets/dd74eca2-5f5b-47ca-be8c-82cbbcf4c3ec" />|<img width="1181" height="393" alt="image" src="https://github.com/user-attachments/assets/2e221153-96af-42f2-a432-93ec00accf71" />|
|  FFT    |<img width="890" height="393" alt="image" src="https://github.com/user-attachments/assets/cad0c7bb-7095-4317-9320-9a4d4f2c4ed6" />|<img width="890" height="393" alt="image" src="https://github.com/user-attachments/assets/48f35fb8-efe0-4433-917b-4c2d89d121fd" />|
| FFT [dB] |<img width="875" height="393" alt="image" src="https://github.com/user-attachments/assets/ea460a99-f9c8-4b14-9dd5-452fddbe5ca2" />|<img width="875" height="393" alt="image" src="https://github.com/user-attachments/assets/e568ea60-58bc-4c92-89f6-627c3c939aef" />|

### 6.3 Reposo basal después del mantenimiento de la respiración
| Tipo                 | Señal original | Señal filtrada                         |
|-------------------------|----------|---------------------------------|
| Ploteo |<img width="1181" height="393" alt="image" src="https://github.com/user-attachments/assets/0f2d2a8f-da31-433f-9061-d6766b7bcb8b" />|<img width="1181" height="393" alt="image" src="https://github.com/user-attachments/assets/40cdc42d-7edf-4cbc-9c64-9733e1e5ca8c" />|
|  FFT    |<img width="890" height="393" alt="image" src="https://github.com/user-attachments/assets/8d3f3d3c-c48e-4bd0-b4e1-99f9013f6c03" />|<img width="890" height="393" alt="image" src="https://github.com/user-attachments/assets/ec60511d-8a85-4c48-94e9-cb56a812950d" />  |
| FFT [dB] |<img width="875" height="393" alt="image" src="https://github.com/user-attachments/assets/3f4105ff-829e-43da-bc7f-445bb87346e6" />|<img width="875" height="393" alt="image" src="https://github.com/user-attachments/assets/5e8625e8-1fbd-4dc1-9e4a-8cfe64dda7f9" />|

## 6.4 Respiración después de actividad aeróbica

**Toma 1:**
| Tipo                 | Señal original | Señal filtrada                         |
|-------------------------|----------|---------------------------------|
| Ploteo |<img width="1181" height="393" alt="image" src="https://github.com/user-attachments/assets/b8781c16-a99c-421b-b028-91c948924a3c" />| <img width="1181" height="393" alt="image" src="https://github.com/user-attachments/assets/fe244dd1-e0a5-411b-a7bf-73cfd20082ef" />|
|  FFT    |<img width="890" height="393" alt="image" src="https://github.com/user-attachments/assets/97916780-29e4-43a1-9b92-65571d309891" />| <img width="890" height="393" alt="image" src="https://github.com/user-attachments/assets/cfbbee03-6025-4f23-a8e6-0e0d3ca797a5" /> |
| FFT [dB] |<img width="875" height="393" alt="image" src="https://github.com/user-attachments/assets/67dc52c0-9974-4905-b46b-6a3643fcd504" />| <img width="875" height="393" alt="image" src="https://github.com/user-attachments/assets/92e53a6d-a594-467f-b9d2-f91a2889169e" />|

**Toma 2:**
| Tipo                 | Señal original | Señal filtrada                         |
|-------------------------|----------|---------------------------------|
| Ploteo | <img width="1180" height="393" alt="image" src="https://github.com/user-attachments/assets/ce0eab54-39a1-43e6-b826-ef05aa667458" />| <img width="1172" height="393" alt="image" src="https://github.com/user-attachments/assets/425fd7bc-6df7-40c3-9bc6-ad8ffb92a9a3" />|
|  FFT    |<img width="890" height="393" alt="image" src="https://github.com/user-attachments/assets/aa504f13-9ece-463e-9923-4b8b6626be14" />| <img width="890" height="393" alt="image" src="https://github.com/user-attachments/assets/356141c7-24a3-4886-a438-ddf95a892c76" />|
| FFT [dB] |<img width="875" height="393" alt="image" src="https://github.com/user-attachments/assets/1485a92b-c995-4058-813f-ebd4e8e71f92" />|<img width="875" height="393" alt="image" src="https://github.com/user-attachments/assets/24456f84-7600-42a4-b699-0f02def51abb" />|


## 7. Discusión y resultados <a name="#resultados-y-limitaciones"></a> 
- **Reposo basal**: El registro del ECG en reposo representa la actividad cardíaca en condiciones normales sin influencia de movimiento o esfuerzo físico. Se observan picos ascendentes (propios de la primera derivada). El complejo QRS positivo corresponde a la despolarización ventricular que es la activación eléctrica de las fibras cardíacas que generan la contracción principal del corazón que impulsa la sangre hacia la circulación sistémica y pulmonar. En la FFT se ve que la señal ECG concentra su energía a frecuencias menores a 40 Hz y que las frecuencias mayores son atenuadas. En la FFT de la señal filtrada se puede observar mejor las atenuaciondes de frecuencias.
- **Mantenimiento de la respiración por 10 segundos**: En los primeros segundos de la señal se presenta una distancia del intervalo R-R corta debido a la "adaptación fisiológica" inicial que se produce al aguantar la respiración. También se observa una disminución progresiva en la amplitud de los picos R en comparación al reposo basal, debido a que la apnea voluntaria genera una menor oxigenación y cambios en la presión intratorácica, lo cual altera la dinámica cardíaca y se manifiesta como una reducción progresiva en la amplitud de los picos del ECG.
- **Reposo basal después del mantenimiento de la respiración**: Al reanudar la respiración tras la apnea voluntaria, se observa la reaparición de la deriva de la línea base y una recuperación de los intervalor R-R, asociada al reinicio del ciclo respiratorio. Aun así, las variaciones de los intervalos R-R son irregulares, característicos de una arritmia sinusal, lo cual tiene sentido ya que esta corresponde a una variación fisiológica a causa de la apnea.
- **Respiración post actividad física**: Después de realizar una actividad aeróbica por 10 minutos, en ambas tomas se puede observar que hay más picos QRS por segundo en comparación con el reposo basal y una reducción de los intervalos R-R, lo que significa que el corazón late más rápido por el esfuerzo físico. Esto se traduce al aumento de la frecuencia cardíaca que conforme pasa el tiempo se va estabilizando tanto los picos como los intervalos R-R. También se observan variaciones en la amplitud de los picos a causa de la fluctuación del retorno venoso y el volumen sistólico.

## 8. Referencias <a name="referencias"></a>
[1] MedlinePlus, Electrocardiograma. MedlinePlus Enciclopedia Médica, U.S. National Library of Medicine. [En línea]. Disponible en: https://medlineplus.gov/spanish/pruebas-de-laboratorio/electrocardiograma/[Accedido: 16-sep-2025].
[2] Cardiopatías Congénitas La Paz, ¿Qué es un ECG de 12 derivaciones? Desde el Pálpito. [En línea]. Disponible en: https://www.cardiopatiascongenitaslapaz.com/desde-el-palpito/que-es-un-ecg-de-12-derivaciones/ [Accedido: 16-sep-2025].
[3]LITFL, ECG Lead Positioning. Life in the Fast Lane, 2025. [En línea]. Disponible en: https://litfl.com/ecg-lead-positioning/.[Accedido: 16-sep-2025].
[4]A. C. F. Siqueira, G. T. C. P. Freitas, T. A. C. Ribeiro, M. C. da Silva, L. B. Ferreira, y A. C. C. Simões, “The 12-lead electrocardiogram: What the general practitioner needs to know,” Rev. Assoc. Med. Bras., vol. 67, no. 4, pp. 618-628, 2021. [En línea]. Disponible en: https://pmc.ncbi.nlm.nih.gov/articles/PMC8415387/.[Accedido: 16-sep-2025].
[5] MedTeq, “ECG Filters,” MedTeq.net, Apr. 1, 2017. [Online]. Available: https://www.medteq.net/article/2017/4/1/ecg-filters
[6] GE Healthcare, “A Guide to ECG Signal Filtering,” GE Healthcare Insights. [Online]. Available: https://www.gehealthcare.co.uk/insights/article/a-guide-to-ecg-signal-filtering



