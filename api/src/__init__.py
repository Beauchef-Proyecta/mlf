from flask import Flask
import os
import sys

sys.path.insert(0, os.path.abspath('..'))
from mlf.core.camera import VideoStream

from mlf.api.video_feed import VideoFeed
from mlf.api.robot_control import RobotController

video_feed_builder = VideoFeed()
robot_controller = RobotController()

def create_app() -> Flask:
    """Factory pattern of Flask Application"""
    app: Flask = Flask(__name__, template_folder='../templates')

    # aca se pueden inicializar mas cosas como bases de datos

    from .views import (
        video_feed_bp,
        robot_control_bp
    )

    app.register_blueprint(video_feed_bp)
    app.register_blueprint(robot_control_bp)
    
    return app