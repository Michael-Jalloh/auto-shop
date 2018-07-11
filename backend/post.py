from flask_restful import Resource, reqparse
from flask import send_from_directory
import werkzeug
import os
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity
import logging, datetime
from models import User, Post

parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('content')
parser.add_argument('pics')
parser.add_argument('id')
parser.add_argument('published')
parser.add_argument('file',type=werkzeug.datastructures.FileStorage, location='files')
parser.add_argument('pic_name')
parser.add_argument('category')
UPLOAD_FOLDER = "static/img"
ALLOWED_EXTENSIONS = set(['png', 'jpg','jpeg'])


def allow_file(filename):
    return '.' in filename and \
            filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

def get_date():
    date = str(datetime.datetime.now()).replace(' ','-')
    date = date.replace(':','-')
    return date.replace('.','-')

class PostPhotoUpload(Resource):
    decorators=[]

    def post(self):
        data = parser.parse_args()
        if (data['id'] == ''):
            post = Post()
            post.title = data['title']
            post.save()
        else:
            post = Post.get(id=int(data['id']))
        if data['file'] == "":
            return {
                    'data':'',
                    'message':'No photo found',
                    'status':'Error'
                    }
        photo = data['file']

        if photo:
            filename = get_date().encode('hex')+'.png'
            post.pic = filename
            post.save()
            photo.save(os.path.join(UPLOAD_FOLDER,filename))
            return {
                    'data': filename,
                    'message':'photo uploaded',
                    'status':'success'
                    }
        print data
        return {
                'data':'',
                'message':'ok',
                'status':'success'
                }


class AddPost(Resource):
    decorators = [] #[jwt_required]

    def post(self):
        user = get_jwt_identity()
        data = parser.parse_args()
        logger = logging.getLogger('app.add-post-get')
        post = Post()
        print "Title: ", data['title']
        post.title = data['title']
        post.content = data['content']
        if (data['published'] == 'True'):
            post.published = True
        try:
            post.save()
            return {
                'data': post.dictionary(),
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

class EditPost(Resource):
    decorators = [] #[jwt_required]

    def post(self):
        #user = User.get(int(get_jwt_identity()))
        data = parser.parse_args()
        logger = logging.getLogger('app.add-post-get')
        post = Post.get(id=int(data['id']))

        post.title = data['title']
        post.content = data['content']
        post.published = False
        if (data['published'] == 'True'):
            post.published = True
        try:
            post.save()
            return {
                'data':post.dictionary(),
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
            'message':"You aren't the creator of the post",
            'status':'error'
            }


class GetPosts(Resource):
    decorators=[]

    def get(self):
        posts = Post.get_published_post()
        return {
                'data':posts,
                'message':'',
                'status':'success'
                }

class GetAllPosts(Resource):
    decorators=[]

    def get(self):
        posts = Post.get_all_post()
        return {
                'data':posts,
                'message':'',
                'status':'success'
                }

class GetPost(Resource):
    decorators = []

    def get(self, post_id):
        data = parser.parse_args()
        logger = logging.getLogger('app.view-post-post')
        try:
            post = Post.get(id=int(post_id))
            return {
                'message':'',
                'data': post.dictionary(),
                'status':'succes'
                }
        except Exception as e:
            logger.error(str(e))
            return {
                    'message':'Post does not exist',
                    'data':'',
                    'status':'error'
                    }

class GetDrafts(Resource):
    decorators = []

    def get(self):
        posts = Post.get_drafts()
        return {
            'data': posts,
            'message':'',
            'status':'success'
            }

class GetImage(Resource):
    def get(self, filename):
        return send_from_directory(UPLOAD_FOLDER,filename)


class GetImagebyId(Resource):
    def get(self,id):
        try:
            post = Post.get(id=int(id))
            return send_from_directory(UPLOAD_FOLDER, post.pic)
        except Exception as e:
            return {
                'data':'',
                'message':'Image not found',
                'status':'error'
                }



class DeletePost(Resource):
    decorators = [] #[jwt_required]

    def delete(self, id):
        #user = User.get(int(get_jwt_identity()))
        post = Post.get(id=int(id))

        if os.path.isfile(UPLOAD_FOLDER+'/'+post.pic):
            os.remove(UPLOAD_FOLDER+'/'+post.pic)
        post.delete_instance()
        return {
            'data': '',
            'message':'The post has been deleted from the server',
            'status':'success'
            }
