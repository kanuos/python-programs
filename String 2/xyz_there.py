# Return True if the given string contains an appearance of "xyz" where the xyz is not directly
# preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.


def xyz_there(string):
    result = False
    if "xyz" in string and ".xyz" not in string:
        result = True
    print(f"xyz_there('{string}') -> {result}")


xyz_there('abcxyz')
xyz_there('abc.xyz')
xyz_there('xyz.abc')
