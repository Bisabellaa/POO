import sqlite3


con = sqlite3.connect("mundoMagicoBD.db")
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                categoria_preferida TEXT,
                presupuesto FLOAT,
                tiempo_disponible FLOAT);''')

# Tabla de Atracciones
cur.execute(''' CREATE TABLE IF NOT EXISTS Atracciones (
                id INTEGER PRIMARY KEY,
                nombre_atraccion TEXT,
                costo_visita FLOAT,
                tiempo_duracion FLOAT,
                cupo_atraccion INTEGER,
                tipo_atraccion TEXT);''')
# Tabla de Promo Porcentual
cur.execute(''' CREATE TABLE IF NOT EXISTS Promociones_porcentuales (
                id INTEGER PRIMARY KEY,
                nombre_promocion TEXT,
                categoria INTEGER,
                atraccion_1 TEXT,
                atraccion_2 TEXT,
                atraccion_n TEXT,
                descuento_porcentual FLOAT);''')
# Tabla de Promo Absoluta
cur.execute(''' CREATE TABLE IF NOT EXISTS Promociones_absolutas (
                id INTEGER PRIMARY KEY,
                nombre_promocion TEXT,
                categoria INTEGER,
                atraccion_1 TEXT,
                atraccion_2 TEXT,
                atraccion_n TEXT,
                descuento_absoluto FLOAT);''')
# Tabla de Promo AxB
cur.execute(''' CREATE TABLE IF NOT EXISTS Promociones_AxB (
                id INTEGER PRIMARY KEY,
                nombre_promocion TEXT,
                categoria INTEGER,
                atraccion_1 TEXT,
                atraccion_2 TEXT,
                atraccion_n TEXT,
                atraccion_gratuita TEXT);''')

cur.execute(''' CREATE TABLE IF NOT EXISTS Atracciones_promos (
                id_atraccion INTEGER,
                id_promo_absoluta INTEGER, 
                id_promo_porcentual INTEGER,
                id_promo_AxB INTEGER,
                FOREIGN KEY (id_atraccion) REFERENCES Atracciones(id),
                FOREIGN KEY (id_promo_absoluta) REFERENCES Promocion_absoluta(id),
                FOREIGN KEY (id_promo_porcentual) REFERENCES Promocion_porcentual(id),
                FOREIGN KEY (id_promo_AxB) REFERENCES Promocion_AxB(id));''')

cur.execute(''' CREATE TABLE IF NOT EXISTS Usuarios_atracciones (
                id_usuario INTEGER,
                id_atraccion INTEGER,
                FOREIGN KEY (id_usuario) REFERENCES Usuarios(id),
                FOREIGN KEY (id_atraccion) REFERENCES Atracciones(id));''')

fileUser = open("__pycache__/usuarios.txt", "r", encoding="utf-8")
lineUser = fileUser.readline()

while lineUser:
    lista_valores = lineUser.split(",") 

    id = lista_valores[0]
    nombre = lista_valores[1]
    categoria_preferida = lista_valores[2]
    presupuesto = lista_valores[3]
    tiempo_disponible = lista_valores[4]

    queryUser = f'''INSERT OR IGNORE INTO Usuarios (id, nombre, categoria_preferida, presupuesto, tiempo_disponible)
                    VALUES({id}, '{nombre}', '{categoria_preferida}', {presupuesto}, {tiempo_disponible});'''
    cur.execute(queryUser)

    lineUser = fileUser.readline()
    con.commit()
fileUser.close()

fileAtracciones = open("__pycache__/atracciones.txt", "r", encoding="utf-8")
lineAtracciones = fileAtracciones.readline()

while lineAtracciones:
    lista_atracciones = lineAtracciones.split(",")

    id = lista_atracciones[0]
    nombre_atraccion = lista_atracciones[1]
    costo_visita = lista_atracciones[2]
    tiempo_duracion = lista_atracciones[3]
    cupo_atraccion = lista_atracciones[4]
    tipo_atraccion = lista_atracciones[5]

    queryAtraccion = f'''INSERT OR IGNORE INTO Atracciones (id ,nombre_atraccion, costo_visita, tiempo_duracion, cupo_atraccion, tipo_atraccion)
                        VALUES({id}, '{nombre_atraccion}', {costo_visita}, {tiempo_duracion}, {cupo_atraccion}, '{tipo_atraccion}');'''
    cur.execute(queryAtraccion)

    lineAtracciones = fileAtracciones.readline()
    con.commit()
fileAtracciones.close()

filePromosAbsolutas = open("__pycache__/promosAbsolutas.txt", "r", encoding="utf-8")
linePromosAbsolutas = filePromosAbsolutas.readline()

while linePromosAbsolutas:
    lista_promos_absolutas = linePromosAbsolutas.split(",")

    id = lista_promos_absolutas[0]
    nombre_promocion = lista_promos_absolutas[1]
    categoria = lista_promos_absolutas[2]
    atraccion_1 = lista_promos_absolutas[3]
    atraccion_2 = lista_promos_absolutas[4]
    atraccion_n = lista_promos_absolutas[5]
    descuento_absoluto = lista_promos_absolutas[6]

    queryPromosAbsolutas = f'''INSERT OR IGNORE INTO Promociones_absolutas(id, nombre_promocion, categoria, atraccion_1, atraccion_2, atraccion_n, descuento_absoluto)
                            VALUES({id}, '{nombre_promocion}', '{categoria}', '{atraccion_1}', '{atraccion_2}', '{atraccion_n}', {descuento_absoluto});'''
    cur.execute(queryPromosAbsolutas)
    
    linePromosAbsolutas = filePromosAbsolutas.readline()
    con.commit()
filePromosAbsolutas.close()

filePromosPorcentuales = open("__pycache__/promosPorcentual.txt", "r", encoding="utf-8")
linePromosPorcentuales = filePromosPorcentuales.readline()

while linePromosPorcentuales:
    lista_promos_porcentuales = linePromosPorcentuales.split(",")

    id = lista_promos_porcentuales[0]
    nombre_promocion = lista_promos_porcentuales[1]
    categoria = lista_promos_porcentuales[2]
    atraccion_1 = lista_promos_porcentuales[3]
    atraccion_2 = lista_promos_porcentuales[4]
    atraccion_n = lista_promos_porcentuales[5]
    descuento_porcentual = lista_promos_porcentuales[6]

    queryPromosPorcentuales = f'''INSERT OR IGNORE INTO Promociones_porcentuales(id, nombre_promocion, categoria, atraccion_1, atraccion_2, atraccion_n, descuento_porcentual)
                                VALUES({id}, '{nombre_promocion}', '{categoria}', '{atraccion_1}', '{atraccion_2}', '{atraccion_n}', {descuento_porcentual});'''
    cur.execute(queryPromosPorcentuales)
    
    linePromosPorcentuales = filePromosPorcentuales.readline()
    con.commit()
filePromosPorcentuales.close()

filePromosAxB = open("__pycache__/promosAxB.txt", "r", encoding="utf-8")
linePromosAxB = filePromosAxB.readline()

while linePromosAxB:
    lista_promos_AxB = linePromosAxB.split(",")

    id = lista_promos_AxB[0]
    nombre_promocion = lista_promos_AxB[1]
    categoria = lista_promos_AxB[2]
    atraccion_1 = lista_promos_AxB[3]
    atraccion_2 = lista_promos_AxB[4]
    atraccion_n = lista_promos_AxB[5]
    atraccion_gratuita = lista_promos_AxB[6]

    queryPromosAxB = f'''INSERT OR IGNORE INTO Promociones_AxB(id, nombre_promocion, categoria, atraccion_1, atraccion_2, atraccion_n, atraccion_gratuita)
                                VALUES({id}, '{nombre_promocion}', '{categoria}', '{atraccion_1}', '{atraccion_2}', '{atraccion_n}', '{atraccion_gratuita}');'''
    cur.execute(queryPromosAxB)
    
    linePromosAxB = filePromosAxB.readline()
    con.commit()
filePromosAxB.close()


con.commit()
cur.close()
con.close()
