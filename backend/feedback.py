from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt
from models import  FeedBack

parser = reqparse.RequestParser()
parser.add_argument('email')
parser.add_argument('name')
parser.add_argument('last_name')
parser.add_argument('tel')
parser.add_argument('msg')


class FeedBacks(Resource):

    def post(self):
        data = parser.parse_args()
        f = FeedBack()
        f.name = data['name']
        f.last_name = data['last_name']
        f.msg = data['msg']
        f.email = data['email']
        f.tel = data['tel']
        f.save()
        return {
            'status': 'OK',
            'message': 'Your message have been saved',
            'data': ''
        }
