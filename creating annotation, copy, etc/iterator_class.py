import main
from main import Data
import next_element as ne
import os

class IteratorOfExemplar:
    """
        class iterator - to bypass elements inside an object of your own class
    """

    def __init__(self, obj: type(Data), pointer: str):
        self.obj = obj
        self.pointer = pointer
        self.counter = 0

    def __next__(self) -> str:
        """
            returns the next element
        """
        self.pointer = ne.next_element(self.obj, self.pointer)
        return self.pointer

if __name__ == "__main__":
    iter = IteratorOfExemplar(Data("dataset"),  "dataset\\rose\\0002.jpg")
    print(iter.__next__())
