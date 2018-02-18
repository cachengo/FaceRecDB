from annoy import AnnoyIndex
import numpy as np
import pickle
import sqlite3
 
 

with sqlite3.connect('/db/facerec.db') as conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM photo_features")
 
    rows = cur.fetchall()
    tf = AnnoyIndex(128)
    caffe = AnnoyIndex(256)
    for row in rows:
        if row[3] == 'tensorflow':
            tf.add_item(row[0], pickle.loads(str(row[2])))
        elif row[3] == 'caffe':
	    print(len(row[2]))
            caffe.add_item(row[0], pickle.loads(str(row[2])))
    tf.build(10)
    caffe.build(10)
    tf.save('/db/tf.ann')
    caffe.save('/db/caffe.ann')
