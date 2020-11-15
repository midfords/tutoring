from abc import ABC, abstractmethod

class Player(ABC):

    @abstractmethod
    def select_single(self):
        pass

    @abstractmethod
    def select_value(self):
        pass

    @abstractmethod
    def select_quantity(self):
        pass


class Human(Player):

    def __init__(self):
        pass

    def select_single(self):
        pass

    def select_value(self):
        pass

    def select_quantity(self):
        pass


class Computer(Player):

    def __init__(self):
        pass

    def select_single(self):
        pass

    def select_value(self):
        pass

    def select_quantity(self):
        pass
