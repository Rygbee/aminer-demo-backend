__author__ = 'yutao'
import time

import pymongo
from bson.objectid import ObjectId
from flask import session, request

## from lib.utils.http import get_remote_ip


class MongoClient(object):
    def __init__(self, host, port, username, password):
        self.db = pymongo.Connection(host, port)["bigsci_test"]
        self.db.authenticate(username, password)
        self.person_col = self.db['people']
        self.log_col = self.db['log']
        self.usr_col = self.db['usr']
        self.pub_col = self.db['publication_dupl']


        self.post_col = self.db['post_content']

        self.in_followed = self.db['followship_in']  # build social network
        self.out_following = self.db['followship_out']
        # self.oausr_col = self.db['oausr']
        self.ccfjconflevel = self.db['ccfjconflevel']
        self.bestpaper = self.db['bestpaper']
        self.venue = self.db['venue_dupl']
        self.venue_def = self.db['venue_def']
        self.publication = self.db['publication_dupl']


    # Author Service
    def get_person_by_id(self, _id):
        try:
            result = self.person_col.find_one({"_id": ObjectId(_id)})
        except:
            return {}
        return result

    def find_person(self,skip=0,limit=20):
        result = self.person_col.find({}).skip(skip).limit(limit)
        return result