# **Laboratorio 9: Tratamiento de señal EEG adquirida del ULTRACORTEX MARK IV con ICA**

## 1. Visualización con MNE



## 2. Procesamiento con ICA
El Análisis de Componentes Independientes (ICA) es un algoritmo de extracción de características que identifica componentes estadísticamente independientes en un conjunto de datos, reduciendo las dependencias de segundo y tercer orden. En el caso de la señal EEG, el ICA permite identificar y eliminar artefactos sin perder las señales neuronales relevantes.
En el presente análisis se empleó la técnica de Análisis de Componentes Independientes (ICA) con el objetivo de separar las fuentes neuronales de los artefactos fisiológicos y eléctricos presentes en la señal EEG. La señal fue adquirida por medio de 8 canales a una frecuencia de muestreo de 250 Hz. En este caso, se extrajeron 7 componentes independientes. Esto se debe a que cada canal representa una mezcla de las mismas fuentes, y el modelo ICA clásico asume que el número de fuentes no puede ser mayor que el número de sensores.Esta elección sigue las recomendaciones de la literatura, donde se establece que el número de componentes extraídos debe ser igual al número de canales después del preprocesamiento (Dharmaprani et al., 2016).
Existen diversas técnicas que permiten discriminar las componentes independientes obtenidas mediante Análisis de Componentes Independientes (ICA), con el fin de diferenciar las fuentes neuronales de los artefactos fisiológicos o eléctricos presentes en la señal EEG. En general, estas técnicas se basan en el análisis de tres tipos de información: topografía espacial, características temporales y contenido espectral de cada componente. Además de estas técnicas visuales, existen métodos automáticos de clasificación, como ADJUST, FASTER o ICLabel, que emplean medidas estadísticas y aprendizaje automático para estimar la probabilidad de que cada componente pertenezca a una categoría específica (neuronal, ocular, muscular, cardíaca o ruido).



