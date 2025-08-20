import wpilib
from commands2 import Command
from ledsubsystem import LEDSubsystem


class SetLEDFlashingRed(Command):
   def __init__(self, led: LEDSubsystem) -> None:
       super().__init__()

       self.counter = 0
       self.led = led
       self.addRequirements(led)


   def initialize(self) -> None:
       self.counter = 0
       pass       #  This function is not being used.


   def execute(self) -> None:
       self.counter = self.counter + 2
       if (self.counter <= 25 ): 
           self.led.setColorRed()
       else:
           self.led.setColorGreen()

       if (self.counter >= 50):
           self.counter = 0



   def end(self, interrupted: bool) -> None:
       pass       #  This function is not being used.


   def isFinished(self) -> bool:
       return False


