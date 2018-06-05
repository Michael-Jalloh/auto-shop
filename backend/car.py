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
                'data': car.dictionary(),
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
            query.append(car.dictionary())

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
            car = Car.get(id=int(car_id))
            return {
                'message':'',
                'data': car.dictionary(),
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


class GetImage(Resource):
    def get(self, filename):
        return send_from_directory(UPLOAD_FOLDER,filename)


class GetImagebyId(Resource):
    def get(self,id):
        try:
            car = Car.get(id=int(id))
            return send_from_directory(UPLOAD_FOLDER, car.pics)
        except Exception as e:
            return {
                'data':'',
                'message':'Image not found',
                'status':'error'
                }


class UserCars(Resource):
    def get(self,user):
        try:
            cars = [car.dictionary() for car in Car.select().where(Car.owner==int(user)).join(User)]
            if cars:
                return {
                    'data': cars,
                    'message':'',
                    'status':'success'
                    }
            else:
                return {
                    'data':'',
                    'message':'User has not cars',
                    'status':'error'
                    }
        except Exception as e:
                print str(e)
                return {
                    'data':'',
                    'message':'An error occur pls contact admin',
                    'status': 'error'
                    }

class DeleteCar(Resource):
    decorators = [jwt_required]

    def delete(self, id):
        user = User.get(int(get_jwt_identity()))
        car = Car.get(id=int(id))
        if car.owner == user:
            print car.pics
            if os.path.isfile(UPLOAD_FOLDER+'/'+car.pics):
                os.remove(UPLOAD_FOLDER+'/'+car.pics)
            car.delete_instance()
            return {
                'data': '',
                'message':'The car has been deleted from the server',
                'status':'success'
                }
        else:
            return {
                'data':'',
                'message':'You do not own this car',
                'status':'error'
                }
