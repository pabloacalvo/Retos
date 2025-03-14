""""
/*
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
 */
"""
from pandas.io.formats.info import series_see_also_sub


class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

#singleton1 = Singleton()
#singleton2 = Singleton()

#print(singleton1 is singleton2)

class UserSession:
    _instance = None

    id = None
    username = None
    name = None
    email = None

    def __new__(cls):

        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance

    def set_user(self,id,username,name,email):
        self.id = id
        self.username = username
        self.name = name
        self.email = email

    def get_user(self):
        return f"{self.id}, {self.username}, {self.name}, {self.email}"

    def clear_user(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None

session1 = UserSession()
session1.set_user(1,'pabloacalvo','Pablo','pabloacalvo@live.com')
print(session1.get_user())

session2 = UserSession()
print(session2.get_user())

session3 = UserSession()
session3.clear_user()
print(session1.get_user())