import commands2
from commands2 import Command, Subsystem
import wpilib


class LaserCannonSubsystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()      # Call the initialization routing of the parent Object
        self.PowerLevel = 50000      # Kilowatts
        print("Laser initialized")

    def charge_laser(self) -> None:
        print("FIRING LASER ---------> ")

    def fire_laser(self) -> None:
        pass


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 


class FireLaserCannon(Command):
   def __init__(self, laser: LaserCannonSubsystem) -> None:
       super().__init__()
       self.laser = laser
       self.addRequirements(laser)

   def initialize(self) -> None:
       pass       #  This function is not being used.

   def execute(self) -> None:
       self.laser.fire_laser()

   def end(self, interrupted: bool) -> None:
       pass       #  This function is not being used.

   def isFinished(self) -> bool:
       return True

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
