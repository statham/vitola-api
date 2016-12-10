from flask_script import Manager
from flask_script import Server

from main import app

manager = Manager(app)

manager.add_command('runserver', Server())

if __name__ == '__main__':
    manager.run()
