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