function Get-RandomFleet {
  $data = Import-Csv .\testdata.csv
  $ships = foreach ($s in $data) {
    [Starship]::new($s.Name, $s.Class, $s.Registry, $s.Crew)
  }
  $testfleet = [Fleet]::new('Starfleet', $ships)
  return $testfleet
}

Describe "Testing Ships and Fleet classes" {
  Context "Testing Starship class" {
    $testship = [Starship]::new('USS Enterprise', 'NX', 'NX-01', 83)
    It "Starship attribute values are of the correct type" {
      $testship.Name | Should -BeOfType string
      $testship.Registry | Should -BeOfType string
      $testship.Crew | Should -BeOfType int
      $testship.Class | Should -BeOfType StarshipClass
    }

    It "Starship attribute values are correct" {
      $testship.Name | Should -Be 'USS Enterprise'
      $testship.Registry | Should -Be 'NX-01' 
      $testship.Crew | Should -Be 83
      $testship.Class | Should -Be NX
    }
  }
  Context "Testing Fleet class" {
    $testfleet = Get-RandomFleet
    $csv = Import-Csv .\testdata.csv
    
    It "Fleet.Ships reports the correct length" {
      $testfleet.Ships.Length | 
      Should -Be $csv.Length -Because "fleet length should be the same as that of the .csv file containing the ships used to compose it"
    }
  }
}

Describe "Testing cmdlets" {
  Context "Testing New-Starship cmdlet" {
    It "Invoking New-Starship with named parameters" {
      { New-Starship -Name 'USS Enterprise' -Registry 'NX-01' -Class NX -Crew 83 } | 
      Should -Not -Throw -Because 'valid arguments are passed to correclty named parameters'
    }
    It "Invoking New-Starship with positional parameters" {
      { New-Starship 'USS Enterprise' NX 'NX-01' 83 } | 
      Should -Not -Throw -Because 'valid arguments are passed in the correct positions'
    }
    It "Invoking New-Starship with invalid StarshipClass" {
      { New-Starship -Class foo  } | 
      Should -Throw -Because 'the argument to `-Class` is not a valid member of the `StarshipClass` enumeration'
    }
  }
}

