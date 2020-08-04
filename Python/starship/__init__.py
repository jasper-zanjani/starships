from enum import Enum

class StarshipClass(Enum):
  NX = 'NX class'
  GALAXY = 'Galaxy class'
  CONSTITUTION = 'Constitution class'
  SOVEREIGN = 'Sovereign class'
  DEFIANT = 'Defiant class'
  INTREPID = 'Intrepid class'
  MIRANDA = 'Miranda class'

  def __repr__(self):
    return self.value

class Starship():
  
  def __init__(self, name = None, starshipclass: StarshipClass = StarshipClass.NX, registry=None, crew=0):
    self.name = name
    self.registry = registry
    self._crew = crew
    self.crew_on_leave = 0
    self._starshipclass = starshipclass

  @property
  def crew(self):
    return self._crew
  
  @crew.setter
  def crew(self, crew: int):
    if crew < 0:
      raise Exception
    else: self._crew = crew

  @property
  def starshipclass(self):
    return self._starshipclass

  @starshipclass.setter
  def starshipclass(self, starshipclass: StarshipClass):
    if starshipclass not in StarshipClass:
      raise Exception
    else: self._starshipclass = starshipclass

  def __add__(self,other):
    output = Fleet()
    output.append(self)
    return output + other

  def __repr__(self):
    return f'Starship({self.name}, {self.starshipclass}, {self.registry}, {self.crew})'

  def __iter__(self):
    yield self.name
    yield self.registry
    yield self.crew

  def drydock(self):
    self.crew_on_leave = self.crew - 10
    self.crew = 10

  def disembark(self):
    self.crew += self.crew_on_leave
    self.crew_on_leave = 0

  def report(self):
    print(f'{self.name}\'s crew is {self.crew} souls with {self.crew_on_leave} on leave!')


class Fleet():

  def __init__(self,name=None):
    self.name = name
    self.ships = []

  def append(self,*args):
    for arg in args:
      if type(arg) == Starship:
        self.ships.append(arg)
      else:
        continue

  def __add__(self, other):
    from copy import deepcopy
    output = deepcopy(self)
    if type(other) is Starship: 
      output.append(other)
      return output
    elif type(other) is fleet: 
      raise NotImplementedError
    else:
      raise NotImplementedError

  def __iadd__(self, other):
    self.append(other)
    return self

  def __len__(self):
    return len( self.ships )

  def roster(self):
    return [[ship.name, ship.registry, ship.crew] for ship in self.ships]

  def __iter__(self):
    for ship in self.ships:
      yield list(ship)

  def __str__(self):
    from tabulate import tabulate
    return tabulate([[ship.name, ship.registry, ship.crew] for ship in self.ships], headers=['Name','Registry','Crew'],tablefmt='plain')