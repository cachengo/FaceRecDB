from annoy import AnnoyIndex
import numpy as np
import pickle
import sqlite3
 
 

with sqlite3.connect('/db/facerec.db') as conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM photo_features")
 
    rows = cur.fetchall()
    tf = AnnoyIndex(128)
    caffe = AnnoyIndex(10575)
    for row in rows:
        if row[2] == 'tensorflow':
            tf.add_item(row[0], pickle.loads(str(row[3]), encoding='bytes'))
        elif row[2] == 'caffe':
            caffe.add_item(row[0], pickle.loads(str(row[3]), encoding='bytes'))
    tf.build(10)
    caffe.build(10)
    tf.save('/db/tf.ann')
    caffe.save('/db/caffe.ann')
