import math
from flask import Flask, request

from core.model.mk2_robot import MK2Model
from core.serial_wrapper.mk2_serial import MK2Serial

app = Flask(__name__)
mk2 = MK2Model()
mk2_serial = MK2Serial()

@app.route("/")
def home():
    return "Hello, World!"


@app.route("/connect")
def connect():
    return "Connected!"


@app.route("/move")
def move_xyz():

    x = float(request.args.get("x"))
    y = float(request.args.get("y"))
    z = float(request.args.get("z"))
    q0, q1, q2 = mk2.inverse_kinematics((x, y, z))
    mk2.set_pose(q0, q1, q2)
    pose = mk2.get_pose()
    [x_new, y_new, z_new] = [int(a) for a in pose["link_4"][1]]

    error = math.sqrt((x_new - x) ** 2 + (y_new - y) ** 2 + (z_new - z) ** 2)

    if error >= 10:
        return (
            f"Parece que no puedo llegar a esa posición -- \n"
            f"({x_new}, {y_new}, {z_new}) - error: {error}"
        )

    print(f"{q0}, {q1}, {q2}")
    angles = [int(q0*2+90) & 0xFF, int(q1+90) & 0xFF, int(180-q2) & 0xFF]
    print(f"{angles}")
    s = mk2_serial.set_joints(angles)

    return f"Me moví a (x, y, x): {(x_new, y_new, z_new)} - error: {error}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
