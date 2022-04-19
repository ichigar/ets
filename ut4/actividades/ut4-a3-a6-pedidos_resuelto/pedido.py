class DetallePedido:
    def __init__(self, cantidad, producto):
        self.__cantidad = cantidad
        self.__producto = producto

    
    def calc_subtotal(self):
        return self.__cantidad * self.__producto.get_precio()
    
class Pedido:
    IGIG = 0.07
    
    def __init__(self, fecha, cliente):
        self.__fecha = fecha
        self.__cliente = cliente
        self.__detalles = []
        self.__pagado = False
    
    def add_detalle(self, detalle):
        self.__detalles.append(detalle)
        
    def calc_sub_total(self):
        sub_total = 0
        for detalle in self.__detalles:
            sub_total += detalle.calc_subtotal()
        return sub_total
    
    def calc_igic(self):
        return self.calc_sub_total() * self.IGIG

    def calc_total(self):
        return self.calc_sub_total() + self.calc_igic()
    
    def get_estado_pago(self):
        return self.__pagado
    
    def realizar_pago(self, pago):
        if pago.get_cantidad() >= self.calc_total():
            self.__pagado = True
        else:
            self.__pagado = False
    
    