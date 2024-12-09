class Promo:
    def __init__(self, nombre_promo, categoria, atracciones):
        self.nombre_promo = nombre_promo
        self.categoria = categoria
        self.atracciones = [self.obtener_atraccion(nombre) for nombre in atracciones]
        self.precio = self.calcular_precio()

    def obtener_atraccion(self, nombre):
        from InstanciacionPA import InstanciacionPA
        for atraccion in InstanciacionPA().obtener_atracciones():
            if atraccion.nombre == nombre:
                return atraccion
        raise ValueError(f"Atraccion con nombre {nombre} no encontrada")

    def calcular_precio(self):
        return sum(atraccion.costo_visita for atraccion in self.atracciones)

    def __repr__(self):
        return (f"Promo: {self.nombre_promo}, Categoria: {self.categoria}, "
                f"Atracciones: {[atraccion.nombre for atraccion in self.atracciones]}, "
                f"Precio: {self.precio}")

class PromoAbsoluta(Promo):
    def __init__(self, nombre_promo, categoria, atracciones, descuento_absoluto):
        super().__init__(nombre_promo, categoria, atracciones)
        self.descuento_absoluto = descuento_absoluto

    def __repr__(self):
        return (super().__repr__() + f", Descuento Absoluto: {self.descuento_absoluto}")

class PromoPorcentual(Promo):
    def __init__(self, nombre_promo, categoria, atracciones, descuento_porcentual):
        super().__init__(nombre_promo, categoria, atracciones)
        self.descuento_porcentual = descuento_porcentual

    def __repr__(self):
        return (super().__repr__() + f", Descuento Porcentual: {self.descuento_porcentual}")

class PromoAxB(Promo):
    def __init__(self, nombre_promo, categoria, atracciones, atraccion_gratuita):
        super().__init__(nombre_promo, categoria, atracciones)
        self.atraccion_gratuita = atraccion_gratuita

    def __repr__(self):
        return (super().__repr__() + f", Atracción Gratuita: {self.atraccion_gratuita}")
