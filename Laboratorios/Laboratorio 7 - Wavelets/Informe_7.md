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
A diferencia del análisis espectral clásico, la WT utiliza funciones denominadas **wavelets**, las cuales son de corta duración y localizadas, permitiendo detectar **cambios transitorios o eventos no estacionarios** en una señal. [4]

Matemáticamente, la **Transformada Wavelet Continua (CWT)** de una señal \( x(t) \) se define como: [5]

$$
W(a,b) = \frac{1}{\sqrt{|a|}} \int_{-\infty}^{\infty} x(t)\,\psi^*\left( \frac{t-b}{a} \right)\,dt
$$
 
donde:  
- $a$ es el **parámetro de escala** (controla la frecuencia),  
- $b$ es el **parámetro de traslación** (controla la posición temporal),  
- $\psi(t)$ es la **wavelet madre**, y  
- $\psi^*(t)$ representa su **conjugado complejo**.  


En la práctica, también se emplea la **Transformada Wavelet Discreta (DWT)**, que descompone la señal en distintos niveles mediante **filtros pasa bajos y pasa altos**, permitiendo representar los componentes de baja y alta frecuencia en cada escala.  
Esta propiedad es útil para la **eliminación de ruido**, **detección de eventos** y **compresión de datos**. [6]


### 2.2 Aplicaciones en Señales Biomédicas  
En el campo biomédico, las señales fisiológicas suelen ser **no estacionarias** y de naturaleza compleja, por lo que la Transformada Wavelet se ha convertido en una herramienta esencial para su análisis. [7]

Algunas aplicaciones destacadas incluyen:  

- **Electrocardiograma (ECG):** la WT se utiliza para **detectar picos R**, **eliminar artefactos de ruido muscular y de línea base**, y **segmentar los intervalos P-QRS-T**.  
  Las wavelets tipo *Daubechies (db4)* y *Symlet* son especialmente útiles por su similitud con la morfología del complejo QRS.  

- **Electroencefalograma (EEG):** permite analizar la actividad cerebral en diferentes **bandas de frecuencia** (delta, theta, alfa, beta, gamma), facilitando la detección de **epilepsia**, **trastornos del sueño** y **respuestas cognitivas** mediante descomposición multirresolución.  

- **Electromiograma (EMG):** la DWT ayuda a **extraer características** del patrón muscular y **eliminar interferencias de alta frecuencia**, mejorando el reconocimiento de movimientos o la evaluación de neuropatías.  

En conjunto, la Transformada Wavelet ofrece una visión **multiescala** del comportamiento fisiológico, posibilitando un procesamiento más preciso y eficiente que las técnicas clásicas basadas únicamente en el dominio del tiempo o de la frecuencia.[8]

---
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
La **familia de wavelets Daubechies (dbN)**, propuesta por Ingrid Daubechies, es una de las más utilizadas en el análisis de señales ECG debido a las siguientes razones:  

- **Similitud morfológica con el complejo QRS:**  
  Las funciones wavelet *Daubechies* poseen una forma asimétrica y una respuesta impulsiva corta, muy parecida a la morfología del complejo QRS del ECG. Esto permite que las descomposiciones capten con precisión los picos R y las variaciones rápidas.[9]

- **Buena localización en tiempo y frecuencia:**  
  Las wavelets *Daubechies* ofrecen un equilibrio óptimo entre resolución temporal y espectral, lo que permite detectar eventos transitorios (picos o artefactos) sin perder información de fondo.[10]

- **Ortogonalidad y eficiencia computacional:**  
  Al ser ortogonales, las *dbN* permiten reconstruir la señal sin redundancia y con bajo costo computacional, cualidad esencial para aplicaciones en tiempo real o sistemas embebidos.  [11]

- **Desempeño probado en filtrado y detección de picos:**  
  Estudios clásicos demuestran que wavelets como *db4* o *db6* logran eliminar el ruido de línea base y resaltar el complejo QRS con alta precisión, lo cual las convierte en un estándar en el análisis ECG. [12]

En consecuencia, en este laboratorio se selecciona la **wavelet madre Daubechies de orden 4 (db4)** por su comprobada eficacia en la detección de picos R y su capacidad para mantener la morfología característica de la señal cardiaca. 


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

<img width="1189" height="989" alt="image" src="https://github.com/user-attachments/assets/7ea8c42c-0025-47e1-b7c8-da6a1e90bea2" />


**Filtrado y selección de nivel óptimo:**  

| Señal           | Original | Filtrada nivel optimo |
|--------------------|----------|-------------|
|Apnea 10 segundos|<img width="1028" height="391" alt="image" src="https://github.com/user-attachments/assets/dff445e4-0c70-4536-b9c3-8ffe55912343" />|<img width="1028" height="391" alt="image" src="https://github.com/user-attachments/assets/629dcab2-4ab6-4ae5-be2c-802c541fdf0e" />|

#### 6.1.3 Posterior a actividad aerobica

**Descomposición y coeficientes de detalle:**  
Se realizó la descomposición en 5 niveles acorde al umbral, obteniendo los coeficientes de detalle para cada nivel:

```python
Umbral Universal calculado: 5.1238
```

<img width="1187" height="989" alt="image" src="https://github.com/user-attachments/assets/b2685130-0ecb-49e4-b704-edc0c159483d" />

**Filtrado y selección de nivel óptimo:**  

| Señal           | Original | Filtrada nivel optimo |
|--------------------|----------|-------------|
|Posterior a actividad aerobica|<img width="1028" height="391" alt="image" src="https://github.com/user-attachments/assets/6fd95d82-f738-407e-9ad3-05ea64983dd6" />|<img width="1028" height="391" alt="image" src="https://github.com/user-attachments/assets/f2371720-9a18-42b2-b817-8d05f42fca44" />|

### 6.2 Señal EMG  
## 6.2 Señal EMG y elección de la familia Wavelet

La señal de **electromiograma (EMG / sEMG)** es inherentemente *no estacionaria*, con variaciones rápidas en amplitud y frecuencia debidas a contracciones musculares, artefactos y ruido. La Transformada Wavelet Discreta (DWT) permite una descomposición multiescala que separa componentes de detalle (alta frecuencia) y aproximación (baja frecuencia), lo cual es ideal para filtrado, extracción de características y clasificación.

### Uso predominante de la familia Daubechies en EMG

La literatura reciente muestra un consenso notable: la familia **Daubechies (dbN)** es frecuentemente utilizada en el análisis de señales EMG por su efectividad y propiedades favorables. Algunos ejemplos relevantes:

- En el artículo *“Surface electromyography (sEMG) feature extraction based on Daubechies wavelets”*, los autores investigan distintos niveles de reconstrucción usando wavelets Daubechies, y señalan que **db7** (Daubechies de orden 7) con detalles de nivel 1 y 2 brindó los mejores resultados para extracción de características (MAV) y separabilidad de clases. :contentReference[oaicite:1]{index=1}  
- En *Wavelet Transform-Based Classification of Electromyogram Signals Using an ANOVA Technique*, se comparó la capacidad denoising de distintas wavelets sobre sEMG relacionados con movimientos del brazo, y se halló que **db4** produjo el mejor desempeño para remover ruido y lograr alta precisión en clasificación (≈ 88.90 %) entre movimientos del miembro superior. :contentReference[oaicite:2]{index=2}  
- En estudios comparativos de extracción de características, Phinyomark et al. muestran que muchas investigaciones sobre EMG han concluido que la familia Daubechies es una opción estándar para análisis multiescala de sEMG, debido a su balance entre resolución temporal y frecuencia. :contentReference[oaicite:3]{index=3}  

###  Justificación técnica del uso de Daubechies

Las razones técnicas que explican por qué Daubechies es tan usada en EMG son:

1. **Ortogonalidad y reconstrucción sin redundancia**  
   Las wavelets Daubechies son ortogonales, lo que permite reconstruir la señal original sin pérdida de información entre sub-bandas.

2. **Capacidad de anular polinomios bajos (vanishing moments)**  
   Las Daubechies tienen un número de *vanishing moments*, que les permite suprimir tendencias suaves (componentes de baja frecuencia) y centrarse en cambios transitorios de alta frecuencia, comunes en la señal EMG.

3. **Buena localización en tiempo y frecuencia**  
   Dado que el EMG contiene eventos rápidos (ráfagas musculares), es importante que la wavelet esté bien localizada en el tiempo para capturar estos eventos sin “difuminar” en escalas grandes.

4. **Forma adecuada para señales asimétricas**  
   La morfología del EMG no es perfectamente simétrica; las Daubechies suelen ser wavelets asimétricas que se adaptan mejor a esa característica.

5. **Historial probado en trabajos aplicados**  
   Como muestran los artículos mencionados, muchas aplicaciones de análisis de EMG ya usan db4, db7, etc., y reportan buenos resultados en denoising y extracción de características útiles.

Por estas razones —combinar buen desempeño empírico con propiedades matemáticas convenientes— se considera **razonable elegir una wavelet Daubechies  db4** para el análisis de señales EMG en tu laboratorio.

#### 6.2.1 Musculo relajado
**Descomposición y coeficientes de detalle:**  
Se realizó la descomposición en 4 niveles acorde al umbral, obteniendo los coeficientes de detalle para cada nivel:

```python
Umbral Universal calculado: 4.9120
```
<img width="1189" height="989" alt="image" src="https://github.com/user-attachments/assets/46682a1e-baa9-4b7c-883e-ad6cb85a8217" />

**Filtrado y selección de nivel óptimo:**  

| Señal           | Original | Filtrada nivel optimo |
|--------------------|----------|-------------|
|Reposo basal|<img width="1041" height="391" alt="image" src="https://github.com/user-attachments/assets/ebe6d4a3-9d5d-4b39-a318-bf86c93bee37" />|<img width="1028" height="391" alt="image" src="https://github.com/user-attachments/assets/8e2d8dd4-0648-4ab5-8a55-80ef9b9f509b" />|
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

[4] S. Mallat, *A Wavelet Tour of Signal Processing: The Sparse Way*, 3rd ed. Burlington, MA: Academic Press, 2008.  

[5] P. S. Addison, *The Illustrated Wavelet Transform Handbook*, 2nd ed. Boca Raton, FL: CRC Press, 2017.  

[6] M. Akay, Ed., *Time–Frequency and Wavelets in Biomedical Signal Processing*. Piscataway, NJ: IEEE Press, 1998.  

[7] A. Subasi, “EEG signal classification using wavelet feature extraction and a mixture of expert model,” *Expert Systems with Applications*, vol. 32, no. 4, pp. 1084–1093, 2007.  

[8] C. Li, C. Zheng, and C. Tai, “Detection of ECG characteristic points using wavelet transforms,” *IEEE Transactions on Biomedical Engineering*, vol. 42, no. 1, pp. 21–28, 1995.  

[9] I. Daubechies, *Ten Lectures on Wavelets*. Philadelphia, PA: SIAM, 1992. 

[10] S. Ghosh-Dastidar and H. Adeli, “Improved spiking neural networks for EEG classification and epilepsy and seizure detection,” *Integrated Computer-Aided Engineering*, vol. 14, no. 3, pp. 187–212

[11]C. Li, C. Zheng, and C. Tai, “Detection of ECG characteristic points using wavelet transforms,” *IEEE Transactions on Biomedical Engineering*, vol. 42, no. 1, pp. 21–28

[12] P. S. Addison, *The Illustrated Wavelet Transform Handbook*, 2nd ed. Boca Raton, FL: CRC Press, 2017.  
