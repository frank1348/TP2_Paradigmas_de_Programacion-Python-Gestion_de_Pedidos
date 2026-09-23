import json
import os

from exceptions import CampoVacioError, PedidoNoEncontradoError, PedidoNoModificableError
from models import Comida, Pizza, Empanada, Cliente, Pedido


class GestionPedidos:
    def __init__(self, archivo_json: str = "pedidos.json"):
        self._archivo_json = archivo_json
        self._pedidos = []
        self._cargar_desde_json()
        
    def _cargar_desde_json(self):
        Pedido._last_id = 0
        if not os.path.exists(self._archivo_json):
            return
        with open(self._archivo_json, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        for item in datos:
            cliente = Cliente(item["cliente"]["nombre"], item["cliente"]["direccion"])
            datos_comida = item["comida"]
            tipo = datos_comida["tipo"].lower()
            if tipo == "pizza":
                comida = Pizza(datos_comida["gusto"], datos_comida["size"])
            elif tipo == "empanada":
                comida = Empanada(datos_comida["gusto"], datos_comida["cantidad"])
            else:
                continue
            pedido = Pedido(cliente, comida, estado=item.get("estado", "pendiente"), id=item["id"])
            self._pedidos.append(pedido)
        if self._pedidos:
            Pedido._last_id = max(pedido.id for pedido in self._pedidos)
    
    def _guardar_en_json(self):
        datos = []
        for pedido in self._pedidos:
            datos_comida = {
                "tipo": pedido.comida.tipo,
                "gusto": pedido.comida.gusto
            }
            if isinstance(pedido.comida, Pizza):
                datos_comida["size"] = pedido.comida.size
            elif isinstance(pedido.comida, Empanada):
                datos_comida["cantidad"] = pedido.comida.cantidad
            
            datos.append({
                "id": pedido.id,
                "cliente": {
                    "nombre": pedido.cliente.nombre,
                    "direccion": pedido.cliente.direccion,
                },
                "comida": datos_comida,
                "estado": pedido.estado,
            })
        with open(self._archivo_json, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=2)
    
    def registrar_pedido(self, cliente: Cliente, comida: Comida):
        if not cliente.nombre or not cliente.direccion or not comida.gusto:
            raise CampoVacioError("Todos los campos son obligatorios")
        pedido = Pedido(cliente, comida, "pendiente")
        self._pedidos.append(pedido)
        self._guardar_en_json()
        return pedido
    
    def buscar_pedido_por_id(self, pedido_id: int):
        for pedido in self._pedidos:
            if pedido.id == pedido_id:
                return pedido
        raise PedidoNoEncontradoError(f"No existe un pedido con id {pedido_id}")
    
    def buscar_pedidos_por_cliente(self, texto = str):
        resultados = [pedido for pedido in self._pedidos if texto.lower() in pedido.cliente.nombre.lower()]
        if not resultados:
            raise PedidoNoEncontradoError(f"No se encontraron pedidos para el cliente: {texto} ")
        return resultados
    
    def modificar_pedido(self, pedido_id: int, nuevo_nombre: str = None, nueva_direccion: str = None, nueva_comida: Comida = None):
        pedido = self.buscar_pedido_por_id(pedido_id)
        if pedido.estado in {"cancelado", "entregado"}:
            raise PedidoNoModificableError("No se puede modificar un pedido cancelado o entregado")
        if nuevo_nombre is not None:
            pedido.cliente.nombre = nuevo_nombre
        
        if nueva_direccion is not None:
            pedido.cliente.direccion = nueva_direccion
        
        if nueva_comida is not None:
            pedido._comida = nueva_comida
        
        self._guardar_en_json()
        return pedido
            
    def actualizar_estado(self, pedido_id: int, nuevo_estado: str):
        pedido = self.buscar_pedido_por_id(pedido_id)
        if pedido.estado in {"cancelado", "entregado"}:
            raise PedidoNoModificableError(f"No se puede modificar un pedido que ya esta {pedido.estado}.")
        pedido.estado = nuevo_estado
        self._guardar_en_json()
        return pedido

    def listar_pedidos(self):
        return sorted(self._pedidos, key=lambda p: p.id)