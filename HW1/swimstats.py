# TEST CASE #1
# distance = 120m, pool size = 60m, time = 30:15 =>
# 2 laps, pace per 100m = 25:12, avg. speed = 0.2 km/hr
# TEST CASE #2
# distance = 2500m, pool size = 25, time = 40:20 =>
# 100 laps, pace per 100m = 2.24, avg. speed = 2.5 km/hr
# TEST CASE #3
# distance = 900m, pool size = 35, time = 55:30 =>
# 25 laps, pace per 100m = 6:10, avg. speed = 1.0 km/hr


def main():


    print("Welcome to the Olympic Swim Calculator!")
    swim_meters = int(input("How many meters did you swim?"))
    pool_length = int(input("How big was the pool in meters?"))
    swim_time_m = int(input("How many minutes did it take?"))
    swim_time_s = int(input("And how many seconds did it take?"))
    swim_time_totalsec = (swim_time_m * 60) + swim_time_s
    swim_n100 = float((swim_meters) / 100)    
    swim_lapstotal = swim_meters // pool_length 
    swim_pace_sec = swim_time_totalsec / swim_n100
    swim_pace_min = int(swim_pace_sec // 60)
    swim_pace_l = int(swim_pace_sec % 60)
    swim_pace_100 = str(swim_pace_min) + ":" + str(swim_pace_l)
    swim_ratekmhr = round((((swim_meters / swim_time_totalsec)/ 1000) * 3600), 1)
    print("You swam", str(swim_lapstotal), "laps in a total of", swim_time_totalsec, "seconds." )
    print("Your pace was", str(swim_pace_100), "per 100m.")
    print("Your average speed was", str(round(swim_ratekmhr, 1)), "km/hr.")


main()
