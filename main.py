#Main: Controller/Initiator of Application
#Author: Richard Fleming
#Create Date: August 10, 2021

# Imports
from alarm_clock import Alarm_Clock

# Instatiate Objects
morning_alarm_clock = Alarm_Clock()
evening_alarm_clock = Alarm_Clock()

#Execution of Object Methods
morning_alarm_clock.set_current_time()
morning_alarm_clock.set_alarm_time()
morning_alarm_clock.toggle_alarm()

evening_alarm_clock.set_current_time()
evening_alarm_clock.set_alarm_time()
evening_alarm_clock.toggle_alarm()