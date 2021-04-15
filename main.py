import datetime


def print_header():
    print("----------------------------")
    print("   Birthday Countdown App")
    print("----------------------------")
    print()


def get_birthday_from_user():
    name = input("Name: ")
    print("Date of Birth")
    day = int(input("[DD]: "))
    month = int(input("[MM]: "))
    year = int(input("[YYYY]: "))

    birthday = datetime.date(year, month, day)
    print(name + ". Your birthday is {}".format(birthday))

    return name, birthday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(year=target_date.year, month=original_date.month, day=original_date.day)

    df = this_year - target_date
    days = df.days

    return days


def print_birthday_information(name, days):
    if days > 0:
        print("{}, your birthday is in {} days!".format(name, days))
    elif days < 0:
        print("{}, looks like your birthday was {} ago!".format(name, -days))
    else:
        print("Happy Birthday!!!!")


def main():
    print_header()
    name, birthday = get_birthday_from_user()
    today = datetime.date.today()
    days = compute_days_between_dates(birthday, today)
    print_birthday_information(name, days)

if __name__ == '__main__':
    main()
