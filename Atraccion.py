class Atraccion:
    def __init__(self, nombre, costo_visita, tiempo_duracion, cupo_atraccion, tipo_atraccion):
        self.nombre = nombre
        self.costo_visita = costo_visita
        self.tiempo_duracion = tiempo_duracion
        self.cupo_atraccion = cupo_atraccion
        self.tipo_atraccion = tipo_atraccion

    def __repr__(self):
        return (f"Atraccion: {self.nombre}, "
                f"Costo de la Visita: {self.costo_visita}, "
                f"Tiempo de Duración: {self.tiempo_duracion}, "
                f"Cupo de la Atracción: {self.cupo_atraccion}, "
                f"Tipo: {self.tipo_atraccion}")
