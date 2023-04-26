import unittest


class Human:
    def __init__(self, name: str, age: int, gender: str):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__status = "alive"
        self.__age_limit = 100

    def grow(self):
        self.__is_alive()
        if self.__age < self.__age_limit:
            self.__age += 1
        else:
            self.__status = "dead"

    def __is_alive(self):
        if self.__status == "alive":
            return True
        else:
            raise Exception(f"{self.__name} is already dead...")

    def change_gender(self, gender: str):
        self.__is_alive()
        self.__validate_gender(gender)

        if self.__gender != gender:
            self.__gender = gender
        else:
            raise Exception(f"{self.__name} already has gender '{gender}'")

    @staticmethod
    def __validate_gender(gender: str):
        if gender not in ["male", "female"]:
            raise Exception("Not correct name of gender")

    @property
    def age(self) -> int:
        return self.__age

    @property
    def gender(self) -> str:
        return self.__gender




class TestHuman(unittest.TestCase):
    def setUp(self):
        self.human = Human(name="John", age=30, gender="male")

    def test_grow(self):
        self.human.grow()
        self.assertEqual(self.human.age, 31)

    def test_grow_past_age_limit(self):
        self.human._Human__age_limit = 30
        self.human.grow()
        self.assertEqual(self.human.age, 30)
        self.assertEqual(self.human._Human__status, "dead")

    def test_change_gender(self):
        self.human.change_gender("female")
        self.assertEqual(self.human.gender, "female")

    def test_change_gender_same_gender(self):
        with self.assertRaises(Exception):
            self.human.change_gender("male")

    def test_change_gender_invalid_gender(self):
        with self.assertRaises(Exception):
            self.human.change_gender("other")

    def test_change_gender_dead_person(self):
        self.human._Human__status = "dead"
        with self.assertRaises(Exception):
            self.human.change_gender("female")

    def test_validate_gender(self):
        self.assertRaises(Exception, Human._Human__validate_gender, "other")
        self.assertRaises(Exception, Human._Human__validate_gender, 123)

if __name__ == '__main__':
    unittest.main()