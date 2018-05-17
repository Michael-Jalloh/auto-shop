from flask_restful import Resource, reqparse
import logging
from datetime import timedelta
from models import User

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('email')
parser.add_argument('password')
parser.add_argument('password_confirm')
parser.add_argument('pics')
parser.add_argument('logo')
parser.add_argument('account_type')
parser.add_argument('body_type')
parser.add_argument('name')
parser.add_argument('search')
parser.add_argument('user')


class Info(Resource):

    decorators = []

    def get(self):
