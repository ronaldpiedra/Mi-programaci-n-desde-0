# mi primera programación de POO
class Personaje:
    def _init_(self, nombre, fuerza, intelecto, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.intelecto = intelecto
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print(".fuerza:", self.fuerza)
        print(".intelecto:", self.intelecto)
        print(".vida:", self.vida)

    def subir_nivel(self, fuerza, intelecto, vida):
        self.fuerza = self.fuerza + fuerza
        self.intelecto = self.intelecto + intelecto
        self.vida = self.vida + vida

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.intelecto

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("la vida de", enemigo.nombre, "es", enemigo.vida)


mi_personaje = Personaje("Yueron", 10, 30, 200)
mi_enemigo = Personaje("Enemigo yue", 9, 2, 199)
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()