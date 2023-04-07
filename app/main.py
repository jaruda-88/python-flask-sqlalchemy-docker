import os
import unittest

from flask import Flask
from commons.config import get_config
from flask_bcrypt import Bcrypt


flask_bcrypt = Bcrypt()


def create_app(build_type: str):
    '''
    create flask app
    :param build_type: build env
    :return: app
    '''
    
    # create app
    app = Flask(__name__)

    # set config
    app.config.from_object(get_config(build_type))

    # set db

    # set protected
    flask_bcrypt.init_app(app)

    return app

# set flask app
app = create_app(os.environ.get('API_ENV', 'test'))
app.app_context().push()

if __name__ == '__main__':
    app.run()



