# Configurar Workspace en VisualCode

Cuando como programadores iniciamos in nuevo proyecto (en cualquier lenguaje de programación) tenemos que configurar un entorno para poder ejecutar nuestro proyecto.

El entorno incluye cosas como un editor, paquetes con librerías, las carpetas con los archivos de nuestro proyecto, extensiones como un depuradorm, un formateador y un linter específico del lenguaje de programación, etc.

Los pasos genéricos para configurar un entorno para cualquier lenguaje suele incluir los siguientes pasos:

1. Instalar el compilador/interprete del lenguaje de programación
2. Instalar un gestor de paquetes
3. Configurar el entorno virtual de trabajo
4. Configurar workspace en IDe

Este tutorial está hecho para crear el workspace en Ubuntu 20.04. Para cualquier otro sistema operativo los pasos son los mismos, cambia la forma específica de llevarlos a cabo.

## 1. Instalación del compilador/intérprete del lenguaje de programación

En las distribuciones de Linux Python viene preinstalado con el sistema operativo, para descargar Python para otros sistemas operativos lo podemos hacer en [el siguiente enlace](https://www.python.org/downloads/)

Para comprobar la versión de Python que tenemos instalada ejecutamos en el terminal

```bash
$ python --version
Python 2.7.18
$ python3 --version
Python 3.8.10
```

## 2. Instalación de un gestor de paquetes

El gestor de paquetes de python más popular es **pip**. Para instalarlo tenemos instrucciones para hacerlo en [este enlace](https://pip.pypa.io/en/stable/installation/). En Ubuntu una de las formas de hacerlos es utilizando el gestor de paquetes del sistema **apt** ejecutando:

```bash
$ sudo apt update
$ sudo apt install python3-pip
```

Podemos comprobar que está instalado ejecutando:

```bash
$ pip --version
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
```

## Configurando un entorno virtual

Las aplicaciones que desarrollemos en Python en muchas ocasiones utilizarán paquetes y módulos que no forman parte de la librería estándar. Las aplicaciones usarán en ocasiones una versión específica de una librería. Se puede, por tanto, dar el caso de que tengamos múltiples aplicaciones con diferentes versiones de python y con diferentes versiones de los módulos requeridos para la aplicación. Tener solo una única versión global puede no ser suficiente para nuestras necesitades.

La solución a este problema es crear un entorno virtual, una carpeta que contenga los archivos de Python para una determinada versión además de los paquetes requeridos para nuestra aplicación.

Hay muchas herramientas de Python disponibles para crear un entorno virtual de Python. Las más conocidas son **venv**, **virtualenv** y **pyenv** usaremos **venv** en este tutorial. Para instalarlo en Ubuntu ejecutamos:

```bash
$ sudo apt install python3.8-venv
```

Todo lo que hemos instalado hasta ahora es para disponer globalmente de las herramientas necesarias. Vamos ahora a preparar un **entorno virtual** para el desarrollo de nuestro proyecto. Empezamos creando la carpeta que contendrá nuestro proyecto, en este ejemplo será `python-demo` 

```bash
$ mkdir proyectos
$ cd proyectos
$ mkdir python-demo

```

Para crear un entorno virtual para nuestro proyecto ejecutamos:

```bash
$ python3 -m venv python-demo
```

Una vez que hemos creado el entorno virtual tenemos que asegurarnos de que instalamos el resto de paquetes de python para nuestro proyecto en nuestro entorno virtual. Para hacerlo activamos el entorno virtual con el siguiente comandos:

```bash
$ source python-demo/bin/activate
```
El prompt del sistema cambiará a :
```bash
(python-demo) $ 
```
Si quisieramos desactivar el entorno virtual ejecutaríamos:

```bash
(python-demo) $ deactivate
$
```

## 4. Configurando workspace en el IDE

Para instalar Vscode en Ubuntu ejecutamos:

```bash
$ sudo snap install vscode
```





Una vez abierto pasamos a crear el **workspace**. Un workspace es un proyecto que contiene uno o más directorio principales (root folders), incluyendo toda la configuración de visual code para ese proyecto. La configuración incluye configuración de Visual Code, extensiones y  configuración de depuración.

El tener un workspace nos permite copiarlo de un ordenador a otro sin perder la configuración y nos permite compartirlo con otras personas.

### 4.1. Creando el workspace

1. Abre Visual Code. Si hay un directorio o workspace abierto, ciérralos.
    a) Si tienes un directorio o workspace abierto,  en el menu “file” aparece al final la opción activa “close folder” o “close workspace”.

   ![create_workspace](imgs/create_workspace.png)

2. Añadimos el directorio de trabajo a un nuevo workspace. Selecciona   el   menú   “file”,   opción   “add   folder   to workspace...”. Selecciona el directorio de trabajo **python-demo**.

3. Guarda el workspace, seleccionando en el menú “file”, la opción “save workspace”. Selecciona el mismo directorio de trabajo para guardarlo.
    a) En el directorio de trabajo se ha creado un archivo con extensión   “.code-workspace”.   En   este   archivo   se guardará la configuración de visual code para nuestro proyecto.

Cuando quieras abrir el workspace puedes pulsar directamente sobre  el archivo   “.code-workspace”   o   desde   VisualCode seleccionar el menú “file”, opción “open workspace...”

## 4.2. Seleccionando el interprete del entorno virtual

Instalamos en Vscode la extensión de Python para VS Code. Accedemos a extensiones, ponemos python en el buscador e instalamos la extensión de Microsoft para Python

![python_extension](imgs/python_extension.png)

Al finalizar la instalación nos pedirá que instalemos dependencias. Abrimos el terminal y ejecutamos:

```bash
$ sudo apt-get install python3 python3-venv python3-pip
```

Seleccionamos interprete de Python a utilizar. El incluido por venv en el proyecto. **<SHIFT> + <CTRL> + P** escribimos **Python:seleccionar interprete** y lo seleccionamos a nivel de workspace:

![select_interpreter_00](/home/ivan/mega/clases/github/ets/ut2/recursos/imgs/select_interpreter_00.png)



Para cualquier lenguaje de programación hay dos herramientas que nuestro IDE debería incluir: un **linter** y una herramienta para dar formato de forma automática al código. Vscode nos permite instalar como extensiones multiples **linters** y **formateadores**

## Recursos

* https://dev.to/idrisrampurawala/setting-up-python-workspace-in-visual-studio-code-vscode-149p
* https://mitelman.engineering/blog/python-best-practice/automating-python-best-practices-for-a-new-project/