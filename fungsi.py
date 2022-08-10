import os

os.system("clear")

class Chara:

def __init__(self, name, health):
  self.name = name
  self.health = health
  self.armory = {
  "nama": "katana",
  "damage": 100
}

def info(self):
  print(f' {self.name} {self.armory} {self.health} ')

def grinding():
  monster = [{
    "nama": "monster1",
    "damage": 100
  }]
  
  for i in monster:
    print(f'monster {i.nama}')

char1 = Chara("char1", 100)

char2 = Chara('char2', 220)

#char1.attack(char2)

char1.grinding()