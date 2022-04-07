class Producto:
    def __init__(self, nombre, precio, peso, descripcion): 
        self.__nombre = nombre
        self.__precio = precio
        self.__peso = peso
        self.__descripcion = descripcion
    
    def get_precio(self):
        return self.__precio