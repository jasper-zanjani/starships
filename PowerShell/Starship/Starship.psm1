class Starship {
  [string]$Name
  [string]$Registry
  [int]$Crew
  hidden [int]$CrewOnLeave
  [StarshipClass]$Class
  
  Starship() {
  }

  Starship([string]$name, [StarshipClass]$class, [string]$registry, [int]$crew) {
    $this.Name = $name
    $this.Class = $class
    $this.Registry = $registry
    $this.Crew = $crew
  }
  
  Drydock () {
    $this.CrewOnLeave = $this.Crew - 10
    $this.Crew = 10
  }
  Disembark () {
    $this.Crew += $this.CrewOnLeave
    $this.CrewOnLeave = 0
  }
  Report () {
    Write-Host -ForegroundColor Cyan $this.Name -NoNewline
    Write-Host "'s crew is " -NoNewline
    Write-Host -ForegroundColor Green $this.Crew -NoNewline
    Write-Host ' souls with ' -NoNewline
    Write-Host -ForegroundColor Red $this.CrewOnLeave -NoNewline
    Write-Host ' away on leave!'
  }
}

enum StarshipClass {
  NX
  Galaxy
  Constitution
  Sovereign
  Defiant
  Intrepid
  Miranda
}

class Fleet {
  [string]$Name
  [Starship[]]$Ships
  Fleet ([string]$n, [Starship[]]$s) {
    $this.Name = $n
    $this.Ships = $s
  }
}

function New-Starship {
  param (
    [Parameter(Position = 0)][string] $Name,
    [Parameter(Position = 1)][StarshipClass] $Class,
    [Parameter(Position = 2)][string] $Registry,
    [Parameter(Position = 3)][int] $Crew=0,
    [Parameter()] [switch] $Random
  )
  if ($Random) {
    Import-Module NameIT
    $name = (Invoke-Generate '[syllable][syllable][syllable]')
    $name = (Get-Culture).TextInfo.ToTitleCase($name)
    $reg = Get-Random -Minimum 1000 -Maximum 99999
    $c = [enum]::GetValues([StarshipClass]).Count
    $cls = [StarshipClass](Get-Random -Minimum 1 -Maximum $c)
    $crew = (Get-Random -Minimum 1 -Maximum 20) * 100

    return (New-Starship -Name "USS $name" -Registry "NCC-$reg" -Class $cls -Crew $crew)
    # return [Starship]::new($name, $cls, $reg, $crew)
  }
  return [Starship]::new($Name, $Class, $Registry, $Crew)
}

function New-Fleet {
  [CmdletBinding()]
  param (
    [Parameter()][string] $Name,
    [Parameter()][System.Array] $Ships,
    [Parameter()][switch] $Random
  )
  if ($Random) {
    return 'Random Fleet'
  }
  return [Fleet]::new($name, $ships)
}

New-Alias -Name ncc -Value New-Starship