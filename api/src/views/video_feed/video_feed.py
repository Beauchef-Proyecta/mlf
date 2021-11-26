from flask import Response, Blueprint, make_response
from ... import video_feed_builder

video_feed_bp = Blueprint("video_feed_bp", __name__)

@video_feed_bp.route("/video_feed", methods=["GET"])
def video_feed():
    return Response(video_feed_builder.gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@video_feed_bp.route('/single_frame', methods=["GET"])
def single_frame():
    response = make_response(video_feed_builder.grab_single_frame())
    response.headers['Content-Type'] = 'image/jpg'
    return response