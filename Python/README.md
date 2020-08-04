# 🚀👩‍🚀🐍 Starships in Python!
An object-oriented implementation of a database of starships.
Intended for educational use.
`starship` objects are instantiated by providing name, registry, and crew number.
```py
enterprise = starship(name='USS Enterprise', registry='NCC-1701', crew=400)
```
If not provided, the constructor demands them interactively.
```py
enterprise = starship()
```
#### Fleet objects
Starship objects can be added to `fleet` objects.
```py
starfleet = fleet(name='Starfleet')
starfleet.add(enterprise)
```
#### Fleet roster
Fleet objects expose a list of ships on the `roster` method
```py
starfleet.roster()
```

Use [`tabulate`](https://github.com/astanin/python-tabulate) to quickly display the output:
```py
from tabulate import tabulate
print(tabulate(starfleet.roster()))
```
