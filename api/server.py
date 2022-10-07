from flask import Flask, request, Response, render_template, make_response
from api.camera import VideoCamera

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
    return "No disponible por el momento ¯\_(ツ)_/¯"


@app.route("/set_joints")
def set_joints():
    q0 = request.args.get("q0")
    q1 = request.args.get("q1")
    q2 = request.args.get("q2")

    s0 = (90 - int(q0) * 2) & 0xFF
    s1 = (90 + int(q1)) & 0xFF
    s2 = (180 - int(q2)) & 0xFF

    mk2_serial.set_joints([s0, s1, s2])
    return f"Mi nueva pose es: (q0={q0}, q1={q1}, q2={q2})"


pi_camera = VideoCamera(flip=False)  # flip pi camera if upside down.
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")  # you can customze index.html here


def gen(camera):
    # get camera frame
    while True:
        frame = camera.get_frame()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")


@app.route("/video_feed")
def video_feed():
    return Response(
        gen(pi_camera), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/get_frame", methods=["GET"])
def single_frame():
    response = make_response(pi_camera.get_frame())
    response.headers["Content-Type"] = "image/jpg"
    return response


if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)
