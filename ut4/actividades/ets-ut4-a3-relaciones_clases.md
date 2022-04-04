# ETS-UT4-A3-Relaciones entre clases
## Conceptos
### Relaciones

Resumen con características de los distintos tipos de relaciones:

#### Asociación

![asociación simple](https://www.cybermedian.com/wp-content/uploads/2022/02/04-simple-association.png)

* Expresa un vínculo **estructural** entre dos clases de **pares**. 
    * Hay una asociación entre Class1 y Class2 
* Se representa mediante una **línea sólida** que conecta dos clases.
* Existen también las **asociaciones reflexivas** (involutivas)
    * Una clase se puede asociar **consigo misma**
    * Se suele dar cuando una clase puede desempeñar diversos roles o papeles.
    * Una persona por ejemplo puede ser Profesor o alumno, para representar estas asociaciones se realiza de la siguiente manera.

![](https://i.imgur.com/oBDgFHc.png)

* Clases asociación
    * En una asociación entre dos clases la propia asociación puede tener **propiedades**.
    * En este caso se usa una **clase asociación** que contiene atributos y métodos que no pertenecen a las clases que relaciona.
    * Se representa con un símbolo de clase unido por línea discontínua a una asociación.
    * Por ejemplo, entre un persona y un departamento puede haber una clase asoción **contrato*+ con atributos como el **cargo** y la **fecha de contratación**. Dichos atributos no pertenecen ni a a la persona ni al departamento:

![](https://i.imgur.com/QrdzZHa.png)

#### **Agregación** 

![Agregación](https://www.cybermedian.com/wp-content/uploads/2022/02/05-aggregation.png)

Características:

* Es un tipo especial de asociación. 
* Expresa una relación de "**parte de**" o "**tiene una**"
    * Class2 es **parte de** Class1 o
    * Class1 **tiene una** Class2
* Muchas instancias (indicadas por *) de Class2 se pueden asociar con Class1. 
* Los objetos de Class1 y Class2 tienen vidas separadas. 
* Se representa con una línea sólida con un rombo sin relleno en el extremo de la asociación conectado a la clase de **compuesto** 

#### Composición

![Composición](https://www.cybermedian.com/wp-content/uploads/2022/02/06-composition.png)


Características:

* También es un tipo especial de asociación.
* Expresa una relación **pertenece a**, pero es más fuerte que en el caso anterior: las partes se destruyen (dejan de tener sentido) cuando se destruye el todo. 
    * Los objetos de Class2 viven y mueren con Class1. 
    * Class2 no puede valerse por sí mismo. 
* Se representa mediante una línea sólida con un rombo lleno en la asociación conectada a la clase de compuesto


#### Herencia (o generalización)

![Herencia (o generalización)](https://www.cybermedian.com/wp-content/uploads/2022/02/08-inheritance-in-class-diagram.png)

* Expresa una relación "**es-un**". 
* Si la clase es abstracta su nombre se muestra en cursiva. 
    * SubClass1 y SubClass2 son **especializaciones** de Super Class. 
* Se representan con una **línea continua** con una **punta de flecha hueca** que apunta desde la clase secundaria a la principal 

#### Dependencia 

![Dependencia](https://www.cybermedian.com/wp-content/uploads/2022/02/07-dependency.png)

Características:

* Se utiliza si la relación entre dos clases es tal que si los cambios en la definición de una pueden causar cambios en la otra (pero no al revés).
    * Clase1 depende de Clase2 
* Una relación de dependencia expresa una relación de **uso**. 
    * Un cambio en una clase en particular puede afectar a otras clases que la **usan**
    * Se emplea esta relación cuando es necesario indicar que una cosa usa otra. 
* Se representa mediante una línea discontinua con una flecha abierta

| 

## Actividad

Dadas las siguientes clases:
* Edita la imagen y, añade a las mismas las líneas que representan la relación entre las mismas. Inserta debajo la frase que expresa el tipo de asociación.
* En caso de haber multiplicidad en las relaciones inserta el valor de las mismas en los extremos de la relación.

### A1

En una aplicación genérica se pueden pagar utilizando una tarjeta de crédito, en efectivo o mediante transferencia bancaria.

![](https://i.imgur.com/1JwkSIV.png)


### A2

* Parking con capacidad para 10 vehículos
* Los vehículos tienen un propietario

![](https://i.imgur.com/U5rNFUS.png)

### A3

* En una empresa hay varios trabajadores
* Cada trabajador tiene un contrato con la empresa en el que se especifican, entre otras cosas su salario.
* Complementario: Uno de los trabajadores es el director de la empresa.

![](https://i.imgur.com/gHxDsKV.png)

### A4

* En un colegio hay alumnos y profesores. 
* Tanto alumnos como profesores tienen datos personales
* Entre los datos personales de alumnos y profesores está su dirección postal
* Los alumnos están matriculados en un Grupo
* Uno de los alumnos es el delegado del grupo
* Los profesores pueden dar clase a 1 o varios grupos 

![](https://i.imgur.com/8IRpMQt.png)

### A5

* Una gasolinera tiene 4 surtidores de combustible.
* A la gasolinera acceden vehículos que repostan combustible en uno de los surtidores
* Los vehículos usan un determinado tipo de combustible (Gasolina, Gasoil,...)

![](https://i.imgur.com/xPEjJTY.png)

### A6

* Una tienda vende diferentes tipos de productos de forma online y presencial.
* Los clientes para poder comprar deben estar registrados y se guarda los datos de los mismos.
* Los clientes pueden hacer pedidos. Del pedido se guarda la fecha y el estado en el que está (en el carrito, pagado, enviado, ...)
* Un pedido tiene varios "**Detalles**". Cada uno de ellos está formado por un producto y por la cantidad de los mismos incluidos en el pedido.
* De cada producto se guarda, entre otras, una descripción, el precio unitario y cuánto pesa.
* Para poder enviar un pedido el pago del mismo debe haber sido confirmado.
* Como médios de pago la empresa acepta efectivo y tarjeta

![](https://i.imgur.com/a2RxhsJ.png)



### A7

* Una empresa tiene contratados empleados y vende a clientes.
* Clientes y empleados comparten el poseer datos personales.
* El director **es un** empleado que dirige a uno o varios empleados

![](https://i.imgur.com/V7IOADJ.png)



## Recursos/referencias

* [cybermedian.com - vpvera : guía de diagramas de clase UML](https://www.cybermedian.com/es/a-comprehensive-guide-to-uml-class-diagram/)
###### tags: `ets` `ut4` `uml` `relaciones` `clase`