# You are driving a little too fast, and a police officer stops you. Write code to compute the
# result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket.
# If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1.
# If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day,
# your speed can be 5 higher in all cases.


def caught_speeding(speed, today_is_birthday):
    if today_is_birthday:
        if speed <= 65:
            no_of_tickets = 0
        elif 85 >= speed >= 66:
            no_of_tickets = 1
        else:
            no_of_tickets = 2
    else:
        if speed <= 60:
            no_of_tickets = 0
        elif 80 >= speed >= 61:
            no_of_tickets = 1
        else:
            no_of_tickets = 2
    print(f"caught_speeding({speed}, {today_is_birthday}) -> {no_of_tickets}")


caught_speeding(60, False)
caught_speeding(65, False)
caught_speeding(65, True)
