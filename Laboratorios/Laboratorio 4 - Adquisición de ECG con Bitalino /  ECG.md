# LABORATORIO 4: – ADQUISICIÓN DE ECG

## Tabla de contenidos
1. [Introducción](#introducción)
2. [Señal ECG](#señal-ecg)
3. [Objetivos del Laboratorio](#objetivos-del-laboratorio)  
4. [Materiales](#materiales)  
5. [Metodología](#metodología)
   - [Preparación inicial](#preparación-inicial)
   - [Colocación de electrodos](#colocación-de-electrodos)
   - [Configuración del sistema](#configuración-del-sistema)
   - [Adquisición de datos](#adquisición-de-datos)
6. [Procesamiento de datos](#procesamiento-de-datos)  
   - [a) Importar Librerías](#importar-librerías)  
   - [b) Cargar archivos](#cargar-archivos)  
   - [c) Aplicación de filtros](#aplicación-de-filtros)  
   - [d) Ploteo de las señales](#visualización)  
7. [Resultados y limitaciones](#resultados-y-limitaciones)  
8. [Referencias](#referencias)  

---

## 1. Introducción <a name="introducción"></a>
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
<p align="center">
  <img src="https://cdn.rohde-schwarz.com/pws/application/cards/3607_3180/capturing-small-ecg-signals-medical-applications_ac_3607-3180-92_01.1_w1280_hX.png" 
       alt="Registro de señales de ECG" 
       width="450"><br>
  <em>Figura 1. Registro de señales de ECG (Rohde & Schwarz, Aplicaciones médicas).</em>
</p>

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
       alt="Electrocardiograma y derivaciones" 
       width="450"><br>
  <em>Figura 2. Electrocardiograma y derivaciones (UNAM, Fisiología).</em>
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

## Metodología
Para la adquisición de la señal de ECG utilizando el kit **BiTalino** y el software **OpenSignals**, se siguió el siguiente procedimiento:  

### Preparación inicial: 
   - Conexión de los electrodos desechables al cable de 3 derivaciones y colocación en la piel según la configuración estándar de ECG.  
   - Encendido del dispositivo BiTalino y vinculación por Bluetooth con la laptop mediante el software OpenSignals.  
   - Verificación de la señal registrada para asegurar calidad y ausencia de ruidos excesivos.

### Colocación de los electrodos: 
Para obtener una señal de ECG de buena calidad, la ubicación correcta de los electrodos es fundamental. A continuación, se presentan dos referencias que explican la posición estándar y los efectos de colocar mal los electrodos:  

   a. **LITFL – ECG Lead Positioning**  
   Según la guía clínica de *Life in the Fast Lane (LITFL)*, los electrodos deben colocarse en puntos anatómicos bien definidos para asegurar registros confiables. En el caso de las derivaciones precordiales:  
   - **V1 y V2**: 4.º espacio intercostal, a la derecha e izquierda del esternón.  
   - **V4**: 5.º espacio intercostal en la línea medio clavicular.  
   - **V3**: entre V2 y V4.  
   - **V5 y V6**: en la misma altura que V4, pero en la línea axilar anterior y media.  

   <p align="center">
     <img src="https://litfl.com/wp-content/uploads/2018/08/Chest-external-landmarks-in-ECG-placament.png" 
          alt="Posición de electrodos precordiales" 
          width="400"><br>
     <em>Figura 3. Posición estándar de electrodos precordiales (LITFL).</em>
   </p>  

   b. **Tung, R. T. et al., 2021 – Electrocardiographic Limb Leads Placement and Its Effect on ECG Interpretation**  
   Este artículo científico analiza el impacto de la colocación de los electrodos de las extremidades en la interpretación del ECG. Explica que mover los electrodos de los brazos o piernas a posiciones no convencionales (por ejemplo, más arriba en el torso) puede cambiar el eje eléctrico aparente del corazón, alterar el segmento ST o incluso simular un infarto inexistente.  

   El estudio concluye que las derivaciones de miembros deben colocarse de forma simétrica en las extremidades (RA, LA, LL y RL), ya que su reposicionamiento sin seguir estándares puede generar errores clínicos serios. Por ello, recomienda seguir las guías internacionales para asegurar lecturas correctas.  

   <p align="center">
     <img src="https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8010/8415387/0b20e08ada27/14-229f3.jpg" 
          alt="Colocación de electrodos en extremidades" 
          width="400"><br>
     <em>Figura 4. Colocación de electrodos en extremidades (Tung et al., 2021).</em>
   </p>  
   
### Configuración del sistema:
- Se instaló el software **OpenSignals** en la laptop para establecer la comunicación con el kit BiTalino.  
- Se activó la conectividad **Bluetooth** de la computadora y se emparejó con el dispositivo BiTalino utilizando el código predeterminado.  
- En el software, se seleccionó el canal correspondiente al **sensor de ECG** y se ajustaron los parámetros de muestreo (frecuencia de adquisición y duración de la señal).  
- Se verificó la correcta recepción de la señal en tiempo real antes de iniciar la adquisición formal.  

### Adquisición de datos
Durante la práctica se registraron señales de ECG en un sujeto voluntario en diferentes condiciones fisiológicas. En total se realizaron las siguientes tomas:  

**1. Reposo**  
   - 1 registro inicial con el sujeto en reposo y en calma.
     
<div align="center">

| **Toma en reposo** |
|:----------------------:|
| <video src="https://github.com/user-attachments/assets/2e581bb9-ceae-4bbf-82a4-4913a6c3245a" controls></video> |

</div>


**2. Respiracion**

<div align="center">
 
| **Toma 1** | **Toma 2** | **Toma 3** |
|:-----------------------:|:--------------------------:|:--------------------------:|
| <video src="https://github.com/user-attachments/assets/ecc5c4b2-8733-4968-9329-2e7f5ea2533f" controls></video> | <video src="https://github.com/user-attachments/assets/40c5edc6-781a-4698-807f-5a9b1ae9d326" controls></video> | <video src="https://github.com/user-attachments/assets/f7e2701a-3f41-422c-91ae-466e512d350b" controls></video> |

</div>

**3. Actividad Fisica**

<div align="center">

| **Pectoral sin oposición** |
|:---------------------------:|
| <video src="https://github.com/user-attachments/assets/22de795a-6e0c-4749-be6b-432d3a4b73ff" controls></video> |

</div>


     

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
