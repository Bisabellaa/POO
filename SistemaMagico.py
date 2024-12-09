from CreacionInstUsuario import CreacionInstUsuarios
from InstanciacionPA import InstanciacionPA

class SistemaMagico:
    def __init__(self):
        self.lista_usuarios = []
    
    def recorrer_usuarios(self):
        for user in self.lista_usuarios:
            print(f"Usuario: {user.nombre}")
            
            # Instancia de InstanciacionPA para obtener atracciones y promociones
            instancia_pa = InstanciacionPA()
            # atracciones y promociones
            instancia_pa.presentar_atracciones_y_promos(user.nombre)
            
            print(f"Lista de Ofertas Inicial: {user.lista_ofertables}")  
            
            while len(user.lista_ofertables) != 0:
                print(f"Hola {user.nombre}")
                user.filtro_presupuesto_user()  
                user.filtrar_compradas()  
                user.ordenar()  
                print(f"Lista Ofertass: {user.lista_ofertables}")
                
                i = 0
                while True:
                    o = user.lista_ofertables[i]
                    respuesta = input(f"Te ofrezco {o}. Compras? S/N: ")
                    if respuesta.lower() == "s":
                        user.comprar_promos(o)
                        user.filtro_presupuesto_user()  
                        user.filtrar_compradas()  
                        print("----------------------------------------")
                        break
                    i += 1
                    if len(user.lista_ofertables) == i:
                        i = 0
                print()
            print(f"Compras realizadas: {user.lista_compras}")

if __name__ == "__main__":
    # Crear el objeto 'CreacionInstUsuarios' y pasarle el nombre de la base de datos
    creador_usuarios = CreacionInstUsuarios('mundoMagicoBD.db') 
    sistema = SistemaMagico()
    sistema.lista_usuarios = creador_usuarios.crear_usuarios()
    
    sistema.recorrer_usuarios()
