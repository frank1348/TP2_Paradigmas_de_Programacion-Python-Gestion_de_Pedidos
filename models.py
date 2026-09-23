from abc import ABC, abstractmethod


class Comida(ABC):
    def __init__(self, tipo: str, gusto: str):
        self._tipo = tipo
        self._gusto = gusto
        
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, value):
        self._tipo = value
    
    @property
    def gusto(self):
        return self._gusto
    
    @gusto.setter
    def gusto(self, value):
        self._gusto = value
    
    @abstractmethod
    def descripcion(self):
        raise NotImplementedError
    

class Pizza(Comida):
    def __init__(self, gusto: str, size: str):
        super().__init__(tipo = "pizza", gusto = gusto)
        self._size = size
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        self._size = value
        
    def descripcion(self):
        return f"Una {self.tipo} {self.size} de {self.gusto}"
   

class Empanada(Comida):
    def __init__(self, gusto: str, cantidad: str):
        super().__init__(tipo = "empanada", gusto = gusto)
        self._cantidad = cantidad
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, value):
        self._cantidad = value
        
    def descripcion(self):
        return f"{self.cantidad} de {self.tipo}s de {self.gusto}"


class Cliente:
    def __init__(self, nombre: str, direccion: str):
        self._nombre = nombre
        self._direccion = direccion
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        self._nombre = value
        
    @property
    def direccion(self):
        return self._direccion
    
    @direccion.setter
    def direccion(self, value):
        self._direccion = value


class Pedido:
    _last_id = 0
    def __init__  (self, cliente: Cliente, comida: Comida, estado: str = "pendiente", id: int = None):
        if id is None:
            Pedido._last_id += 1
            self._id = Pedido._last_id
        else:
            self._id = id
            if id > Pedido._last_id:
                Pedido._last_id = id
        self._cliente = cliente
        self._comida = comida
        self._estado = estado
    
    @property
    def id(self):
        return self._id

    @property
    def cliente(self):
        return self._cliente

    @property
    def comida(self):
        return self._comida

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = value
        
    def mostar_detalle(self):
        return (
            f"ID       : {self.id}\n"
            f"CLIENTE  : {self.cliente.nombre}\n"
            f"DIRECCION: {self.cliente.direccion}\n"
            f"DETALLE  : {self.comida.descripcion()}\n"
            f"ESTADO   : {self.estado}\n"
        )
    
    def __str__(self):
        return self.mostar_detalle()

