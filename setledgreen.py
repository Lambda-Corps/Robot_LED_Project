import wpilib
from commands2 import Command
from ledsubsystem import LEDSubsystem


class SetLEDGreen(Command):
   def __init__(self, led: LEDSubsystem) -> None:
       super().__init__()


       self.led = led
       self.addRequirements(led)


   def initialize(self) -> None:
       pass       #  This function is not being used.


   def execute(self) -> None:
       self.led.setColorGreen()


   def end(self, interrupted: bool) -> None:
       pass       #  This function is not being used.


   def isFinished(self) -> bool:
       return False


