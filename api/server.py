from flask import Flask, request

from core.model.mk2_robot import MK2Model

app = Flask(__name__)
mk2 = MK2Model()

@app.route("/")
def home():
    return "Hello, World!"


@app.route("/connect")
def connect():
    return "Connected!"


@app.route("/move")
def move_xyz():

    x = request.args.get("x")
    y = request.args.get("y")
    z = request.args.get("z")
    mk2.set_pose([int(x), int(y), int(z)])
    pose = mk2.get_pose()
    return f"Me moví a (x, y, x): ({pose})"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
