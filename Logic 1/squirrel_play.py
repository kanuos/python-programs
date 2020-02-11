# The squirrels in Palo Alto spend most of the day playing. In particular, they play if the
# temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is
# 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels
# play and False otherwise.


def squirrel_play(temperature, is_summer):
    play = False
    if is_summer:
        if 100 >= temperature >= 90:
            play = True
    else:
        if 90 >= temperature >= 60:
            play = True
    print(f"squirrel_play({temperature}, {is_summer}) -> {play}")


squirrel_play(70, False)
squirrel_play(95, False)
squirrel_play(95, True)

