import argparse
import cv2
import imutils

from core.vision.camera import VideoStream


def parse_input():
    parser = argparse.ArgumentParser(description="VideoStream Example.")
    parser.add_argument(
        "source",
        type=int,
        default=0,
        nargs="?",
        help="camera source, default 0",
    )
    return vars(parser.parse_args())


def main():
    src = parse_input()["source"]
    vs = VideoStream(src=src)
    vs.start()

    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=400)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

    cv2.destroyAllWindows()
    vs.stop()


if __name__ == "__main__":
    main()
