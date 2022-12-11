#Copy object
from abc import ABCMeta, abstractmethod
import copy


class PyAD(metaclass=ABCMeta):

    def __init__(self):
        self.id = None
        self.type = None

    def course(self):
        pass

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid

    def clone(self):
        return copy.copy(self)



class DP(PyAD):
    def __init__(self):
        super().__init__()
        self.type = "Design Pattern"

    def course(self):
        print("Inside DP::course() method")


class CP(PyAD):
    def __init__(self):
        super().__init__()
        self.type = "Creational Pattern"

    def course(self):
        print("Inside SDE::course() method.")


class PP(PyAD):
    def __init__(self):
        super().__init__()
        self.type = "Prototype Pattern"

    def course(self):
        print("Inside STL::course() method.")



class CoursesHCMUS:

    cache = {}

    def get_course(id):
        COURSE = CoursesHCMUS.cache.get(id, None)
        return COURSE.clone()

    def load():
        dp = DP()
        dp.set_id("1")
        CoursesHCMUS.cache[dp.get_id()] = dp

        cp = CP()
        cp.set_id("2")
        CoursesHCMUS.cache[cp.get_id()] = cp

        pp = PP()
        pp.set_id("3")
        CoursesHCMUS.cache[pp.get_id()] = pp


if __name__ == '__main__':
    CoursesHCMUS.load()

    dp = CoursesHCMUS.get_course("1")
    print(dp.get_type())

    dp2 = CoursesHCMUS.get_course("1")
    print( dp is dp2)