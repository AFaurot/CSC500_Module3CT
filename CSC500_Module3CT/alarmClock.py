def main():

    #User input variable for current time and how far to set out the alarm
    current_time=int(input("What is the current time value in hours?\nPlease input a number from 0-24 : "))
    alarm_hours=int(input("How many hours out do you want to set the alarm? : "))
    #modulo used here to ensure conversion to 24 hour time
    time_to_add=alarm_hours % 24
    #modulo here ensures that if (time_to_add + current_time > 24), it will convert to 24 hour time
    alarm_time=(time_to_add + current_time) % 24

    print('Alarm is set for {}:00'.format(alarm_time))


if __name__ == '__main__': main()