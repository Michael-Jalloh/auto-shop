from fabric.api import *

env.use_ssh_config = True

def production():
    env.hosts = ['auto-shop']

def deploy():
    production()
    git()
    sudo('systemctl restart auto_shop')
    #sudo('/etc/init.d/nginx restart')
    #run('whoami')
    #local('whoami')

def update():
    sudo('apt-get update && apt-get upgrade -y')

def git():
    with cd('~/auto-shop'):
        #local('git add .')
        #local('git commit -m {0}'.format('a'))
        #local('git push')
        run('git pull')
