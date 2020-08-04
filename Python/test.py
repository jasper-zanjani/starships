from starship import *

def test_starship(name, registry, crew):
  output = Starship ( name, registry, crew)
  
  assert output.name == name, f'Expected "{name}", got "{output.name}"'
  assert output.registry == registry, f'Expected "{registry}", got "{output.registry}"'
  assert output.crew == crew, f'Expected "{crew}", got "{output.crew}"'
  assert output.crew_on_leave == 0, f'Expected "0", got "{output.crew_on_leave}"'

  output.drydock()
  assert output.crew_on_leave == crew - 10, f'Expected "{crew - 10}"'
  
  output.disembark()
  return output
  
def test_fleet(arg):
  output = Fleet()
  for ship in ships:
    output += ship
  return output

if __name__ == '__main__':
  enterprise = test_starship('USS Enterprise', 'NCC-1701', 203)
  constitution = test_starship('USS Constitution', 'NCC-1700', 204)
  defiant = test_starship('USS Defiant','NX-74205',50)
  voyager = test_starship('USS Voyager','NCC-74656',141)
  enterprise_d = test_starship('USS Enterprise','NCC-1701-D',6000)
  reliant = test_starship('USS Reliant','NCC-1864',35)

  ships = [enterprise,constitution, defiant,voyager,enterprise_d, reliant]
  starfleet = fleet()
  for ship in ships:
    starfleet.append(ship)
  assert len(starfleet) == len(ships), f'Expected "{len(ships)}", got "{len(starfleet)}"'
  print(str(starfleet))
