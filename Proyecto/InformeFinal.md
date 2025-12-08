# **NeuroMotion XR: Sistema Interfaz Cerebro-Computador para Rehabilitación Post-ACV Basada en Imaginería Motora y Neurofeedback**

## *Resumen*

## *Palabras clave*

## **1. Introducción**

## **2. Planteamiento del problema**

## 3. Metodología (CRISP-DM)

### 3.1 Business Understanding

*(Sección pendiente de desarrollo)*

### 3.2 Data Understanding

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


#### 3.2.1 Fuentes de Datos

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


#### 3.2.2 Exploración de Datos

##### 3.2.2.1 Carga y Visualización Inicial

Los datos se cargaron utilizando la biblioteca MNE-Python (`mne.io.read_raw_gdf()`), que permite leer archivos en formato GDF (General Data Format) utilizados comúnmente en BCI. Se realizó una inspección inicial de:

- **Estructura de canales**: Identificación de canales EEG y EOG disponibles
- **Información de muestreo**: Frecuencia de muestreo, duración de las grabaciones
- **Metadatos**: Información sobre eventos, anotaciones y estructura temporal

| Señal original - Database 2a | Señal original - Database 2b | Señal original - Adriana|                    
|-------------------------|----------|---------------------------------|
|Ploteo   |<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/28d5a92b-c238-4200-9b27-3853f5fd7fa8" />|<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/651a937b-3868-49ad-a85c-bb04dbd2b22d" />|
|  PSD |<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/c4967867-017a-4389-b0a5-371ea8b0f58b" />|<img width="704" height="463" alt="image" src="https://github.com/user-attachments/assets/78dbddfa-836b-4129-be68-74ca7bcc7258" />|

##### 3.2.2.2 Análisis de Eventos y Anotaciones

Se extrajeron los eventos de las anotaciones utilizando `mne.events_from_annotations()`, identificando:

- **Eventos de Motor Imagery**: 
  - Dataset 2a: Eventos 7, 8, 9, 10 correspondientes a las 4 clases de MI
  - Dataset 2b: Eventos 10, 11 (mapeados desde eventos originales 769, 770) correspondientes a mano izquierda y derecha
  - Grabación de laboratorio: Eventos 10, 11 correspondientes a mano izquierda y derecha

- **Eventos de control**: Eventos relacionados con inicio de trials, movimientos oculares, artefactos, etc.

Ejemplo de la estructura de eventos del 2a:

<img width="1189" height="990" alt="image" src="https://github.com/user-attachments/assets/28d5a92b-c238-4200-9b27-3853f5fd7fa8" />


#### 3.2.3 Verificación de Distribución de Clases

Se implementó un sistema de verificación para confirmar la distribución correcta de trials por clase, asegurando que:

- Las etiquetas de eventos correspondan correctamente a las clases de MI.
- La distribución de trials sea balanceada o al menos representativa.
- Los eventos estén correctamente mapeados según la documentación de cada dataset.

### 3.3 Data Preparation

La fase de Data Preparation incluye todas las transformaciones y limpiezas necesarias para preparar los datos para el análisis y modelado posterior.

#### 3.3.1 Eliminación de Canales EOG

Los canales EOG (Electrooculografía) capturan actividad ocular y no son relevantes para el análisis de Motor Imagery. Se eliminaron sistemáticamente todos los canales que contenían "EOG" en su nombre utilizando `raw.drop_channels()`.

**Justificación**: Los canales EOG introducen artefactos relacionados con movimientos oculares y parpadeos que pueden contaminar las señales EEG de interés. Su eliminación mejora la calidad de los datos para el análisis de ritmos sensoriomotores.

#### 3.3.2 Filtrado de Señales

Se aplicaron dos tipos de filtros para mejorar la calidad de las señales y enfocarse en las bandas de frecuencia relevantes:

##### 3.3.2.1 Filtro Pasabanda (Bandpass Filter)

- **Rango de frecuencias**: 8-30 Hz
- **Método**: Filtro IIR (Infinite Impulse Response) tipo Butterworth de fase cero
- **Justificación**: 
  - La banda de 8-30 Hz engloba los ritmos mu (8-12 Hz) y beta (13-30 Hz), que son los ritmos sensoriomotores más relevantes para Motor Imagery
  - Elimina componentes de baja frecuencia (drift, artefactos de movimiento) y alta frecuencia (ruido electromagnético, actividad muscular)

##### 3.3.2.2 Filtro Notch (Bandstop Filter)

- **Frecuencia central**: 50 Hz
- **Método**: Filtro FIR (Finite Impulse Response) tipo Hamming
- **Justificación**: Elimina el ruido de la línea eléctrica, que es una fuente común de contaminación en señales EEG

#### 3.3.3 Segmentación Temporal (Epoching)

Se segmentaron las señales continuas en epochs (ventanas temporales) centradas en los eventos de Motor Imagery:

- **Ventana temporal**: Desde -0.5 s hasta 4.0 s respecto al evento
  - **Período pre-evento (-0.5 a 0 s)**: Utilizado como línea base (baseline) para normalización
  - **Período post-evento (0 a 4 s)**: Contiene la actividad de Motor Imagery de interés

- **Parámetros**:
  - `tmin=-0.5`: Inicio de la ventana antes del evento
  - `tmax=4.0`: Fin de la ventana después del evento
  - `baseline=None`: Se aplica baseline correction posteriormente en el análisis TFR

**Justificación**: La segmentación permite analizar la evolución temporal de la actividad cerebral relacionada con cada tarea de MI, facilitando la identificación de patrones ERD/ERS.

#### 3.3.4 Análisis Espectral (PSD)

Se realizó un análisis de densidad espectral de potencia (Power Spectral Density, PSD) utilizando el método `compute_psd()` de MNE-Python para:

- **Identificar bandas de frecuencia relevantes**: Confirmar la presencia de actividad en las bandas mu (8-12 Hz) y beta (13-30 Hz), características de los ritmos sensoriomotores (SMR).
- **Evaluar calidad de señal**: Detectar posibles artefactos, ruido de línea eléctrica (50 Hz), y características espectrales generales.
- **Comparar entre datasets**: Analizar diferencias espectrales entre los diferentes datasets y sujetos.

#### 3.3.5 Análisis de Representación Tiempo-Frecuencia (TFR)

Se realizó un análisis de representación tiempo-frecuencia utilizando wavelets de Morlet para caracterizar los fenómenos de Event-Related Desynchronization (ERD) y Event-Related Synchronization (ERS).

##### 3.3.5.1 Cálculo de TFR

- **Método**: `compute_tfr(method='morlet')` de MNE-Python
- **Frecuencias analizadas**: 8-30 Hz con resolución de 1 Hz
- **Número de ciclos**: `n_cycles = freqs / 2.0` (adaptativo según frecuencia)
- **Decimación**: Factor de 3 para reducir la resolución temporal y el costo computacional
- **Promediado**: Se promediaron los TFRs de todos los trials de cada clase

##### 3.3.5.2 Corrección de Baseline

Se aplicó corrección de baseline utilizando el modo log-ratio:

- **Ventana de baseline**: -0.5 a 0 s (período pre-evento)
- **Modo**: `mode='logratio'` (logaritmo de la razón entre potencia post-evento y baseline)
- **Fórmula**: `log10(power_post / power_baseline)`

**Interpretación**:

- **Valores negativos**: Indican ERD (disminución de potencia respecto al baseline)

- **Valores positivos**: Indican ERS (aumento de potencia respecto al baseline)

##### 3.3.5.3 Visualizaciones de ERD/ERS

Se generaron múltiples visualizaciones para analizar los patrones ERD/ERS:

1. **Espectrogramas TFR por canal**: Comparación de MI izquierda vs derecha para canales C3 y C4
   - Visualización lado a lado para facilitar la comparación
   - Escala de colores RdBu_r (rojo-azul invertido) donde rojo indica ERD y azul indica ERS

2. **Evolución temporal y frecuencial**: Gráficos de 8 paneles mostrando:
   - Evolución temporal de bandas mu (8-12 Hz) y beta (13-30 Hz) para C3 y C4
   - Espectrogramas frecuenciales de las mismas bandas
   - Promedio de condiciones izquierda y derecha para visualizar patrones generales

3. **Visualización de diferencia**: Para el recording de Adriana, se calculó la diferencia directa (derecha - izquierda) para reducir ruido común y resaltar diferencias específicas entre condiciones


### 3.4 Modeling

*(Sección pendiente de desarrollo - se implementará en fases posteriores)*

### 3.5 Evaluation

*(Sección pendiente de desarrollo - se implementará después del modeling)*

### 3.6 Deployment

*(Sección pendiente de desarrollo - se implementará al final del proyecto)*


## **4. Propuesta de solución**

## **5. Resultados**

## **6. Conclusiones**

## **7. Referencias Bibliograficas**



