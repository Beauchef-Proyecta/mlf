import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import Slider, Button

from core.model.mk2_robot import MK2Model


class MK2Plotter:
    def __init__(self):
        self.robot = MK2Model()
        self.robot.set_pose([0, 30, 90])
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.sliders = []

    def setup(self):
        self.fig.set_size_inches(7, 4)

        axcolor = "lightgoldenrodyellow"
        self.ax.margins(x=0)
        plt.subplots_adjust(right=0.5)

        axq0 = plt.axes([0.65, 0.3, 0.03, 0.4], facecolor=axcolor)
        self.sliders.append(
            Slider(
                ax=axq0,
                label="q0 [º]",
                valmin=-45,
                valmax=45,
                valinit=0,
                orientation="vertical",
            )
        )

        axq1 = plt.axes([0.75, 0.3, 0.03, 0.4], facecolor=axcolor)
        self.sliders.append(
            Slider(
                ax=axq1,
                label="q1 [º]",
                valmin=-20,
                valmax=90,
                valinit=0,
                orientation="vertical",
            )
        )

        axq2 = plt.axes([0.85, 0.3, 0.03, 0.4], facecolor=axcolor)
        self.sliders.append(
            Slider(
                ax=axq2,
                label="q2 [º]",
                valmin=70,
                valmax=170,
                valinit=90,
                orientation="vertical",
            )
        )

        self.sliders[0].on_changed(self.update_plot)
        self.sliders[1].on_changed(self.update_plot)
        self.sliders[2].on_changed(self.update_plot)

        self.update_plot()

        plt.show()

    def update_plot(self, val=None):
        self.robot.set_pose(
            [self.sliders[0].val, self.sliders[1].val, self.sliders[2].val]
        )
        pose = self.robot.get_pose()

        self.ax.clear()
        for name, coords in pose.items():
            origin = coords[0]
            end = coords[1]

            self.ax.scatter(origin[0], origin[1], origin[2], zdir="z", s=10)
            self.ax.plot(
                [origin[0], end[0]],
                [origin[1], end[1]],
                [origin[2], end[2]],
            )

        self.ax.set_xlabel("X [mm]")
        self.ax.set_ylabel("Y [mm]")
        self.ax.set_zlabel("Z [mm]")

        self.ax.set_xlim(-100, 400)
        self.ax.set_ylim(-250, 250)
        self.ax.set_zlim(0, 500)

        self.fig.canvas.draw_idle()


if __name__ == "__main__":
    p = MK2Plotter().setup()
