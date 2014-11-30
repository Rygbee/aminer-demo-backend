# !env python2
#encoding: utf8

__author__ = 'yutao'

# Configs
from aminer.config import DefaultConfig

# Models
from models import Person

# Data Inter3ace Clients
from lib.mongoclient import MongoClient


mongo = MongoClient(DefaultConfig.MONGO_ADDRESS, DefaultConfig.MONGO_PORT, DefaultConfig.MONGO_USER,
                    DefaultConfig.MONGO_PASS)

class PersonService(object):
    def __init__(self):
        pass

    #find by id from elastic search
    @staticmethod
    def get_person_by_id(id):
        person = mongo.get_person_by_id(id)
        if not person:
            return {}
        pub_ids = [p["i"] for p in person["pubs"]]
        data = {
            "id": str(person["_id"]),
            "name": person["name"],
            "org": person["org"],
            "contact": person.get("contact", {}),
            "n_pubs": len(pub_ids)
        }

        return data

    @staticmethod
    def get_person_list(skip=0,limit=20):
        persons = mongo.find_person(skip,limit)
        data = []
        for person in persons :
            if person :
                pub_ids = [p["i"] for p in person["pubs"]]
                data.append({
                    "id": str(person["_id"]),
                    "name": person["name"],
                    "org": person["org"],
                    "contact": person.get("contact", {}),
                    "n_pubs": len(pub_ids)
                })
        return data