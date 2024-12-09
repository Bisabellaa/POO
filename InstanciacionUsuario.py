from LecturaBD import LecturaBD
from CreacionInstUsuario import CreacionInstUsuarios

class InstanciacionUsuarios:
    def __init__(self, lector_bd=None):
        self.lector_bd = lector_bd if lector_bd else LecturaBD()
        self.creador_usuarios = CreacionInstUsuarios()

    def obtener_usuarios(self):
        """Obtiene usuarios como objetos a partir de la base de datos."""
        usuarios_leidos_BD = self.lector_bd.leer_tabla("Usuarios")
        objetos_tipo_usuarios = self.creador_usuarios.crear_usuarios(usuarios_leidos_BD)
        return objetos_tipo_usuarios
