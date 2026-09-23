from exceptions import CampoVacioError, PedidoNoEncontradoError, PedidoNoModificableError
from manager import GestionPedidos
from models import Cliente, Pizza, Empanada
import os


GUSTOS_PIZZA = {
    "1":  "muzarella",
    "2":  "tomate",
    "3":  "fugazzetta",
    "4":  "ajo",
    "5":  "pepperoni",
    "6":  "champiñones",
    "7":  "anana",
    "8":  "anchoas",
    "9":  "palmitos",
    "10": "rucula"
}

GUSTOS_EMPANADA = {
    "1":  "jamon y queso",
    "2":  "carne",
    "3":  "cebolla y queso",
    "4":  "caprese",
    "5":  "palmitos",
    "6":  "espinaca",
    "7":  "champiñones",
    "8":  "anana",
    "9":  "humita",
    "10": "panceta"   
}

SIZE_PIZZA = {
    "1": "estandar",
    "2": "media",
    "3": "grande"
}


def menu_principal():
    separador()
    print("[____________]                                [____________]")
    print(" \  0     0 /                                  \  0     0 / ")
    print("  \    0   /             SISTEMA DE             \    0   /  ")
    print("   \ 0   0/               GESTION                \ 0   0/   ")
    print("    \  0 /               DE PEDIDOS               \  0 /    ")
    print("     \  /                                          \  /     ")
    print("      \/                                            \/      ")
    separador()
    print("1. Registrar pedido")
    print("2. Buscar pedido por id")
    print("3. Buscar pedido por cliente")
    print("4. Modificar pedido")
    print("5. Actualizar estado del pedido")
    print("6. Ver todos los pedidos")
    print("0. Salir")
    separador()

def menu_pizza():
    print("1. Muzarella       |    6. Champiñones")
    print("2. Tomate          |    7. Anana      ")
    print("3. Fugazzetta      |    8. Anchoas    ")
    print("4. Ajo             |    9. Palmitos   ")
    print("5. Pepperoni       |   10. Rucula     ")
    
def menu_empanada():
    print("1. Jamon y queso   |    6. Espinaca   ")
    print("2. Carne           |    7. Champiñones")
    print("3. Cebolla y queso |    8. Anana      ")
    print("4. Capresse        |    9. Humita     ")
    print("5. Palmitos        |   10. Panceta    ")

def menu_size():
    print("1. Pizza estandar")
    print("2. Media pizza   ")
    print("3. Pizza grande  ")

def separador():
    print("------------------------------------------------------------")

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def pedidos_formateados(pedidos):
    if not pedidos:
        print("No hay pedidos registrados")
        return
    print("\nListado de pedidos:")
    print("-" * 105)
    print(f"{'ID':<4} {'Estado':<12} {'Cliente':<20} {'Dirección':<25} {'Detalle del Pedido':<40}")
    print("-" * 105)
    for pedido in pedidos:
        print(f"{pedido.id:<4} {pedido.estado:<12} {pedido.cliente.nombre:<20} {pedido.cliente.direccion:<25} {pedido.comida.descripcion():<40}")
    print("-" * 100)
    print(f"Total de pedidos: {len(pedidos)}")
    
    

def main():
    gestor = GestionPedidos("pedidos.json")
    while True:
        clear()
        menu_principal()
        opcion = input("Seleccione una opcion: ").strip()
        try:
            if opcion == "1":
                separador()
                print("=====================REGISTRAR PEDIDO=======================")
                separador()
                
                nombre_cliente = input("Nombre del cliente: ").strip()
                separador()
                direccion = input("Direccion de entrega: ").strip()
                separador()
                cliente = Cliente(nombre_cliente, direccion)
                
                tipo = input("Tipo de comida (pizza/empanada): ").strip().lower()
                separador()
                
                if tipo == "pizza":
                    menu_pizza()
                    num_gusto = input("Seleccione el gusto: ").strip()
                    separador()
                    if num_gusto not in GUSTOS_PIZZA:
                        raise ValueError("Ese no es un gusto valido.")
                    gusto = GUSTOS_PIZZA[num_gusto]
                    menu_size()
                    num_size = input("Seleccione el tamaño: ").strip()
                    if num_size not in SIZE_PIZZA:
                        raise ValueError("Ese no es un tamaño valido.")
                    size = SIZE_PIZZA[num_size]
                    separador()
                    comida = Pizza(gusto, size)
                    
                elif tipo == "empanada":
                    menu_empanada()
                    num_gusto = input("Seleccione el gusto: ").strip()
                    if num_gusto not in GUSTOS_EMPANADA:
                        raise ValueError("Ese no es un gusto valido.")
                    gusto = GUSTOS_EMPANADA[num_gusto]
                    separador()
                    cantidad = input("Cantidad: ").strip()
                    separador()
                    comida = Empanada(gusto, cantidad)
                    
                else:
                    raise ValueError("Tipo de comida no existe")
                
                pedido = gestor.registrar_pedido(cliente, comida)
                print("¡Pedido registrado correctamente!")
                separador()
                print(pedido)
                print("Precione ENTER para volver al menu principal...")
                input()
       
            elif opcion == "2":
                separador()
                print("===================BUSCAR PEDIDO POR ID=====================")
                separador()
                
                pedido_id = int(input("Ingrese ID del pedido: ").strip())
                pedido = gestor.buscar_pedido_por_id(pedido_id)
                separador()
                print(pedido)
                print("Presione ENTER para volver al menu principal... ")
                input()
                
            elif opcion == "3":
                separador()
                print("=================BUSCAR PEDIDO POR CLIENTE==================")
                separador()
                
                texto = input("Ingrese nombre o parte del nombre del cliente: ").strip()
                separador()
                pedidos = gestor.buscar_pedidos_por_cliente(texto)
                for pedido in pedidos:
                    print(pedido)
                print("Presione ENTER para volver al menu principal... ")
                input()
                
            elif opcion == "4":
                separador()
                print("======================MODIFICAR PEDIDO======================")
                separador()
                
                pedido_id = int(input("Ingrese el ID del pedido que desea modificar: ").strip())
                pedido_actual = gestor.buscar_pedido_por_id(pedido_id)
                print("\n---- Datos actuales del pedido ----")
                print(pedido_actual)
                print("(Presione ENTER sin escribir nada para conservar el dato actual)")
                
                nuevo_nombre = input(f"Nuevo nombre (presione ENTER para conservar dato actual): ").strip() or None
                separador()
                
                nueva_direccion = input(f"Nueva direccion (presione ENTER para conservar dato actual): ").strip() or None
                separador()
                
                cambiar_comida = input("¿Desea cambiar la comida? (s/n): ").strip().lower() == "s"
                separador()
                nueva_comida = None
                
                if cambiar_comida:
                    tipo = input("Tipo de comida (pizza/empanada): ").strip().lower()
                    separador()
                    if tipo == "pizza":
                        menu_pizza()
                        num_gusto = input("Seleccione el gusto: ").strip()
                        if num_gusto not in GUSTOS_PIZZA:
                            raise ValueError("Ese no es un gusto valido.")
                        gusto = GUSTOS_PIZZA[num_gusto]
                        separador()
                            
                        menu_size()
                        num_size = input("Seleccione el tamaño: ").strip()
                        if num_size not in GUSTOS_EMPANADA:
                            raise ValueError("Ese no es un tamaño valido.")
                        size = SIZE_PIZZA[num_size]
                        separador()
                            
                        nueva_comida = Pizza(gusto, size)
                        
                    elif tipo == "empanada":
                        menu_empanada()
                        num_gusto = input("Seleccione el gusto: ").strip()
                        if num_gusto not in GUSTOS_EMPANADA:
                            raise ValueError("Ese no es un gusto valido")
                        gusto = GUSTOS_EMPANADA[num_gusto]
                        separador()
                        
                        cantidad = input("Cantidad: ").strip()
                        separador()
                        if not cantidad:
                            raise ValueError("La cantidad no puede estar vacia")
                        
                        nueva_comida = Empanada(gusto, cantidad)
                        
                    else:
                        raise ValueError("Tipo de comida inexistente")
                
                pedido_modificado = gestor.modificar_pedido(pedido_id = pedido_id, nuevo_nombre = nuevo_nombre, nueva_direccion = nueva_direccion, nueva_comida = nueva_comida)
                
                print("¡Pedido modificado correctamente!")
                separador()
                print(pedido_modificado)
                print("Presione ENTER para volver al menu principal...")
                input()
                
            elif opcion == "5":
                separador()
                print("=====================ACTUALIZAR ESTADO======================")
                separador()
                
                pedido_id = int(input("Ingrese ID del pedido que desea actualizar su estado: ").strip())
                separador()
                pedido_actual = gestor.buscar_pedido_por_id(pedido_id)
                print("\n---- Datos actuales del pedido ----")
                print(pedido_actual)
                print("1. Actualizar estado a entregado")
                print("2. Cancelar pedido")
                print("0. Volver al menu")
                separador()
                sub_opcion = input("Seleccione una opcion: ").strip()
                separador()
                
                if sub_opcion == "1":
                    confirmar = input("¿Confirmar pedido como 'entregado'? (s/n): ").strip().lower() == "s"
                    separador()
                    if confirmar:
                        pedido = gestor.actualizar_estado(pedido_id, "entregado")
                        print("¡Estado actualizado con exito!")
                        separador()
                        print(pedido)
                        print("Presione ENTER para voler al menu principal...")
                        input()
                    else:
                        print("Operacion abortada. Presione ENTER para volver al menu principal...")
                        input()
                        
                elif sub_opcion == "2":
                    confirmar = input("¿Esta seguro de cancelar el pedido? (s/n): ").strip().lower() == "s"
                    separador()
                    if confirmar:
                        pedido = gestor.actualizar_estado(pedido_id, "cancelado")
                        print("¡Pedido cancelado con exito!")
                        separador()
                        print(pedido)
                        print("Presione ENTER para voler al menu principal...")
                        input()
                    else:
                        print("Operacion abortada. Presione ENTER para volver al menu principal...")
                        input()
                elif sub_opcion == "0":
                    print("Regresando al menu principal...")
                    input()
                else:
                    print("\nOpcion no valida. Regresando al menu principal.")
                    input()

            elif opcion == "6":
                separador()
                print("===================PEDIDOS EN EL SISTEMA====================")
                separador()
                
                pedidos = gestor.listar_pedidos()
                pedidos_formateados(pedidos)
                
                print("Presione ENTER para volver al menu principal...")
                input()
                
            elif opcion == "0":
                print("Bye Bye")
                break
            
            else:
                print("Opcion invalida, vuelva a intentar")
                input()
                
        except (CampoVacioError, PedidoNoEncontradoError, PedidoNoModificableError) as exc:
            print(f"Error: {exc}")
            input()
        except ValueError as exc:
            print(f"Entrada invalida: {exc}")
            input()
    
    
if __name__ == "__main__":
    main()
                
