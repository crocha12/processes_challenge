import multiprocessing
import time
import os

class Person:
  def __init__(self, name, maxAge, birth, children):
    self.name = name
    self.maxAge = maxAge
    self.birth = birth
    self.children = children

def process(person, current_time):
  print(f"{person.name} - [{os.getpid()}] was born")
  while True:
    time.sleep(1)
    current_time += 1
    print(f"{person.name} - [{os.getpid()}] turned {current_time - person.birth} years old")
    for child in person.children:
      if current_time == child.birth:
        multiprocessing.Process(target=process, args=(child, current_time)).start()
    if current_time == (person.maxAge + person.birth):
      print(f"{person.name} - [{os.getpid()}] died")
      break

grandchild_1 = Person('Neto 1', 12, 26, [])
grandchild_2 = Person('Neto 2', 18, 30, [])
son_1 = Person('Filho 1', 30, 14, [grandchild_1])
son_2 = Person('Filho 2', 30, 16, [grandchild_2])
father = Person('Pai', 60, 0, [son_1, son_2])
process(father, 0)