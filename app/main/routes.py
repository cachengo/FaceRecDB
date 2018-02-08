from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from app import db, tf_feats, caffe_feats
from app.models import PhotoFeatures
from app.main import bp

import pickle
import numpy as np

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    return 'Yo'


@bp.route('/add', methods=['POST'])
def add_vector():
    data = request.get_json()
    features = PhotoFeatures(person_name=data['name'], 
                             vector=pickle.loads(data['vector']), 
                             model=data['model']
                            )
    db.session.add(features)
    db.session.commit()
    return 'Vector added. It will be queriable in the next app restart'


@bp.route('/find', methods=['POST'])
def find_vector():
    data = request.get_json()
    vector = pickle.loads(data['vector'])
    model = data.get('model', '')
    if model == 'tensorflow':
        match = tf_feats.get_nns_by_vector(vector, 1, search_k=-1, include_distances=True)
    elif model == 'caffe':
        match = caffe_feats.get_nns_by_vector(vector, 1, search_k=-1, include_distances=True)
    else:
        return 'Unsupported model'

    hit = PhotoFeatures.query.get(match[0][0])
    result = {'name': hit.person_name, 'distance': match[1][0]}
    return jsonify(result)
