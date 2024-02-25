def main():
    time = input("What time is it? " )

    #Assigns variable to time conversion
    conversion = convert(time)

    #sets breakfast time between 7:00-8:00 & prints
    if conversion >= 7 and conversion <= 8:
        print("Breakfast Time")
    #sets lunch time between 12:00-13:00 & prints
    elif conversion >= 12 and conversion <= 13:
        print("Lunch Time")
    #sets breakfast time between 18:00-19:00 & prints
    elif conversion >= 18 and conversion <= 19:
        print("Dinner Time")


def convert(time):
    #splits string values by either side of ":"
    hours, minutes = time.split(":")

    #convert string to integer
    hr_int = int(hours)
    min_int = int(minutes)

    #convert time to float
    float_t = hr_int + min_int / 60

    return float_t


if __name__ == "__main__":
    main()
