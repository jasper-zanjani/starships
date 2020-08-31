# 🚀👩‍🚀🐍 Starships in Python!
An object-oriented implementation of a database of starships.
Intended for educational use.

## :keyboard: CLI frontend
A CLI application frontend [**starship_cli**](starship_cli.py), written using the [Click](https://github.com/pallets/click) package,
provides user-friendly access to the Python API. The user will be prompted for required information, like name. Click also helps in 
producing progressive help messages to the end-user, which are dynamically generated from docstrings, type hints, and variable values.
```sh
starship_cli ship create --name "USS Enterprise" --class "Constitution" 
  # => Starship('USS Enterprise','Constitution', None, None)
starship_cli ship create
  # => Enter name of new starship:
starship_cli --help
  # Usage: starship_cli [OPTIONS] COMMAND [ARGS]...

  # Options:
  #   --help  Show this message and exit.

  # Commands:
  #   fleet
  #   ship
```
## :snake: Python backend
`starship` objects are instantiated by providing name, registry, and crew number.
```py
enterprise = starship(name='USS Enterprise', registry='NCC-1701', crew=400)
```
If not provided, the constructor demands them interactively.
```py
enterprise = starship()
```
Starship objects can be added to `fleet` objects.
```py
starfleet = fleet(name='Starfleet')
starfleet.add(enterprise)
```
Fleet objects expose a list of ships on the `roster` method
```py
starfleet.roster()
```

Use [`tabulate`](https://github.com/astanin/python-tabulate) to quickly display the output:
```py
from tabulate import tabulate
print(tabulate(starfleet.roster()))
```
