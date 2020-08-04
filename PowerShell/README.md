# 🚀👨‍🚀🐚 Starships in PowerShell!
An object-oriented implementation of a database of starships for Powershell, ported from [Python](https://github.com/jasper-zanjani/starship), also incorporating Pester unit testing.
Intended for educational use.

On the frontend, sitting in the captain's chair, is the `New-Starship` cmdlet.
```powershell
New-Starship -Name 'Enterprise' -Class NX -Registry 'NX-01' -Crew 83 
```
For brevity, you can make use of the alias `ncc` and positional parameters:
```powershell
ncc 'Enterprise' NX 'NX-01' 83
```
If you're tired of the same old starships, try the `-Random` parameter to see what Powershell can come up with:
```powershell
New-Starship -Random
```
On the backend, starships are implemented as `Starship` objects instantiated by specifying name, ship class, registry, and crew count. among other (as yet undocumented) attributes.
```powershell
[Starship]::new('Enterprise', 'NX', 'NX-01', 83)
```
None of these parameters are required when instantiating in this manner, although even when instantiating without providing any arguments PowerShell will choose the NX class for the object because that is listed first in the enumeration.
```powershell
[Starship]::new()
```
Starships can be added to `Fleet` objects
```powershell
$e = [Starship]::new('Enterprise', 'NX', 'NX-01', 83)
$c = [Starship]::new('Columbia', 'NX', 'NX-02', 85)
$ships = $e, $c
$starfleet = [Fleet]::new('Starfleet', $ships)
```
