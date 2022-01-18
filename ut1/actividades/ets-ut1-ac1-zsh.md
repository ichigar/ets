# ETS-UT1-AC1-zsh
## Caracterícas de zsh

El interprete de comandos es el programa que ejecuta los comandos que tecleamos en el terminal. Es una herramienta muy versatil y muy utilizada por administradores de sistemas y programadores.

La mayoría de distribuciones de Linux utiliza por defecto bash, pero existen múltiples alternativas para realizar esta función.

Dentro del mundo de los desarrolladores, una de las alternativas a **bash** más utilizadas es **zsh**. 

Algunas de las ventajas que ofrece **zsh** frente a **bash** son:
* Mejoras en autocompletado
* Autocorrección ortográfica
* Historial de directorios
* Altamente personalizable
* Soporte para extensiones
* Instalación de **plugins**

### 1. Instalación de zsh

> **Nota**: Todos los pasos siguientes los puedes hacer en la máquina virtual de Xubuntu

Para instalar **zsh** en Ubuntu ejecutamos:

```bash
$ sudo apt updtate
$ sudo apt install zsh
```

Para hacer que **zsh** sea el interprete de comandos que se utiliza por defecto al abrir un terminal en lugar de **bash** ejecutamos:

```bash
$ chsh -s /usr/bin/zsh
```

### 2. El framework para zsh oh-my-zsh

La configuración base de **zsh** es bástante básica, pero como hemos visto, **zsh** es extensible. Una de las extensiones más utilizada es **oh-my-zsh** que es un **framework** que extienden la funcionalidad base de **zsh** y facilitan la configuración del mismo. Entre otras cosas nos permite instalar **plugins** que extinenden la funcionalidad y **temas** que nos permiten personalizar la aparicia.

#### Instalación de oh-my-zsh

En el terminal ejecutamos:

```bash
sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
```

Nos preguntará si queremos establecer **zsh** como nuestro intérprete por defecto. Aceptamos.

```bash
Do you want to change your default shell to zsh? [Y/n] 
Changing the shell...
Password: 
Shell successfully changed to '/usr/bin/zsh'.

         __                                     __   
  ____  / /_     ____ ___  __  __   ____  _____/ /_  
 / __ \/ __ \   / __ `__ \/ / / /  /_  / / ___/ __ \ 
/ /_/ / / / /  / / / / / / /_/ /    / /_(__  ) / / / 
\____/_/ /_/  /_/ /_/ /_/\__, /    /___/____/_/ /_/  
                        /____/                       ....is now installed!


Before you scream Oh My Zsh! look over the `.zshrc` file to select plugins, themes, and options.

• Follow us on Twitter: https://twitter.com/ohmyzsh
• Join our Discord community: https://discord.gg/ohmyzsh
• Get stickers, t-shirts, coffee mugs and more: https://shop.planetargon.com/collections/oh-my-zsh
```

### 3. Utilizando funcionalidades  base de **zsh**

#### Autocompletado

Al introducir un comando si hacemos clic en **TAB** una vez se nos mostrarán las opciones de autocompletado disponible y si pulasmos **TAB** dos veces podremos navegar por las opciones con las flechas del teclado

![](https://cdn.linuxfordevices.com/wp-content/uploads/2020/11/Autocompletion-in-zsh.gif)

#### Ayuda con las opciones de los comandos

Los comandos de linux suelen ofrecer opciones que introducimos poniendo el caracter `-` antes de la opción. Si tecleamos un comando, a continuación `-` y el tabulador nos saldrán las opciones disponibles:

```bash
$ mkdir -
--context  -Z  -- set SELinux context                                        
--help         -- display help information                                   
--mode     -m  -- set permission mode                                        
--parents  -p  -- make parent directories as needed                          
--verbose  -v  -- print message for each created directory                   
--version      -- display version information
```

#### Autocorrección

Para errores típicos al teclear un comando zsh nos ofrece alternativas. Para habilitar esta funcionalidad tenemos que descomentar la línea `ENABLE_CORRECTION="true"` en el fichero `~/.zshrc` recuerda aplicar los cambios ejecutando:

```bash
$ source ~/.zshrc
```

A partir de este momento con algunos comandos se nos ofreceran alternativas:

```bash
$ mdkir test
zsh: correct 'mdkir' to 'mkdir' [nyae]? y
```


#### Historial de parámetros de comados

Si escribimos un comando usado anteriormente y pulsamos **flecha arriba** para ver el historial se nos mostrarán los parámetros usados recientemente para dicho comando

#### Predicción de ruta de archivos

Para ver esta características prueba a poner en el terminal:

```bash
$ cd /h/u/E
```
Y pulsa en el **tabulador**

#### Uso de globs para localizar archivos/carpetas

La técnica que permite especificar ficheros o directorios para usarlos en algún comando en función de alguna característica relacionada con el nombre o alguno de los atributos del mismo se llama **globing**
Todos los intérpretes de comandos implementan esta característica, pero **zsh** tiene herramientas avanzadas para usar globbing.

##### Por nombre y extensión

En **bash** (y en **zsh** también), si queremos acceder a todos los archivos que tienen una determinada extensión (en este caso para listarlo) lo podemos hacer con **bash** ejecutando. 

```bash
$ ls *.pdf
```
Con **zsh** podemos extender dicha funcionalidad y que nos haga la búsqueda en la carpeta actual y en todas las subcarpetas de la misma con:

```bash
$ ls **/*.pdf
```

O archivos que tengan un nombre determinado y cualquier extensión:

```bash
$ ls **/README.*
```

O que el nombre del archivo empiece, termine o contenga una determinada palabra/frase:

```bash
## Starts with READ y  tienen extensión
$ ls **/(READ)*.*
## Empiezan por READ y tienen o no extensión
$ ls **/(READ)*
## Ends With READ
$ ls **/*(READ).*
## Contains READ Anywhere
$ ls **/*(READ)*.*
```

También se puede especificar un número concreto de caracteres:

```bash
# All files that start with A
$ ls **/[A]*
# All files that start with A or a
$ ls **/[Aa]*
# All Files that contain the number
$ ls **/*[1]*
# archivos que terminan en vocal con extensión txt
$ ls **/*[aeiou].txt
```

> **Nota:** el comando **ls** si una carpeta cumple el criterio de búsqueda muestra no solo la carpeta, sino tambien todo su contenidor. Si solo queremos que muestre la carpeta usamos la opción **-d**. Así, por ejemplo, `ls -d */**[AEIOU]` mostraría todos los archivos y carpetas que termian por una vocal en mayúscula y no mostraría el contenido de las carpetas que cumplen con el criterio.

Si queremos limitar la búsqueda a archivos o carpetas

```bash
# Files Only
$ ls **/*(.)
# Folders Only
$ ls **/*(/)
```

También podemos excluir los caracteres a incluir:

```bash
# Files that don't start with A or a
$ ls **/[^Aa](.)
```

O aplicar un rango de caracteres

```bash
## Archivos que termianan en A, B, C, D, E o F
$ ls  **/*[A-F](.)
```
##### Por fecha de modificación/creación
Si queremos ver los archivos pdf modificados en el último mes:

```bash
$ ls **/*.pdf(.aM-1)
```
En general podemos consultar archivos por:
* fecha de modificación (m) o último acceso (a), respectivamente. 
* Podemos buscar por fecha exacta o por periodos de tiempo. Antes de (-) o después de (+) de la fecha elegida que se puede especificar en:
    * meses (M)
    * semanas (w)
    * días (d)
    * horas (h)
    * minutos (m)
    * segundos (s).

##### Por tamaño
Podemos ver los archivos de más de 10G que hay en la carpeta actual y subcarpetas con:

```bash
$ ls **/*(.Lg+10)
```

También podemos especificar el tamaño usando:
* **m** para Megabytes
* **k** para **Kilobytes**
* **g** para Gigabytes

Podemos combinar criterios:

```
$ ls -lh **/*.txt(.md-5.Lk-20)
```

El ejemplo anterio lista en formato largo por pantalla los archivos con extensión **txt** contenidos en la carpeta actual y cualuiera de las subcarpetas modificados hace menos de 5 días que tienen un tamaño menor de 20KBytes

### 4.  Temas. Personalizando la apariencia

Los temas disponibles de **oh-my-zsh** los tenemos en [https://github.com/ohmyzsh/ohmyzsh/wiki/Themes](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes)

Al instalar **oh-my-zsh** se descargan en nuestro equipo. Los podemos listar ejecutando:

```bash
$ ls -a ~/.oh-my-zsh/themes/
```

Una vez que hayamos elegido un tema, para cambiarlo editamos el fichero de configuración de zsh del usuarios que está en `~/.zshrc`

Si, por ejemplo, quisiéramos cambiar el definido actualmente por **agnoster**, editamos el fichero de configuración:

```bash
$ nano ~/.zshrc
```

Y en la línea `ZSH_THEME` cambiamos el contenido por el del tema seleccionado:

```bash
# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/home/usuario/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="agnoster"
```
Salimos con **CTRL + X** e **y**

Este tema utiliza una tipografía que no tenemos instalada y no se mostará correctamente si no las instalamos previamente:

```bash
$ sudo apt install fonts-powerline
```

Ya podemos aplicar el nuevo tema ejecutamos:

```bash
$ source ~/.zshrc
```

Si quieres probar otros temas de zsh, puedes previsualizarlos antes de aplicarlos en la [siguiente web](https://zshthem.es/browse-zsh-themes/)

### 5. Plugins de oh-my-zsh

Cómo se comentó, el framework **Oh my zsh** permite extender la funcionalidad base de **zsh** añadiendo de forma sencilla temas y plugins. 

La lista de plugins disponibles para **zsh** los tenemos en la web del proyecto en el [siguiente enlace](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins)

### 6. Actividad

En la [siguiente web](https://travis.media/top-10-oh-my-zsh-plugins-for-productive-developers/) tienes 10 plugins de **zsh** con funcionalidades que pueden resultar útiles.

1) Instala, **al menos, 5 plugins de zsh** y comprueba su funcionamiento. Pueden ser de la web anterior u otros.

> **Nota:** para los plugins que hacen uso del portapapeles desde el terminal debemos instalar **xclip** para que funcionen correctamente: `sudo apt update && sudo apt install xclip`

2) Configura zsh para tu usuario de forma que cada vez que habras un terminal utilice un tema a azar entre 5 que hayas seleccionado. 

3) A partir de la [web del proyecto zsh-systax-highlighting](zsh-syntax-highlighting) explica para que sirve dicho plugin y sigue los pasos para instalarlo con **oh-my-zsh**
 
4) Instala y configura zsh y oh-my-zsh en **WSL** de máquina virtual de Windows 10.



**Producto:**

Entrega un documento en **formato PDF** en el que se incluya un **tutorial** con la descripción de los pasos necesarios y capturas de pantalla que ilustren los pasos realizados 

> **Nota**: se considera tutorial a un documento que incluye pasos necesarios para desarrollar una tarea de tal forma que la persona que siga el tutorial consiga, sin necesidad de ningún otro recurso, el resultado final esperado

## Recursos

[Tips con zsh-sitepoint.com](https://www.sitepoint.com/zsh-tips-tricks/)

###### tags: `ets` `ut1` `zsh` `complementaria`