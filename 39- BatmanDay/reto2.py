""" * RETO 2:
 * Crea un programa que implemente el sistema de seguridad de la Batcueva.
 * Este sistema está diseñado para monitorear múltiples sensores distribuidos
 * por Gotham, detectar intrusos y activar respuestas automatizadas.
 * Cada sensor reporta su estado en tiempo real, y Batman necesita un programa
 * que procese estos datos para tomar decisiones estratégicas.
 * Requisitos:
 * - El mapa de Gotham y los sensores se representa con una cuadrícula 20x20.
 * - Cada sensor se identifica con una coordenada (x, y) y un nivel
 *   de amenaza entre 0 a 10 (número entero).
 * - Batman debe concentrar recursos en el área más crítica de Gotham.
 * - El programa recibe un listado de tuplas representando coordenadas de los
 *   sensores y su nivel de amenaza. El umbral de activación del protocolo de
 *   seguridad es 20 (sumatorio de amenazas en una cuadrícula 3x3).
 * Acciones:
 * - Identifica el área con mayor concentración de amenazas
 *   (sumatorio de amenazas en una cuadrícula 3x3).
 * - Si el sumatorio de amenazas es mayor al umbral, activa el
 *   protocolo de seguridad.
 * - Calcula la distancia desde la Batcueva, situada en (0, 0). La distancia es
 *   la suma absoluta de las coordenadas al centro de la cuadrícula amenazada.
 * - Muestra la coordenada al centro de la cuadrícula más amenazada, la suma de
 *   sus amenazas, la distancia a la Batcueva y si se debe activar el
 *   protocolo de seguridad.
 */ 
"""

def sum_subgrid_alerts(sensors, center_x, center_y)->int:
    total = 0
    for x in range(center_x-1, center_x+1):
        for y in range(center_y-1, center_y+1):
            for sensor in sensors:
                if sensor[0] == x and sensor[1] == y:
                    total += sensor[2]
    return total

def batcave_security_system(sensors):
    max_alert_level = 0
    max_alert_level_cordinate = (0,0)
    for x in range(1,19):
        for y in range(1,19):
            alert_level = sum_subgrid_alerts(sensors,x,y)
            if alert_level > max_alert_level:
                max_alert_level = alert_level
                max_alert_level_cordinate = (x,y)
    # Da un bool
    activate_protocol = max_alert_level > 20
    distance = abs(max_alert_level_cordinate[0]) + abs(max_alert_level_cordinate[1])
    
    return max_alert_level_cordinate,max_alert_level,distance, activate_protocol

sensors = [
    (2,3,5),
    (4,3,6),
    (2,2,7),
    (10,12,8),
    (15,18,4)
]

result = batcave_security_system(sensors)
print(f"Centro de cuadricula mas amenazada: {result[0]}")
print(f"Maximo nivel de alerta: {result[1]}")
print(f"Distancia a la baticueca: {result[2]}")
print(f"Activar protocolo de seguridad: {"Si" if result[3] else "No"}")