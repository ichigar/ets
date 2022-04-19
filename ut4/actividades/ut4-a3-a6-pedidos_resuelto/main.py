from pedido import *
from producto import *
from pago import *
from cliente import *

# Creamos un cliente ficticio
c1 = Cliente("41222333a", "Juan", "Perez", "Calle Falsa 123", "666345678", "jperez@example.com")

# Creamos productos para nuestro restaurante 
p1 = Producto("Pizza", 10, 0.2, "Pizza de jamón y queso")
p2 = Producto("Hamburguesa", 15, 0.11, "Hamburguesa con queso")

# Inicializamos un pedido
pedido1 = Pedido("2022-04-01 20:06:30", c1)

# Detalles del pedido
pedido1_d1 = DetallePedido(2, p1) # 2 pizzas de 10 euros cada una
pedido1_d2 = DetallePedido(1, p2) # 1 hamburguesa de 15 euros

# Añadimos los detalles al pedido
pedido1.add_detalle(pedido1_d1)
pedido1.add_detalle(pedido1_d2)

# Mostramos detalles de precios del pedido
print(pedido1.calc_sub_total())
print(pedido1.calc_igic())
print(pedido1.calc_total())

# Mostramos el estado del pago
print(pedido1.get_estado_pago())

# preparamos tarjeta para realizar el pago
t_c1_p1 = Tarjeta(38, "1234567890123456", "12/20", "123")
# realizamos el pago
pedido1.realizar_pago(t_c1_p1)
# Mostramos el estado del pago
print(pedido1.get_estado_pago())