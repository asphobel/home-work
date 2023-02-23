class Action:
    def __init__(self, action_name):
        self.action_name = action_name

    def actionn(self):
        print(f"i am {self.action_name}")


class Human:
    def __init__(self, action):
        self._action = action

    @property
    def action(self):
        return self._action


if __name__ == "__main__":
    humans = [Human(Action("walking")), Human(Action("runing")), Human(Action("jumping"))]

    for human in humans:
        human.action.actionn()