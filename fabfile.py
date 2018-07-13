from fabric.api import *

def dev():
    build()
    run()

def build():
    local('cd frontend && npm run build')

def run():
    local('cd backend && python app.py')
