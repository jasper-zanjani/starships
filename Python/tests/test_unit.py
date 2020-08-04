import unittest
from starship import Starship, Fleet, StarshipClass


def random_ship():
  '''
  Return a starship with randomly generated values
  TO-DO:
  - Randomness needs to implemented, possibly using `faker` module
  '''
  return Starship('USS Enterprise',StarshipClass.CONSTITUTION,'NCC-1701',400)

class TestShip(unittest.TestCase):
  # def random_ship(self):
  #   return starship.starship('USS Enterprise','NCC-1701',400)
  def test_ship_types(self):
    '''
      Test if data types of a `Starship` instance are correct.
    '''
    ship = random_ship()
    self.assertIsInstance(ship.name,str)
    self.assertIsInstance(ship.registry,str)
    self.assertIsInstance(ship.crew,int)
    self.assertIsInstance(str(ship),str)
    self.assertIsInstance(ship.starshipclass, StarshipClass)

  def test_ship_values(self):
    '''
      Test if data values of a `Starship` instance are correct.
    '''
    ship = random_ship()
    self.assertEqual(ship.name,'USS Enterprise')
    self.assertEqual(ship.registry,'NCC-1701')
    self.assertEqual(ship.starshipclass,StarshipClass.CONSTITUTION)
    self.assertEqual(ship.crew,400)
    self.assertEqual(ship.crew_on_leave,0)

  def test_ship_add(self):
    '''
      Test if the `__add__` dunder method returns a `Fleet` object
    '''
    ships = random_ship() + random_ship()
    self.assertIsInstance(ships,Fleet)

  def test_ship_iadd(self):
    '''
      Test if the `__iadd__` dunder method returns a `Fleet` object
    '''
    ships = random_ship()
    ships += random_ship()
    self.assertIsInstance(ships,Fleet)

  def test_bad_ship_values(self):
    '''
      Test effect of bad validation on `Starship` instantiation.
    '''
    pass

if __name__ == '__main__':
  unittest.main()
