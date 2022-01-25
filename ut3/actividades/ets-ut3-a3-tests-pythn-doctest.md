# UT3-A3. Pruebas del software en Python con doctest

## Elementos curriculares
Resultado de aprendizaje:

3. Verifica el funcionamiento de programas, diseñando y realizando pruebas.

Criterios de evaluación:

3.a. Se han identificado los diferentes tipos de pruebas.
3.b. Se han definido casos de prueba.

Contenidos:

* Planificación de Pruebas.
* Procedimientos y casos de prueba.
* Pruebas de código: cubrimiento, valores límite, clases de equivalencia, etc.
* Pruebas unitarias; herramientas.

## Introducción

A partir de los casos de prueba diseñados en la actividad anterior añadir tests a los programas utilizando la librería `doctest`

## Actividad 1. Salario semanal

Para la siguiente función:

```python
def salario(precio_hora, horas):
    total = 0
    if horas <= 40:
        total = horas * precio_hora
    elif horas <= 48:
        horas_extra = horas - 40
        total = 40 * precio_hora + 2 * precio_hora * horas_extra
    else: 
        horas_extra_triple = horas - 48
        total = 40 * precio_hora + 2 * precio_hora * 8 + 3 * precio_hora * horas_extra_triple
    return total
```

Inserta aquí los casos de prueba obtenidos, utilizando la prueba del camino básico, para la función en la actividad anterior:

```

```

A partir de dichos casos de prueba incluye en el encabezado de la función la documentación de la misma y los tests que permitan comprobar todos los casos de prueba. Inserta a continuación la función con los casos de prueba incorporados:

```python

```

Ejecuta desde el terminal los tests e inserta a continuación el resultado:

```bash

```

## Actividad 2. Segundo siguiente.

a) Para la siguiente función:

```python=
def segundo_siguiente(h, m, s):
    if s < 59:
        s += 1
    elif m < 59:
        m += 1
        s = 0
    elif h < 23:
        h += 1
        m = 0
        s = 0
    else:
        h = m = s = 0
    return [h, m, s]
```

Inserta aquí los casos de prueba obtenidos, utilizando la prueba del camino básico, para la función en la actividad anterior:

```

```

A partir de dichos casos de prueba incluye en el encabezado de la función la documentación de la misma y los tests que permitan comprobar todos los casos de prueba. Inserta a continuación la función con los casos de prueba incorporados:

```python

```

Ejecuta desde el terminal los tests e inserta a continuación el resultado:

```bash

```
b) Si introducimos a la función anterior un error cambiando la línea 7 del programa de forma que pase de:

```python
    elif h < 23:
```
a:

```python
    elif h <= 23:
```

Ejecuta nuevamente los tests a la función e inserta el resultado:

```bash

```

¿Se detecta el error?¿En cuántas pruebas?¿Facilita el test localizar el error?

```
```