"""
 * EJERCICIO:
 * ¡La Casa del Dragón ha finalizado y no volverá hasta 2026!
 * ¿Alguien se entera de todas las relaciones de parentesco
 * entre personajes que aparecen en la saga?
 * Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
 * Requisitos:
 * 1. Estará formado por personas con las siguientes propiedades:
 *    - Identificador único (obligatorio)
 *    - Nombre (obligatorio)
 *    - Pareja (opcional)
 *    - Hijos (opcional)
 * 2. Una persona sólo puede tener una pareja (para simplificarlo).
 * 3. Las relaciones deben validarse dentro de lo posible.
 *    Ejemplo: Un hijo no puede tener tres padres.
 * Acciones:
 * 1. Crea un programa que permita crear y modificar el árbol.
 *    - Añadir y eliminar personas
 *    - Modificar pareja e hijo
 * 2. Podrás imprimir el árbol (de la manera que consideres).
 * 
 * NOTA: Ten en cuenta que la complejidad puede ser alta si
 * se implementan todas las posibles relaciones. Intenta marcar
 * tus propias reglas y límites para que te resulte asumible.
 */
"""


class Person:

    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.partner = None
        self.childrens = []
        self.has_parents = None
        
    def add_partner(self,partner):
        if self.partner:
            print(f'{self.name} ya tiene pareja: {self.partner.name}')
        else:
            self.partner = partner
            partner.partner = self
            print(f'{self.name} {partner.name} son pareja.')

    def add_children(self,children):
        if children not in self.childrens:
            self.childrens.append(children)
            print(f'{self.name} tiene un hijo: {children.name}')
        else:
            print(f'{children.name} ya es hijo de {self.name}')

    def get_children(self):
        for children in self.childrens:
            print(f'Id: {children.id} Nombre: {children.name}')



class FamilyTree:

    def __init__(self):
        self.people = {}

    def add_person(self,person,view=False):
        if person.id in self.people:
            print(f'Ya existe una persona con id: {id} ya existe en el arbol')
        else:
            self.people[person.id]=person
            if view:
                print(f'La persona con nombre {person.name} [ID: {person.id}] se añadio al arbol')
        
    def delete_person(self,id):
        if id in self.people:
            person = self.people[id]
            del self.people[id]
            print(f'Se elimino la persona {person.name} con id {person.id}')
        else:
            print(f'La persona con id:{id} no existe')

    def set_partner(self,person1,person2):
        if person1.id in self.people and person2.id in self.people:
            person1.add_partner(person2)
        else:
            print('Alguna de los personas no existe en el arbol')
        

    def set_children(self,parent,children):
        if parent.id != children.id: 
            if parent.id in self.people and children.id in self.people:
                if parent.partner is not None:
                    if children.has_parents:
                        print(f"{children.name} ya tiene padres")
                    else:
                        children.has_parents = True
                        parent.add_children(children)
                        #parent.partner.add_children(children)
                else:
                    print(f'La persona {parent.name} debe tener asignado pareja para tener un hijo')
            else:
                print('Alguna de las personas no existe')
        else:
            print('Datos incorrectos, los id de las personas son iguales')
        

    def print_tree(self):

        visited = set()

        def print_person(person, level=0):
            if person.id in visited:
                return
            visited.add(person.id)
            indent = '\t' * level
            print(f'{indent} - {person.name}[ID: {person.id}]')

            if person.partner:
                print(f'{indent} \t - Pareja: {person.partner.name}')
            if person.childrens:
                print(f'{indent} \t - Hijos:')
                for children in person.childrens:
                    print_person(children, level + 2)


        for person in self.people.values():
            is_children = person.has_parents
            if not is_children:
                print_person(person)





person1 = Person(1,'Pablo')
person3 = Person(4,'Rocio')
children1 = Person(3,'Juan Pablo')

tree = FamilyTree()
tree.add_person(person1)
tree.add_person(person3)
tree.add_person(children1)
tree.set_partner(person1,person3)
tree.set_children(person1,children1)
tree.print_tree()



