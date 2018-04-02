from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt
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


class Signup(Resource):
    decorators = []

    def post(self):
        logger = logging.getLogger('app.user-signup-post')
        data = parser.parse_args()
        user = User()
        user.username = data['username']
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

class Login(Resource):
    def post(self):
        data = parser.parse_args()
        logger = logging.getLogger('app.user-login-post')
        try:
            email = data['email']
            password = data['password']
            user = User.get(User.email == email)
            expires = timedelta(days=0.5)
            if user is not None and user.verify_password(password):
                access_token = create_access_token(identity=user.id)
                refresh_token = create_refresh_token(identity=user.id)
                return {
                    'status':'success',
                    'message':'Logged in as {}'.format(user.username),
                    'access-token':access_token,
                    'refresh-token': refresh_token
                    }
            else:
                return {
                        'status':'error',
                        'message':'Wrong credentials'
                        }

        except Exception as e:
            logger.error(str(e))
            return {
                    'status':'error',
                    'message':'Exception - Wrong credentials'
                    }



class TokenRefresh(Resource):
    decorators = [jwt_refresh_token_required]

    def get(self):
        id = get_jwt_identity()
        access_token = create_access_token(identity = id)
        return {
                "status":"success",
                "message":"Your token has been refreshed",
                "access-token":access_token
                }


class LogoutAccesToken(Resource):
    decorators = [jwt_required]
    def get(self):
        jti = get_raw_jwt()['jti']
        try:
            RevokedToken.create(jti=jti)
            return {'status':'success',
                    'message':'You are now logged out'
                    }
        except:
            return {
                    'status':'error',
                    'message':'An error occur, Contact Admin'
                    }

class LogoutRefreshToken(Resource):
    decorators = [jwt_refresh_token_required]

    def get(self):
        jti = get_raw_jwt()
        try:
            RevokedToken.create(jti=jti)
            return {
                    'status':'succes',
                    'message':'Refresh Token revoked'
                    }
        except:
            return {
                    'status':'error',
                    'message':'An error occur, Contact Admin'
                    }
