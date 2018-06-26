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
parser.add_argument('file',type=werkzeug.datastructures.FileStorage, location='files')
parser.add_argument('pic_name')
parser.add_argument('car_id')
parser.add_argument('car_type')
parser.add_argument('type')

UPLOAD_FOLDER = "static/img"
ALLOWED_EXTENSIONS = set(['png', 'jpg','jpeg'])


def allow_file(filename):
    return '.' in filename and \
            filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

def get_date():
    date = str(datetime.datetime.now()).replace(' ','-')
    date = date.replace(':','-')
    return date.replace('.','-')

class AdminGetCars(Resource):
    def get(self):
        cars = [car.dictionary() for car in Car.select()]
        return {
            'data':cars,
            'message':'',
            'status':'success'
            }

class AdminDeleteCar(Resource):

    def delete(self,id):
        try:
            car = Car.get(id=int(id))
            car.delete_instance()

            return {
                'data':'',
                'messsage':'Car deleted',
                'status':'success'
                }
        except Exception as e:
            print str(e)

            return {
                'data':'',
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
