from fabric.api import *

env.use_ssh_config = True

def production():
    env.hosts = ['wide']

def deploy():
    production()
    git()
    sudo('systemctl restart wide-express')
    #sudo('/etc/init.d/nginx restart')
    #run('whoami')
    #local('whoami')

def update():
    sudo('apt-get update && apt-get upgrade -y')

def git():
    with cd('~/webapps/wide-express'):
        #local('git add .')
        #local('git commit -m {0}'.format('a'))
        #local('git push')
        run('git pull')
