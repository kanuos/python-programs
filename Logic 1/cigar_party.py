# When squirrels get together for a party, they like to have cigars. A squirrel party is
# successful when the number of cigars is between 40 and 60, inclusive. Unless it is the
# weekend, in which case there is no upper bound on the number of cigars. Return True if the
# party with the given values is successful, or False otherwise.


def cigar_party(cigars, weekend):
    result = False
    if weekend:
        if cigars >= 40:
            result = True
    else:
        if 60 >= cigars >= 40:
            result = True
    print(f"cigar_party({cigars}, {weekend}) -> {result} ")


cigar_party(30, False)
cigar_party(50, False)
cigar_party(70, True)
