# Paul Cruz
# CS5001
# HW 2
# Problem 2
# workout.py

# Example
# Input:
# What day of the week is it (M, Tu, W, Th, F, Sa, Su)? ​Th
# Is it a holiday (Y/N)? ​Y
# Is it raining (Y/N)? ​N
# What is the temperature? ​64
# Output:
# Go hiking for 45 minutes.
def main():

    # Ask what day of the week it is
    day = input("What day of the week is it (M, Tu, W, Th, F, Sa, Su)? ")
    if day == "M" or day == "W" or day == "F":
        activity = "Go running "
    elif day == "Sa":
        activity = "Go hiking "
    else:
        activity = "Go swimming "
    # Ask if it is a holiday
    holiday = input("Is it a holiday (Y/N)? ")
    if holiday == "Y":
        activity = "Go hiking "
    else:
        activity = "Go swimming "
    # Ask if it is raining
    raining = input("Is it raining (Y/N)? ")
    if raining == "Y" and day == "M" or day \
            == "W" or day == "F" and holiday == "Y":
        activity = "Go swimming "
    else:
        activity = "Go swimming "
    # Ask what the temperature is
    temp = int(input("What is the temperature (0-100)? "))
    min_temp = int(35)
    max_temp = int(75)

    if temp <= min_temp:
        time_workout = "for 30 minutes"
    # Check if the temperature is between 35 and 75
    elif temp >= max_temp:
        activity = "Go running "
        time_workout = "for 30 minutes"
    elif min_temp <= temp <= max_temp:
        time_workout = "for 45 minutes"
    else:
        time_workout = "for 35 minutes"
    # Ensure the user did not choose a rest day that was a holiday
    if day == "Tu" or day == "Su" and holiday == "N":
        print("This is a rest day.")
        quit()
    elif day == "Sa" or holiday == "Y":
        activity = "Go hiking "
        print(activity + time_workout)
    else:
        print(activity + time_workout)


main()
