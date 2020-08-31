from enum import Enum

class StarshipClass(Enum):
  NX = 'NX'
  GALAXY = 'Galaxy'
  CONSTITUTION = 'Constitution'
  SOVEREIGN = 'Sovereign'
  DEFIANT = 'Defiant'
  INTREPID = 'Intrepid'
  MIRANDA = 'Miranda'

  
  def __repr__(self):
    return self.value