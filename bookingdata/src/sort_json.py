import json

day_of_week = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}
quarter_hour_blocks = {
    0: 0,
    1: 15,
    2: 30,
    3: 45
}


def main():
    data = json.load(open('bookingdata.json'))
    sort_data = sorted(data, key=lambda data: data['car'])

    # for i in range(5):
    print(json.dumps(sort_data))


def date_converter(time):
    """ 
    Time is in blocks of 15 minutes, starting at Sunday 6am. 
    E.g 4 = Sunday 7am, 96 = Monday 6am, etc.
    6 AM = 0, 6.15 AM = 1, 6.30 AM = 2, 6.45 AM = 3, 7 AM = 4

    Sunday is Day 0, Monday Day 1
    """
    # Offset time to Sunday 12 AM as 0 for easier processing.
    time = time + 24
    # 99 = 96 + 95
    day = day_of_week[int(time/96)]
    hour = int((time % 96)/4)
    quarter_hour = quarter_hour_blocks[(time % 96) % 4]

    print("The time was:" + day + "," + str(hour) + ":" + str(quarter_hour))


if __name__ == '__main__':
    # main()
    date_converter(0)
