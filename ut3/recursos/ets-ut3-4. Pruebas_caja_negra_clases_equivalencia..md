# ETS-UT3-A4. Casos de prueba con clases de equivalencia

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

1. Tabla de clases de equivalencia

Completar:

| Condición de entrada | Clase de equivalencia | Clases Válidas | COD | Clases no válidas | COD |
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

## Actividad 2

En un formulario se leen dos campos de texto con la nueva contraseña de un usuario. Nuestro programa debe validar la nueva contraseña.

Entradas:

* **passwd1** cadena de texo. 
* **passwd2** cadena de texto

Resultado si las entradas son correctas:

* **P1**: `True` en caso de que la contraseña sea válida y las dos contraseñas coinciden

Mensajes de error:

* **ER1**: Las contraseñas no coinciden
* **ER2**: La longitud de la contraseña es de menos de 10 caracteres
* **ER3**: La contraseña no contiene caracteres especiales
* **ER4**: La contraseña no contiene caracter en mayúscula

Tenemos la siguiente función de Python, de la que no disponemos del código, que recibe los parámetros de entrada y debe generar la salida correspondiente:

```python
def new_passwd(passwd1, passwd2):
    """
    Dadas dos contraseñas de registro comprueba validez
    :param passwd1: str
    :param passwd2: str
    :return:str
    """
```

Se pide obtener:

1. Tabla de clases de equivalencia

Completar:

| Condición de entrada | Clase de equivalencia | Clases Válidas | COD | Clases no válidas | COD |
| -------------------- | --------------------- | -------------- | --- | ----------------- | --- |
|                      |                       |                |     |                   |     |

2. Tabla con casos de prueba

Completar:

| Caso de prueba | Clases de equivalencia | passwd1 | passwd2 | Resultado esperado |
| -------------- | ---------------------- | ------- | ------- | ------------------ |
|                |                        |         |         |                    |

3. Tests unitarios de la función usando Doctest

Añadir a:

```python
def new_passwd(passwd1, passwd2):
    """
    Dada información de empleado devuelve su salario
    :param passwd1: str
    :param passwd2: str
    :return:str
    """
```
