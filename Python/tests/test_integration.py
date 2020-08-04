import unittest
from starship import *

def get_ships():
  '''
  Return a list of Starships from "data.csv", placed in the CWD
  '''
  with open('data.csv', newline='') as f:
    from csv import reader
    data = [row for row in reader(f)]
  ships = [Starship(*i) for i in data]
  return ships

class TestFleet(unittest.TestCase):
  def test_fleet_len(self):
    '''
    Test if a `Fleet` object reports the correct length.
    '''
    ships = get_ships()
    self.assertGreater(len(ships), 0, msg="More than 0 ships")
    starfleet = Fleet()
    for ship in ships:
      starfleet += ship
    self.assertEqual( len(starfleet) , len(ships) )

if __name__ == '__main__':
  unittest.main()
