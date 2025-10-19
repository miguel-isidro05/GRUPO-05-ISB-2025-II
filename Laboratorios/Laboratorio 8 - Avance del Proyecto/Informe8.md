# LABORATORIO 8: Avance del Proyecto (Analisis exploratorio de datos)

## Tabla de Contenidos  
 
1. [Introducción](#1-introducción)  
2. [Planteamiento del Problema](#2-marco-teórico)  
3. [Propuesta de Solución](#3-objetivos)  
4. [Análisis Exploratorio de Datos (EDA)](#4-materiales-y-equipos)
   - [4.1. Database Competition IV 2a](#71-comparación-de-resultados-entre-señales)  
   - [4.2. Database Competition IV 2b](#72-ventajas-y-limitaciones-de-la-transformada-wavelet)  
5. [Proximos pasos y roles definidos](#5-metodología)  
6. [Material del entregable](#6-resultados)  
7. [Bibliografía](#9-bibliografía)  

---

## 1. Introducción  

El análisis de bioseñales como el electrocardiograma (ECG), el electromiograma (EMG) y el electroencefalograma (EEG) constituye uno de los pilares fundamentales en la ingeniería biomédica, tanto en la investigación como para el diagnóstico clínico. En estas representaciones graficas, las señales naturalmente suelen suelen presentar ruido y artefactos que dificultan su interpretación directa, ademas de poseer una naturaleza inherentemente no estacionaria. Con el fin de solventar dicha problemática, la Transformada Wavelet se ha consolidado en las últimas décadas como una técnica muy robusta para el procesamiento de señales, pues permite descomponerlas en diferentes escalas de tiempo y frecuencia sin perder información temporal crítica. [1]

<p align="center">
  <img src="https://github.com/user-attachments/assets/706eca35-0ff2-458e-9282-d7e6c2a19804" width="300"><br>
  <em>Figura 1. Señal EKG en reposo.</em>
</p>

Ademas a diferencia de la Transformada de Fourier, el cual ofrece un panorama global de las frecuencias sin detallar su evolución temporal, la Wavelet ajusta su resolución de forma adaptativam brindando mayor precisión temporal en altas frecuencias y mejor resolución frecuencial en componentes de baja frecuencia, la cual es una propiedad especialmente útil para la detección de fenómenos transitorios, como complejos QRS en ECG, artefactos de contracción en EMG o patrones de actividad cerebral en EEG.[2]


Por ello, un aspecto clave en la aplicación práctica es la elección de la wavelet madre, pues existen distintas familias, como Haar, Daubechies, Symlet o Coiflet, las cuales ofrecen características particulares en términos de suavidad, simetría y soporte, lo cual impacta directamente en la calidad de la descomposición y la fidelidad de la reconstrucción. En ese sentido, investigaciones recientes han demostrado que las wavelets de orden elevado, como la Daubechies 44 (db44), pueden presentan una alta similitud morfológica con múltiples biosignales, lo que las hace especialmente útiles para extraer características relevantes en contextos clínicos y experimentales.[3]

<p align="center">
  <img src="https://github.com/user-attachments/assets/b0931f49-23a8-4b70-907a-dba00c0c4964" width="450"><br>
  <em>Figura 2. Transformada Wavelet de la señal EKG.</em>
</p>

Estos hallazgos sugieren que la selección de la función base no debe limitarse a la semejanza superficial con la señal, sino que debe considerar la capacidad de capturar patrones comunes entre distintos dominios biológicos.  

En este informe se exploran los fundamentos de la Transformada Wavelet y su aplicación en señales biomédicas (ECG, EMG y EEG), comparando su desempeño. De esta manera, se busca ofrecer una visión integral sobre su potencial en el procesamiento avanzado de bioseñales y sus implicancias para la práctica clínica y la investigación interdisciplinaria.

## 2. Marco Teórico  

### 2.1 Fundamentos de la Transformada Wavelet  

