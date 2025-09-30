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
Para cada toma de cada señal (ECG, EEG) se diseñaron tres filtros FIR Pasa Banda utilizando las ventanas Hamming, Hann y Blackman para comparar cómo las diferentes formas de ventana afectan la respuesta temporal y la atenuación del ruido en la señal ECG. Se usaron estas ventanas porque son clásicas en procesamiento de señales y permiten diseñar filtros FIR estables, con respuesta en frecuencia controlada, además de ser adecuadas para señales EEG y ECG.
También se diseñaron filtros IIR de tipo Butterworth Y Chevyshev tipo 1 para las señales ECG y EEG; y adicionalmente se realizó un filtro Bessel para las señales EMG. Se diseñaron para evidenciar que con un número menor de orden se pueden obtener filtros igual de efectivos que los FIR a pesar de presentar un desfase no lineal.

## 6.1 ECG
Las frecuencias de interés se encuentran entre 0.5Hz y 40Hz, por lo que se optó por diseñar un filtro Pasa Banda en pyFDA. Se ajustaron los parámetros de las frecuencias de corte para obtener un filtro que nos permita obtener las frecuencias de interés de las señales ECG.
### 6.1.a Reposo
*Filtros FIR*: Al filtrar la señal con las diferentes ventanas se puede observar que se preservan los picos R y que se presenta un desfase constante respecto a la señal cruda, lo cual es una característica bastante común de los filtros FIR. Para el diseño de cada uno de los filtros se necesitó un número de orden mayor a 100. Por ejemplo para Hamming se necesitaron 200 coeficientes (N=200), para Hann 118 y para Blackman 120. Un mayor número de coeficientes permite que la transición entre la banda de paso y la banda de rechazo sea más pronunciada, reduciendo ruido. La ventaja de usar pyFDA para el diseño es que se podía observar si se estaba usando un número de orden ideal y modular la selectividad aumentando o disminuyendo el número de orden.

| Señal           | Hamming | Hann |Blackman |
|--------------------|----------|-------------|-----|
|filtro en pyFDA| <img width="1447" height="740" alt="image" src="https://github.com/user-attachments/assets/a798648c-dbe8-4e0f-b6e8-ca1140d3aae6" />|<img width="1437" height="821" alt="image" src="https://github.com/user-attachments/assets/6f26d3fd-3fa7-4617-b6c2-43427910e2bf" />|<img width="1438" height="847" alt="image" src="https://github.com/user-attachments/assets/785c1216-d817-4eb5-944e-025efe24953d" />|
| Reposo |<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/5e202eae-9cee-4714-aaea-0f2f2b3b8a0f" />|<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/9e70ae25-7728-493b-bab6-34da22e7584f" />|<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/c531f5e5-45d1-4843-9bea-b6df0038cca7" />|


*Filtros IIR*: Se diseñaron los filtros Butterworth y Chebyshev tipo 1 de tipo Pasa Bajas, ya que en Pasa Banda se presentaba inestabilidad en las regiones de transición incluso al modificar el orden del filtro. La opción de un filtro Pasa Bajas permitió un comportamiento más estable y un filtrado correcto, asegurando la adecuada obtención de la banda de frecuencia de interés en la señal.
Se observa la señal de reposo tras aplicarles ambos filtros:
************
<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/9573450d-140c-49ee-b15d-0045c064b586" />



### 6.1.b Apnea 10 segundos
| Señal                                   | Hamming | Hann |Blackman |
|--------------------|----------|-------------|-----|
|filtro en pyFDA| <img width="1447" height="740" alt="image" src="https://github.com/user-attachments/assets/a798648c-dbe8-4e0f-b6e8-ca1140d3aae6" />|<img width="1437" height="821" alt="image" src="https://github.com/user-attachments/assets/6f26d3fd-3fa7-4617-b6c2-43427910e2bf" />|<img width="1438" height="847" alt="image" src="https://github.com/user-attachments/assets/785c1216-d817-4eb5-944e-025efe24953d" />|
|Apnea|<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/ef939ec9-6090-4513-bf67-9c3317326adc" />|<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/87c430d7-f88a-4d37-8091-ada1234d2ee7" />|<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/bfa6f89f-1072-4d8e-8868-956596a0040c" />|
 

*Filtros IIR*: Se dise
### 6.1.c Actividad Aeróbica
| Señal                                   | Hamming | Hann |Blackman |
|--------------------|----------|-------------|-----|
|filtro en pyFDA| <img width="1447" height="740" alt="image" src="https://github.com/user-attachments/assets/a798648c-dbe8-4e0f-b6e8-ca1140d3aae6" />|<img width="1437" height="821" alt="image" src="https://github.com/user-attachments/assets/6f26d3fd-3fa7-4617-b6c2-43427910e2bf" />|<img width="1438" height="847" alt="image" src="https://github.com/user-attachments/assets/785c1216-d817-4eb5-944e-025efe24953d" />|
|Actividad aeróbica|<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/3aa3f2b7-255d-4e29-b1cf-27b2ed7100aa" />|<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/374830a1-bf90-4c15-ba04-8974719503ba" />|<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/e431b31a-173c-4a71-8694-fa27ed9af5c6" />|

*Filtros IIR*: Se dise
<img width="989" height="490" alt="image" src="https://github.com/user-attachments/assets/82b7704b-ec84-458a-9d27-1b8ecc23cced" />





#### Resultados de los filtros de las señales ECG
Comparamos las respuestas en frecuencia de los filtros FIR de todas las 3 señales
<img width="989" height="490" alt="image" src="https://github.com/user-attachments/assets/bb358571-90c8-434e-be58-b7cd77e8d0aa" />
Análogamente, las respuestas en frecuencia de los filtros IIR: 
<img width="630" height="470" alt="image" src="https://github.com/user-attachments/assets/8e6a31e7-fcf4-4786-8991-49ab2bf95a5f" />
## 6.2 EEG
### 6.2.a Estado basal
| Señal                                   | Hamming | Hann |Blackman |
|--------------------|----------|-------------|-----|
|Basal|<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/748de29b-7aa2-4f09-8501-fc69e54caeae" />|<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/c8447fbd-de1c-405e-801c-51887c3e59b6" />|<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/81545631-63d8-42e1-82d0-641d330775d9" />|

*Filtros IIR*: chev y but
<img width="989" height="490" alt="image" src="https://github.com/user-attachments/assets/451780fc-57b1-44f2-8e94-4bd60a2e370a" />

### 6.2.b Mirada Fija
| Señal                                   | Hamming | Hann |Blackman |
|--------------------|----------|-------------|-----|
|Mirada fija|<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/6a2569e5-9c0b-4f06-adfb-f08c07779ea6" />|<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/5fceffe4-3c10-4105-86a6-c8cbd0e043ca" />|<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/6c34c529-9812-4af9-b11b-be63c814a4bb" />|


*Filtros IIR*: Se dise
<img width="989" height="490" alt="image" src="https://github.com/user-attachments/assets/8893ced8-df42-4e19-98d7-0c6c34a839c7" />

### 6.2.c Preguntas
| Señal                                   | Hamming | Hann |Blackman |
|--------------------|----------|-------------|-----|
|Preguntas|<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/3648a775-3f05-456e-9d48-f6423a62e93e" />|<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/33dabba3-4b30-4fed-8a5c-1b147d41f2d6" />|<img width="989" height="389" alt="image" src="https://github.com/user-attachments/assets/61818343-e524-4ed1-8382-ceab4a1c2f8c" />|


*Filtros IIR*: Se dise
<img width="988" height="490" alt="image" src="https://github.com/user-attachments/assets/4cd54bcf-4ad9-4fc4-a526-4136bebd75c9" />

#### Resultados de los filtros de las señales EEG
Comparamos las respuestas en frecuencia de los filtros FIR de todas las 3 señales
<img width="989" height="490" alt="image" src="https://github.com/user-attachments/assets/ba2bad5d-ab0b-4542-bcec-a9f07d617f14" />
IIR:
<img width="630" height="470" alt="image" src="https://github.com/user-attachments/assets/552822b4-47e8-4cb9-8b4a-dabbab9c0553" />

## 6.3 EMG
En este caso, se tomaron las señales de los bíceps en 3 estados:
### 6.3.a Bicep relajado
| Señal                                   |Señal Cruda | Señal Filtrada|
|--------------------|---------------------|-----|
| Relajado |<img width="866" height="393" alt="image" src="https://github.com/user-attachments/assets/9d0eb69f-c2f2-4b19-bf6c-b8690646c87d" />|<img width="1189" height="790" alt="image" src="https://github.com/user-attachments/assets/f0495b3d-ddaf-42c3-8048-03ade2c399c3" />|



### 6.3.b Movimiento Leve
|Señal                                   |Señal Cruda | Señal Filtrada|
|--------------------|---------------|-----|
|Leve |<img width="850" height="393" alt="image" src="https://github.com/user-attachments/assets/d8aadf16-6bee-4435-9a56-7eab3eb2b69f" />|<img width="1189" height="790" alt="image" src="https://github.com/user-attachments/assets/53d207c3-6642-41fa-86e6-abecf479cf44" />|



### 6.3.c Aplicando fuerza 
|Señal                                   |Señal Cruda | Señal Filtrada|
|--------------------|--------|--------|
|Fuerza |<img width="859" height="393" alt="image" src="https://github.com/user-attachments/assets/e6c427d3-a6b3-4250-ac4d-8285be4bb0c5" />|<img width="1189" height="790" alt="image" src="https://github.com/user-attachments/assets/2973eb70-c102-4c02-bf89-2bc2560100c5" />|



#### Resultados de los filtros de las señales EMG
Comparamos las respuestas en frecuencia de los filtros FIR de todas las 3 señales

IIR:
<img width="989" height="490" alt="image" src="https://github.com/user-attachments/assets/a5664f9a-9a43-4ee2-990e-fec462d5d04c" />


## **7. Referencias bibliográficas** <a name="id1"></a>

[1] ScienceDirect. Analog filter [Internet]. Amsterdam: Elsevier. Disponible en: https://www.sciencedirect.com/topics/engineering/analog-filter

[2] Advanced Solutions Nederland. Difference between IIR and FIR filters: a practical design guide [Internet]. Disponible en: https://www.advsolned.com/difference-between-iir-and-fir-filters-a-practical-design-guide/

[3] V. R. Zschorlich, "Digital filtering of EMG-signals," Electromyogr. Clin. Neurophysiol., vol. 29, pp. 81–86.

[4] E. Kwatny, D. H. Thomas, and H. G. Kwatny, "An application of signal processing techniques to the study of myoelectric signals," IEEE Transactions on Biomedical Engineering, vol. 17, no. 4, pp. 303–313.

[5] A. Thys et al., "Stabilization of the isoelectric line of surface EMG by means of high pass filters," Electromyogr. Clin. Neurophysiol., vol. 17, pp. 393–400.

[6] C. Saxena, A. Sharma, R. Srivastav, and H. K. Gupta, "Denoising of ECG signals using FIR & IIR filter: a performance analysis," International Journal of Engineering & Technology, vol. 7, no. 4.12, pp. 1–5, 2018.

[7] A. Pant and A. Kumar, "Hanning FIR window filtering analysis for EEG signals," Biomedical Analysis, vol. 1, pp. 111–123, 2024, doi: 10.1016/j.bioana.2024.05.003.

