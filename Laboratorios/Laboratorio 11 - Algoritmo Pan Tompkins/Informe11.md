## 1. Introducción al tema
### ¿Qué es el algoritmo Pan–Tompkins?

El algoritmo Pan–Tompkins, desarrollado en 1985, es uno de los métodos más influyentes para la detección automática del complejo QRS en señales electrocardiográficas (ECG). Su diseño combina filtrado digital, derivadas, transformaciones no lineales y umbrales adaptativos, permitiendo identificar latidos cardíacos en tiempo real con alta confiabilidad.

A pesar de haberse propuesto hace casi cuatro décadas, sigue siendo un estándar de referencia en investigación y en aplicaciones biomédicas modernas debido a su robustez,baja complejidad computacional y excelente desempeño en condiciones reales de ruido.

<p align="center">
 <img width="412" height="141" alt="image" src="https://github.com/user-attachments/assets/b7a0aa40-0637-454b-969f-152c813088ce" />
</p>

<p align="center"><em>Figura 1. Algoritmo de Pan–Tompkins</em></p>


### ¿Por qué es importante en el procesamiento de señales biomédicas?

La detección automática del QRS es una tarea fundamental para el análisis de señales biomédicas, ya que constituye el punto de partida para cálculos como:

- Frecuencia cardíaca
- Variabilidad del ritmo (HRV)  
- Detección de arritmias  
- Segmentación de ondas P, QRS y T  
- Parámetros clínicos como PR y QT  
<p align="center">
  <img width="225" height="225" alt="image" src="https://github.com/user-attachments/assets/df2413da-bb3b-4f01-9fa5-2c341985031e" />

</p>

<p align="center"><em>Figura 2. Señal ECG</em></p>


Pan–Tompkins destaca porque puede operar con gran precisión incluso cuando la señal ECG está contaminada por ruido muscular (EMG), artefacto de movimiento, baseline wander o interferencia de red eléctrica. Este comportamiento ha sido confirmado en evaluaciones recientes que analizan su rendimiento bajo distintos niveles de ruido y con bases estándar como MIT-BIH y la Noise Stress Test Database .

### Un aspecto relevante: desempeño bajo ruido

Un punto especialmente interesante para mencionar en la introducción es que el algoritmo no solo funciona bien en ECG clínicos limpios, sino que también mantiene un desempeño sólido cuando la señal es de baja calidad.

Estudios actuales han mostrado que Pan–Tompkins puede mantener **alta sensibilidad de detección** incluso con señales ruidosas con niveles de **SNR entre 24 dB y 12 dB**, antes de que el rendimiento disminuya de manera notable en ambientes extremadamente ruidosos (por ejemplo, −6 dB).

Esto evidencia su capacidad para ser utilizado en entornos reales como:

- Monitoreo ambulatorio  
- Holters  
- Wearables  
- Sistemas de telemedicina  

### Papel del algoritmo en el análisis del ECG

El complejo QRS es la estructura eléctrica dominante en cada latido y es la referencia para segmentar el resto del ECG. De hecho, una vez identificado el QRS, las demás ondas (P y T) pueden localizarse con mayor facilidad, tal como reportan diversos estudios de análisis automatizado del ECG.

Detectar el QRS con precisión es indispensable porque afecta directamente:

- La estimación del ritmo cardíaco  
- La toma de decisiones clínicas automatizadas  
- La detección de arritmias  
- La estabilidad de los algoritmos de monitoreo  

Por ello, Pan–Tompkins se consolidó como un **pilar metodológico** en el procesamiento digital de señales ECG.

