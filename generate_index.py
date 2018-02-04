from annoy import AnnoyIndex
import numpy as np
import pickle
import sqlite3
 
 

with sqlite3.connect('/db/facerec.db') as conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM photo_features")
 
    rows = cur.fetchall()
    t = AnnoyIndex(128)
    for row in rows:
        t.add_item(row[0], pickle.loads(str(row[3])))
    t.build(10)
    t.save('index.ann')
