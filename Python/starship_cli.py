import click
from starship import Starship, Fleet

starship_classes='Constitution Galaxy NX Defiant Sovereign Intrepid Miranda'.split()

@click.group()
def cli():
  pass

@cli.group('ship')
def ship_group():
  pass

@cli.group('fleet')
def fleet_group():
  pass

@fleet_group.command('create')
def fleet_gen():
  pass

@ship_group.command('create')
@click.option('--name','-n','_name', type=str, prompt='Enter name of new starship:')
@click.option('--class','-C','_class', type=click.Choice(starship_classes), help="Ship class of the new ship (only Federation vessels supported)")
@click.option('--registry','-r','_registry', type=str, help="Registry or hull number of the new ship")
@click.option('--crew','-c','_crew', type=int, help="Number of crew")
def ship_gen(_name, _class, _registry, _crew):
  ship = Starship(_name, _class, _registry, _crew)
  print(ship)

if __name__ == "__main__":
    cli()