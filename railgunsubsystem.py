import commands2
from commands2 import Command, Subsystem
import wpilib


class RailGunSubsystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()      # Call the initialization routing of the parent Object
        self.PowerLevel = 50000      # Kilowatts
        print("RailGun initialized")

    def charge_rail_gun(self) -> None:
        print("FIRING RailGun ---------> ")

    def fire_rail_gun(self) -> None:
        pass

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 

class FireRailGun(Command):
   def __init__(self, rail: RailGunSubsystem) -> None:
       super().__init__()
       self.rail = rail
       self.addRequirements(rail)

   def initialize(self) -> None:
       pass       #  This function is not being used.

   def execute(self) -> None:
       self.rail.fire_rail_gun

   def end(self, interrupted: bool) -> None:
       pass       #  This function is not being used.

   def isFinished(self) -> bool:
       return True

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
