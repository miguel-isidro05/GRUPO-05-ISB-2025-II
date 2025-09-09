# **LABORATORIO 3: Uso de BITalino para EMG**

## **Tabla de contenidos**

1. [Introducción](#id1)
2. [Objetivos específicos de la práctica](#id2)
3. [Materiales y equipos](#id3)
4. [Procedimiento](#id4)\
     4.1. [EMG - Biceps Braquial](#id5)\
     4.2. [EMG - Triceps](#id6)
5. [Resultados](#id7)
6. [Análisis y discusión](#id8)
7. [Referencias](#id9)

## **1. Introducción** <a name="id1"></a>
La electromiografía (EMG) es una prueba diagnóstica que evalúa el estado y salud de los músculos así como de los nervios que los controlan [1].
En una prueba EMG se analizan las señales eléctricas que emiten los músculos cuando están en reposo y en movimiento. Gracias a estas evaluaciones se puede detectar si existe una afección o transtorno muscular [2].
Durante la contracción muscular, ya sea en reposo en un músculo normal o anormal, el sistema nervioso envía impulsos eléctricos a través de las neuronas motoras las cuales activan las fibras musculares generando un potencial de acción muscular que produce la contracción[3]. De este modo las pruebas de EMG proporcionan datos sobre los impulsos nerviosos y las reacciones de las fibras musculares.

Para obtener dichas señales fisiológicas se hace uso del BITalino, un dispositivo que permite la recolección de datos biomédicos. Este equipo cuenta con sensores diseñados para la obtención de EDA, ECG, EEG y EMG. Además, cuenta con el software OpenSignals (r)evolution para visualizar en tiempo real las señales adquiridas, almacenarlas y exportarlas para un posterior análisis. 


## **2. Objetivos específicos de la práctica** <a name="id2"></a>
* Familiarizarse con el hardware y software del BITalino para el procesamiento de señales EMG.
* Registrar señales EMG en reposo y contracción en diferentes grupos musculares.
* Aplicar filtros y procesamiento a las señales obtenidas del software para mejorar la calidad.
* Analizar e interpretar las señales obtenidas.


## **3. Materiales y equipos** <a name="id3"></a>

| Materiales                                   | Cantidad | Imagen                          |
|----------------------------------------------|----------|---------------------------------|
| Batería 3.7V                                 | 1        | ![bateria](https://github.com/user-attachments/assets/25fe9643-a7fa-4bd9-85ad-e1ce78a926ab) |
| Software OpenSignals                         | 1        | ![opensignals](https://github.com/user-attachments/assets/270de790-173f-42fc-9960-5b12a7fff042) |
| Electrodos de superficie descartables        | 3        | ![electrodos (1)](https://github.com/user-attachments/assets/2e58ad27-7c4a-4336-9fdf-fe54129be397) |
| Cable de los 3 electrodos                    | 1        | ![cable](https://github.com/user-attachments/assets/2d397e32-3ec4-4982-91fe-0d6855e3aec0) |
| Kit BITalino                                 | 1        | ![bitalino](https://github.com/user-attachments/assets/a60c127f-27c2-4a03-b852-454d23f54163) |
| Laptop                                       | 1        | ![laptop](https://github.com/user-attachments/assets/c1394461-1a65-41fc-b6f4-8d8ae5b3b37b) |

## **4. Procedimiento** <a name="id4"></a>
1. Se debe seleccionar el músculo a evaluar y limpiar la zona. De ser posible seleccionar una zona sin vellos para mejorar la impedancia de los electródos.
2. Colocar 2 electrodos (Positivo y Negativo) en el músculo objetivo y un tercer electrodo de referencia sobre una región electricamente muerta. En el presente laboratorio se eligio poner el electrodo en la cresta hiliaca (hueso de la cadera).
3. Sincronizar mediante protocolo Bluetooth el BITalino y la computadora con el software previamente instalado
4. Realizar las mediciones con el software de 3 diferentes ejercicios para cada músculo: en reposo, fuerza leve sin oposición y fuerza con oposición.
   
### **4.1. EMG - Biceps Braquial** <a name="id5"></a>

A continuación, presentamos el material audiovisual del EMG en entranamiento con el biceps braquial:

<div align="center">
 
|  **Biceps en reposo**  | **Biceps sin oposición** | **Biceps con oposición** |
|:----------------------:|:------------------------:|:------------------------:|
| <video src="https://github.com/user-attachments/assets/a20d28f2-9160-462d-9f0d-921bce4582ed"></video> | <video src="https://github.com/user-attachments/assets/e34ea912-98a3-4a99-8bbd-69a006e5b189"></video> | <video src="https://github.com/user-attachments/assets/582a7d62-79ef-40fb-a2c3-521d561ef5de"></video> |

</div>


### **4.2. EMG - Triceps** <a name="id6"></a>

A continuación, presentamos el material audiovisual del EMG en entranamiento con el triceps:

<div align="center">
 
|  **Triceps en reposo**  | **Triceps sin oposición** | **Triceps con oposición** |
|:----------------------:|:------------------------:|:------------------------:|
| <video src="https://github.com/user-attachments/assets/122f538e-1267-4ab4-ba6d-a0584519151f" controls></video> | <video src="https://github.com/user-attachments/assets/5412d4e4-d70a-40e8-b306-6c804fc63fcb" controls></video> | <video src="https://github.com/user-attachments/assets/dc13e13e-e735-4437-a025-f35a0cd603c7" controls></video> |

</div>




## **6. Resultados** <a name="id7"></a>

Para los resultados haremos uso del archivo "CodigosEMG.ipynb" que se encuentra en el mismo folder. El cual contiene todos los codigos hechos para la visualización de las gráficas de las señales adquiridas. Asi como su respectivo filtrado y análisis de frecuencia.

## **7. Análisis y discusión** <a name="id8"></a>


## **8. Referencias** <a name="id9"></a>
[1]
[2]
[3]
