# Examen 3er Parcial 
Alisson García Mejía 

1. ¿Cuál es la diferencia entre métodos de aprendizaje supervisado y no supervisado?

    En el supervisado usamos **etiquetas**, el modelo se entrena con datos etiquetados para que identifiquemos que cada entrada tenga una salida esperada, con base al entrenamiento que se le dió. A partir de estas, podemos predecir qué etiquetas tendrá en nuevos datos.
   
    Mientras que en el no supervisado no tenemos datos etiquetados, ya que su función es identificar patrones ocultos, estructuras o relaciones entre los datos, para así agruparlos en clusters e identificar también los datos inusuales.
    
    En un ejemplo clínico, el aprendizaje supervisado nos indica el diagnóstico: enfermo o sano (en base a un entrenamiento con etiquetas), mientras que el no supervisado agruparía pacientes por síntomas al encontrar similitudes entre ellos (o también identificar anomalías). 


2. ¿En cuál dataset se pueden aplicar métodos de Aprendizaje supervisado y en cuál métodos de Aprendizaje no supervisado? 

    En el **Dataset 1** se puede aplicar método de aprendizaje **supervisado** ya que cuenta con etiquetas (SleepStage) que está indicando la etapa de sueño basada en las señales EEG. 
Lo que nos permite clasificar y predecir, algo característico de este tipo de aprendizaje. 

    En el **Dataset 2** aplicaría aprendizaje **no supervisado** ya que no contamos con etiquetas que nos indiquen la naturaleza de los datos. Si aplicamos Aprendizaje no supervisado podremos identificar algún patrón que nos permita clasificar los datos o identificar alguna relación entre ellos 


3. ¿Cuál es la diferencia entre un problema de clasificación y uno de regresión? 

Su principal diferencia radica en el tipo de variable que analiza y sale, en los problemas de **clasificación** queremos predecir una categoría o clase, haciéndo que nuestra salida sea una variable **cualitativa** como positivo/negativo, setosa/versicolor, por ejemplo. En este tipo de problemas usamos métricas como matrices de confusión, F1-score, accuracy.

En problemas de **regresión** queremos predecir un valor **numérico continuo**, en donde nuestra salida será **cuantitativa** como lo es que en el caso de modelos de regresión linela o polinomial, para estos problemas usamos métricas como el MSE, RMSE, MAE y R^2 


4. ¿Cuál es la diferencia entre over-fitting y under-fitting? 

El overfitting es un problema de **sobreajuste**, se ajustan demasiado los datos de entrenamiento, donde no aprende de los datos principales sino de los que provocan ruido y son irrelevantes. Lo que hace que tengamos un excelente rendimiento en el entrenamiento pero bajo rendimiento en el test al aplicarlo con datos nuevos. 

En el **underfitting**, este es un problema de **sub-ajuste**, es decir, el modelo es muy simple y no está capacitado para analizar datos complejos e identificar patrones, lo que hace que tengamos un rendimiento bajo tanto en el entrenamiento como en el test. 


5. **¿Qué ensayo dirías que corresponde a casos con over-fitting, under-fitting o balanceado?**
    * Casos de over-fitting: 1, 4 y 6 
    * Casos de under-fitting: 2 y 3 
    * Balanceado: 5 

6. **A. Escribe las fórmulas de accuracy, precisión, recall y f1-score**
    
    * Accuracy: (TP + TN) / (TP + TN + FP + FN)
    * Precisión: TP / TP + FP 
    * Recall: TP / TP + FN 
    * F1-score: (2 x precisión x recall) / (precisión + recall)

    **B. Con base a la tabla, calcular: accuracy, precisión, recall y f1-score**
        
    * Accuracy: 85 / 100 = 0.85
    * Precisión: 40 / 45 = 0.8889
    * Recall: 40 / 50 = 0.8 
    * F1-score: (2 x 0.8889 x 0.8) / (0.8889 + 0.8) = 0.842 
            
    **C. 3 descripciones métricas en un problema de clasificación, indica a qué métrica corresponde**
    1. Proporción de predicciones correctas (P y N)... -> Accuracy 
    2. Porcentaje de verdaderos positivos... -> Recall
    3. Porcentaje de aciertos entre los casos... -> Precisión
   

7. Características de algoritmos de Machine Learning supervisado, indica a qué método corresponde cada una de las afirmaciones: 

   1. Análisis discriminante
   2. Vecino más cercano
   3. SVM
   4. árbol de decisión
   5. árbol de decision
   6. SMV
   7. Análisis discriminante
   8. Vecino más cercano
   9. Bosques aleatorios
   10. Árbol de decisión
   11. Análisis discriminante
   12. SVM
   13. Bosques aleatorios
   14. SVM
   15. Bosques aleatorios


8. ¿Cuál es la diferencia entre Perceptron, Red Neuronal Artificial y Red Neuronal Convolucional? 

    El Perceptron es la unidad más básica de una red neuronal artificial, tiene una sola capa de neuronas con pesos ajustables y se usa para problemas de clasificación lineal, la RNA es una extensión del perceptrón, tiene múltiples capas de neuronas y puede procesar información más compleja porque cuenta con capas ocultas. La Red neuronal convolucional es un tipo de RNA diseñada para procesar imágenes y señales visuales, usa capas convolucionales para detectar características en imágenes. 


9. En el contexto de aprendizaje de una red neuronal, ¿qué es un epoch? 

Consiste en un cíclo que se cumple de todo el conjunto de datos de entrenamiento de un modelo. En una epoch se ajustan los pesos para mejorar el desempeño, en cada epoch se calcula la salida y se compara con el valor real 

10. Lista las principales funciones de activación y describe la diferencia entre las funciones sigmoid y softmax

Las funciones de activación son: sigmoid, ReLU, Leaky ReLu, Softmax y Tanh (tangente hiperbólica)

Sigmoid se usa para problemas de clasificación binaria, convierte valores en un rango de 0 a 1 para determinar una única clase. Mientras que Softmax se usa en clasificación multiclase, aquí se elije la clase con mayor certeza
