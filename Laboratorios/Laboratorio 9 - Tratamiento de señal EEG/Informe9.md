# **Laboratorio 9: Tratamiento de señal EEG adquirida del ULTRACORTEX MARK IV con ICA**

## 1. Visualización con MNE



## 2. Procesamiento con ICA
El Análisis de Componentes Independientes (ICA) es un algoritmo de extracción de características que identifica componentes estadísticamente independientes en un conjunto de datos, reduciendo las dependencias de segundo y tercer orden. En el caso de la señal EEG, el ICA permite identificar y eliminar artefactos sin perder las señales neuronales relevantes.
En el presente análisis se empleó la técnica de Análisis de Componentes Independientes (ICA) con el objetivo de separar las fuentes neuronales de los artefactos fisiológicos y eléctricos presentes en la señal EEG. La señal fue adquirida por medio de 8 canales a una frecuencia de muestreo de 250 Hz. En este caso, se extrajeron 7 componentes independientes. Esto se debe a que cada canal representa una mezcla de las mismas fuentes, y el modelo ICA clásico asume que el número de fuentes no puede ser mayor que el número de sensores.Esta elección sigue las recomendaciones de la literatura, donde se establece que el número de componentes extraídos debe ser igual al número de canales después del preprocesamiento (Dharmaprani et al., 2016).


