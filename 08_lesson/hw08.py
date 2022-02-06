from datetime import datetime, timedelta
from typing import ItemsView

users = [{
    "Bob":{"phones":["30674567676",],"birthday":"07/02/1990"},
    "Peter":{"phones":[], "birthday":"08/02/1967"},
    "Olga":{"phones":['050 1525452'],"birthday":"09/02/2021"},
    "Mike":{"phones":['0661234567'], "birthday":"10/02/2021"},
    "Anna":{"phones":[''], "birthday":"11/02/2021"},
    "Nick":{"phones":[''], "birthday":"12/02/2021"},
    "lia":{"phones":[''], "birthday":"13/02/2021"},
    "ХЗ":{"phones":['067 155545455'], "birthday":""}
    }]


def get_birthdays_per_week(users):
    current_datetime = datetime.now()
    delta = timedelta(weeks=1)
    birthdays_list = []
    birthdays_list_for_week = []
    birthdays_list_for_week = {}
    monday1 = []
    tuesday1 = []
    wednesday1 = []
    thursday1 = []
    friday1 = []

    for i in users:
        for name, val in i.items():
            date_birthdays = val["birthday"]

            if date_birthdays:
                d = datetime.strptime(date_birthdays, "%d/%m/%Y")
                d = d.replace(year = current_datetime.year)
                
                if current_datetime <= d and d <= (current_datetime + delta):
                    birthdays_list.append(datetime.strftime(d, "%A") + " " + name)
            else:
                continue

    for birt in birthdays_list:
        d, t = birt.split(" ")
        if d == 'Monday':
            monday1.append(t)
        elif d == 'Tuesday':
            tuesday1.append(t)
        elif d == 'Wednesday':
            wednesday1.append(t)
        elif d == 'Thursday':
            thursday1.append(t)
        elif d == 'Friday':
            friday1.append(t)
        else:
            monday1.append(t)

    birthdays_list_for_week['Monday'] = monday1
    birthdays_list_for_week['Tuesday'] = tuesday1
    birthdays_list_for_week['Wednesday'] = wednesday1
    birthdays_list_for_week['Tuesday'] = tuesday1
    birthdays_list_for_week['Friday'] = friday1


    for day, birt_date in birthdays_list_for_week.items():
        print(day + ": " + (", ".join(birt_date)))

    return



print(get_birthdays_per_week(users))
