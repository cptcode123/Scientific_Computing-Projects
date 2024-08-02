def add_time(start, duration, starting_day = ''):
    days_of_week = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
        ]
    am_or_pm = ['AM', 'PM']
    days_passed = 0

    # Start Time

    # Starting hour
    starting_hour = int(start[:start.index(':')])

    # Starting minute
    starting_minute = int(start[start.index(':')+1:start.index(' ')])

    # Starting time of Day
    if start[start.index(' ')+1:] == 'AM':
        is_it_morning = 0
    else:
        is_it_morning = 1
        starting_hour += 12
    
    # Duration 

    # Hours gone
    hours_passed = int(duration[:duration.index(':')])
    # Minutes passed
    minutes_passed = int(duration[duration.index(':')+1:])


    # Final Time
    end_hour = starting_hour + hours_passed
    end_minute = starting_minute + minutes_passed

    # Minute Overflow
    if end_minute >= 60:
        end_hour += 1
        end_minute = end_minute % 60
    
    # Hour to Day Overflow
    if end_hour > 24:
        days_passed += end_hour // 24
        end_hour = end_hour % 24
    
    # AM or PM
    if end_hour > 12:
        is_it_morning = 1
        end_hour = end_hour % 12
    elif end_hour <= 12:
        is_it_morning = 0
        if end_hour == 12:
            is_it_morning = not is_it_morning
        if end_hour == 0:
            end_hour = 12
    
    

    # Final Formatting
    new_hour = str(end_hour)
    if len(str(end_minute)) == 1:
        new_minute = str(end_minute).rjust(2,'0')
    else:
        new_minute = str(end_minute)
    
    new_time = f'{new_hour}:{new_minute} {am_or_pm[is_it_morning]}'
    
    if starting_day:
        new_time += ', ' + days_of_week[(days_of_week.index(starting_day.capitalize()) + days_passed) % 7]
        
    
    if days_passed == 1:
        new_time += ' (next day)'
    elif days_passed > 1:
        new_time += f' ({days_passed} days later)'

    print(new_time)
    return new_time
            

