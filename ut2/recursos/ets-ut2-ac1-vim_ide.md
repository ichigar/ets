# ETS - UT1-AC2 . VIM IDE

## Introducción. Vim como IDE para Python

![](https://files.realpython.com/media/vim-ide.90be624b30bf.png)

Vim es un editor de texto ligero que normalmente se ejecuta en el terminal y que se puede personalizar y configurar de manera muy flexible.

Vim consume muy pocos recursos y se ejecuta de forma muy rápida. Al ser una herramienta que se ejecuta en el terminal no vamos a poder utilizar el ratón en el mismo, su potencia se basa en el uso de atajos de teclado. Por tanto, tiene una curva de aprendizaje más alta que los IDEs tradicionales pero una vez que adquirimos soltura en su utilización el desarrollo en el mismo es bastante productivo. 

Vim no es para todo el mundo, pese a ello hay muchísimos desarrolladores que programan con él y que no lo cambian por ninguno de los IDEs visuales existentes.

El objetivo de esta práctica es realizar una breve introducción al mismo y realizar una configuración básica que nos permita desarrollar en Python utilizando vim.

## Práctica

### Instalación

Se puede instalar en Linux, OSX y Windows. Cómo no tenemos permisos de administrador en nuestro equipo realizaremos la práctica en la máquina virtual de Xubuntu. Para la instalción abrimos un terminal y ejecutamos:

```bash
$ sudo apt update
$ sudo apt install vim git
```

Podemos comprobar que se ha ejecutado ejecutando:

```bash
$ vim --version
```

### Primeros pasos

Usar vim es complejo al principio. Para aprender los conceptos básicos podemos utilizar su **tutor** integrado; un asistente que nos guiará en el aprendizaje de uso de vim. Nos enseñará desde lo  más básico que es moverse entre el texto, comandos para  copiar, pegar,  buscar y reemplazar, y muchas de las tareas típicas que nos permite  un editor de textos. 

Para iniciar el tutor ejecutamos en el terminal:

```bash
$ vimtutor es
```

### Vim como IDE. Funcionalidades incluidas

#### Dividiendo la pantalla en pestañas horizontales y verticales

El fichero en el que se define la configuración de vim para el usuario está en la carpeta de inicio del usuario (~) en un fichero de nombre `.vimrc` vamos a empezar a personalizar el comportamiento de **vim**

Abrimos el fichero ejecutando:

```bash
vim ~/.vimrc
```

Pegamos en el mismo el siguiente texto. Para ello, primero lo copiamos en el portapapeles y luego pulsando `<shift>+<ctrl>+v` lo pegamos.

```
set splitbelow
set splitright

"split navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>
```

Una vez pegado guardamos y salimos con `<ESC>` y luego tecleamos `:wq`:

Las líneas que acabamos de añadir nos permiten definir **como se va a dividir** el terminal si abrimos más de un fichero para editarlo y crear combinaciones de teclas que nos permitirán movernos de un **panel** a otro con `<ctrl>+ ` las teclas de movimiento `h`, `j`, `k` y `l`

#### Comprobando

Empezamos creando una carpeta y en la misma realizaremos algunas pruebas.

```bash
$ mkdir temp
$ cd temp
$ vim test.py
```

Pulsamos **i** para pasar al modo inserción y escribimos un código de prueba.

```python
print("Hola Mundo")
```

Al crear el archivo con la extensión `.py` automáticamente **vim** resalta el código.

Para guardar  pulsando `<ESC>` y luego tecleamos:

```
:w
```

Para abrir un archivo dividiendo horizontalmente el panel actual lo hacemos con `:sp test2.py`:

Si quisieramos dividir verticalmente el panel actual lo hacemos con `:vs test3.py`

Podemos movernos de una división a otra con `<ctrl> +` las teclas de movimiento `h`, `j`, `k` y `l`

### Buffers

Muchos programadores prefieren tener el terminal organizado en varios paneles e ir cargando en cada una de ellos alguno de los ficheros (buffers) que actualmente están abiertos.

Para movernos al buffer siguiente o al anterior al actual, podemos usar, respectivamente: `:bn` y `:bp`

 Para ver los buffers que tenemos abiertos y su nombre y número asociado ejecutamos:

```bash
:ls
  1      "test.py"                      línea 1
  2 #a   "test2.py"                     línea 1
  3 %a   "test3.py"                     línea 1

```

Para cargar en la pestaña actual uno de los buffers tecleamos `:b` y el **nombre** o el **número** del **buffer**. Por ejempolo `:b2` cargará el archivo `test2.py` en la pestaña actual.

#### Abriendo un terminal

Con `:ter` se nos abrirá un terminal en una dividión horizontal del la ventana actual. Para cerrarlo ejecutamos en el mismo

```bash
$ exit
```

#### Mostrar/ocultar números de línea

Para que lás líneas se muestren numeradas `:set nu` para desactivarlo `:set nonu`

### Extendiendo VIM. Uso de plugins

Muchas de las cosas que necesitamos para desarrollar vienen incluidas en la instalación base de vim. Además dispone de gran cantidad de **extensiones** que hacen que se comporte como un IDE moderno. Lo primero que necesitamos es un buen gestor de extensiones (una extensión que nos permite gestionar las extensiones)

#### Vundle

Es uno de los gestores de extensiones existentes para vim que facilita la instalación y actualización de extensiones. Para instalarlo ejecutamos en el terminal:

```bash
$ git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

Abrimos el fichero de configuración de vim para el usaurio ejecutando:

```bash
vim ~/.vimrc
```

Pasamos a modo **INSERT** pulsando la tecla **i** nos movemos al final del mismo mismo y pegamos el siguiente texto pulsando `<ctrl>+<shift>+v` 

```
set nocompatible              " required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" add all your plugins here (note older versions of Vundle
" used Bundle instead of Plugin)

" ...

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

```
Guardamos y salimos tal y como vimos en **vimtutor** con `<ESC>` y luego `:wq`:

Para aplicar volvemos a abrir el fichero de configuración:

```bash
$ vim ~/.vimrc
```

Indicamos a **vim** que instale la extensión añadida pulsado `<ESC>` y luego tecleamos `:PluginInstall`

Salimos del fichero de configuración pulsando `<ESC>` y luego tecleamos `:q!`

#### Resaltado de sintaxis

Para mejorar la apariencia del código lo podemos hacer añadiendo al final del fichero **vimrc** las líneas:

```
let python_highlight_all=1
syntax on
```

Podemos hacer que vim compruebe la sintáxis del archivo python que estamos editando cada vez que guardemos usando la extensión **syntastic**. Si además queremos que se comprueben las reglas de estilo **PEP8** lo podemos hacer con el plugin **vim-flake8** 

Primero instalamos las **dependencias** del plugin. En un terminal ejecutamos_

```bash
$ sudo apt update
$ sudo apt install flake8 pylint
```

Luego añadimos debajo de la línea `Plugin 'gmarik/Vundle.vim' ` del fichero `~/.vimrc` las líneas:

```
Plugin 'vim-syntastic/syntastic'
Plugin 'nvie/vim-flake8'
```

Por último añadimos al final del fichero la configuración recomendada del Plugin. Insertamos:

```
" syntastic                                                    "" Recommended settings
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
"" Display checker-name for that error-message
let g:syntastic_aggregate_errors = 1
```

Guardamos y salimos `:wq` Volvemos a editar el fichero de configuración:

```bash
vim ~/.vimrc
```

E instalamos los plugins con `:PluginInstall` 

Para comprobar abrimos o creamos con **vim** un fichero de Python. Al guardar con `:w` se nos mostrarán los errores de sintaxis en un **buffer** infoerior.

### Actividad

Investiga funcionalidades de vim y plugins de **vim** que te resulten interesantes. Inserta a continuación la utilidad y las instrucciones de instalación/configuración para dichas funcionalidades o plugins y ejemplos de cómo usarlos. Los **plugins** deberías instalarlos usando **vundle**

Posibles funcionalidades:

* Cambiar codificación de caracteres a **utf-8**
* Cambiar el tamaño de los paneles divididos
* Habilitar plegado de código (code-folding)

Posibles plugins:

* Cambiar apariencia/esquema de colores
* Mostrar arbol de archivos y directorios (Nerdtree)
* Plegado de código (code-folding)
* Autocompletado de código(jedi-vim)
* Ejecutar código desde vim

> Insertar aquí pasos realizadors

### Entrega

Convierte a PDF este documento. Aségurate de que incluye tutorial de funcionanlidades y plugins añadidos.

Entrega el documento en el CAMPUS

## Recursos

* [Vim cheatsheet - rtorr.com](https://vim.rtorr.com/lang/es_es)
* [How to Make Vim a Python IDE - Best IDE for Python - dev.to](https://dev.to/shahinsha/how-to-make-vim-a-python-ide-best-ide-for-python-23e1)
* [VIM and Python – A Match Made in Heaven - RealPython](https://realpython.com/vim-and-python-a-match-made-in-heaven/)
* [Vim as a Python IDE - rapphil.github.io](https://rapphil.github.io/vim-python-ide/)

###### tags: `ets` `ut2` `actividad` `vim` `ide`