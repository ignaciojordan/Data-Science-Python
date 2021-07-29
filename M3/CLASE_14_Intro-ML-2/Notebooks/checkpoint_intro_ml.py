import sys
sys.path.insert(1, '../../../common')
from checkpoint import *

descripcion_1 = '''
Indicá cuáles de los siguientes son ejemplos de aprendizaje supervisado (puede haber más de una opción correcta):
'''
opciones_1 = ['Predecir que un cliente se está por dar de baja de un servicio',
              'Visualizar en dos dimensiones un conjunto de observaciones representadas por 20 features',
              'Estimar la cantidad de retweets de una publicación de acuerdo a su contenido',
              'Segmentar en grupos a los usuarios de un e-commerce']
correct_1 = ['Predecir que un cliente se está por dar de baja de un servicio',
             'Estimar la cantidad de retweets de una publicación de acuerdo a su contenido']
test_1 = create_checkbox(descripcion_1, opciones_1, correct_1)


descripcion_2 = '''
Si un modelo aprende perfectamente los datos de entrenamiento pero no generaliza bien a los datos de testeo,
estamos ante una situación de:
'''
opciones_2 = ['Alto sesgo o subajuste (underfitting)',
              'Alta varianza o sobreajuste (overfitting)',
              'Ajuste óptimo',
              'Ninguna de las opciones es correcta']
feedback_2 = ['Si un modelo subajusta a los datos de entrenamiento, no los está aprendiendo perfectamente.',
              '¡Correcto! Cuando un modelo sobreajusta a los datos de entrenamiento, pierde capacidad de generalización y no tiene un buen desempeño prediciendo los datos de testeo.',
              'El ajuste óptimo se da cuando un modelo ajusta bien a los datos de entrenamiento y también generaliza correctamente.',
              '¡Repasá bien las opciones porque hay una que es correcta!']
test_2 = create_multiple_choice(descripcion_2, opciones_2, opciones_2[1], feedback=feedback_2)


descripcion_3 = '''
Si estamos desarrollando un modelo para predecir el precio de reventa de autos usados, nos encontramos trabajando en un problema de 
'''
opciones_3 = ['Regresión', 'Clasificación', 'Clustering', 'Reducción de la dimensionalidad']
feedback_3 = ['¡Muy bien! Nuestra variable objetivo, el precio de reventa, es cuantitativa, por lo que se trata de un problema de regresión.',
              'Un clasificador podría predecir si un auto usado se va a revender o no, pero no nos permitiría predecir a qué precio.',
              'No estamos buscando encontrar grupos de autos similares entre sí, sino más bien predecir una variable objetivo que es el precio de reventa.',
              'Si bien podríamos hacer una reducción de la dimensionalidad como paso previo al entrenamiento del modelo, en este caso contamos con una variable objetivo que es el precio de reventa.']

test_3 = create_multiple_choice(descripcion_3, opciones_3, opciones_3[0], feedback_3)


descripcion_4 = '''
Clustering se diferencia de una clasificación en que:
'''
opciones_4 = ['Los clusters tienen etiquetas predefinidas y las clasificaciones, no',
              'Al hacer una clasificación, necesitamos features numéricas, mientras que al hacer clustering, precisamos features cualitativas',
              'Clustering forma parte de las técnicas de aprendizaje supervisado, mientras que la clasificación es un problema típico de aprendizaje no supervisado',
              'Ninguna de las anteriores es correcta']
feedback_4 = ['Mmm... ¿es así o es al revés?',
              'Hay distintos algortimos de clasificación y de clustering que, con la representación adecuada, pueden lidiar con cualquier tipo de feature, se trate de variables cuantitativas o cualitativas.',
              'Mmm... ¿es así o es al revés?',
              '¡Muy bien! Clustering es una técnica de aprendizaje no supervisado, mientras que las clasificaciones corresponden al marco del aprendizaje supervisado y ninguna de las opciones refleja esto correctamente.']

test_4 = create_multiple_choice(descripcion_4, opciones_4, opciones_4[-1], feedback_4)


descripcion_5 = '''
PCA:
'''
opciones_5 = ['Es una técnica de clasificación para variables de alta dimensionalidad',
              'Es una técnica de regresión para cuando tengo alta correlación entre las features',
              'Es una técnica para agrupar observaciones según la correlación entre sus features',
              'Es una técnica para proyectar en un subespacio de menor dimensión mis variables, preservando la mayor cantidad de información posible']

feedback_5 = ['PCA es una técnica de aprendizaje no supervisado, por lo cual no se utiliza para hacer clasificaciones.',
              'PCA es una técnica de aprendizaje no supervisado, por lo cual no se utiliza para hacer regresiones.',
              'Si bien PCA es una técnica de aprendizaje no supervisado, no se utiliza para generar clusters de observaciones.',
              '¡Correcto! PCA es una técnica de reducción de la dimensionalidad que retiene las características esenciales de los datos originales.']
test_5 = create_multiple_choice(descripcion_5, opciones_5, opciones_5[-1], feedback_5)