## 1. Introducción al tema
### ¿Qué es el algoritmo Pan–Tompkins?

El algoritmo Pan–Tompkins, desarrollado en 1985, es uno de los métodos más influyentes para la detección automática del complejo QRS en señales electrocardiográficas (ECG). Su diseño combina filtrado digital, derivadas, transformaciones no lineales y umbrales adaptativos, permitiendo identificar latidos cardíacos en tiempo real con alta confiabilidad.

A pesar de haberse propuesto hace casi cuatro décadas, sigue siendo un estándar de referencia en investigación y en aplicaciones biomédicas modernas debido a su robustez,baja complejidad computacional y excelente desempeño en condiciones reales de ruido.

<p align="center">
 <img width="412" height="141" alt="image" src="https://github.com/user-attachments/assets/b7a0aa40-0637-454b-969f-152c813088ce" />
</p>

<p align="center"><em>Figura 1. Algoritmo de Pan–Tompkins</em></p>


### ¿Por qué es importante en el procesamiento de señales biomédicas?

La detección automática del QRS es una tarea fundamental para el análisis de señales biomédicas, ya que constituye el punto de partida para cálculos como:

- Frecuencia cardíaca
- Variabilidad del ritmo (HRV)  
- Detección de arritmias  
- Segmentación de ondas P, QRS y T  
- Parámetros clínicos como PR y QT  
<p align="center">
  <img width="225" height="225" alt="image" src="https://github.com/user-attachments/assets/df2413da-bb3b-4f01-9fa5-2c341985031e" />

</p>

<p align="center"><em>Figura 2. Señal ECG</em></p>


Pan–Tompkins destaca porque puede operar con gran precisión incluso cuando la señal ECG está contaminada por ruido muscular (EMG), artefacto de movimiento, baseline wander o interferencia de red eléctrica. Este comportamiento ha sido confirmado en evaluaciones recientes que analizan su rendimiento bajo distintos niveles de ruido y con bases estándar como MIT-BIH y la Noise Stress Test Database .

### Un aspecto relevante: desempeño bajo ruido

Un punto especialmente interesante para mencionar en la introducción es que el algoritmo no solo funciona bien en ECG clínicos limpios, sino que también mantiene un desempeño sólido cuando la señal es de baja calidad.

Estudios actuales han mostrado que Pan–Tompkins puede mantener **alta sensibilidad de detección** incluso con señales ruidosas con niveles de **SNR entre 24 dB y 12 dB**, antes de que el rendimiento disminuya de manera notable en ambientes extremadamente ruidosos (por ejemplo, −6 dB).

Esto evidencia su capacidad para ser utilizado en entornos reales como:

- Monitoreo ambulatorio  
- Holters  
- Wearables  
- Sistemas de telemedicina  

### Papel del algoritmo en el análisis del ECG

El complejo QRS es la estructura eléctrica dominante en cada latido y es la referencia para segmentar el resto del ECG. De hecho, una vez identificado el QRS, las demás ondas (P y T) pueden localizarse con mayor facilidad, tal como reportan diversos estudios de análisis automatizado del ECG.

Detectar el QRS con precisión es indispensable porque afecta directamente:

- La estimación del ritmo cardíaco  
- La toma de decisiones clínicas automatizadas  
- La detección de arritmias  
- La estabilidad de los algoritmos de monitoreo  

Por ello, Pan–Tompkins se consolidó como un **pilar metodológico** en el procesamiento digital de señales ECG.

### Flujo general
#### Filtro Paso Bajo
El filtro paso bajo elimina el ruido de alta frecuencia (principalmente EMG y componentes rápidas), 
preservando las características esenciales del QRS.

<p align="center">
  <img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/ee37e0d5-14ca-4484-ba44-461820c8866f" />
</p>

<p align="center"><em>Figura 3. Filtro Paso Bajo</em></p>


#### Filtro Paso Alta
El filtro paso bajo elimina el ruido de alta frecuencia (principalmente EMG y componentes rápidas), 
preservando las características esenciales del QRS.

<p align="center">
  <img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/318ca12d-85ba-4ce4-8ed8-34154020f994" />

</p>

<p align="center"><em>Figura 3. Filtro Paso Bajo</em></p>


#### Filtro Derivador
La derivada resalta los cambios abruptos y pendientes pronunciadas, características típicas 
del complejo QRS, mientras reduce el aporte de ondas P y T.

<p align="center">
  <img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/d5904074-2e3c-4d06-9d9a-b0369109b748" />
</p>

<p align="center"><em>Figura 4. Filtro Derivador</em></p>


#### Cuadrado de la señal
El operador al cuadrado amplifica los valores con alta pendiente y energía del QRS, 
haciendo más evidente su forma y reduciendo la influencia de valores negativos.

<p align="center">
  <img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/b6e7934a-8082-49ab-bf14-e17615837ac3" />
</p>

<p align="center"><em>Figura 5. Filtro Cuadrado de la señal</em></p>


#### Integración por ventana móvil
La integración calcula energía dentro de una ventana fija, suavizando la señal 
y resaltando la anchura característica del QRS para facilitar la detección.

<p align="center">
  <img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/e3406a8b-e06c-472e-8730-30aec9a5d646" />
</p>

<p align="center"><em>Figura 6. Filtro Integrador</em></p>



## 2. Estudios Realizados
### 2.1 "Predominant peak detection of QRS complexes" []
En esta investigación, se presenta una metodología para la detección del complejo QRS basada en una adaptación del algoritmo clásico de Pan–Tompkins. Ya que, aunque Pan Tompkins es uno de los métodos más confiables para detectar picos R en señales ECG, su desempeño puede verse afectado por ruido, interferencias y latidos anormales. Del algoritmo se modifica principalmente el filtrado pasa-banda y los umbrales de detección para mejorar la eliminación de ruido sin perder la energía característica del QRS. 

Primero, la señal ECG pasa por un filtrado pasa banda para eliminar interferencias como el ruido muscular y la línea base. Luego se aplica una derivada para resaltar las pendientes pronunciadas del QRS, seguida de una operación de cuadrado que amplifica las diferencias y hace más prominentes los picos de interés. Tras esto, la señal se somete a una integración por ventana móvil, que ayuda a suavizar variaciones rápidas y a resaltar los segmentos temporales donde aparecen los complejos QRS. Una vez obtenida esta señal procesada, se aplica un umbral adaptativo para decidir cuáles picos son candidatos a QRS. Finalmente se incorpora un mecanismo de cancelación de falsos picos y un algoritmo para seleccionar el “pico predominante”, es decir, el verdadero pico R entre varios picos que pueden aparecer cercanos en casos de ruido o latidos ectópicos. 

| **ECG baseline** |**Peak of QRS complex (ectopic beats)** |**Peak of QRS complex (multifocal ectopic beat)**|
|<img width="820" height="217" alt="image" src="https://github.com/user-attachments/assets/7b117e52-034a-4751-a0d0-cc42ca439845" />|<img width="765" height="292" alt="image" src="https://github.com/user-attachments/assets/294ae98e-9529-4af7-8ce4-5d96b5a3dfe5" />|<img width="850" height="283" alt="image" src="https://github.com/user-attachments/assets/6b7f07e7-3227-463e-94da-94c3db78e7e4" />|

La inclusión del mecanismo de detección del pico predominante ofrece un criterio fisiológico adicional para identificar el verdadero pico R entre varios candidatos generados durante el procesamiento. Esta mejora es importante en registros donde los latidos son irregulares o existen extrasístoles simples. Sin embargo, el trabajo también reconoce que, aunque el método es robusto ante ruido y ectopias simples, todavía presenta limitaciones ante latidos ectópicos multifocales, donde la morfología del QRS puede variar tanto que disminuye la eficacia de los umbrales adaptativos.
El uso de la base de datos MIT-BIH, ampliamente empleada como estándar, permitió validar el método en condiciones comparables a otros algoritmos. La alta precisión obtenida (99.68%) sugiere que las modificaciones propuestas aportan beneficios significativos, aunque sería necesario evaluar el método en señales ambulatorias o de larga duración para determinar su generalización

### 2.2 "Analysis of Pan-Tompkins Algorithm Performance with Noisy ECG Signals" []

#### 2.2.1. Introduccion
El paper evalúa el desempeño del algoritmo Pan–Tompkins para detectar complejos QRS en señales ECG contaminadas con distintos tipos de ruido usando las bases MIT-BIH Noise Stress Test y MIT-BIH Arrhythmia. Implementa cada etapa del algoritmo —filtrado, derivada, cuadrado, integración y umbrales adaptativos— y analiza su respuesta frente a variaciones del SNR. Los resultados muestran alta sensibilidad y predictividad cuando el ruido es leve o moderado. Sin embargo, el rendimiento disminuye significativamente ante artefactos intensos, especialmente el Motion Artefact. También verifica que Pan–Tompkins mantiene alta precisión en señales con arritmias reales. En conjunto, el estudio evidencia las fortalezas y limitaciones del algoritmo en entornos ruidosos y ambulatorios.

#### 2.2.2 Metodologia
a. Bases de datos

- Database MIT – BIH NST: Es un database de ECG limpio contaminado artificialmente con diferentes niveles de ruido (SNR: 24 dB a –6 dB). Contiene 12 horas de grabación de ECG con 3 horas de grabación de ruidos de ECG. Divididos en segmentos de 2 minutos alternados con secciones limpias. El ruido fue registrado los 5 primeros minutos de cada archivo. El principal artefacto evaluado es el Motion Artifact, uno de los más críticos por su similitud con ectopías
- Database MIT – BIH Arrhytmia: El databe incluye 48 grabaciones de ECG grabados a 360 Hz. Cada grabación es de pacientes diferentes 

b. Etapas del algoritmo Pan Thompkins

- Filtro pasabandas: Se usaron frecuencias de corte de 5 a 15 Hz para eliminar ruido de red eléctrica, de alta frecuencia, de señales musculares, ruido de base e interferencias de la onda T.
  <img width="655" height="309" alt="image" src="https://github.com/user-attachments/assets/aa7271aa-6a14-4a2c-a508-fe2a12bcc300" />
  <img width="645" height="294" alt="image" src="https://github.com/user-attachments/assets/239225a6-fbd7-453c-9bbb-df14f0506194" />

- Derivativo:
  
  <img width="618" height="376" alt="image" src="https://github.com/user-attachments/assets/4ff0610e-e404-40b8-9945-44a045e6befe" />

- Elevacion al cuadrado:
- 
  <img width="613" height="165" alt="image" src="https://github.com/user-attachments/assets/53cb604e-09a9-4616-9c53-d4286fbf903a" />
  <img width="611" height="173" alt="image" src="https://github.com/user-attachments/assets/da781fb0-a908-4964-94b8-f5dbd0c66ebf" />


- Integración de la ventana deslizante (MWI): Se uso una ventana de 150 ms (30 muestras en el tiempo)

 <img width="583" height="379" alt="image" src="https://github.com/user-attachments/assets/01d23dfa-2446-42d8-8da4-c592678c6d14" />

c. Conclusiones:

•	El algoritmo Pan–Tompkins mantiene un desempeño excelente con ruido leve o moderado, logrando sensibilidades y predictividades cercanas al 100% cuando el SNR se mantiene entre 24 y 12 dB.

•	El rendimiento se deteriora significativamente en condiciones de ruido severo, especialmente ante Motion Artefact, que genera picos similares al QRS y reduce tanto la sensibilidad como la predictividad positiva.

•	El algoritmo demuestra ser robusto frente a arritmias reales, mostrando alta precisión en la detección de QRS en la base MIT-BIH Arrhythmia, lo que confirma su utilidad como detector confiable en entornos clínicos y ambulatorios


## 3.Referencias:


[] A. S. Al-Ghabban, A. F. Al-Hashimi, and Z. T. Al-Dahan,“Predominant peak detection of QRS complexes,” International Journal of Medical Imaging, vol. 2, no. 6, pp. 133–137, Nov. 2014, doi: 10.11648/j.ijmi.20140206.12.




