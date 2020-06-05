def hourAndMinuteHandleAngle(hour, minute):
    # 12 hours  = 360
    # 1 hour = 360/12 ->30
    # ----
    # 60 min = 360
    # 1 min = 360/60 ->6
    oneHourAngle = 30
    oneMinuteAngle = 6

    # Step 1 - Calculate hour angle
    exactHour = hour + (minute / 60)
    hourAngle = exactHour * oneHourAngle

    # Step 2 - Calculate minute angle
    minuteAngle = minute * oneMinuteAngle

    result = hourAngle - minuteAngle

    print(abs(result))
    return abs(result)


if __name__ == "__main__":
    hourAndMinuteHandleAngle(8, 30)