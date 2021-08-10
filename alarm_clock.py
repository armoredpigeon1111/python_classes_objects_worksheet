#CLASS: Alarm Clock
#Author: Richard Fleming
#Create Date: August 10, 2021


class Alarm_Clock:
    #Constructor
    def __init__(self):
        self.current_time = "12:00"
        self.alarm_on = False
        self.alarm_time = "12:00"
        


    #Methods
    def set_current_time(self):
        self.current_time = input("Please enter current time: ")
        print("You set the time to " + self.current_time + ".")

    def toggle_alarm(self):
        if(self.alarm_on):
            self.alarm_on = False
            print("The alarm is now off.")
        else:
            self.alarm_on = True
            print("The alarm is now on.")

    def set_alarm_time(self):
        self.alarm_time = input("Enter the desired alarm time: ")
        print("The alarm is set for " + self.alarm_time + ".")


