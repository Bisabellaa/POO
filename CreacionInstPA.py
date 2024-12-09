from Promo import PromoAbsoluta, PromoPorcentual, PromoAxB
from Atraccion import Atraccion

class CreacionInstPA:
    def crear_atracciones(self, atracciones):
        atrac = []
        for atraccion in atracciones:
            atr = Atraccion(
                nombre=atraccion[1],
                costo_visita=atraccion[2],
                tiempo_duracion=atraccion[3],
                cupo_atraccion=atraccion[4],
                tipo_atraccion=atraccion[5]
            )
            atrac.append(atr)
        return atrac
    
    def crear_promociones(self, promociones_absolutas, promociones_porcentuales, promociones_AxB):
        promo_absolutas = []
        promo_porcentuales = []
        promo_AxB = []

        for promocion in promociones_absolutas:
            atracciones = promocion[3].split(';')  # Lista de nombres de atracciones
            promo = PromoAbsoluta(
                nombre_promo=promocion[1],
                categoria=promocion[2],
                atracciones=atracciones,
                descuento_absoluto=promocion[4]
            )
            promo_absolutas.append(promo)

        for promocion in promociones_porcentuales:
            atracciones = promocion[3].split(';')  # Lista de nombres de atracciones
            promo = PromoPorcentual(
                nombre_promo=promocion[1],
                categoria=promocion[2],
                atracciones=atracciones,
                descuento_porcentual=promocion[4]
            )
            promo_porcentuales.append(promo)

        for promocion in promociones_AxB:
            atracciones = promocion[3].split(';')  # Lista de nombres de atracciones
            promo = PromoAxB(
                nombre_promo=promocion[1],
                categoria=promocion[2],
                atracciones=atracciones,
                atraccion_gratuita=promocion[4]
            )
            promo_AxB.append(promo)

        return {
            'promo_absolutas': promo_absolutas,
            'promo_porcentuales': promo_porcentuales,
            'promo_AxB': promo_AxB
        }
