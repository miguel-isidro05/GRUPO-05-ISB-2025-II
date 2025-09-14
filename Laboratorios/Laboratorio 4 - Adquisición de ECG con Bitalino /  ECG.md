# LABORATORIO 4: – ADQUISICIÓN DE ECG

## Tabla de contenidos
1. [Introducción](#introducción)
2. [Señal ECG](#señal-ecg)
3. [Objetivos del Laboratorio](#objetivos-del-laboratorio)  
4. [Materiales y metodología](#materiales-y-metodología)  
   3.1 [Materiales utilizados](#materiales-utilizados)  
   3.2 [Metodología](#metodología)  
   - [Colocación de electrodos](#colocación-de-electrodos)  
   - [Configuración del sistema](#configuración-del-sistema)  
   - [Adquisición de datos](#adquisición-de-datos)  
5. [Procesamiento de datos](#procesamiento-de-datos)  
   - [Lectura de archivos](#lectura-de-archivos)  
   - [Preprocesamiento de la señal](#preprocesamiento-de-la-señal)  
   - [Análisis en ventana de 100 ms](#análisis-en-ventana-de-100-ms)  
   - [Visualización](#visualización)  
6. [Resultados y limitaciones](#resultados-y-limitaciones)  
7. [Referencias](#referencias)  

---

## Introducción
El electrocardiograma (ECG) es una herramienta fundamental en el ámbito biomédico, ya que permite registrar la actividad eléctrica del corazón de manera no invasiva. Su análisis facilita la detección de alteraciones en el ritmo y la conducción cardiaca, así como la evaluación del estado fisiológico del paciente en diferentes condiciones, como reposo o actividad física.[1]

Los resultados de un electrocardiograma pueden ayudar a diagnosticar:

- Arritmia
- Miocardiopatía
- Enfermedad de las arterias coronarias
- Ataque cardiaco
- Insuficiencia cardiaca
- Enfermedades de las válvulas del corazón
- Defectos cardiacos congénitos

## Señal ECG
![Señal ECG](https://cdn.rohde-schwarz.com/pws/application/cards/3607_3180/capturing-small-ecg-signals-medical-applications_ac_3607-3180-92_01.1_w1280_hX.png)
| Segmento      | Descripción                                                                 |
|---------------|------------------------------------------------------------------------------|
| **Onda P**    | Indica la activación eléctrica de las aurículas previo al paso al ventrículo.|
| **Intervalo PR** | Tiempo que tarda el impulso en propagarse desde las aurículas hasta los ventrículos.|
| **Complejo QRS** | Señal que refleja la contracción eléctrica de los ventrículos.             |
| **Intervalo QT** | Periodo que abarca desde la activación ventricular hasta su recuperación completa.|
| **Segmento ST** | Marca la fase en la que el ventrículo está totalmente despolarizado.       |
| **Onda T**    | Representa el proceso de recuperación de la actividad eléctrica ventricular. |
| **Onda U**    | Se asocia con la recuperación tardía de fibras especializadas o miocitos.    |

## Electrocardiograma  

El ECG clínico estándar se registra con 12 derivaciones, que permiten observar la actividad eléctrica cardíaca desde distintos planos. Estas derivaciones se obtienen a partir de electrodos ubicados en las extremidades y en la región torácica. De ellas, seis corresponden al plano frontal (derivaciones I, II, III, aVR, aVL y aVF) y las otras seis al plano horizontal (precordiales V1 a V6). Esta disposición brinda una visión completa del proceso de despolarización y repolarización del corazón.[3]

<p align="center">
  <img src="https://fisiologia.facmed.unam.mx/wp-content/uploads/2021/11/UTII-2B-img-Vectores-de-despo-ventri.jpg" 
       alt="Vectores de despolarización ventricular" 
       width="350">
</p>

## Objetivos del Laboratorio
- Configurar adecuadamente el sistema BiTalino para la adquisición de señales cardíacas.

- Registrar y visualizar una señal de ECG en condiciones controladas usando el software OpenSignals.

- Reconocer las ondas principales (P, QRS y T) dentro del registro electrocardiográfico.

- Analizar los cambios en la señal de ECG bajo diferentes condiciones fisiológicas (reposo, apnea breve y actividad física).

## Materiales:
| Materiales                                   | Cantidad | Imagen                          |
|----------------------------------------------|----------|---------------------------------|
| Batería 3.7V                                 | 1        | ![bateria](https://github.com/user-attachments/assets/25fe9643-a7fa-4bd9-85ad-e1ce78a926ab) |
| Software OpenSignals                         | 1        | ![opensignals](https://github.com/user-attachments/assets/270de790-173f-42fc-9960-5b12a7fff042) |
| Electrodos de superficie descartables        | 3        | ![electrodos (1)](https://github.com/user-attachments/assets/2e58ad27-7c4a-4336-9fdf-fe54129be397) |
| Cable de los 3 electrodos                    | 1        | ![cable](https://github.com/user-attachments/assets/2d397e32-3ec4-4982-91fe-0d6855e3aec0) |
| Kit BITalino                                 | 1        | ![bitalino](https://github.com/user-attachments/assets/a60c127f-27c2-4a03-b852-454d23f54163) |
| Laptop                                       | 1        | ![laptop](https://github.com/user-attachments/assets/c1394461-1a65-41fc-b6f4-8d8ae5b3b37b) |

### Metodología


#### Colocación de electrodos
Describe la posición estándar para registrar ECG.

#### Configuración del sistema
Explica la conexión entre hardware y software.

#### Adquisición de datos
Cómo se registraron las señales, duración, sujeto, etc.

## Procesamiento de datos

### Lectura de archivos
Cómo se importaron los datos al software.

### Preprocesamiento de la señal
Filtros pasabanda y notch aplicados.

### Análisis en ventana de 100 ms
Explica la técnica usada.

### Visualización
Inserta las gráficas obtenidas.

## Resultados y limitaciones
Discusión de los hallazgos y dificultades encontradas.

## Referencias
Formato APA o IEEE.
