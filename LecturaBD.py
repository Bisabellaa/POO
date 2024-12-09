import sqlite3

class LecturaBD:
    def leer_tabla(self, nombre_tabla):
        """Obtiene todos los registros de una tabla."""
        con = sqlite3.connect("mundoMagicoBD.db")
        try:
            cur = con.cursor()
            query = f"SELECT * FROM {nombre_tabla};"  
            comando = cur.execute(query)
            items = comando.fetchall()
            print(f"Registros de {nombre_tabla}: {items}") 
        except sqlite3.Error as e:
            print(f"Error al leer de la tabla {nombre_tabla}: {e}")
            items = []
        finally:
            con.close()
        return items

    def leer_promos(self):
        """Lee todas las promociones y sus atracciones asociadas."""
        con = sqlite3.connect("mundoMagicoBD.db")
        promociones_porcentuales = []
        promociones_absolutas = []
        promociones_AxB = []

        try:
            cur = con.cursor()
            
            # Promociones Porcentuales
            query_porcentuales = '''
                SELECT p.id, p.nombre_promocion, p.categoria, a.nombre_atraccion, p.descuento_porcentual 
                FROM Promociones_porcentuales AS p
                JOIN Atracciones_promos AS ap ON p.id = ap.id_promo_porcentual 
                JOIN Atracciones AS a ON ap.id_atraccion = a.id;
            '''
            promociones_porcentuales = cur.execute(query_porcentuales).fetchall()
            print(f"Promociones Porcentuales: {promociones_porcentuales}")
            
            # Promociones Absolutas
            query_absolutas = '''
                SELECT p.id, p.nombre_promocion, p.categoria, a.nombre_atraccion, p.descuento_absoluto 
                FROM Promociones_absolutas AS p 
                JOIN Atracciones_promos AS ap ON p.id = ap.id_promo_absoluta 
                JOIN Atracciones AS a ON ap.id_atraccion = a.id;
            '''
            promociones_absolutas = cur.execute(query_absolutas).fetchall()
            print(f"Promociones Absolutas: {promociones_absolutas}")
            
            # Promociones AxB
            query_AxB = '''
                SELECT p.id, p.nombre_promocion, p.categoria, a.nombre_atraccion, p.atraccion_gratuita 
                FROM Promociones_AxB AS p 
                JOIN Atracciones_promos AS ap ON p.id = ap.id_promo_AxB 
                JOIN Atracciones AS a ON ap.id_atraccion = a.id;
            '''
            promociones_AxB = cur.execute(query_AxB).fetchall()
            print(f"Promociones AxB: {promociones_AxB}")
            
        except sqlite3.Error as e:
            print(f"Error al leer las promociones: {e}")
            promociones_porcentuales = []
            promociones_absolutas = []
            promociones_AxB = []
        finally:
            con.close()

        return { 
            'promociones_porcentuales': promociones_porcentuales, 
            'promociones_absolutas': promociones_absolutas, 
            'promociones_AxB': promociones_AxB
        }

# # Ejemplo de uso
# leer = LecturaBD()
# promociones = leer.leer_promos()
# print(promociones['promociones_porcentuales']) 
# print(promociones['promociones_absolutas'])   
# print(promociones['promociones_AxB'])
