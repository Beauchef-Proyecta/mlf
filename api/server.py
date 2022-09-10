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
    return f"No disponible por el momento ¯\_(ツ)_/¯"


@app.route("/set_joints")
def set_joints():
    q0 = request.args.get("q0")
    q1 = request.args.get("q1")
    q2 = request.args.get("q2")

    s0 = (90 - int(q0) * 2) & 0xFF
    s1 = (90 + int(q1)) & 0xFF
    s2 = (180 - int(q2) - int(q1)) & 0xFF

    mk2_serial.set_joints([s0, s1, s2])
    return f"Mi nueva pose es: (q0={q0}, q1={q1}, q2={q2})"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
