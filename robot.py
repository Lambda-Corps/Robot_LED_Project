import wpilib
from commands2 import TimedCommandRobot, button
import ledsubsystem
import joystickcontrol
import setledgreen
import setledred
import lasercannonsubsystem
import railgunsubsystem



class MyRobot(TimedCommandRobot):
   def robotInit(self):
       """
       This function is called upon program startup and
       should be used for any initialization code.
       """

       self.controller = wpilib.Joystick(0)
       self.led = ledsubsystem.LEDSubsystem()
       self.led.setDefaultCommand(joystickcontrol.JoyStickControl(self.led, self.controller) )
       button.JoystickButton(self.controller,1).whileTrue( setledgreen.SetLEDGreen(self.led)  )
       button.JoystickButton(self.controller,2).whileTrue( setledred.SetLEDRed(self.led)  )

       self.laser = lasercannonsubsystem.LaserCannonSubsystem()
       button.JoystickButton(self.controller,3).onTrue(lasercannonsubsystem.FireLaserCannon(self.laser))
       self.rail = railgunsubsystem.RailGunSubsystem()
       button.JoystickButton(self.controller,4).onTrue( railgunsubsystem.FireRailGun(self.rail))

       print ("Robot Initialization (robotInit) Completed ")


   def autonomousInit(self):
       """This function is run once each time the robot enters autonomous mode."""
       print ("Autonomous Initialization (autonomousInit) Completed ")


   def autonomousPeriodic(self):
       """This function is called periodically during autonomous."""


   def teleopInit(self):
       """This function is called once each time the robot enters teleoperated mode."""
       print ("TeleOpInit Initialization (teleopInit) Completed ")


   def teleopPeriodic(self):
       """This function is called periodically during teleoperated mode."""
       Xaxis = self.controller.getRawAxis(0)
       Yaxis = self.controller.getRawAxis(1)
       print(f"Joystick: Forward Motion Axis: {Yaxis:5.2f}  Turning Motion Axis: {Xaxis:5.2f} ")


   def testInit(self):
       """This function is called once each time the robot enters test mode."""
       print ("TestInit Initialization (testInit) Completed ")


   def testPeriodic(self):
       """This function is called periodically during test mode."""
