from flask_restful import Resource, reqparse
from flask import request
import os
from flask_jwt_extended import jwt_required, get_jwt_identity
import logging, datetime
from models import User, Post, PageView
import urlparse
from peewee import *

parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('params')
parser.add_argument('type')
parser.add_argument('category')
parser.add_argument('is_page')

class TrackPage(Resource):

    decorators = []

    def post(self):
        data = parser.parse_args()
        data['request'] = request
        PageView.create_from_request(**data)
        return {}

class Last7days(Resource):

    decorators = []

    def get(self):
        week_ago = datetime.date.today() - datetime.timedelta(days=7)
        base = PageView.select().where(PageView.timestamp >= week_ago)
        last_7days_view = base.count()
        diff_users = base.select(PageView.ip).ground_by(PageView.ip).count()
        top_10pages = base.select(PageView.title, fn.Count(PageView.id))
                      .group_by(PageView.title)
                      .order_by(fn.Count(PageView.id).desc())
                      .tuples())[:5]
        
