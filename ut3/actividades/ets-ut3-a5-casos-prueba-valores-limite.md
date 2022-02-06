# ETS-UT3-A5. Casos de prueba con valores límite

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
## Actividad 1

A una función se le pasan el número de horas trabajadas durante la semana (entero) y el precio por hora (real) y determina el salario de un trabajador

Entradas:

* **n_horas** entero entre 1 y 60.
* **p_hora** real entre 10 y 30

Resultado si las entradas son correctas:

* **P1**: n_horas * p_hora si `n_horas <= 40`
* **P2**: 40 * p_hora + (n_horas - 40) * 2 * p_hora si `40 < n_horas <= 48`
* **P3**: 40 * p_hora + 8 * 2 * p_hora + (n_horas - 48) * 3 * p_hora si `48 < n_horas < 60`

Mensajes de error:

* **ER1**: Número de horas incorrecto
* **ER2**: Precio de la hora incorrecto


Tenemos la siguiente función de Python, de la que no disponemos del código, que recibe los parámetros de entrada y debe generar la salida correspondiente:

```python
def salario_semanal(n_horas, p_hora):
    """
    Dada información de empleado devuelve su salario
    :param n_horas: int
    :param p_hora: float
    :return:float
    """
```

1. Tabla de clases de equivalencia usando valores límite

Se ha de tener en cuenta que las **salidas** de este supuesto son rangos de valores. Si tomamos como `p_hora = 10.0` para que los casos sean más sencillos, los valores límite de salida son estos 3 rangos:

* [10 - 400] para n_horas entre 10.0 y 40.0
* [420 - 560] para n_horas entre 41 y 48 horas
* [590 - 920] para n_horas entre 49 y 60

No se pueden generar valores de salida no válidos. La tabla quedaría:
 

| Condiciónes entrada/salida          | Clase de equivalencia | Valores válidos | COD    | Valores no válidas | COD      |
| ----------------------------------- | --------------------- | --------------- | ------ | ------------------ | -------- |
| Número de horas                     | Rango                 | 1, 60           | V1,V2  | 0, 61              | NV1, NV2 |
| p_hora                              | Rango                 | 10.0, 30.0      | V3,V4  | 9.99, 30.01        | NV3, NV4 |
| salario semanal (**p_hora = 10.0**) | Rango                 | 10, 400         | V5,V6  | no hay             |          |
| salario semanal (**p_hora = 10.0**) | Rango                 | 420, 560        | V7,V8  | no hay             |          |
| salario semanal (**p_hora = 10.0**) | Rango                 | 590, 920        | V9,V10 | no hay             |          |

2. Tabla con casos de prueba

Completar:

| Caso de prueba | Clases de equivalencia | n_horas | p_hora | Resultado esperado           |
| -------------- | ---------------------- | ------- | ------ | ---------------------------- |
| CP1            | V1, V3                 | 1       | 10.0   | 40.0                         |
| CP2            | V2, V4                 | 60      | 30.0   | 2760.0                       |
| CP3            | V3, V5                 | 1       | 10.0   | 10.0                         |
| CP4            | V3, V6                 | 40      | 10.0   | **400.0**                    |
| CP5            | V3, V7                 | 41      | 10.0   | **420.0**                    |
| CP6            | V3, V8                 | 47      | 10.0   | **560.0**                    |
| CP7            | V3, V9                 | 60      | 10.0   | **920.0**                    |
| CP8            | NV1, V3                | 0       | 10.0   | Número de horas incorrecto   |
| CP9            | NV2, V4                | 61      | 30.0   | Número de horas incorrecto   |
| CP10           | V1, NV3                | 1       | 9.99   | Precio de la hora incorrecto |
| CP11           | V2, NV4                | 60      | 30.01  | Precio de la hora incorrecto |


3. Tests unitarios de la función usando Doctest

Completar:

```python
def salario_semanal(n_horas, p_hora):
    """
    Dada información de empleado devuelve su salario
    :param n_horas: int
    :param p_hora: float
    :return:float
    """
```

4. Ejecutar Tests unitarios

El siguiente código para la función `salario_semanal()` contiene 1 o más errores. Añade a la misma los tests unitarios obtenidos en el apartados anterior, ejecútalos. 

```python
def salario_semanal(n_horas, p_hora):
    """
    Dada información de empleado devuelve su salario
    :param n_horas: int
    :param p_hora: float
    :return:float
    """
    MIN_HORAS = 0
    MAX_HORAS = 60
    P_MIN_HORA = 10.0
    P_MAX_HORA = 30.0
    PAGA_DOBLE_MIN = 40
    PAGA_TRIPLE_MIN = 48
    
    if n_horas < MIN_HORAS or n_horas >= MAX_HORAS:
        return Número de horas incorrecto
    if p_hora < P_MIN_HORA or p_hora > P_MAX_HORA:
        return Precio de la hora incorrecto
    if n_horas <= 41:
        return n_horas * p_hora
    if n_horas <= 48:
        return 40 * p_hora + (n_horas - 40) * 2 * p_hora
    return 40 * p_hora + 8 * 2 * p_hora + (n_horas - 48) * 3 * p_hora
    
```
A partir de los tests que no pasa intenta depurar el código y corregir el error o errores que pueda contener:

Inserta a continuación las líneas con los errores ya corregidos:

```python

```

¿Si no se hubiesen usado valores límite para generar los casos de prueba se hubieran detectado el/los error/es?¿Explica el motivo?

> **Respuesta**: 

## Actividad 2

Un programa calcula la prima anual de un empleado a partir de los datos siguientes datos de entrasa:
* **Empleado**: número de 3 dígitos entre 100 y 999 . Campo de entrada numérico.
* **Nombre**: cadena de texto de entre 5 y 10 caracteres de longitud. Campo de entrada de texto
* **Meses antiguedad**: entero positivo entre 0 y 99. Campo de entrada numérico.
* **Pertenece a la directiva**: Valor lógico . Lista desplegable con los valores Si, No, Elige tipo empleado.

Si la entrada es correcta la prima se calcula de la siguiente forma: 

* **P1** = 500 si el empleado no es de la directiva y lleva menos de 12 meses en la empresa
* **P2** = 700 si el empleado no es de la directiva y lleva en mas de 12 meses en la empresa
* **P3** = 1000 si el empleado es de la directiva y lleva menos de 12 meses en la empresa
* **P4** = 1200 si el empleado es de la directiva y lleva más de 12 meses en la empresa

Para las entradas incorrectas los mensajes de error son:

* **ER1** si el número de empleado no es correcto
* **ER2** si el nombre del empleado es incorrecto
* **ER3** si la antiguedad es incorrecta
* **ER4** si no elige el tipo de empleado.

Tenemos la siguiente función de Python, de la que no disponemos del código, que recibe los parámetros de entrada y debe generar la salida correspondiente:

```python
def prima_empleado(num_empleado, nom_empleado, antiguedad, directiva):
    """
    Dada información de empleado devuelve su salario
    :param num_empleado: int
    :param nom_empleado: str
    :param antiguedad: int
    :param directiva: str
    :return int
    """
```

Se pide obtener:

1. Tabla de clases de equivalencia usando valores límite.

Completar:

| Condición de entrada | Clase de equivalencia | Valores límite válidos | COD | Valores límite no válidos | COD |
| -------------------- | --------------------- | -------------- | --- | ----------------- | --- |
|                      |                       |                |     |                   |     |

2. Tabla con casos de prueba

Completar:

| Caso de prueba | Clases de equivalencia | num_e | nom_e | ant | directiva | Resultado esperado |
| -------------- | ---------------------- | ----- | ----- | --- | --------- | ------------------ |
|                |                        |       |       |     |           |                    |
3. Tests unitarios de la función usando Doctest

Añadir a:

```python
def prima_empleado(num_empleado, nom_empleado, antiguedad, directiva):
    """
    Dada información de empleado devuelve su salario
    :param num_empleado: int
    :param nom_empleado: str
    :param antiguedad: int
    :param directiva: str
    :return int
    """
```


###### tags: `ets` `ut3` `actividad` `partición` `valores` `límite` `clases` `equivalencia`