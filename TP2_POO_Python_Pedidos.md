# **TRABAJO PRÁCTICO N° 2** 

### Paradigmas de Programación 

Ingeniería de Sistemas - 2do Año 

### **Paradigma Orientado a Objetos - Lenguaje Python** 

_CRUD: Gestion de pedidos de una pizzeria/empanaderia_ 

|**Campo**|**Detalle**|
|---|---|
|Alumno|Francisco O'Connell|
|Materia|Paradigmas de Programación|
|Año|2do. Año - Ingeniería de Sistemas|
|Modalidad|Grupal (2 o 3 alumnos - mismo grupo que TP1, de ser posible)|
|Lenguaje|Python (POO)|
|Entrega|Presentación y defensa oral en clase|
|Requisito previo|Haber entregado el TP1 (versión estructurada en Pascal)|



## **1. Historia de Usuario** 

|**Campo**|**Descripción**|
|---|---|
|Como|encargado de una pizzería y empanaderia|
|Quiero|registrar, consultar, modificar y cancelar pedidos de clientes|
|Para|gestionar la preparación y el envío de pizzas y empanadas de forma eficiente y ordenada|



## **2. Modelo de Clases del Sistema** 

#### **2.1 Clase abstracta Comida** 

Clase base con los atributos comunes a Pizza y Empanadas. No se instancia directamente. 

|**Atributo**|**Tipo**|**Descripción**|
|---|---|---|
|tipo|str|Tipo de comida(pizza o empanada)|
|gusto|str|Gusto de la comida|



#### **2.2 Clase Pizza (hereda de Comida)** 

|**Atributo**|**Tipo**|**Descripción**|
|---|---|---|
|size|str|Tamaño de la pizza|



#### **2.3 Clase Empanada (hereda de Comida)** 

|**Atributo**|**Tipo**|**Descripción**|
|---|---|---|
|cantidad|str|Cantidad de empanadas|



#### **2.4 Clase Cliente** 

|**Atributo**|**Tipo**|**Descripción**|
|---|---|---|
|nombre|str|Nombre del cliente|
|direccion|str|Direccion del cliente|



#### **2.5 Clase Pedido** 

|**Atributo**|**Tipo**|**Descripción**|
|---|---|---|
|id|int|Identificador único, asignado automáticamente|
|comida|Comida|Objeto comida|
|cliente|Cliente|Objeto cliente|
|estado|str|pendiente / entregado / cancelado|



## **3. Requerimientos Funcionales (CRUD)** 

#### **3.1 Alta - Registrar Pedido** 

- Permitir crear un nuevo objeto Pedido a partir de un Cliente y una Comida.

- El sistema debe asignar automáticamente un ID correlativo único.

- No se aceptan campos vacíos: la validación debe lanzar una excepción (“CampoVacioError) 

- El estado inicial siempre debe ser 'pendiente'. 

#### **3.2 Consulta - Buscar Pedido** 

- Permitir buscar un pedido por su ID. 

- Permitir buscar pedidos por nombre parcial del cliente (puede devolver una lista de objetos Pedido) 

- Si no se encuentra ningún resultado, se debe manejar una excepción propia (“PedidoNoEncontradoError”) y mostrar un mensaje claro al usuario. 

- Mostrar todos los datos del pedido encontrado con formato legible, delegando la presentación a un método propio del objeto (“mostrar_detalle())

#### **3.3 Modificación - Editar Pedido** 

- Permitir modificar: cliente, dirección y comida de un pedido existente.

- El ID del pedido no puede ser modificado.

- Si el pedido está 'entregado' o 'cancelado', este no puede ser modificado lanzando una excepción propia (PedidoNoModificableError)

#### **3.4 Baja - Cancelar Pedido** 

- El sistema debe pedir confirmación antes de cancelar un pedido. 

- Un pedido con estado ‘entregado’ No puede ser dado de baja. 

- La baja lógica cambia el estado a 'Cancelado' (no elimina el registro).

#### **3.5 Listado - Ver Todos los Pedidos** 

- Mostrar todos los pedidos registrados en formato de tabla. 

- Diferenciar visualmente los pedidos según su estado.

- Mostrar la cantidad total de pedidos al pie del listado.



## **4. Requisitos de Diseño Orientado a Objetos** 

#### **4.1 Encapsulamiento** 

- Todos los atributos de las clases deben ser privados o protegidos (prefijo _ o __). 

- El acceso externo debe hacerse mediante @property y, cuando corresponda, sus respectivos setters con validación.

- Ningún atributo interno de GestionPedidos debe ser accedido ni modificado directamente desde fuera de la clase. 

#### **4.2 Herencia** 

- Pizza y Empanada deben heredar de Comida, reutilizando atributos y/o métodos comunes. 

- Se debe usar super().__init__() correctamente en los constructores de las subclases. 

#### **4.3 Polimorfismo** 

- Debe existir al menos un método que se comporte de forma distinta según el tipo de objeto que lo invoca (por ejemplo, un método presentación() distinto en Pizza y Empanada). 

#### **4.4 Manejo de excepciones** 

- Se deben definir al menos dos excepciones propias, heredadas de Exception (PedidoNoEncontradoError, CampoVacioError, PedidoNoModificableError). 

- El menú principal debe capturar estas excepciones con try/except y mostrar mensajes claros, sin que el programa se caiga ante una entrada inválida.

#### **4.5 Persistencia** 

- Guardado y carga de los pedidos en un archivo JSON, de modo que los datos no se pierdan al cerrar el programa. 



## **5. Criterios de Aceptación** 

|**Operación**|**Escenario**|**Acción / Entrada**|**Resultado Esperado**|
|---|---|---|---|
|Alta|Pedido válido|Todos los campos completos|Pedido creado con ID único y estado “pendiente”|
|Alta|Campo vacío|Intentar guardar sin nombre de cliente|CampoVacioError. No se guarda|
|Consulta|Id existente|Buscar por id válido|Muestra todos los datos del pedido|
|Consulta|Id inexistente|Buscar id que no existe|PedidoNoEncontradoError. Mensaje de error claro|
|Modificación|Pedido pendiente|Cambiar dirección, gusto y tamaño|Datos actualizados correctamente|
|Modificación|Pedido cancelado|Intentar modificar pedido cancelado|PedidoNoModificableError. Cambios no son guardados|
|Baja|Con confirmación|Confirmar cancelación|Estado cambia a 'cancelado'|
|Baja|Turno atendido|Intentar cancelar turno|PedidoNoModificableError|
|Listado|Sin registros|Listar con colección vacía|Informa que no hay pedidos registrados|
|Listado|Con registros|Listar con datos cargados|Listado de todos los pedidos en el sistema|



## **6. Estructura del Programa Requerida** 

|**Elemento**|**Tipo Python**|**Responsabilidad**|
|---|---|---|
|Comida|Clase abstracta|Atributos y comportamiento común a pizzas y empanadas|
|Pizza|Clase (hereda de Comida)|Representa una pizza|
|Empanada|Clase (hereda de Comida)|Representa empanadas|
|Cliente|Clase|Representa un cliente que desea hacer un pedido|
|Pedido|Clase|Representa un pedido de una comida junto al cliente que la ordenó|
|GestionPedidos|Clase|Encapsula la coleccion de pedidos y el CRUD completo|
|CampoVacioError, PedidoNoEncontradoError, PedidoNoModificableError|Clases de excepción (Exception)|Errores de negocio propios del dominio|
|menu_principal(), menu_pizza(), menu_empanada(), menu_size(), separador()|Funcion|Muestra menús en pantalla/separan|
|clear()|Funcion|Elimina todo el texto en consola|
|pedidos_formateados()|Funcion|Muestra los pedidos formateados|
|main()|Funcion|Punto de entrada del programa, contiene el bucle del menú|

