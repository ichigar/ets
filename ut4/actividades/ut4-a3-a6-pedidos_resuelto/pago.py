class Pago:
    def __init__(self, cantidad):
        self._cantidad = cantidad
    
    def get_cantidad(self):
        return self._cantidad
        
class Tarjeta(Pago):
    def __init__(self, cantidad, numero, cvv, vencimiento):
        super().__init__(cantidad)
        self.__numero = numero
        self.___cvv = cvv
        self.___vencimiento = vencimiento
        
class Efectivo(Pago):
    def __init__(self, cantidad, caja):
        super().__init__(cantidad)
        self.__caja = caja