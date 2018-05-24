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

UPLOAD_FOLDER = "static/img"
ALLOWED_EXTENSIONS = set(['png', 'jpg','jpeg'])


def allow_file(filename):
    return '.' in filename and \
            filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

def get_date():
    date = str(datetime.datetime.now()).replace(' ','-')
    date = date.replace(':','-')
    return date.replace('.','-')

class PhotoUpload(Resource):
    decorators=[]

    def post(self):
        data = parser.parse_args()
        car = Car.get(id=int(data['car_id']))
        if data['file'] == "":
            return {
                    'data':'',
                    'message':'No photo found',
                    'status':'Error'
                    }
        photo = data['file']

        if photo:
            filename = get_date()+'.png'
            car.pics = filename
            car.save()
            photo.save(os.path.join(UPLOAD_FOLDER,filename))
            c = Car.car_to_dict(car)
            print c
            return {
                    'data': c,
                    'message':'photo uploaded',
                    'status':'success'
                    }
        print data
        return {
                'data':'',
                'message':'ok',
                'status':'success'
                }

class GetPhoto(Resource):

    decorators=[]

    def get(self, name):
        return send_from_directory(name)


class AddCar(Resource):
    decorators = [jwt_required]

    def post(self):
        user = get_jwt_identity()
        data = parser.parse_args()
        logger = logging.getLogger('app.add-car-get')
        car = Car()
        car.name = data['name']
        car.price = data['price']
        car.description = data['description']
        car.brand = data['brand']
        car.model = data['model']
        d = data['year'].split(',')
        car.year = date(int(d[0]), int(d[1]), int(d[2]))
        car.transmission = data['transmission']
        car.engine = data['engine']
        car.mileage = data['mileage']
        car.fuel = data['fuel']
        car.drive_train = data['drive_train']
        try:
            car.owner = int(user) #User.get(id=int(user)) #int(data['user']))
            car.save()
            return {
                'data':Car.car_to_dict(car),
                'message':'Posting saved',
                'status':'success'
                }
        except Exception as e:
            logger.error(str(e))
            return {
                'data':'',
                'message':'And error occur please check your fields',
                'status':'error'
                }

class EditCar(Resource):
    decorators = [jwt_required]

    def post(self):
        user = User.get(int(get_jwt_identity()))
        data = parser.parse_args()
        logger = logging.getLogger('app.add-car-get')
        car = Car.get(id=int(data['car_id']))
        if car.owner == user:
            car.name = data['name']
            car.price = data['price']
            car.description = data['description']
            car.brand = data['brand']
            car.model = data['model']
            d = data['year'].split(',')
            car.year = date(int(d[0]), int(d[1]), int(d[2]))
            car.transmission = data['transmission']
            car.engine = data['engine']
            car.mileage = data['mileage']
            car.fuel = data['fuel']
            car.drive_train = data['drive_train']
            try:
                car.save()
                return {
                    'data':Car.car_to_dict(car),
                    'message':'Posting saved',
                    'status':'success'
                    }
            except Exception as e:
                logger.error(str(e))
                return {
                'data':'',
                'message':'And error occur please check your    fields',
                'status':'error'
                }
        return {
            'data':'',
            'message':"You aren't the creator of the car",
            'status':'error'
            }


class GetCars(Resource):
    decorators=[]

    def get(self):
        cars = Car.select()
        query = []
        for car in cars:
            query.append(Car.car_to_dict(car))

        return {
                'data':query,
                'message':'',
                'status':'success'
                }

class GetCar(Resource):
    decorators = []

    def get(self, car_id):
        data = parser.parse_args()
        logger = logging.getLogger('app.view-car-post')
        try:
            car = Car.car_to_dict(Car.get(id=int(car_id)))
            return {
                'message':'',
                'data': car,
                'status':'succes'
                }
        except Exception as e:
            logger.error(str(e))
            return {
                    'message':'An error occur',
                    'data':'',
                    'status':'error'
                    }

class GetMyCars(Resource):
    decorators = [jwt_required]

    def get(self):
        user = User.get(int(get_jwt_identity()))
        return {
            'status':'OK',
            'message':'',
            'data': user.get_cars()
            }

class TestCar(Resource):
    def post(self):
        data = parser.parse_args()
        print data['file']
        return {
                'data':'',
                'message': 'data received',
                'status': 'success'
                }
class GetImage(Resource):
    def get(self, filename):
        send_from_directory(UPLOAD_FOLDER,filename)
