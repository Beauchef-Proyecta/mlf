import os
import sys
import threading
import time

from flask import Flask, render_template, Response, request

from video_feed import VideoFeed
from robot_control import RobotController


# App Globals (do not edit)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 


video_feed_builder = VideoFeed()
@app.route('/video_feed')
def video_feed():
    return Response(video_feed_builder.gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# TODO: how to pass GET/POST parameters???
"""
robot_controller = RobotController()
@app.route('/move_robot')
def move_robot():
    return Response(robot_controller.set_position_xyz())
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
    


