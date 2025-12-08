# **NeuroMotion XR: Sistema Interfaz Cerebro-Computador para Rehabilitación Post-ACV Basada en Imaginería Motora y Neurofeedback**

## *Resumen*

Este estudio presenta NeuroMotion XR, un sistema BCI para rehabilitación motora post-stroke basado en la detección de imaginería motora mediante EEG y neurofeedback. Se analizaron datos de los datasets BCI Competition IV 2a y 2b, así como registros propios obtenidos con OpenBCI. El procesamiento incluyó filtrado, extracción de características con CSP y clasificación mediante LDA y EEGNet. Los modelos alcanzaron precisiones de 92% (2a), 73–78% (2b) y ~68% con señales reales, demostrando la viabilidad del enfoque y su potencial como herramienta complementaria de bajo costo en rehabilitación motora.


## *Palabras clave*

## **1. Introducción**

El Accidente Cerebrovascular (ACV) es un trastorno neurológico caracterizado por la interrupción súbita del flujo sanguíneo cerebral, ya sea por obstrucción de una arteria (ACV isquémico) o por ruptura de un vaso sanguíneo (ACV hemorrágico). Esta interrupción impide que las neuronas reciban oxígeno y nutrientes, lo que provoca daño cerebral focal o global y puede generar secuelas motoras, cognitivas, sensoriales o del lenguaje según la región afectada [1].
Constituye la segunda causa de muerte y de las principales causas de discapacidad en adultos a nivel mundial, generando secuelas que impactan profundamente en la calidad de vida de los pacientes [2]. 
Tras la fase aguda inicial, la mayoría de personas transita hacia el periodo post-stroke, que comprende desde las primeras semanas hasta varios años después del evento. Este periodo se subdivide usualmente en una fase subaguda, que abarca aproximadamente desde la primera semana hasta los 3–6 meses posteriores al ACV, y una fase crónica, que comienza alrededor de los 6 meses y puede prolongarse indefinidamente [3].
Durante la fase subaguda, el sistema nervioso central atraviesa un “período sensible” caracterizado por una intensa plasticidad neuronal, reflejada en procesos como el crecimiento dendrítico, la formación de nuevas sinapsis y la reorganización cortical. Estos mecanismos facilitan una recuperación funcional activa y representan una ventana terapéutica crítica [4]. En contraste, la fase crónica se caracteriza por una estabilización del daño neurológico: aunque la plasticidad persiste, la recuperación espontánea disminuye y las secuelas tienden a consolidarse, lo que hace necesario implementar intervenciones sostenidas enfocadas en el mantenimiento funcional, la compensación y la rehabilitación a largo plazo [5].


## **2. Planteamiento del problema**

Una de las secuelas más persistentes y limitantes del ACV es el deterioro motor del miembro superior, presente en aproximadamente el 60–80% de los sobrevivientes, incluso meses después del evento [6]. Aunque la mayor capacidad de recuperación ocurre en la etapa subaguda (7 días a 6 meses), muchos pacientes no acceden a rehabilitación intensiva en este periodo crítico. Como resultado, ingresan a la etapa crónica con déficits estables y difícilmente reversibles, afectando su independencia funcional y calidad de vida.
En Perú, esta situación se agudiza por la limitada disponibilidad de servicios de rehabilitación especializados, listas de espera prolongadas y escasa implementación de tecnologías terapéuticas avanzadas. La mayoría de establecimientos públicos prioriza terapias convencionales con tiempos de sesión reducidos debido a la alta demanda, lo que impide alcanzar la intensidad y repetitividad necesarias para generar cambios neuroplásticos significativos. Esta brecha asistencial deja a un amplio número de pacientes con secuelas persistentes del miembro superior post-stroke, dificultando actividades básicas como alimentarse, vestirse o manipular objetos, y restringiendo su reintegración laboral.
En consecuencia, existe una necesidad urgente de desarrollar soluciones accesibles, eficaces y contextualizadas al sistema de salud peruano, que permitan mejorar la función del miembro superior tanto en etapa subaguda como crónica, reduciendo la carga social, económica y asistencial asociada al ACV en el país.


## **3. Propuesta de solución**

## **4. Metodología (CRISP-DM)**

### 4.1 Business Understanding

El proyecto está dirigido a pacientes post-ACV con déficit motor en el miembro superior, una población altamente afectada por secuelas persistentes. El ACV representa la segunda causa de muerte y la tercera causa de discapacidad, por lo que su impacto clínico, funcional y socioeconómico es significativo.
Resolver este problema es importante porque las terapias convencionales muestran baja adherencia y una estimulación limitada de la neuroplasticidad, lo que dificulta una recuperación adecuada. La solución propuesta —un sistema BCI basado en imaginería motora y neurofeedback— aporta valor al potenciar la reorganización cortical, mejorar la participación del paciente y complementar la rehabilitación tradicional mediante retroalimentación en tiempo real.
El éxito se evaluará a través de:
- Precisión ≥ 80% en la clasificación de señales de imaginería motora,

- Consistencia neurofisiológica entre datasets clínicos y señales reales,

- La viabilidad técnica del sistema como herramienta accesible y complementaria en la rehabilitación post-ACV.


### 4.2 Data Understanding

Las señales empleadas en este proyecto provienen de tareas de motor imagery (MI), base de los BCI basados en Sensorimotor Rhythms (SMR). En reposo, la corteza sensoriomotora muestra actividad en dos bandas principales:

- Mu (8–12 Hz)
- Beta (13–30 Hz)

Cuando el usuario ejecuta o imagina un movimiento, estos ritmos dejan su estado de reposo y aparecen dos fenómenos clave:

- ERD: disminución de potencia en mu/beta durante la imaginación motora.
- ERS: recuperación o aumento de potencia al regresar al reposo.

Estos cambios son específicos de la región cortical correspondiente (por ejemplo, C3 para mano derecha) y permiten distinguir distintas clases de MI.

##### Hipótesis del proyecto

> Los patrones SMR característicos de la ERS y EDS deben manifestarse en los datos registrados con el sistema Ultracortex Mark IV y la placa Cyton de forma consistente con los observados en los datasets de referencia BCI Competition IV 2a y 2b, evidenciando diferencias distinguibles entre las clases de imaginación motora.

Esta consistencia es fundamental para validar que Neuromotion XR pueda funcionar tanto con datos clínicos estandarizados como con señales reales capturadas con hardware accesible.


#### 4.2.1 Fuentes de Datos

Se utilizaron tres fuentes principales de datos:

1. **BCI Competition IV Dataset 2a**: Dataset público de la competencia BCI que contiene señales EEG de 9 sujetos realizando tareas de MI con 4 clases (mano izquierda, mano derecha, pies, lengua). Cada sujeto tiene 22 canales EEG y 3 canales EOG, con una frecuencia de muestreo de 250 Hz.

2. **BCI Competition IV Dataset 2b**: Dataset público que contiene señales EEG de 9 sujetos realizando tareas de MI con 2 clases (mano izquierda, mano derecha). Cada sujeto tiene 3 canales EEG (C3, Cz, C4) y 3 canales EOG, con una frecuencia de muestreo de 250 Hz.

| Característica         | Dataset 2a                                          | Dataset 2b                                          |
| ---------------------- | --------------------------------------------------- | --------------------------------------------------- |
| Nº de canales EEG      | 22 (más resolución espacial)                        | 3 bipolares (simplificado)                          |
| Canales EOG            | 3                                                   | 3                                                   |
| Frecuencia de muestreo | 250 Hz                                              | 250 Hz                                              |
| Nº de clases           | 4 (mano izq., mano der., pies, lengua)              | 2 (mano izq., mano der.)                            |
| Nº de sujetos          | 9                                                   | 9                                                   |
| Complejidad            | Alta – más realista                                 | Baja – más ligero                                   |
| Relevancia clínica     | Mejor para simular rehab. con múltiples movimientos | Bueno para prototipos iniciales o hardware limitado |

3. **Grabación de laboratorio**: Señal EEG adquirida en laboratorio con 8 canales genéricos, frecuencia de muestreo de 250 Hz, realizando tareas de MI con 2 clases (mano izquierda, mano derecha) mediante la placa Cyton y el Ultracortex Mark IV.


#### 4.2.2 Exploración de Datos

##### 4.2.2.1 Carga y Visualización Inicial

Los datos se cargaron utilizando la biblioteca MNE-Python (`mne.io.read_raw_gdf()`), que permite leer archivos en formato GDF (General Data Format) utilizados comúnmente en BCI. Se realizó una inspección inicial de:

- **Estructura de canales**: Identificación de canales EEG y EOG disponibles
- **Información de muestreo**: Frecuencia de muestreo, duración de las grabaciones
- **Metadatos**: Información sobre eventos, anotaciones y estructura temporal

| Señal original - Database 2a | Señal original - Database 2b | Señal original - Adriana|                    
|-------------------------|----------|---------------------------------|
|<img width="1427" height="999" alt="image" src="https://github.com/user-attachments/assets/c636513b-2c74-4bfc-b469-1fdb11f586b6" />| <img width="1427" height="999" alt="image" src="https://github.com/user-attachments/assets/96596962-763f-4f27-ac2a-24757fcc1805" />| <img width="1446" height="999" alt="image" src="https://github.com/user-attachments/assets/58abb11f-b303-4bbc-b2cb-f10c56a16d38" />|

##### 4.2.2.2 Análisis de Eventos y Anotaciones

Se extrajeron los eventos de las anotaciones utilizando `mne.events_from_annotations()`, identificando:

- **Eventos de Motor Imagery**: 
  - Dataset 2a: Eventos 7, 8, 9, 10 correspondientes a las 4 clases de MI
  - Dataset 2b: Eventos 10, 11 (mapeados desde eventos originales 769, 770) correspondientes a mano izquierda y derecha
  - Grabación de laboratorio: Eventos 10, 11 correspondientes a mano izquierda y derecha

- **Eventos de control**: Eventos relacionados con inicio de trials, movimientos oculares, artefactos, etc.

Ejemplo de la estructura de eventos del 2a:

<p align="center">
  <img src="https://github.com/user-attachments/assets/f975e85b-87dd-49b5-9015-8da2f830e37b" width="60%">
</p>


#### 4.2.3 Verificación de Distribución de Clases

Se implementó un sistema de verificación para confirmar la distribución correcta de trials por clase, asegurando que:

- Las etiquetas de eventos correspondan correctamente a las clases de MI.
- La distribución de trials sea balanceada o al menos representativa.
- Los eventos estén correctamente mapeados según la documentación de cada dataset.

### 4.3 Data Preparation

La fase de Data Preparation incluye todas las transformaciones y limpiezas necesarias para preparar los datos para el análisis y modelado posterior.

#### 4.3.1 Eliminación de Canales EOG

Los canales EOG (Electrooculografía) capturan actividad ocular y no son relevantes para el análisis de Motor Imagery. Se eliminaron sistemáticamente todos los canales que contenían "EOG" en su nombre utilizando `raw.drop_channels()`.

**Justificación**: Los canales EOG introducen artefactos relacionados con movimientos oculares y parpadeos que pueden contaminar las señales EEG de interés. Su eliminación mejora la calidad de los datos para el análisis de ritmos sensoriomotores.

#### 4.3.2 Filtrado de Señales

Se aplicaron dos tipos de filtros para mejorar la calidad de las señales y enfocarse en las bandas de frecuencia relevantes:

##### 4.3.2.1 Filtro Pasabanda (Bandpass Filter)

- **Rango de frecuencias**: 8-30 Hz
- **Método**: Filtro IIR (Infinite Impulse Response) tipo Butterworth de fase cero
- **Justificación**: 
  - La banda de 8-30 Hz engloba los ritmos mu (8-12 Hz) y beta (13-30 Hz), que son los ritmos sensoriomotores más relevantes para Motor Imagery
  - Elimina componentes de baja frecuencia (drift, artefactos de movimiento) y alta frecuencia (ruido electromagnético, actividad muscular)

##### 4.3.2.2 Filtro Notch (Bandstop Filter)

- **Frecuencia central**: 50 Hz
- **Método**: Filtro FIR (Finite Impulse Response) tipo Hamming
- **Justificación**: Elimina el ruido de la línea eléctrica, que es una fuente común de contaminación en señales EEG

| Señal filtrada - Database 2a | Señal filtrada - Database 2b | Señal filtrada - Adriana|                    
|-------------------------|----------|---------------------------------|
|<img width="1427" height="999" alt="image" src="https://github.com/user-attachments/assets/a7b3fe89-2c4b-4007-bd12-7e4241ea1216" />| <img width="1427" height="999" alt="image" src="https://github.com/user-attachments/assets/05ae3484-b976-42a5-932a-132b1751af78" />| <img width="1446" height="999" alt="image" src="https://github.com/user-attachments/assets/d661af50-a189-4423-80f3-dca4cf9bf447" />|

#### 4.3.3 Segmentación Temporal (Epoching)

Se segmentaron las señales continuas en epochs (ventanas temporales) centradas en los eventos de Motor Imagery:

- **Ventana temporal**: Desde -0.5 s hasta 4.0 s respecto al evento
  - **Período pre-evento (-0.5 a 0 s)**: Utilizado como línea base (baseline) para normalización
  - **Período post-evento (0 a 4 s)**: Contiene la actividad de Motor Imagery de interés

- **Parámetros**:
  - `tmin=-0.5`: Inicio de la ventana antes del evento
  - `tmax=4.0`: Fin de la ventana después del evento
  - `baseline=None`: Se aplica baseline correction posteriormente en el análisis TFR

**Justificación**: La segmentación permite analizar la evolución temporal de la actividad cerebral relacionada con cada tarea de MI, facilitando la identificación de patrones ERD/ERS.

#### 4.3.4 Análisis Espectral (PSD)

Se realizó un análisis de densidad espectral de potencia (Power Spectral Density, PSD) utilizando el método `compute_psd()` de MNE-Python para:

- **Identificar bandas de frecuencia relevantes**: Confirmar la presencia de actividad en las bandas mu (8-12 Hz) y beta (13-30 Hz), características de los ritmos sensoriomotores (SMR).
- **Evaluar calidad de señal**: Detectar posibles artefactos, ruido de línea eléctrica (50 Hz), y características espectrales generales.
- **Comparar entre datasets**: Analizar diferencias espectrales entre los diferentes datasets y sujetos.


| PSD - Database 2a | PSD - Database 2b | PSD - Adriana|                    
|-------------------------|----------|---------------------------------|
|<img width="1511" height="1011" alt="image" src="https://github.com/user-attachments/assets/a5e6a7c0-c1e2-49c6-b912-9ae294c3cfd9" />| <img width="1511" height="1011" alt="image" src="https://github.com/user-attachments/assets/a8fb836a-d2b0-4a3f-b43b-16e434007829" />| <img width="1011" height="361" alt="image" src="https://github.com/user-attachments/assets/c9a66a79-674b-46cc-b48d-69477deffb73" />|

#### 4.3.5 Análisis de Representación Tiempo-Frecuencia (TFR)

Se realizó un análisis de representación tiempo-frecuencia utilizando wavelets de Morlet para caracterizar los fenómenos de Event-Related Desynchronization (ERD) y Event-Related Synchronization (ERS).

##### 4.3.5.1 Cálculo de TFR

- **Método**: `compute_tfr(method='morlet')` de MNE-Python
- **Frecuencias analizadas**: 8-30 Hz con resolución de 1 Hz
- **Número de ciclos**: `n_cycles = freqs / 2.0` (adaptativo según frecuencia)
- **Decimación**: Factor de 3 para reducir la resolución temporal y el costo computacional
- **Promediado**: Se promediaron los TFRs de todos los trials de cada clase

##### 4.3.5.2 Corrección de Baseline

Se aplicó corrección de baseline utilizando el modo log-ratio:

- **Ventana de baseline**: -0.5 a 0 s (período pre-evento)
- **Modo**: `mode='logratio'` (logaritmo de la razón entre potencia post-evento y baseline)
- **Fórmula**: `log10(power_post / power_baseline)`


| TFR - Database 2a | TFR - Database 2b | TFR - Adriana|                    
|-------------------------|----------|---------------------------------|
|<img width="1511" height="1011" alt="image" src="https://github.com/miguel-isidro05/GRUPO-05-ISB-2025-II/blob/main/Proyecto/Software/Data_analysis/tfr_C3_left_vs_right.png" />| <img width="1511" height="1011" alt="image" src="https://github.com/miguel-isidro05/GRUPO-05-ISB-2025-II/blob/main/Proyecto/Software/Data_analysis/tfr_C3_left_vs_right_2b.png"/>| <img width="1600" height="600" alt="image" src="https://github.com/user-attachments/assets/5a4d3da3-e3b9-4875-af96-e7916df6c0f0" />
| <img width="1600" height="600" alt="image" src="https://github.com/user-attachments/assets/c0ff4a6b-fbc0-45c9-b68b-ce1c43c9d7f7" />| <img width="1600" height="600" alt="image" src="https://github.com/user-attachments/assets/4b1c2252-2f04-494e-9778-2bed83c788e5" />| <img width="1600" height="600" alt="image" src="https://github.com/user-attachments/assets/0681ed15-39a1-4880-b224-30ed6ce2c4fb" />|

**Interpretación**:

- **Valores negativos**: Indican ERD (disminución de potencia respecto al baseline)

- **Valores positivos**: Indican ERS (aumento de potencia respecto al baseline)

##### 4.3.5.3 Visualizaciones de ERD/ERS

Se generaron múltiples visualizaciones para analizar los patrones ERD/ERS:

1. **Espectrogramas TFR por canal**: Comparación de MI izquierda vs derecha para canales C3 y C4
   - Visualización lado a lado para facilitar la comparación
   - Escala de colores RdBu_r (rojo-azul invertido) donde rojo indica ERD y azul indica ERS

2. **Evolución temporal y frecuencial**: Gráficos de 8 paneles mostrando:
   - Evolución temporal de bandas mu (8-12 Hz) y beta (13-30 Hz) para C3 y C4
   - Espectrogramas frecuenciales de las mismas bandas
   - Promedio de condiciones izquierda y derecha para visualizar patrones generales

3. **Visualización de diferencia**: Para el recording de Adriana, se calculó la diferencia directa (derecha - izquierda) para reducir ruido común y resaltar diferencias específicas entre condiciones


### 4.4 Modeling

#### 4.4.1. Algoritmo FBCSP

El algoritmo FBCSP es una optimización del método Common Spatial Patterns (CSP) que incorpora un banco de filtros para capturar información discriminativa en distintas bandas de frecuencia relevantes para Motor Imagery (MI). Este enfoque mejora la robustez del modelo frente a la variabilidad espectral entre sujetos y sesiones, permitiendo una extracción de características más estable y completa.

<p align="center">
  <img src="https://github.com/user-attachments/assets/0873a6eb-d1bb-439f-9a70-015883d5f6e9" width="70%">
</p>

##### *4.4.1.2. Filter Bank:* 
El primer paso consiste en aplicar un conjunto de filtros pasabanda distribuidos en intervalos consecutivos dentro del rango asociado al control motor, típicamente ondas μ (8–13 Hz) y ondas β (13–30 Hz).
Cada filtro genera una versión distinta de la misma señal EEG, preservando información específica de cada sub-banda. El objetivo es capturar patrones espectrales relevantes que no necesariamente se expresan igual en todos los sujetos o en todas las frecuencias.

##### *4.4.1.2. Common Spatial Pattern (CSP):*
Una vez filtrada la señal en cada banda, se aplica el algoritmo CSP, cuya finalidad es encontrar proyecciones espaciales óptimas que maximicen la varianza para una clase y la minimicen para la otra. Esto es especialmente útil en BCI porque la varianza del EEG en bandas específicas se correlaciona con la potencia y, por extensión, con la activación cortical.
*Idea central:* CSP asigna mayor peso espacial a los electrodos ubicados en áreas sensoriomotoras (C3 y C4), y entre ellos selecciona aquellos con mayor capacidad discriminante para diferenciar entre ambas clases.

##### *4.4.1.2. Feature Extraction:*
De cada componente espacial generado por CSP, se calcula la varianza normalizada o la log-varianza, obteniendo características robustas que representan la potencia de las señales.
La salida final por cada banda de frecuencia es un vector de features que posteriormente se concatenan y se alimentan a un clasificador en la siguiente etapa como lo es el LDA.

*Nota:* Nosotros para el análisis OFFLINE usamos el algoritmo FBCSP entre bandas alpha y beta para maximizar el accuracy. Sin embargo, para el análisis ONLINE y entrenamiento de los modelos nos vimos obligados a usar CSP debido a la complejidad de usar FBCSP en la implementación con OPEN VIBE.

#### 4.4.2. EEGNET


EEGNet es una arquitectura de red neuronal convolucional compacta diseñada específicamente para aplicaciones de BCI basadas en EEG. Esta arquitectura fue seleccionada para el proyecto debido a sus características clave: (1) puede aplicarse a diferentes paradigmas de BCI, (2) puede entrenarse con datos limitados, y (3) produce características neurofisiológicamente interpretables. Para este proyecto, se utilizó principalmente el **BCI Competition IV Dataset 2b** para entrenar y evaluar el modelo, permitiendo comparaciones directas con otros métodos.

#### 3.4.2.1 Arquitectura del Modelo

EEGNet implementa una arquitectura de dos bloques principales que procesan señales EEG de forma eficiente:

<img width="391" height="220" alt="image" src="https://github.com/user-attachments/assets/0bcca46f-f2eb-4e80-a85c-acba854af9c7" />

**Bloque 1: Filtrado Temporal y Espacial**

- **Convolución Temporal**: Se aplican F1 filtros convolucionales 2D de tamaño (1, 64), donde la longitud del filtro temporal se elige como la mitad de la frecuencia de muestreo de los datos (128 Hz en este caso). Esta configuración permite capturar información de frecuencia a partir de 2 Hz y superior. Para el dataset 2b con frecuencia de muestreo de 250 Hz, se ajustó el kernel temporal a 32 muestras (equivalente a ~128 ms).

- **Convolución Depthwise**: Se utiliza una convolución depthwise de tamaño (C, 1), donde C es el número de canales EEG. Esta operación aprende filtros espaciales específicos para cada filtro temporal, permitiendo la extracción eficiente de filtros espaciales específicos de frecuencia. Un parámetro de profundidad D controla el número de filtros espaciales a aprender para cada mapa de características (feature map).

- **Normalización y Activación**: Se aplica Batch Normalization a lo largo de la dimensión del mapa de características, seguido de la función de activación ELU (Exponential Linear Unit).

- **Regularización**: Se utiliza Dropout con probabilidad 0.5 para clasificación within-subject (para prevenir sobreajuste con tamaños de muestra pequeños) y 0.25 para clasificación cross-subject. Además, se aplica una restricción de norma máxima de 1 a los pesos de cada filtro espacial (||w||₂ < 1).

- **Reducción Dimensional**: Se aplica Average Pooling de tamaño (1, 4) para reducir la frecuencia de muestreo de la señal a aproximadamente 32 Hz.

**Bloque 2: Convolución Separable**

- **Convolución Separable**: Consiste en una convolución depthwise de tamaño (1, 16), que representa aproximadamente 500 ms de actividad EEG a 32 Hz, seguida de F2 convoluciones pointwise de tamaño (1, 1). Esta operación separa explícitamente la relación dentro y entre mapas de características, aprendiendo primero un kernel que resume cada mapa de características individualmente, y luego combinando óptimamente las salidas.

- **Reducción Dimensional**: Se aplica Average Pooling de tamaño (1, 8) para reducción adicional de dimensiones.

**Bloque de Clasificación**

- Las características se pasan directamente a una capa de clasificación softmax con N unidades, donde N es el número de clases (2 en este caso: mano izquierda y mano derecha). Se omite el uso de una capa densa para agregación de características previa a la capa softmax para reducir el número de parámetros libres del modelo.

Asimismo el modelo se entrenó utilizando:

- **Optimizador**: Adam con parámetros por defecto
- **Función de pérdida**: Categorical Cross-Entropy
- **Epochs**: 500 iteraciones de entrenamiento
- **Validación**: Se implementó early stopping, guardando los pesos del modelo que produjeron la menor pérdida en el conjunto de validación
- **Dataset principal**: BCI Competition IV Dataset 2b (2 clases: mano izquierda y mano derecha)
  
#### 4.4.3. Openvibe

Para la implementación del pipeline de clasificación en tiempo real, se utilizó OpenVIBE, una plataforma de código abierto diseñada específicamente para interfaces cerebro-computadora (BCI) y procesamiento de señales biomédicas. El flujo de trabajo implementado utiliza Common Spatial Patterns (CSP) para la extracción de características espaciales y Linear Discriminant Analysis (LDA) como clasificador.

<img width="968" height="601" alt="image" src="https://github.com/user-attachments/assets/b1d76bc9-62ac-438d-b9fc-4c963218f551" />

##### 4.4.3.1 Configuración Inicial y Adquisición de Datos

Antes de realizar las grabaciones en laboratorio, se siguió un protocolo manual de configuración:

**Acceso al Acquisition Server**

- El Acquisition Server viene incluido al instalar OpenVIBE y se abre desde el menú de inicio junto con una terminal que muestra mensajes de estado útiles (logs).
- Es el primer paso antes de abrir el **Designer**, ya que este último recibirá los datos desde el servidor.
- Preferiblemente se conecta OpenBCI GUI para verificar la impedancia de los electrodos y realizar configuraciones iniciales correctas antes de conectar directamente a OpenVIBE.

**Escenarios de Entrenamiento**

El pipeline de entrenamiento consta de cuatro escenarios principales:

1. **mi-csp-0-signal-monitoring.xml**: Sirve para verificar la calidad de la señal y el correcto funcionamiento de la adquisición de datos. Una vez confirmado que todo funciona correctamente, se procede con el siguiente escenario.

2. **mi-csp-1-acquisition.xml**: Adquiere datos EEG de entrenamiento cuando el usuario imagina mover la mano izquierda o derecha. Se ajusta con el **LUA stimulator** (número de ensayos, duración de cada ensayo, descansos, etc.), donde se guarda el archivo con los datos de entrenamiento.

   - **Nota importante**: Si se van a modificar parámetros, se debe realizar una copia del escenario.
   - El archivo de grabación se nombra como "motor-imagery-csp-1-acquisition-[$core{date}-$core{time}].ov".
   - **Error común**: Se debe configurar solo con enteros dentro de los parámetros, de lo contrario el sistema se cuelga y deja de funcionar.
   - Una vez que empieza el Graz visualization, puede parecer que el escenario nunca termina, pero está cargando inicialmente. Se debe dejar recargar un rato (asegurándose de haber configurado la adquisición de datos correctamente).
   - El marcador indica si el proceso ya terminó o no.


3. **mi-csp-2-train-csp.xml**: Calcula los filtros espaciales con el método Common Spatial Pattern (CSP). Toma los EEG crudos y aprende combinaciones lineales de los canales que maximizan la varianza para clase A (mano izquierda) y minimizan para clase B (mano derecha), y viceversa. Este proceso transforma los datos pero no aprende a clasificar.

   - **Entrada**: Archivo previamente adquirido en el paso de adquisición de señales.
   - **Salida**: Conjunto de filtros espaciales entrenados.
   - **Parámetros**: Se ajustan para reducir la información por electrodos a 4 filtros espaciales.


##### 4.4.3.2 Análisis del Escenario de Entrenamiento

Durante el **entrenamiento**, se utiliza:

- **Stimulus-based epoching**: 0.5 – 4 s después del estímulo.
  - Esto define *una sola época por intento* (por ejemplo, cada ensayo de "mano izquierda" o "mano derecha").
  - El propósito aquí es **extraer una sola característica representativa por intento**.

El flujo de entrenamiento es:

```text
EEG → Stimulus-based Epoching (0.5–4s)
     → CSP Trainer
     → CSP Apply
     → Feature Extraction (varianza/log-varianza)
     → Feature Aggregator (opcional)
     → Classifier Trainer
```

En esta fase, el sistema **aprende**:

- Qué combinaciones espaciales (CSP) separan mejor las clases.
- Qué distribución de *features* (energía, log-varianza, etc.) corresponde a cada clase.

No se necesita "time-based epoching" aquí porque **ya sabemos cuándo comienza y termina cada intento**.

4. **mi-csp-3-classifier-trainer.xml**: Entrena el clasificador LDA con los datos ya filtrados por CSP. Se ajusta el canal de referencia y otros parámetros según el paradigma de EEG. Aquí se genera el modelo que discrimina entre derecha e izquierda.

   - Se asegura que el archivo se encuentre en el directorio donde se grabó la data.
   - Al ejecutar el escenario, se espera a que entrene el clasificador LDA.
   - Al finalizar correctamente, el sistema muestra un mensaje de confirmación.



## **5. Resultados**

### 5.1. Métricas de Performance

#### 5.1.1. Accuracy

<div align="center">

<table>
  <tr>
    <th>Dataset</th>
    <th>Accuracy</th>
  </tr>
  <tr>
    <td><b>Dataseet Competition IV 2a</b></td>
    <td><b>91.71%</b></td>
  </tr>
  <tr>
    <td><b>Dataseet Competition IV 2b</b></td>
    <td><b>75.50%</b></td>
  </tr>
  <tr>
    <td><b>Testeo técnico de Adriana</b></td>
    <td><b>69.48%</b></td>
  </tr>
</table>

</div>

#### 5.1.2. Matriz de confusión

<div align="center">

<table>
  <tr>
    <th>Matriz de confusión – Dataset 2a</th>
    <th>Matriz de confusión – Dataset 2b</th>
    <th>Matriz de confusión – Adriana</th>
  </tr>
  <tr>
    <td><img width="300" src="https://github.com/user-attachments/assets/1768fd7d-c0ff-4529-b9c5-38699977734c" /></td>
    <td><img width="300" src="https://github.com/user-attachments/assets/eb18d78d-effe-484a-b2c1-4c9c2508f737" /></td>
    <td><img width="300" src="https://github.com/user-attachments/assets/0e69a059-cb12-4c6b-ab66-00874637d6e9" /></td>
  </tr>
</table>

</div>


#### 5.1.3. Curvas ROC

<div align="center">

<table>
  <tr>
    <th>ROC – Dataset 2a</th>
    <th>ROC – Dataset 2b</th>
  </tr>
  <tr>
    <td><img width="350" src="https://github.com/user-attachments/assets/158e95b8-ef1d-462e-b3f0-709c8ede50e3" /></td>
    <td><img width="350" src="https://github.com/user-attachments/assets/b8fe63e3-b581-40f9-aa6b-e1096dc8ebb3" /></td>
  </tr>
</table>

</div>

#### 5.1.4. Comparación entre métricas

<div align="center">

<table>
  <tr>
    <th><b>Fuente de datos</b></th>
    <th><b>Acierto clase izquierda</b></th>
    <th><b>Acierto clase derecha</b></th>
    <th><b>Error / Confusión</b></th>
    <th><b>Observaciones</b></th>
  </tr>

  <tr>
    <td><b>Dataset 2a</b></td>
    <td>92%</td>
    <td>92%</td>
    <td>8% – 8%</td>
    <td>
      Alto rendimiento y excelente separabilidad.<br>
      Beneficia la mayor cantidad de electrodos (22 canales).<br>
      Patrones SMR bien definidos.
    </td>
  </tr>

  <tr>
    <td><b>Dataset 2b</b></td>
    <td>78%</td>
    <td>73%</td>
    <td>23% – 27%</td>
    <td>
      Disminución esperada por uso de solo 3 canales (C3, Cz, C4).<br>
      Mayor confusión entre clases.<br>
      Aun así, desempeño estable.
    </td>
  </tr>

  <tr>
    <td><b>OpenBCI (Testeo real)</b></td>
    <td>67%</td>
    <td>70%</td>
    <td>30% – 33%</td>
    <td>
      Variabilidad real del EEG y artefactos incrementan la confusión.<br>
      Número de canales limitado.<br>
      Confirma viabilidad técnica del sistema en condiciones reales.
    </td>
  </tr>

</table>

</div>


### 5.2. Resultados del análisis de los dataseets (OFFLINE)

#### 5.2.1. Componentes CSP 

<div align="center">

<table>
  <tr>
    <th><b>Dataset 2a</b></th>
    <th><b>Dataset 2b</b></th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/d3dc4f81-6153-4a55-a401-aad068e820df" width="90%">
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/d7b9dd5c-f08c-48b4-84da-0e2f00d8cea9" width="90%">
    </td>
  </tr>
</table>

</div>

- En el Dataset 2a se observan patrones CSP bien diferenciados entre clases. Los mapas muestran activación distribuida principalmente sobre regiones sensorimotoras (C3 y C4), con contrastes claros entre hemisferios. Los componentes CSP0 y CSP3 resaltan la actividad contralateral, exhibiendo valores más altos sobre un hemisferio específico según la clase de MI (izquierda o derecha). Esta topografía compleja y rica se debe al mayor número de canales (22 EEG), lo que permite al algoritmo capturar con mayor precisión los cambios ERD/ERS asociados a cada movimiento imaginado.

- En el Dataset 2b, los patrones CSP son más simétricos y muestran una separación más limitada entre hemisferios. Los mapas CSP0 y CSP1 exhiben contrastes amplios pero con menor detalle espacial, debido a que el dataset solo dispone de 3 canales bipolares (C3, Cz, C4). Esto restringe la capacidad del algoritmo para capturar variaciones locales de ERD/ERS, produciendo patrones más generalizados y menos discriminativos.

#### 5.2.2. Observaciones relevanmtes por dataseets

##### 5.2.2.1. Dataset 2a

- Presenta 22 canales EEG, lo que proporciona mayor resolución espacial y permite identificar con más claridad la actividad contralateral asociada al Motor Imagery.

- Los patrones ERD/ERS en C3 y C4 son más definidos y consistentes entre sujetos, facilitando la discriminación entre mano izquierda y mano derecha.

- La calidad de la señal es elevada, con menor presencia de artefactos comparado con registros de hardware de bajo costo.

- La mayor cantidad de ensayos por sujeto permite entrenar modelos más robustos y menos sensibles al ruido.

- Se observa alta separabilidad entre clases, evidenciada por los valores elevados de acierto y por la claridad de las componentes CSP filtradas.

##### 5.2.2.2. Dataset 2b

- Utiliza solo 3 canales bipolares (C3, Cz, C4), lo cual reduce considerablemente la información espacial disponible.

- La discriminación entre tareas motoras se vuelve más dependiente del sujeto, mostrando mayor variabilidad inter-sujeto.

- La definición de los patrones ERD/ERS es más tenue, especialmente en presencia de ruido muscular o mala colocación del electrodo Cz.

- Aunque su rendimiento es menor que en 2a, mantiene consistencia funcional, demostrando que incluso configuraciones minimalistas pueden capturar información útil para BCI.

- El protocolo sin feedback visual hace que algunos sujetos generen señales menos estables.

## **6. Conclusiones**

## **7. Referencias Bibliograficas**


[1] V. L. Feigin et al., “World Stroke Organization: Global Stroke Fact Sheet 2025,” Int. J. Stroke, vol. 20, no. 2, pp. 132–144, 2025. [Online]. Available: https://pmc.ncbi.nlm.nih.gov/articles/PMC11786524/

[2] V. L. Feigin et al., “Global burden of stroke,” The Lancet, vol. 383, no. 9913, pp. 245–254, 2014. [Online]. Available: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(13)61953-4/fulltext

[3] Bernhardt, J. et al. “Agreed definitions and a shared vision for new standards in stroke recovery research.” International Journal of Stroke (2017).
 https://journals.sagepub.com/doi/10.1177/1747493017730746

[4] Cramer, S. et al. “Harnessing neuroplasticity for clinical applications.” Brain (2011).
 https://academic.oup.com/brain/article/134/5/1591/415847

[5] Kwakkel, G. et al. “Effects of intensity of rehabilitation after stroke.” Lancet Neurology (2004).
 https://www.sciencedirect.com/science/article/pii/S1474442204008952

[6] A. Rafferty et al., “Recommendations for Upper Limb Motor Recovery: An Overview of the UK and European Rehabilitation after Stroke Guidelines,” Healthcare, vol. 12, no. 14, p. 1433, 2024. doi: 10.3390/healthcare12141433.










