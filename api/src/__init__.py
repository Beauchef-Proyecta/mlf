import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from flask import Flask

import os
import sys

def create_app() -> Flask:
    """Factory pattern of Flask Application"""
    app: Flask = Flask(__name__, template_folder='../templates')

    # aca se pueden inicializar mas cosas como bases de datos

    from .views import (
        video_feed_bp
    )

    app.register_blueprint(video_feed_bp)
    #app.register_blueprint(robot_control_bp)
    
    return app