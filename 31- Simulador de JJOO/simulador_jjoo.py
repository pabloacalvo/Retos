"""* EJERCICIO:
 * ¡Los JJOO de París 2024 han comenzado!
 * Crea un programa que simule la celebración de los juegos.
 * El programa debe permitir al usuario registrar eventos y participantes,
 * realizar la simulación de los eventos asignando posiciones de manera aleatoria
 * y generar un informe final. Todo ello por terminal.
 * Requisitos:
 * 1. Registrar eventos deportivos.
 * 2. Registrar participantes por nombre y país.
 * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
 * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
 * 5. Mostrar los ganadores por cada evento.
 * 6. Mostrar el ranking de países según el número de medallas.
 * Acciones:
 * 1. Registro de eventos.
 * 2. Registro de participantes.
 * 3. Simulación de eventos.
 * 4. Creación de informes.
 * 5. Salir del programa.
 """

import random

class Participant():
    
    def __init__(self,name,nacinality):
        self.name = name
        self.nacionalaty = nacinality

    def __str__(self):
        return f"{self.name} - {self.nacionalaty}"
    
    # Metodo equals, utilizamos esto porque la estructura de datos donde se van a guardar sus intancias es un diccionario.
    def __eq__(self, value: object) -> bool:
        # Verificamos que sea una intancia
        if isinstance(value, Participant):
            # Establecemos condicion para decir que son iguales
            if value.name == self.name and value.nacionalaty == self.nacionalaty:
                return True
            else:
                return False
    # Metodo para crear el hsh de los objetos    
    def __hash__(self) -> int:
        return hash((self.name, self.nacionalaty))


class Olympics():

    def __init__(self):
        self.events = []
        self.parcipants = {}
        self.event_results = {}
        self.country_results = {}
        

    def register_event(self):
        event = input("Ingresa el nombre del evento deportivo: ").strip().capitalize()
        if event in self.events:
            print("El evento ya existe")
        else:
            self.events.append(event)
            print(f"El evento {event} se agrego correctamente")


    def register_parcipant(self):

        if not self.events:
            print("No es posible registrar el parcipante porque no hay eventos creados.")
        else:
            name = input("Ingresa el nombre del parcipante: ").strip()
            nacionality = input("Ingresa la nacionalidad del parcipante: ").strip().capitalize()
            participant = Participant(name,nacionality)
            for num,event in enumerate(self.events):
                print(f"{num+1}.- {event}")
            opc = int(input("Selecciona uno de los eventos para el parcipante: ")) - 1 
            if opc >= 0 and opc <= len(self.events):
                event = self.events[opc]

                if event in self.parcipants and participant in self.parcipants[event]:
                    print(f"El parcipante {participant.name} ya esta registrado en una actividad")
                else:
                    # Validar la clave en el diccionario
                    if event not in self.parcipants:
                        self.parcipants[event] = []
                    self.parcipants[event].append(participant)
                    print(f"El parcipante {participant.name} registrado correctamente en {event}")
            else:
                print("Opcion invalida.")
        

        
    def event_simulate(self):
        if not self.events:
            print("No hay eventos para simular.")
        else:
            for event in self.events:
                if len(self.parcipants[event]) < 3:
                    print("No hay la cantidad necesaria de participantes (3).")
                    continue

                participants_event = random.sample(self.parcipants[event],3)
                random.shuffle(participants_event)
                gold, silver, bronze = participants_event
                self.event_results[event] = [gold,silver,bronze] 
                self.update_country_result(gold.nacionalaty, 'Oro')
                self.update_country_result(silver.nacionalaty, 'Plata')
                self.update_country_result(bronze.nacionalaty, 'Bronce')
                print(f"Simulacion del evento: {event}")
                print(f"Listado de ganadores de {event}\nOro: {gold}\nPlata: {silver}\nBronce {bronze}\n")


    def update_country_result(self,country,medal):
        if country not in self.country_results:
            self.country_results[country] = {'Oro':0, 'Plata':0,'Bronce':0}

        self.country_results[country][medal] += 1

    
    def show_result(self):
        print('*** Informe de resultados por evento ***')
        if self.event_results:
            for event,winner in self.event_results.items():
                print(f"Evento {event}")
                print(f'Oro:{winner[0].name} ({winner[0].nacionalaty})')
                print(f'Plata:{winner[1].name} ({winner[1].nacionalaty})')
                print(f'Bronce:{winner[2].name} ({winner[2].nacionalaty})')
        else:
            print('No hay resultados para mostrar.')
            return
        
        if self.country_results:
            print('*** Informe de resultados por paises ***')
            sorted_countries = sorted(self.country_results.items(),key=lambda x:(x[1]['Oro'], x[1]['Plata'], x[1]['Bronce']))
            for country, medal in sorted_countries:
                print(f"{country}: Oro {medal['Oro']}, Plata {medal['Plata']}, Bronce {medal['Bronce']}\n") 


        else:
            print('No hay medallas registradas por pais.')



            


olimpycs = Olympics()

while True:
    print("1. Registrar evento deportivo")
    print("2. Registrar parcipante")
    print("3. Simular evento") 
    print("4. Ver ranking")
    print("5. Salir")

    opcion = int(input(f"Selecciona una opcion: "))
    match opcion:
        case 1:
            olimpycs.register_event()
        case 2:
            olimpycs.register_parcipant()
        case 3:
            olimpycs.event_simulate()
        case 4:
            olimpycs.show_result()
        case 5:
            break
