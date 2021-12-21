# UT2-A4. VSCode con WSL en Windows 
## Terminal de Windows

Windows Terminal es una aplicación de Windows que permite acceder a una interfaz de usuario en modo texto enriquecido (con soporte de emojis) y que incluso se beneficia del renderizado de texto vía la GPU.

Esta nueva terminal de Windows unifica a las tres consolas existentes hasta ahora: PowerShell, Cmd y Windows Subsystem for Linux (WSL).

Ofrece soporte para atajos de teclado, pestañas, ventanas podemos separar extensiones y plantillas y temas personalizados.

### Instalación de Terminal de Windows

Accedemos a la tienda de Linux y buscamos **Windows Terminal**

![](https://www.mjlivesey.co.uk/img/getterminal.png)

De forma alternativa podemos utilizar **ConEmu** que podemos descargar en [https://conemu.github.io/](https://conemu.github.io/)

## WSL

Windows Subsystem for Linux (WSL) es una característica opcional de Windows 10 que nos permite instalar un Kernel Linux directamente sobre el sistema operativo de Microsoft. 

### Ventajas de WSL

La mayoría de aplicaciones que se desarrolla para la web se ejecutan en servidores Linux, WSL permite disponer desde Windows de un entorno de desarrollo similar al entorno de producción en el que se van a ejecutar dichas apliaciones.

WSL permite a los administradores de sistemas, y a los programadores, usar todas las herramientas y todos los servicios de Linux directamente desde Windows sin tener que usar máquinas virtuales u otro tipo de infraestructuras complejas.

Frente al uso de Máquinas virtuales, las venjas que ofrece son:
* Tiempos de carga bajos. Se puede cargar Linus en menos de 1 segundo.
* Bajo consumo de recursos.
* Tenemos acceso directo al sistema de archivos de Windows y podemos interactuar directamente con él.

### Instalación de WSL

Podemos activarlo desde la herramienta de **Activar o desactivar las características de Windows**

![](https://www.softzone.es/app/uploads-softzone.es/2020/07/Abrir-caracter%C3%ADsticas-de-Windows-10.jpg)

O desde Powershell en modo administrador ejecutando:

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```
Después de ejecutarlo se nos pedirá reiniciar el equipo.

Una vez instalado, si abrimos **CMD** y ejecutamos 

```
wsl
```

Se nos informára de que **wsl** está habilitado y no tenemos todavía instalada ninguna distribución de Linux

![](https://code.visualstudio.com/assets/docs/remote/wsl-tutorial/wsl-check.png)

### Descargar Linux en Windows 10

Para instalar una distribución de Linux accedemos a la **Tienda de Windows** y buscamos **Ubuntu**. Seleccionamos **Ubun tu 20.04** y lo instalamos.

Cuando termine instalación abrimos 

Nos solicitará un nuevo usuario y contraseña. Podemos poner `usuario` y contraseña `daw1234`
Ubuntu y actualizamos ejecutando:

```bash
$ sudo apt update
$ sudo apt upgrade
```

### Instalación de Visual Studio Code

Descargamos en https://code.visualstudio.com/

### Desarrollo en Python

Para instalar Python abrimos un terminal WSL en Ubuntu y ejecutamos:

```bash
$ sudo apt update
$ sudo apt install python3 python3-pip python3-venv
```

Verificamos que se ha instalado ejecutando:

```bash
$ python3 --version
Python 3.8.10
```

### Configuración de VSCode para usar WSL

Instalamos la extensión **Remote - WSL** que permite a VSCode trabajar dendor del Windows Subsystem for Linux

![](https://code.visualstudio.com/assets/docs/remote/wsl-tutorial/remote-wsl-extension.png)

Una vez instalado veremos un nuevo icono  en la parte izquierda de la barra de estado de VScode

![](https://code.visualstudio.com/assets/docs/remote/wsl-tutorial/remote-status-bar.png)

Haciendo clic en el mismo mostrará comandos asociados a WSL:

![](https://code.visualstudio.com/assets/docs/remote/wsl-tutorial/remote-wsl-commands.png)

Como Python está instalado en la distribución de Ubuntu asociada a **WSL** para poder ejecutar y depurar archivos de Ubuntu desde Windows accedemos a un terminal de WSL usando **ConEmu** o **Windows Terminal**

Creamos una carpeta en la que vamos a crear nuestra aplicación de prueba y accedemos a la misma:

```bash
$ mkdir helloWorld
$ cd helloWorld
```

Y desde la misma ejecutamos VSCode ejecutando `code .`. El "." equivale a la carpeta actual en `bash`

![](https://code.visualstudio.com/assets/docs/remote/wsl-tutorial/launch-code.png)

Se descargará e instalará un **servidor de code** en Linux con el que se comunicará **VScode**  a la hora de depurar y ejecutar nuestros programas.

Creamos un nuevo archivo `hello.py` en la carpeta que acabamos de crear:

![](https://code.visualstudio.com/assets/docs/remote/wsl-tutorial/show-linux-path.png)

**VScode** nos preguntará si queremos instalar la extensión que da soporte para Python (si no la tenemos ya instalada).

A partir de ese momento VSCode comprobará la sintáxis del programa que escribamos mostrándonos errores, aplicará colores a las sentencias y elementos del programa, nos permitirá depurar y ejecutar el programa. En conclusión, dispondremos de las mismas herramientas de desarrollo que en nuestro sistema operativo Ubuntu de clase.

![](https://code.visualstudio.com/assets/docs/remote/wsl-tutorial/debug-view.png)

Para cerrar la conexión de VSCode con WSL y trabajar de modo local, accedemos a **Archivo > Cerrar conexión remota**

## Recursos
* [Activar WSL en Windows-softzone.es](https://www.softzone.es/windows-10/como-se-hace/subsistema-windows-linux/)
* [Desarrollo en Python usando WSL2-mjlivesey.co.uk](https://www.mjlivesey.co.uk/2020/08/02/vs-code-wsl2-python.html)
* [Desarrollo remoto en WSL con VScode](https://code.visualstudio.com/docs/remote/wsl-tutorial)
###### tags: `ets` `ut2` `windows` `wsl`