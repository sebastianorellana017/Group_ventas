import requests
import sqlite3


def mi_funcion():
    con = sqlite3.connect('C:/Users/sebas/OneDrive/Escritorio/Integracion/editar/src/db.sqlite3')
    #con = sqlite3.connect("D:/basedatos/db.sqlite3")
    cur = con.cursor()

    #cur.execute('DROP TABLE IF EXISTS Products13 ')
    #cur.execute("CREATE TABLE Products13 (ID INTEGER, NOMBRE TEXT, DESCRIPCION TEXT, VALOR INTEGER, CANTIDAD INTEGER);")

    r = requests.get('http://54.242.117.221:5000/Productos')
    to_db = r.json()

    n = 10

    for i in range(n): 
       slu = to_db[i][1]
       des = to_db[i][1]
       img = to_db[i][10]
       code = to_db[i][6]
       val = to_db[i][4]
       can = to_db[i][5]
       mar = to_db[i][3]
       pes = to_db[i][7]
       tam = to_db[i][8]
       prov = to_db[i][9]
       #cat = to_db[i][2]
       
       #cur.execute("INSERT INTO cart_product ( slug, nombre, image, descripcion, valor, cantidad, marca) VALUES (? ,? ,?, ?, ?, ?, ?);", ( slu,des, img,code, val, can, mar))
       cur.execute("INSERT INTO cart_product ( slug, nombre, image,descripcion, valor, peso, tamano, proveedor,cantidad, marca) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", ( slu,des,img,code, val, pes, tam, prov,can, mar))
    
   

    con.commit()

    cur.execute('''SELECT * FROM cart_product''')
    print(cur.fetchall())

    con.close()

    #cur.execute(mi_funcion())
    #print(mi_funcion())

print(mi_funcion())