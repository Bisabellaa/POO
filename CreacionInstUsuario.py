import sqlite3
from Usuario import Usuario

class CreacionInstUsuarios:
    def __init__(self, mundoMagicoBD):
        self.db_name = mundoMagicoBD
        self.con = sqlite3.connect(self.db_name) 

    def obtener_usuarios_desde_db(self):
        cursor = self.con.cursor()
        cursor.execute("SELECT id, nombre, categoria_preferida, presupuesto, tiempo_disponible FROM Usuarios")
        usuarios = cursor.fetchall()
    
        if not usuarios:
            print("No se encontraron usuarios en la base de datos.")
    
        return usuarios

    def crear_usuarios(self):
        usuarios_data = self.obtener_usuarios_desde_db()
        usuarios = []
        for user_data in usuarios_data:
            usuario = Usuario(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4])
            usuarios.append(usuario)
        print("usuarios")
        print()
        return usuarios
