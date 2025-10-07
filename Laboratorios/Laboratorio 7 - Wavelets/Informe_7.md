# LABORATORIO 7: Aplicación de la Transformada Wavelet en Señales Biomédicas

## Tabla de Contenidos  
 
1. [Introducción](#1-introducción)  
2. [Marco Teórico](#2-marco-teórico)  
   - [2.1 Fundamentos de la Transformada Wavelet](#21-fundamentos-de-la-transformada-wavelet)  
   - [2.2 Aplicaciones en Señales Biomédicas](#22-aplicaciones-en-señales-biomédicas)  
3. [Objetivos](#3-objetivos)  
   - [3.1 Objetivo General](#31-objetivo-general)  
   - [3.2 Objetivos Específicos](#32-objetivos-específicos)  
4. [Materiales y Equipos](#4-materiales-y-equipos)  
5. [Metodología](#5-metodología)  
6. [Resultados](#6-resultados)  
   - [6.1 Señal ECG](#61-señal-signal)  
     - [6.1.1 Reposo basal](#611-reposo-basal)  
     - [6.1.2 Apnea 10 segundos](#612-apnea-10-segundos)  
     - [6.1.3 Posterior a actividad aeróbica](#613-posterior-a-actividad-aeróbica)  
   - [6.2 Señal EMG](#62-señal-emg)  
     - [6.2.1 Músculo relajado](#621-músculo-relajado)  
     - [6.2.2 Movimiento leve](#622-movimiento-leve)  
     - [6.2.3 Aplicando fuerza](#623-aplicando-fuerza)  
   - [6.3 Señal EEG](#63-señal-eeg)  
     - [6.3.1 Estado basal](#631-estado-basal)  
     - [6.3.2 Mirada fija](#632-mirada-fija)  
     - [6.3.3 Preguntas](#633-preguntas)  
7. [Discusión](#7-discusión)  
   - [7.1 Comparación de Resultados entre Señales](#71-comparación-de-resultados-entre-señales)  
   - [7.2 Ventajas y Limitaciones de la Transformada Wavelet](#72-ventajas-y-limitaciones-de-la-transformada-wavelet)  
8. [Conclusiones](#8-conclusiones)  
9. [Bibliografía](#9-bibliografía)  

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
La **Transformada Wavelet (WT)** es una herramienta matemática que permite analizar señales tanto en el **dominio del tiempo como en el de la frecuencia**, superando las limitaciones de la Transformada de Fourier tradicional.  
A diferencia del análisis espectral clásico, la WT utiliza funciones denominadas **wavelets**, las cuales son de corta duración y localizadas, permitiendo detectar **cambios transitorios o eventos no estacionarios** en una señal. 

Matemáticamente, la **Transformada Wavelet Continua (CWT)** de una señal \( x(t) \) se define como:  

$$
W(a,b) = \frac{1}{\sqrt{|a|}} \int_{-\infty}^{\infty} x(t)\,\psi^*\left( \frac{t-b}{a} \right)\,dt
$$
 
donde:  
- $a$ es el **parámetro de escala** (controla la frecuencia),  
- $b$ es el **parámetro de traslación** (controla la posición temporal),  
- $\psi(t)$ es la **wavelet madre**, y  
- $\psi^*(t)$ representa su **conjugado complejo**.  


En la práctica, también se emplea la **Transformada Wavelet Discreta (DWT)**, que descompone la señal en distintos niveles mediante **filtros pasa bajos y pasa altos**, permitiendo representar los componentes de baja y alta frecuencia en cada escala.  
Esta propiedad es útil para la **eliminación de ruido**, **detección de eventos** y **compresión de datos**.  


### 2.2 Aplicaciones en Señales Biomédicas  

## 3. Objetivos  

### 3.1 Objetivo General  

Aplicar la Transformada Wavelet en el procesamiento de bioseñales (ECG, EMG y EEG) y evaluar su utilidad en comparación con métodos de filtrado convencionales, destacando sus implicancias en el análisis de señales no estacionarias y su posible implementación en el analisis de sistemas BCI basados en motor imagery.

### 3.2 Objetivos Específicos  

- Seleccionar y justificar la familia de wavelet madre más adecuada para cada tipo de bioseñal (ECG, EMG, EEG), con respaldo en literatura científica.  

- Definir parámetros de filtrado (nivel de descomposición, tipo de umbral, método de reconstrucción) y aplicarlos a las señales biomédicas registradas.  

- Implementar el proceso de descomposición, filtrado y reconstrucción, evaluando la efectividad de cada wavelet madre en la preservación de la morfología de la señal.  

- Comparar el desempeño de diferentes wavelets y niveles de descomposición mediante métricas (Correlación, similitud morfológica), identificando ventajas y limitaciones.  

## 4. Materiales y Equipos <a name="4-materiales-y-equipos"></a>  

<div align="center">

| **Modelo / Material** | **Descripción** | **Cantidad** | **Imagen** |
|:---------------------:|:---------------:|:------------:|:----------:|
| Kit (R)EVOLUTION BITalino | Sistema de adquisición de bioseñales con capacidad para ECG, EMG y EEG | 1 | <img width="120" src="https://github.com/user-attachments/assets/a60c127f-27c2-4a03-b852-454d23f54163"> |
| Electrodos de superficie descartables | Electrodos con gel para registro de señales biomédicas | 3 | <img width="120" src="https://github.com/user-attachments/assets/2e58ad27-7c4a-4336-9fdf-fe54129be397"> |
| Cable conector para 3 electrodos | Interfaz entre electrodos y el Kit BITalino | 1 | <img width="120" src="https://github.com/user-attachments/assets/2d397e32-3ec4-4982-91fe-0d6855e3aec0"> |
| Batería recargable 3.7V | Fuente de alimentación para el sistema BITalino | 1 | <img width="120" src="https://github.com/user-attachments/assets/25fe9643-a7fa-4bd9-85ad-e1ce78a926ab"> |
| Software OpenSignals | Herramienta para adquisición y visualización de señales biomédicas | 1 | <img width="120" src="https://github.com/user-attachments/assets/270de790-173f-42fc-9960-5b12a7fff042"> |
| Laptop o PC | Laptop equipada con Python y librerías para implementar códigos de procesamiento y filtrado | 1 | <img width="120" src="https://seovalladolid.es/wp-content/webp-express/webp-images/uploads/2021/02/python.png.webp"> |

</div>

## 5. Metodología

| **Etapa**                | **Descripción**                                                                                                   | **Ejemplo** |
|---------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------------|
| Tipo de wavelet  | Elegir la familia de wavelet madre considerando similitud morfológica, suavidad, simetría y uso reportado en la literatura. | `db4`, `db44`, `sym5`            |
| Definición de parámetros | Determinar nivel de descomposición, tipo de umbral (hard/soft), método de reconstrucción. | Nivel 5, soft-threshold, `pywt.waverec()` |
| Filtrado de coeficientes | Reducir componentes asociados al ruido sin perder información relevante de la señal. | Soft-threshold en `db4` elimina ruido de alta frecuencia. |
| Reconstrucción       | Reconstituir la señal filtrada a partir de los coeficientes procesados, preservando la morfología clínica relevante. | `pywt.waverec()` reconstruye la señal. |
| Verificación y discusión | Comparar señal original vs. filtrada; analizar eliminación de ruido y preservación de características. | Gráficas comparativas y métricas de calidad. |

## 6. Resultados  

### 6.1 Señal ECG

**Justificación de la elección de wavelet:**  
Se utilizó la familia Daubechies (`db6`), adecuada para señales ECG debido a su similitud morfológica con los complejos QRS y su buena capacidad para separar ruido de alta frecuencia sin distorsionar la forma de la señal fisiologica [a].

/inclusir referencia

#### 6.1.1 Reposo basal

**Descomposición y coeficientes de detalle:**  
Se realizó la descomposición en 5 niveles acorde al umbral, obteniendo los coeficientes de detalle para cada nivel:

```python
Umbral Universal calculado: 5.1393
```

<img width="1189" height="989" alt="image" src="https://github.com/user-attachments/assets/be363501-006e-44e1-aff2-2844841396f5" />


**Filtrado y selección de nivel óptimo:**  

| Señal           | Original | Filtrada nivel optimo |
|--------------------|----------|-------------|
|Reposo basal|<img width="1028" height="391" alt="image" src="https://github.com/user-attachments/assets/287dd1f0-dbf6-42b5-87e7-53061f4947fb" />|<img width="1028" height="391" alt="image" src="https://github.com/user-attachments/assets/d3d15c56-aee9-4e4e-b8b9-34686acb0731" />|



#### 6.1.2 Apnea 10 segundos

**Descomposición y coeficientes de detalle:**  
Se realizó la descomposición en 5 niveles acorde al umbral, obteniendo los coeficientes de detalle para cada nivel:

```python
Umbral Universal calculado: 5.3815
```

//colocar imagen de coeficientes por niveles

**Filtrado y selección de nivel óptimo:**  

| Señal           | Original | Filtrada nivel optimo |
|--------------------|----------|-------------|
|Apnea 10 segundos| | |

#### 6.1.3 Posterior a actividad aerobica

**Descomposición y coeficientes de detalle:**  
Se realizó la descomposición en 5 niveles acorde al umbral, obteniendo los coeficientes de detalle para cada nivel:

```python
Umbral Universal calculado: 5.1238
```

//colocar imagen de coeficientes por niveles

**Filtrado y selección de nivel óptimo:**  

| Señal           | Original | Filtrada nivel optimo |
|--------------------|----------|-------------|
|Posterior a actividad aerobica| | |

### 6.2 Señal EMG  

#### 6.2.1 Musculo relajado

#### 6.2.2 Movimiento leve

#### 6.2.3 Aplicando fuerza

### 6.3 Señal EEG  

#### 6.3.1 Estado basal

#### 6.3.2 Mirada fija

#### 6.3.3 Preguntas

## 7. Discusión  

### 7.1 Comparación de Resultados entre Señales  

### 7.2 Ventajas y Limitaciones de la Transformada Wavelet  

## 8. Conclusiones  

## 9. Bibliografía  
[1] https://www.sciencedirect.com/science/article/abs/pii/S0957417410012881
[2] https://books.google.com.pe/books?hl=es&lr=&id=SuIlBQAAQBAJ&oi=fnd&pg=PR13&dq=wavelets+basics&ots=xRC1nChqym&sig=RuK8E3d9M3jrKAU-2qtVRHpSjeo#v=onepage&q=wavelets%20basics&f=false
[3]https://doi.org/10.1016/j.procs.2018.05.054
