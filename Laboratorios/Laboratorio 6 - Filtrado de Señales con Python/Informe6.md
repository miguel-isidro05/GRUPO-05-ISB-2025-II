# **LABORATORIO 6: Filtrado de Señales EMG y ECG con python**

## **Tabla de contenidos**

1. [Introducción](#id1)
2. [Objetivos de la práctica](#id2)
3. [Filtrado de la señal EMG](#id7)\
4. [Filtrado de la señal ECG](#id5)\
5. [Discusión y Análisis](#id9)
6. [Referencias Bibliograficas](#id9)

## **1. Introducción** <a name="id1"></a>

Un filtro es un sistema representado como un bloque o una ecuacion en diferencias cuyo objetivo es atenuar la información no util de la señal original. 

### *Filtros Analogicos:* 
Existen filtro analógicos y digitales. Los filtro analógicos son los que se usan en el preprocesamiento de la señal, en sí, son dispositivos electrónicos diseñados para modificar señales continuas. Estos filtros utilizan componentes pasivos como resistencias, inductores y capacitores, o componentes activos como amplificadores operacionales que en conjunto logran filtrar la señal en el tiempo continuo físicamente. A pesar de que los filtros analógicos son faciles de implementar, en sistemas mas complejos donde se requiere una mayor extracción de caracteristicas su diseño se vuelve complejo. Es por ello que recurrimos a filtros digitales para el procesamiento real de la señal [1].

### *Filtros Digitales:* 
Son algoritmos matemáticos representados como ecuaciones en diferencias que operan sobre señales discretas por lo que el orden de estos filtros puede ser mucho mayor que el de los analógicos sin verse afectada tanto su complejidad. Se dividen en filtros FIR e IIR.

- *Filtros FIR (Finite Impulse Response)*: Son filtros recursivos que utilizan entradas actuales como pasadas por lo que pueden volverse inestables bajo un calculo erroneo. Son análogos a los filtros analógicos que mediante diferentes transformaciones como la bilineal pueden pasar al dominio digital. Son excelentes para aplicaciones biomédicas debido a su baja latencia lo que los vuelve muy rapidos para aplicaciones en tiempo real. Sin embargo, suelen presentar un desfase no lineal por lo que no tienen un group delay constante asi que debemos controlar eso. Pero a pesar de este problema son elegidos mas que todo debido a su bajo costo computacional a comparacion de los IIR [2].

<div align="center">
  <img width="530" height="203" alt="image" src="https://github.com/user-attachments/assets/ba117ce1-e836-4da1-a88e-9529d6d5b239" />
  <p><em>Fig. 1. Diagrama de bloques y ecuación general en diferencias de un filtro FIR</em></p>
</div>

- *Filtros IIR (Infinite Impulse Response)*: Son filtros que solo dependen de las entradas actuales por lo que siempre seran estables y suelen presentar un desfase lineal por lo que no ingresan ruido no filtrable. Sin embargo, no son tan usados debido a su alta latencia que los vuelve mas lentos debido a su alto costo computacional para lograr lo mismo que un filtro FIR [2].
  
<div align="center">
  <img width="549" height="208" alt="image" src="https://github.com/user-attachments/assets/ac4e99ff-a516-4301-8dfc-9b566f4a3bb7" />
  <p><em>Fig. 2. Diagrama de bloques y ecuación general en diferencias de un filtro IIR</em></p>
</div>

## **2. Objetivos de la práctica** <a name="id1"></a>

- Comprender los fundamentos de filtros digitales, el funcionamiento y la aplicación de filtros IIR y FIR
- Diferenciar entre las aplicaciones de los diferentes tipo de filtros digitales, las ventanas que se usan para los filtro FIR y las aproximaciones que se usan en los filtros IIR
- Analizar el efecto de los filtros sobre señales EMG y ECG para la extracción de características.

## **3. Filtrado de la señal EMG** <a name="id1"></a>

La señal electromiográfica (EMG) constituye una herramienta clave para evaluar la actividad muscular tanto en contextos clínicos como experimentales. No obstante, su registro suele verse afectado por diversas fuentes de ruido, como los artefactos de movimiento, el desplazamiento de electrodos, el drift de la línea base y la interferencia de la red eléctrica (50 Hz), lo que puede comprometer la validez de los análisis posteriores [3]. 

El análisis espectral de la EMG ha demostrado que la banda de interés se encuentra entre 10 y 500 Hz, ya que por debajo de 10 Hz predominan artefactos asociados al movimiento y variaciones lentas de la línea base, mientras que por encima de 500 Hz se registran principalmente ruidos de alta frecuencia sin valor clínico ni biomecánico [4]. Este rango asegura la preservación de la actividad eléctrica muscular más representativa, utilizada en cálculos de amplitud, frecuencia y potencia de la señal.

Los filtros de Respuesta Infinita al Impulso (IIR) son especialmente recomendados debido a su eficiencia computacional y su capacidad para generar pendientes de atenuación pronunciadas con un número reducido de coeficientes [5]. 
En particular, el filtro Butterworth IIR ha demostrado ser una alternativa robusta, ya que presenta una respuesta en frecuencia suavemente decreciente, es estable en cascadas de primer orden y es eficaz para eliminar tanto los artefactos de baja frecuencia (<10 Hz) como la interferencia de la red eléctrica, preservando al mismo tiempo los componentes musculares útiles. 

## **4. Filtrado de la señal ECG** <a name="id1"></a>

El electrocardiograma (ECG) es la técnica más utilizada para evaluar la actividad eléctrica del corazón. Sin embargo, el registro de la señal suele verse afectado por artefactos como el drift de línea base (producido por movimientos respiratorios o desplazamiento de electrodos), la interferencia de la red eléctrica (50/60 Hz) y el ruido muscular (EMG) que ocupa frecuencias más altas [6].

Diversos estudios han establecido que la señal útil del ECG se concentra en un rango de 0.5 a 40 Hz. El límite inferior (≈0.5 Hz) se emplea para eliminar el drift de baja frecuencia, asegurando que ondas lentas debidas a artefactos no distorsionen el complejo P-QRS-T. Por su parte, el límite superior (≈40 Hz) permite reducir el ruido muscular y de alta frecuencia, que puede enmascarar detalles relevantes del QRS y otras componentes de interés diagnóstico [6].

De esta forma, filtrar la señal en el rango de 0.5–40 Hz asegura la preservación de la información fisiológica esencial del ECG (ondas P, QRS y T), a la vez que minimiza la influencia de interferencias externas y ruidos que afectan la interpretación clínica.

## **5. Filtrado de la señal EEG** <a name="id1"></a>

El electroencefalograma (EEG) es una técnica esencial para el estudio de la actividad eléctrica cerebral, ampliamente utilizada en investigación y aplicaciones clínicas. Sin embargo, la señal bruta suele estar contaminada por artefactos de movimiento, parpadeo ocular, ruido muscular (EMG) y la interferencia de la red eléctrica (50/60 Hz), lo que dificulta su análisis directo [7].

Diversos estudios han establecido que la información útil del EEG se encuentra en el rango de 0.5 a 100 Hz. El límite inferior de 0.5 Hz se emplea para eliminar el drift de baja frecuencia producido por movimientos respiratorios, desplazamientos de electrodos o sudoración, que no forman parte de la actividad cerebral. Por otro lado, el límite superior de 100 Hz se selecciona porque la mayoría de las oscilaciones corticales relevantes (delta, theta, alpha, beta y gamma) se encuentran por debajo de este umbral. Las frecuencias mayores a 100 Hz suelen asociarse con ruido de alta frecuencia o artefactos musculares, los cuales no aportan información relevante para el análisis neurofisiológico convencional [7].

Dentro de esta banda, se distinguen los principales ritmos cerebrales: delta (0.5–4 Hz), theta (4–8 Hz), alpha (8–12 Hz), beta (12–40 Hz) y gamma (40–80 Hz). Cada uno refleja distintos estados funcionales del cerebro, desde el sueño profundo hasta la atención y el procesamiento cognitivo. Por tanto, limitar la señal al rango de 0.5–100 Hz garantiza la preservación de las oscilaciones neuronales de interés, a la vez que se reducen artefactos y ruidos externos, facilitando el análisis clínico y computacional [7].

## **6. Discusión y Análisis** <a name="id1"></a>
## 6.1 ECG
Las frecuencias de interés se encuentran entre 0.5Hz y 40Hz, por lo que se optó por diseñar un filtro Pasa Banda en pyFDA. Se ajustaron los parámetros de las frecuencias de corte para obtener un filtro que nos permita obtener las frecuencias de interés de las señales EMG
### 6.1.a Reposo
*Filtros FIR*: Para observarfernvev enventanamiento
| Señal                                   | Hamming | Hann |Blackman |
|--------------------|----------|-------------|-----|
| Reposo |<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/5e202eae-9cee-4714-aaea-0f2f2b3b8a0f" />|<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/9e70ae25-7728-493b-bab6-34da22e7584f" />|<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/c531f5e5-45d1-4843-9bea-b6df0038cca7" />|
Comparamos las respuestas en frecuencia de los filtros FIR 
<img width="989" height="490" alt="image" src="https://github.com/user-attachments/assets/bb358571-90c8-434e-be58-b7cd77e8d0aa" />

*Filtros IIR*: Se diseñaron los filtros Butterworth y Chevishev tipo 1 de tipo Pasa Bajas; esto debido a que al ser jcdcjsjvjf no eprmite sjdcbebv por lo que se comportaba muy inestable en las regiones de transición a pesar de modificar el orden del filtro, por lo que se optó diseñar un Pasa Bajas que se mostraba más estable y permitía un correcto filtrado y obtención de la banda de frecuencia de inetrés
*************iamgen de pyfda

Se observa la señal de reposo tras aplicarles ambos filtros:
************
<img width="989" height="490" alt="image" src="https://github.com/user-attachments/assets/9573450d-140c-49ee-b15d-0045c064b586" />

Comparamos las respuestas en frecuencia de los filtros IIR 
<img width="630" height="470" alt="image" src="https://github.com/user-attachments/assets/8e6a31e7-fcf4-4786-8991-49ab2bf95a5f" />


### 6.1.b Apnea 10 segundos

### 6.1.c Actividad Aeróbica

## 6.2 EEG
### 6.2.a Estado basal

### 6.2.b Mirada Fija
### 6.2.c Preguntas

## 6.3 EMG
En este caso, se tomaron las señales de los bíceps en 3 estados:
### 6.3.a Bicep relajado

### 6.3.b Movimiento Leve

### 6.3.c Aplicando fuerza 


## **7. Referencias bibliográficas** <a name="id1"></a>

[1] ScienceDirect. Analog filter [Internet]. Amsterdam: Elsevier. Disponible en: https://www.sciencedirect.com/topics/engineering/analog-filter

[2] Advanced Solutions Nederland. Difference between IIR and FIR filters: a practical design guide [Internet]. Disponible en: https://www.advsolned.com/difference-between-iir-and-fir-filters-a-practical-design-guide/

[3] V. R. Zschorlich, "Digital filtering of EMG-signals," Electromyogr. Clin. Neurophysiol., vol. 29, pp. 81–86.

[4] E. Kwatny, D. H. Thomas, and H. G. Kwatny, "An application of signal processing techniques to the study of myoelectric signals," IEEE Transactions on Biomedical Engineering, vol. 17, no. 4, pp. 303–313.

[5] A. Thys et al., "Stabilization of the isoelectric line of surface EMG by means of high pass filters," Electromyogr. Clin. Neurophysiol., vol. 17, pp. 393–400.

[6] C. Saxena, A. Sharma, R. Srivastav, and H. K. Gupta, "Denoising of ECG signals using FIR & IIR filter: a performance analysis," International Journal of Engineering & Technology, vol. 7, no. 4.12, pp. 1–5, 2018.

[7] A. Pant and A. Kumar, "Hanning FIR window filtering analysis for EEG signals," Biomedical Analysis, vol. 1, pp. 111–123, 2024, doi: 10.1016/j.bioana.2024.05.003.

