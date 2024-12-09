from LecturaBD import LecturaBD
from CreacionInstPA import CreacionInstPA

class InstanciacionPA:
    def __init__(self, lector_bd=None):
        self.lector_bd = lector_bd if lector_bd else LecturaBD()
        self.creador_atracciones = CreacionInstPA()

    def obtener_atracciones(self):
        """Obtiene atracciones como objetos a partir de la base de datos."""
        atracciones_leidas_BD = self.lector_bd.leer_tabla("Atracciones")
        objetos_tipo_atracciones = self.creador_atracciones.crear_atracciones(atracciones_leidas_BD)
        return objetos_tipo_atracciones

    def obtener_promos(self):
        """Obtiene promociones como objetos a partir de la base de datos."""
        promos_leidas_BD = self.lector_bd.leer_promos()
        objetos_tipo_promos = self.creador_atracciones.crear_promociones(
            promos_leidas_BD['promociones_absolutas'],
            promos_leidas_BD['promociones_porcentuales'],
            promos_leidas_BD['promociones_AxB']
        )
        return objetos_tipo_promos
    
    def presentar_atracciones_y_promos(self, nombre_usuario):
        """Método para presentar atracciones y promociones para un usuario."""
        print(f"Atracciones y promociones para el usuario {nombre_usuario}:")
        
        # Obtener las atracciones y promociones
        atracciones = self.obtener_atracciones()
        promociones = self.obtener_promos()
        
        # Mostrar las atracciones
        print("Atracciones disponibles:")
        for atraccion in atracciones:
            print(f"- {atraccion.nombre}: {atraccion.tipo_atraccion}, Costo: {atraccion.costo_visita}, Cupo: {atraccion.cupo_atraccion} y tiempo de duracion: {atraccion.tiempo_duracion}")
        
        # Mostrar las promociones
        print("Promociones disponibles:")
        for promo in promociones['promo_absolutas']:
            print(f"- {promo.nombre_promo}: {promo.descuento_absoluto} de descuento absoluto")
        for promo in promociones['promo_porcentuales']:
            print(f"- {promo.nombre_promo}: {promo.descuento_porcentual}% de descuento")
        for promo in promociones['promo_AxB']:
            print(f"- {promo.nombre_promo}: Compra 1 y obtén otro gratis")

