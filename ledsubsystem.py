import commands2
import wpilib


class LEDSubsystem(commands2.SubsystemBase):


   def __init__(self) -> None:
       super().__init__()      # Call the initialization routing of the parent Object


       self.kLEDBuffer = 5      # Number of LEDs


       # Instantiate the LED Object on RoboRIO PWM Pin 9
       self.LED = wpilib.AddressableLED(9)


       # Create an array of data to hold the color of each LED
       self.ledData = [wpilib.AddressableLED.LEDData() for _ in range(self.kLEDBuffer)]


       # Store what the last hue of the first pixel is
       self.rainbowFirstPixelHue = 0


       # Set the number of LEDs in the LED Array
       self.LED.setLength(self.kLEDBuffer)


       # Push the array of LED color information into the physical LED strip
       self.LED.setData(self.ledData)
       self.LED.start()
       print (">>>> Robot Initialization complete in __init__ in LEDSubsystem.py")




   def joystickControlsColor(self, xInput, yInput):
       # Loop through the array and load it with color. 
       for i in range(self.kLEDBuffer):
           hue = int(90 + (xInput * 90))          #  Resulting range is 0 to 180
           brigthness = int(128 + (yInput * 128)) #  Resulting range is 0 to 255
           # Set the value
           self.ledData[i].setHSV(hue, 255, brigthness)
           self.LED.setData(self.ledData)
           print("Joystick: X-Axis: %:", int(100*xInput), " Y-Axis %: ",
           int(100*yInput),  "   Hue: ", hue, "     Brightness: ", brigthness )


   def rainbow(self):
       # Loop thru the array and load it with color.  In this case a changing rainbow
       for i in range(self.kLEDBuffer):
           # Calculate the hue - hue is easier for rainbows because the color
           # shape is a circle so only one value needs to precess
           hue = (self.rainbowFirstPixelHue + (i * 180 / self.kLEDBuffer)) % 180
           # Set the value
           self.ledData[i].setHSV(int(hue), 255, 128)
       # Increase by to make the rainbow "move"
       self.rainbowFirstPixelHue += 3
       # Check bounds
       self.rainbowFirstPixelHue %= 180
       self.LED.setData(self.ledData)

   def setColorGreen(self):
       # Loop thru the array and load it with color.  In this case a changing Green
       for i in range(self.kLEDBuffer):
           hue = 240  #  240 is green, 120 is blue, 0 is red
           self.ledData[i].setHSV(int(hue), 255, 128)
       self.LED.setData(self.ledData)

   def setColorRed(self):
       # Loop thru the array and load it with color.  In this case a changing Green
       for i in range(self.kLEDBuffer):
           hue = 0  #  240 is green, 120 is blue, 0 is red
           self.ledData[i].setHSV(int(hue), 255, 128)
       self.LED.setData(self.ledData)
