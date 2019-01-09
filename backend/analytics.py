from flask_restful import Resource, reqparse
from flask import request
import os
from flask_jwt_extended import jwt_required, get_jwt_identity
import logging, datetime
from models import User, Post, Tracker
import urlparse
from peewee import *

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('params')
parser.add_argument('type')
parser.add_argument('category')
parser.add_argument('post_id')

class TrackPage(Resource):

    decorators = []

    def post(self):
        data = parser.parse_args()
        data['request'] = request
        print "[*] Request: ", data["request"]
        Tracker.create_from_request(**data)
        return {}

class Last7days(Resource):

    decorators = [jwt_required]

    def get(self):
        user = User.get(id=int(get_jwt_identity()))
        if user.account_type != "admin":
            return {}, 403
            
        week_ago = datetime.date.today() - datetime.timedelta(days=7)
        base = Tracker.select().where((Tracker.timestamp >= week_ago) & (Tracker.page_type == "car"))
        last_7days_view = base.count()
        diff_users = base.select(Tracker.ip).group_by(Tracker.ip).count()
        top_10pages = base.select(Tracker.title, fn.Count(Tracker.id)).group_by(Tracker.title).order_by(fn.Count(Tracker.id).desc()).tuples()[:10]
        for track in top_10pages:
            print track
        return {
            "data":{"last_7days":last_7days_view, "top_10":top_10pages
            },
            "message":"",
            "status":"success"
            }
