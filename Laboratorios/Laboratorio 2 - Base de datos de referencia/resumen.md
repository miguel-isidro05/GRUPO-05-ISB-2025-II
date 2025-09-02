# Resumen  

## 1. Comprensión del Problema (Business Understanding)  
Las **interfaces cerebro–computadora (BCI)** permiten transformar la actividad cerebral en comandos de control sin necesidad de actividad muscular.  
Un sistema típico BCI incluye:  

- Adquisición de señales EEG  
- Preprocesamiento  
- Extracción de características  
- Clasificación mediante IA  
- Retroalimentación hacia el usuario  

En rehabilitación, uno de los paradigmas más relevantes es la **imaginería motora (MI)**, que activa redes corticales similares a las del movimiento real, facilitando la **plasticidad cerebral** y la **recuperación funcional** en pacientes con secuelas neurológicas.  
Este enfoque ha demostrado gran potencial en el control de **dispositivos robóticos** o **avatares virtuales**, justificando su aplicación en rehabilitación motora y **síndrome de miembro fantasma**.  

### 🎯 Objetivos del análisis  
- Revisar y analizar bases de datos de señales EEG de MI para establecer parámetros de referencia.  
- Preprocesar las señales EEG (filtrado, eliminación de artefactos, segmentación).  
- Implementar un módulo de retroalimentación visual en tiempo real.  
- Validar experimentalmente la efectividad del sistema en rehabilitación de miembro fantasma.  

---

## 2. Comprensión de los Datos (Data Understanding)  

El uso de **datasets estandarizados** es esencial para entrenar, validar y comparar algoritmos en BCI.  
Existen múltiples repositorios (OpenBCI, Graz, PhysioNet), pero los datasets de las **BCI Competitions** se han convertido en benchmarks fundamentales.  
- **BCI Competition IV Dataset 2a**:  
  - 22 canales EEG + 3 EOG  
  - 9 sujetos  
  - 4 clases de MI (mano izquierda, mano derecha, pie, lengua)  
  - Es el más robusto y ampliamente usado en rehabilitación motora compleja.  
- **BCI Competition IV Dataset 2b**:  
  - 3 canales EEG  
  - 2 clases de MI (mano izquierda/derecha)  
  - Útil para validaciones rápidas o sistemas con limitaciones de hardware.  
- **Otros datasets (I, III)**:  
  - Se emplean para análisis específicos de señales no estacionarias o clasificación multicategoría.  

👉 En este proyecto, el **Dataset 2a** es la fuente principal, mientras que el **Dataset 2b** se considera complementario para pruebas y validaciones iniciales.  

