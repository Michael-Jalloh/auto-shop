from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
import logging
from models import User

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('email')
parser.add_argument('password')
parser.add_argument('pics')
parser.add_argument('logo')
parser.add_argument('account_type')
parser.add_argument('body_type')
parser.add_argument('name')
parser.add_argument('search')
parser.add_argument('user')


class Signup(Resource):
    decorators = []

    def post(self):
        logger = logging.getLogger('app.user-signup-post')
        data = parser.parse_args()
        user = User()
        user.username = data['username']
        user.account_type = data['account_type']
        user.email = data['email']
        user.password = data['password']
        try:
            user.save()
            return {
                'data':'',
                'message':'Your account has been created',
                'status':'succes'
                }
        except Exception as e:
            logger.error(str(e))
            return {
                'data':'',
                'message':'An error occur',
                'status':'error'
                }
