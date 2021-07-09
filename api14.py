import requests
import sqlite3


def mi_funcion():
    con = sqlite3.connect('C:/Users/sebas/OneDrive/Escritorio/Integracion/editar/src/db.sqlite3')
    #con = sqlite3.connect("D:/basedatos/db.sqlite3")
    cur = con.cursor()

    #cur.execute('DROP TABLE IF EXISTS Products13 ')
    #cur.execute("CREATE TABLE Products13 (ID INTEGER, NOMBRE TEXT, DESCRIPCION TEXT, VALOR INTEGER, CANTIDAD INTEGER);")

    f = requests.get('http://54.242.117.221:5000/Productos/Categorias')

    to_fb = f.json()

    m = 5
    for i in range(m):
        cat = to_fb[i][0]

        cur.execute("INSERT INTO cart_category (name) VALUES (?);"(cat))

    con.commit()

    cur.execute('''SELECT * FROM cart_category''')
    print(cur.fetchall())

    con.close()

    #cur.execute(mi_funcion())
    #print(mi_funcion())

print(mi_funcion())