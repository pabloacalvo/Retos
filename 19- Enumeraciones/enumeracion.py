"""
/*
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
 */
"""


from enum import Enum

class Weekday(Enum):
    MONDAY=1
    TUESDAY=2
    WEEDNESDAY=3
    THURDAY=4
    FRIDAY=5
    SATURDAY=6
    SUNDAY=7

    def get_day(number:int):
        print(Weekday(number).name)


class OrderStatus(Enum):
    PENDING=1
    SHIPPED=2
    DELIVERED=3
    CANCELLED=4

class Order:
    
    status=OrderStatus.PENDING

    def __init__(self,id:int):
        self.id = id

    def ship(self):
        if self.status.value == 1:
            self.status = OrderStatus.SHIPPED
            self.display_status()
        else:
            print("El pedido ya se esta enviando")
        

    def deliver(self):
        if self.status.value == 2:
            self.status = OrderStatus.DELIVERED
            self.display_status()
        else:
            print("El pedido se tiene que enviar antes de entregar")

    def cancel(self):
        if self.status.value != 3:
            self.status = OrderStatus.CANCELLED
            self.display_status()
        else:
            print("El pedido ya esta entregado, no se puede cancelar")

    def display_status(self):
        print(f"El estado del pedido {self.id} es: {self.status.name}")

