# **Laboratorio 9: Tratamiento de señal EEG adquirida del ULTRACORTEX MARK IV con ICA**

## 1. Visualización con MNE

Para una primera visualización, se generó un gráfico de densidad espectral de potencia (PSD) del EEG sin aplicar ningún filtrado. En este gráfico se mostraria la distribución de la energía de la señal a lo largo de las distintas frecuencias (de 0 a 125 Hz), permitiendo observar en qué bandas se concentra la mayor parte de la potencia del registro original, para luego mostrar como cambia con el filtrado.

<img width="1011" height="361" alt="image" src="https://github.com/user-attachments/assets/8602bb05-c21a-4811-a0fb-ab87b80d9207" />

Luego, se aplicó un filtro pasa banda de 0 a 30 Hz y se volvió a graficar el PSD con los mismos parámetros, del cual se puede observar una reducción notable de la potencia en las frecuencias altas, eliminando ruido y preservando las bandas cerebrales más relevantes (delta, theta, alfa y beta).

<img width="1011" height="361" alt="image" src="https://github.com/user-attachments/assets/3f4eff05-1b9d-4873-ac58-7d7a95a41ec0" />


### Plot para visualización temporal del recording de EEG
Para la visualización y análisis de las señales EEG se utilizó la biblioteca MNE-Python, la cual permite representar las señales en el dominio temporal y frecuencial.

Se cargan los datos crudos de EEG registrados con OpenBCI y se seleccionan únicamente los canales correspondientes a la actividad cerebral. Los datos se organizan de manera que cada canal representara una serie temporal de voltajes, y también la frecuencia de muestreo para que las señales puedan analizarse correctamente en el dominio temporal y espectral. Así se puede visualizar las señales EEG, mostrando cómo varía la actividad eléctrica en cada canal a lo largo del tiempo y facilitando la identificación de patrones o artefactos.
<img width="1439" height="975" alt="image" src="https://github.com/user-attachments/assets/aa3ecb37-a831-48e3-9012-21900d4d3d8c" />


### Plot para comparar la actividad eléctrica cerebral registrada en distintos momentos de tu señal EEG.

Aqui se puede visualizar cómo varía la actividad cerebral en ese intervalo mediante tres tipos de gráficos: las señales promedio por canal, los mapas topográficos del potencial en distintos momentos y un gráfico conjunto que muestra simultáneamente la evolución temporal y espacial de la señal.

<img width="651" height="311" alt="image" src="https://github.com/user-attachments/assets/89e7b842-2db2-4688-93b3-072795863937" />
<img width="810" height="431" alt="image" src="https://github.com/user-attachments/assets/80ce43ff-f547-4524-8c9a-65707caffc24" />

Asimismo, se guardan segmentos en un diccionario y se visualizan como se organiza los canales en su posición real sobre el cuero cabelludo,  mostrando cómo difiere la distribución espacial y temporal de la actividad entre los dos intervalos.

<img width="1586" height="1375" alt="image" src="https://github.com/user-attachments/assets/7bb46117-73d1-46b9-9411-1a38301f1de4" />

## 2. Procesamiento con ICA
El Análisis de Componentes Independientes (ICA) es un algoritmo de extracción de características que identifica componentes estadísticamente independientes en un conjunto de datos, reduciendo las dependencias de segundo y tercer orden. En el caso de la señal EEG, el ICA permite identificar y eliminar artefactos sin perder las señales neuronales relevantes.
En el presente análisis se empleó la técnica de Análisis de Componentes Independientes (ICA) con el objetivo de separar las fuentes neuronales de los artefactos fisiológicos y eléctricos presentes en la señal EEG. La señal fue adquirida por medio de 8 canales a una frecuencia de muestreo de 250 Hz. En este caso, se extrajeron 7 componentes independientes. Esto se debe a que cada canal representa una mezcla de las mismas fuentes, y el modelo ICA clásico asume que el número de fuentes no puede ser mayor que el número de sensores.Esta elección sigue las recomendaciones de la literatura, donde se establece que el número de componentes extraídos debe ser igual al número de canales después del preprocesamiento (Dharmaprani et al., 2016).
Existen diversas técnicas que permiten discriminar las componentes independientes obtenidas mediante Análisis de Componentes Independientes (ICA), con el fin de diferenciar las fuentes neuronales de los artefactos fisiológicos o eléctricos presentes en la señal EEG. En general, estas técnicas se basan en el análisis de tres tipos de información: topografía espacial, características temporales y contenido espectral de cada componente. Además de estas técnicas visuales, existen métodos automáticos de clasificación, como ADJUST, FASTER o ICLabel, que emplean medidas estadísticas y aprendizaje automático para estimar la probabilidad de que cada componente pertenezca a una categoría específica (neuronal, ocular, muscular, cardíaca o ruido).


# Ploteo general del ICA
<img width="770" height="793" alt="image" src="https://github.com/user-attachments/assets/6a941e5d-c244-47d2-b696-92abf884433a" />



<img width="681" height="589" alt="image" src="https://github.com/user-attachments/assets/a83e8f2a-7439-4571-bf48-24a2d59b482a" />
<img width="681" height="589" alt="image" src="https://github.com/user-attachments/assets/1c0e8349-2918-4fb7-8828-12f7742c13de" />
<img width="681" height="589" alt="image" src="https://github.com/user-attachments/assets/caca9f16-3166-45a4-af1f-2c2ae9d5fb39" />
<img width="681" height="589" alt="image" src="https://github.com/user-attachments/assets/3e8e6f63-d24c-433c-ae81-2df2e81cab73" />
<img width="681" height="589" alt="image" src="https://github.com/user-attachments/assets/6477bdc5-a7a5-4d8c-ba1a-a90537d9b14d" />
<img width="681" height="589" alt="image" src="https://github.com/user-attachments/assets/10e42ab6-179a-43ca-bf79-edcdc86bafd0" />
<img width="681" height="589" alt="image" src="https://github.com/user-attachments/assets/bab72eef-d2c5-4dd1-a4ee-0404cd5ad2e6" />









