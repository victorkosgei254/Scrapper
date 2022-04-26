import imp
from unicodedata import name
from packages.factorial import factorial
from packages.list import arraysWithFiles
from classes.Point import Point
if __name__ == "__main__":
    print("Project Started")
    print(factorial(10))
    point = Point(12,12)
    point.draw()