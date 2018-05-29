from flask_restful import Resource, reqparse
import logging
from flask import send_from_directory
from werkzeug.datastructures import FileStorage
from datetime import timedelta
import os
from models import User

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('email')
parser.add_argument('password')
parser.add_argument('location')
parser.add_argument('contact')
parser.add_argument('bio')
parser.add_argument('search')
parser.add_argument('comfirm_password')
parser.add_argument('user_id')
parser.add_argument('id')
parser.add_argument('file', type=FileStorage, location='files')

UPLOAD_FOLDER = "static/img/profiles"
ALLOWED_EXTENSIONS = set(['png', 'jpg','jpeg'])


class ProfileUpload(Resource):

    decorators = []

    def post(self):
        data = parser.parse_args()
        user = User.get(id=int(data['user_id']))
        if data['file'] == "":
            return {
                'data': '',
                'message':'No photo found',
                'status':'error'
                }
        photo = data['file']

        if photo:
            filename = user.email+'.png'
            user.avatar = filename
            user.save()
            photo.save(os.path.join(UPLOAD_FOLDER,filename))
            u = user.dictionary()
            return {
                'data':u,
                'message':'profile uploaded',
                'status':'success'
                }
        return {
            'data':'',
            'message':'photo not uploaded',
            'status':'error'
            }

class GetProfilePic(Resource):
    def get(self, user_id):
        user = User.get(id=int(user_id))
        return send_from_directory(UPLOAD_FOLDER,user.avatar)


class EditProfile(Resource):
    def post(self):
        data = parser.parse_args()
        user = User.get(id=int(data['id']))
        if data['username']:
            user.username = data['username']
        if data['email']:
            user.email = data['email']
        if data['password'] and (data['password'] == data['comfirm_password']):
            user.password = data['password']
        if data['location']:
            user.location = data['location']
        if data['contact']:
            user.contact = data['contact']
        if data['bio']:
            user.bio = data['bio']
        user.save()

        return {
            'data': user.dictionary(),
            'message': 'Profile Updated',
            'status': 'success'
            }

class GetProfile(Resource):
    def get(self,user_id):
        user = User.get(id=int(user_id))
        return {
            'data': user.dictionary(),
            'message':'',
            'status':'success'
            }
