using System;

namespace starship_cs {
  class Program {
    static void Main(string[] args) {
      Starship enterprise = new Starship();
      enterprise.name = "USS Enterprise";
      enterprise.registry = "NCC-1701";
      enterprise.starshipclass = StarshipClass.CONSTITUTION;
      enterprise.crew = 400;

      Console.WriteLine("{0} {1} {2} {3}", enterprise.name, enterprise.registry, enterprise.starshipclass, enterprise.crew);
    }

    class Starship {
      public string name {get; set;}
      public string registry {get; set;}
      public int crew {get; set;}
      public StarshipClass starshipclass {get; set; }
    }
    enum StarshipClass {
      NX, GALAXY, CONSTITUTION, DEFIANT, INTREPID, MIRANDA, SOVEREIGN
    }
  }
}

