from flask import Response, Blueprint, request
from ... import robot_controller

robot_control_bp = Blueprint("robot_control", __name__)

@robot_control_bp.route('/move_robot', methods=["GET"])
def move_robot():
    # pasar argumentos por la url, ej: localhost/move_robot?x=12&y=10
    # los valores que no se pasan se asignan 0
    x = int(request.args.get("x", 0))
    y = int(request.args.get("y", 0))
    z = int(request.args.get("z", 0))
    position = [x, y, z]
    robot_controller.set_position_xyz(position)
    return Response()