from typing import Callable


class Action:
    def __init__(self, action_name):
        self.action_name = action_name

    def __call__(self):
        print(f"I am {self.action_name}")


class Human:
    def __init__(self, action, name, age):
        self.name = name
        self.age = age
        self.__action = action

    @property
    def action(self):
        return self.__action

    def describe(self):
        return f"{self.name} is {self.age} years old and likes to {self.action.action_name}"


if __name__ == "__main__":
    humans = [
        Human(Action("walking"), "Alice", 25),
        Human(Action("running"), "Bob", 30),
        Human(Action("jumping"), "Charlie", 20),
    ]

    for human in humans:
        human.action()
        print(human.describe())

class CustomIterator:
    def __init__(self, sequence, start_index, end_index):
        self.sequence = sequence
        self.start_index = start_index
        self.end_index = end_index
        self.index = start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.end_index:
            value = self.sequence[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

if __name__ == "__main__":
    humans = [
        Human(Action("walking"), "Alice", 25),
        Human(Action("running"), "Bob", 30),
        Human(Action("jumping"), "Charlie", 20),
    ]

    names = [human.name for human in humans]
    iterator = CustomIterator(names, 1, 3)

    for name in iterator:
        print(name)