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

## **4. Filtrado de la señal ECG** <a name="id1"></a>

## **5. Discusión y Análisis** <a name="id1"></a>



## **6. Referencias bibliográficas** <a name="id1"></a>

[1] ScienceDirect. Analog filter [Internet]. Amsterdam: Elsevier. Disponible en: https://www.sciencedirect.com/topics/engineering/analog-filter

[2] Advanced Solutions Nederland. Difference between IIR and FIR filters: a practical design guide [Internet]. Disponible en: https://www.advsolned.com/difference-between-iir-and-fir-filters-a-practical-design-guide/

