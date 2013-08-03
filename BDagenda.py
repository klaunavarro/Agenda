# -*- coding: utf-8 -*-

import os
import sqlite3

def create_db(db_name):
	
    conn = sqlite3.connect(db_name)
    
    c= conn.cursor()
    
    query = """CREATE TABLE calendarios (id_calendario integer PRIMARY KEY AUTOINCREMENT,
                                         nombre text)"""
      
    c.execute(query)
    
    
    query = """CREATE TABLE eventos(id_evento integer primary key AUTOINCREMENT,
                                     detalle text,
                                     fecha_desde datetime,
                                     fecha_hasta datetime,
                                     lugar text,
                                     participantes text,
                                     fk_id_calendario integer,
			                         FOREIGN KEY (fk_id_calendario) REFERENCES calendarios (id_calendario))"""
    c.execute(query)
    
if __name__ == "__main__":
    db_name = 'base12.db'
    if not os.path.exists(db_name):
        create_db(db_name)
        
    conn = sqlite3.connect(db_name)
    c = conn.cursor()


    query = "INSERT INTO calendarios(id_calendario,nombre) VALUES (?,?)"	
    
    v0 =["0", "Trabajo"]
    v1 =["1","Familia"]
    v2 =["2",u"Recreación"]
    
    c.execute("INSERT INTO calendarios VALUES (?,?)",v0)
    c.execute("INSERT INTO calendarios VALUES (?,?)",v1)
    c.execute("INSERT INTO calendarios VALUES (?,?)",v2)
    
    conn.commit()

    	
    query1 = "INSERT INTO eventos(id_evento,detalle,fecha_desde,fecha_hasta,lugar,participantes,fk_id_calendario) VALUES (?,?,?,?,?,?,?)"
   
    e1=["3",u"Reunión de jefes","2013-08-06 08:00:00","2013-08-06 09:30:00",
        "Oficina 2",
        "Sr. Castro , Sr. Jerez",
        "0"]
    e2=["4","Entregar informe final proyecto","2013-08-07 13:00:00","2013-11-14 13:00:00",
        "Oficina",
         u"Sr. Yañez , Srta. Gallardo, Sr. Alvarado",
        "0"]
    e3=["5",u"Cumpleaños de Mamá","2013-08-23 07:30:00","2013-08-24 04:00:00",
        "Casa de Jimena",
        "Toda la familia",
        "1"]
    e4=["6","Partido de futbol de Miguel","2013-08-27 16:00:00","2013-08-27 18:00:00",
        "Cancha Rayada",
        "Miguel, Carla, Jaime",
        "1"]
    e5=["7","Partido baby futbol","2013-08-29 21:00:00","2012-08,29 23:00:00",
        "Cancha Liceo Industrial",
        "Colegas de trabajo",
        "2"]
    e6=["8","Ir al cine ","2013-09-01 22:00:00","2013-09-02 00:30:00",
        "Cine Movieland",
        "Carla,Alejandra, Miguel",
        "2"]
    e7=["9",u"Curso de capacitación","2013-11-02 08:00:00","2014-02-02 11:00:00",
        "Empresa de Construccion ADHY S.A",
        "Trabajadores Planta C",
        "0"]    
    e8=["10",u"Reunión del personal","2013-10-15  09:30:00","2013-10-15 11:00:00",
        "Sala de reuniones",
        "Trabajadores planta A",
        "0"]    
    e9=["11","Cena de navidad","2013-12-24 20:00:00","2013-12-25 00:00:00",
        "Casa de Jaime",
        "Toda la familia",
        "1"]        
    e10=["12",u"Graduación de Tomás","2013-12-10 14:00:00","2013-12-10 17:00:00",
         "Gimnasio Liceo Galvarino Riveros",
         "Familia y amigos",
         "1"]        
    e11=["13","Paseo en bote","2013-12-11 12:00:00","2013-12-11 14:00:00",
         u"Río calle-calle",
         "Familia",
         "2"]        
    e12=["14","Caminata","2013-12-20 16:00:00","2013-12-20 18:00:00",
         u"Bosque Nativo Chiloé",
         "Familia y amigos",
         "2"]        
        
    c.execute("INSERT INTO eventos VALUES (?,?,?,?,?,?,?)",e1)
    c.execute("INSERT INTO eventos VALUES (?,?,?,?,?,?,?)",e2)
    c.execute("INSERT INTO eventos VALUES (?,?,?,?,?,?,?)",e3)
    c.execute("INSERT INTO eventos VALUES (?,?,?,?,?,?,?)",e4)
    c.execute("INSERT INTO eventos VALUES (?,?,?,?,?,?,?)",e5)
    c.execute("INSERT INTO eventos VALUES (?,?,?,?,?,?,?)",e6)
    c.execute("INSERT INTO eventos VALUES (?,?,?,?,?,?,?)",e7)
    c.execute("INSERT INTO eventos VALUES (?,?,?,?,?,?,?)",e8)
    c.execute("INSERT INTO eventos VALUES (?,?,?,?,?,?,?)",e9)
    c.execute("INSERT INTO eventos VALUES (?,?,?,?,?,?,?)",e10)
    c.execute("INSERT INTO eventos VALUES (?,?,?,?,?,?,?)",e11)
    c.execute("INSERT INTO eventos VALUES (?,?,?,?,?,?,?)",e12)   
    
    conn.commit()
