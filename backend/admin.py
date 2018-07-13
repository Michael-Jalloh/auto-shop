from flask_restful import Resource, reqparse
from flask import send_from_directory
import werkzeug
import os
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity
import logging, datetime
from models import User, Car

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('price')
parser.add_argument('description')
parser.add_argument('pics')
parser.add_argument('model')
parser.add_argument('brand')
parser.add_argument('body_type')
parser.add_argument('year')
parser.add_argument('search')
parser.add_argument('user')
parser.add_argument('transmission')
parser.add_argument('engine')
parser.add_argument('mileage')
parser.add_argument('fuel')
parser.add_argument('drive_train')
parser.add_argument('published')
parser.add_argument('car_id')
parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
parser.add_argument('pic_name')
parser.add_argument('car_id')
parser.add_argument('car_type')
parser.add_argument('type')
parser.add_argument('featured')
parser.add_argument('flagged')
UPLOAD_FOLDER = "static/img"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allow_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_date():
    date = str(datetime.datetime.now()).replace(' ', '-')
    date = date.replace(':','-')
    return date.replace('.','-')

class AdminGetCars(Resource):
    decorators = [jwt_required]
    def get(self):
        user = User.get(id = int(get_jwt_identity()))
        if user.account_type != 'admin':
            return {}, 401
        cars = [car.dictionary() for car in Car.select()]
        return {
            'data':cars,
            'message':'',
            'status':'success'
            }


class AdminDeleteCar(Resource):

    decorators = [jwt_required]

    def delete(self, id):
        try:
            user = User.get(id = int(get_jwt_identity()))
            if user.account_type != 'admin':
                return {}, 401

            if (user == 'admin'):
                car = Car.get(id=int(id))
                car.delete_instance()

                return {
                    'data': '',
                    'messsage': 'Car deleted',
                    'status': 'success'
                    }
            return {
                'data': '',
                'message': 'Forbidden',
                'status': 'error'
                }
        except Exception as e:
            print str(e)

            return {
                'data': '',
                'message': "Car couldn't be deleted",
                'status': 'success'
                }

class FlaggedCars(Resource):

  decorators = []

  def get(self):
    logger = logging.getLogger('app.get-car-')

    cars = [car.dictionary() for car in Car.select().where(Car.flagged == True)]

    return {
        'data': cars,
        'message':'',
        'status':'success'
        }

class AdminFeatured(Resource):
  decorators = [jwt_required]

  def post(self):
    logger = logging.getLogger('app.post-admin-featured')
    data = parser.parse_args()

    try:
        user = User.get(id = int(get_jwt_identity()))
        if user.account_type != 'admin':
            return {}, 401
        car = Car.get(id=int(data['car_id']))
        car.featured = False
        if data['featured'] == 'True':
            car.featured =  True

        car.save()
        if car.featured:
            return {
                    'data':'Featured',
                    'message':'Car {} has been featured'.format(car.name),
                    'status': 'success'
                    }
        return {
            'data': 'Featured',
            'message':'Car {} has been removed from the featured cars'.format(car.name),
            'status':'success'
            }

    except Exception as e:
        print str(e)
        logger.error(e)
        return {
                'data':'',
                'message':'An error occur',
                'status': 'error'
                }

class AdminPublished(Resource):
  decorators = [jwt_required]

  def post(self):
    logger = logging.getLogger('app.post-admin-published')
    data = parser.parse_args()
    try:
        user = User.get(id = int(get_jwt_identity()))
        if user.account_type != 'admin':
            return {}, 401

        car = Car.get(id=int(data['car_id']))
        car.published = False
        if data['published'] == 'True':
            car.published =  True

        car.save()
        if car.published:
            return {
                    'data':'',
                    'message':'Car {} has been published'.format(car.name),
                    'status': 'success'
                    }
        return {
            'data': '',
            'message':'Car {} has been removed from the published cars'.format(car.name),
            'status':'success'
            }

    except Exception as e:
        print str(e)
        logger.error(e)
        return {
                'data': '',
                'message': 'An error occur',
                'status': 'error'
                }

class AdminUsers(Resource):
    decorators = [jwt_required]

    def get(self):
        users = [user.dictionary() for user in User.select()]
        return {
            'data':users,
            'message': '',
            'status':'success'
            }

class AdminFlagCar(Resource):
    decorators = [jwt_required]

    def post(self):
        user = User.get(id = int(get_jwt_identity()))
        if user.account_type != 'admin':
            return {}, 401

        data = parser.parse_args()
        logger = logging.getLogger('app.admin-flagger')
        car = Car.get(id=int(data['car_id']))

        car.flagged = False
        if data['flagged'] == 'True':
            car.flagged = True

        car.save()
        return {
            'data': '',
            'message': 'Updated',
            'status': ''
            }
