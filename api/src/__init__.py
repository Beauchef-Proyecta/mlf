from flask import Flask
from ..video_feed import VideoFeed
from ..robot_control import RobotController

video_feed_builder = VideoFeed()
robot_controller = RobotController()

def create_app() -> Flask:
    """Factory pattern of Flask Application"""
    app: Flask = Flask(__name__)

    # aca se pueden inicializar mas cosas como bases de datos

    from .views import (
        video_feed_bp,
        robot_control_bp
    )

    app.register_blueprint(video_feed_bp)
    app.register_blueprint(robot_control_bp)
    
    return app