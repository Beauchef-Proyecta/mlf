from .link_model import Link


class GenericRobot:
    def __init__(self, build_instructions: dict):
        self._links = []
        self._home = []
        self._limits = []
        self.build_instructions = build_instructions

    def assemble(self):
        for id, params in self.build_instructions.items():

            link = Link(params["length"], params["axis"], params["rotation"])
            if params["parent"] != None:
                link.set_parent(self._links[params["parent"]])
            self._links.append(link)

        return self

    @property
    def get_pose(self):
        return tuple(l.end for l in self._links)

    def set_pose(self, angles):
        for index, angle in enumerate(angles):
            self._links[index].set_pose(angle)
