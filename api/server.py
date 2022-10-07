import math
from flask import Flask, request, Response, Blueprint, make_response

from core.model.mk2_robot import MK2Model
from core.serial_wrapper.mk2_serial import MK2Serial
from api.video_feed import VideoFeed

app = Flask(__name__)
mk2 = MK2Model()
# mk2_serial = MK2Serial()
video_feed_builder = VideoFeed()


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

    # mk2_serial.set_joints([s0, s1, s2])
    return f"Mi nueva pose es: (q0={q0}, q1={q1}, q2={q2})"


@app.route("/video_feed", methods=["GET"])
def video_feed():
    return Response(
        video_feed_builder.gen(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/get_frame", methods=["GET"])
def single_frame():
    response = make_response(video_feed_builder.grab_single_frame())
    response.headers["Content-Type"] = "image/jpg"
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
