# -*- coding: utf-8 -*-

import json

from flask import Blueprint, make_response

api = Blueprint('api', __name__, url_prefix='/api')

from flask.ext.cors import cross_origin
from flask import request

from aminer.service.person.service import PersonService

from lib.mongoclient.mongoclient import MongoClient
from flask import Blueprint, session, make_response, request, current_app

person_service = PersonService()


from aminer.config import DefaultConfig


@api.route('/people/basic/<id>', methods=['GET'])
@cross_origin(headers=['Content-Type', 'Authorization'])
def get_people_by_id(id):
    data = person_service.get_person_by_id(id)
    response = make_response(json.dumps(data))
    response.headers['Content-Type'] = 'application/json'
    return response

@api.route("/people/list/<int:offset>/<int:size>",methods=['GET'])
@cross_origin(headers=['Content-Type', 'Authorization'])
def get_people_list(offset,size):
    data = person_service.get_person_list(offset,size)
    response = make_response(json.dumps(data))
    response.headers['Content-Type'] = 'application/json'
    return response
