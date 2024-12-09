from InstanciacionPA import InstanciacionPA
from Promo import PromoAbsoluta, PromoAxB, PromoPorcentual
from Atraccion import Atraccion

class Usuario:
    def __init__(self, id_usuario, nombre, categoria, presupuesto, tiempo_disponible):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.categoria = categoria
        self.presupuesto = presupuesto
        self.tiempo_disponible = tiempo_disponible
        self.lista_compras = []  
        promo_atraccion = InstanciacionPA()
        self.lista_promos = promo_atraccion.obtener_promos()
        self.lista_atraccion = promo_atraccion.obtener_atracciones()

        self.lista_ofertables = self.lista_atraccion + self.lista_promos['promo_absolutas'] + \
                                self.lista_promos['promo_porcentuales'] + self.lista_promos['promo_AxB']
        
        print(f"Ofertas obtenidas: {self.lista_ofertables}")
    
    def filtro_presupuesto_user(self):
        filtro_list_ofertables = []
        for promociones in self.lista_ofertables:
            if isinstance(promociones, Atraccion):
                if promociones.costo_visita <= self.presupuesto:
                    filtro_list_ofertables.append(promociones)
            else:
                # Calcular el precio de la promoción basándose en las atracciones que contiene
                precio_promo = self.calcular_precio_promo(promociones)
                if precio_promo <= self.presupuesto:
                    filtro_list_ofertables.append(promociones)
        self.lista_ofertables = filtro_list_ofertables

    def calcular_precio_promo(self, promo):
    # Si es una atracción, simplemente retorna costo
        if isinstance(promo, Atraccion):
            return promo.costo_visita

    # Si es una promoción, calculamos el precio total de las atracciones dentro de esa promoción
        precio_total = 0
        if isinstance(promo, PromoAbsoluta) or isinstance(promo, PromoPorcentual) or isinstance(promo, PromoAxB):
        # Promoción que tiene una lista de atracciones asociadas
            for atraccion in promo.atracciones:
            # Buscar la atracción en la lista de atracciones del usuario y agregar su costo
                atraccion_obj = next((atr for atr in self.lista_atraccion if atr.nombre == atraccion), None)
                if atraccion_obj:
                    precio_total += atraccion_obj.costo_visita

    # Dependiendo del tipo de promoción, aplicamos el descuento
        if isinstance(promo, PromoAbsoluta):
            return precio_total - promo.descuento_absoluto
        elif isinstance(promo, PromoPorcentual):
            return precio_total * (1 - promo.descuento_porcentual / 100)
        elif isinstance(promo, PromoAxB):
            # Para el tipo AxB, solo devolvemos el precio total de las atracciones
            return precio_total
        return precio_total

    
    def separar_promos_compradas(self):
        lista_promos_compradas = []
        for promociones in self.lista_compras:
            if isinstance(promociones, (PromoAbsoluta, PromoAxB, PromoPorcentual)):
                lista_promos_compradas.append(promociones)
        return lista_promos_compradas

    def filtrar_compradas(self):
        lista_promociones_filtrada = []
        for promociones in self.lista_ofertables:
        # Si el producto comprado es una atracción
            if hasattr(self, 'ultima_promo_comprada') and isinstance(self.ultima_promo_comprada, Atraccion):
            # Si la última compra fue una atracción, aseguramos que no se repita
                if self.ultima_promo_comprada.nombre != promociones.nombre:
                    lista_promociones_filtrada.append(promociones)
        # Si el producto comprado es una promoción
            elif hasattr(self, 'ultima_promo_comprada') and isinstance(self.ultima_promo_comprada, (PromoAbsoluta, PromoAxB, PromoPorcentual)):
                if isinstance(promociones, Atraccion):
                    lista_promociones_filtrada.append(promociones)
                elif promociones.nombre_promo != self.ultima_promo_comprada.nombre_promo:
                    lista_promociones_filtrada.append(promociones)
            else:
                    lista_promociones_filtrada.append(promociones)
    
        self.lista_ofertables = lista_promociones_filtrada


    def comprar_promos(self, promociones):
        self.lista_compras.append(promociones)
        self.presupuesto -= self.calcular_precio_promo(promociones)
        self.ultima_promo_comprada = promociones

    def ordenar(self):
        self.lista_ofertables.sort(key=lambda x: self.calcular_precio_promo(x) if not isinstance(x, Atraccion) else x.costo_visita)
    
    def obtener_promos_y_atracciones(self):
        promo_atraccion = InstanciacionPA()
        self.lista_promos = promo_atraccion.obtener_promos()
        self.lista_atraccion = promo_atraccion.obtener_atracciones()

    def __repr__(self):
        return (f"Usuario nombre: {self.nombre}, presupuesto {self.presupuesto}, "
                f"categoria {self.categoria}, tiempo disponible {self.tiempo_disponible}")
