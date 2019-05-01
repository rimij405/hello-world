"""
This class is supposed to hold game logic for fractions to be used in several
suitcase minigames.
"""
import random as rand
import math
import fraction as f

__author__= "jks7743"

"""
Generates a base fraction that isnt a mixed fraction.
"""
def generate_base_frac(max_value_num, max_value_den):
    rand.seed()
    numerator = rand.randint(1, max_value_num)
    denominator = rand.randint(1, max_value_den)
    frac = f.Fraction(numerator, denominator)

    while denominator <= numerator:
        numerator = rand.randint(1, max_value_num)
        denominator = rand.randint(1, max_value_den)
        frac = f.Fraction(numerator, denominator)
    return frac

"""
Simplifies fractions
"""
def simplify(fraction):
    divisor = math.gcd(fraction.numerator, fraction.denominator)
    return f.Fraction(int(fraction.numerator / divisor), int(fraction.denominator / divisor))

"""
Determines whether the fraction is in the current fraction listd
"""
def frac_in(fraction, fraction_list):
    for frac in fraction_list:
        if frac.numerator == fraction.numerator:
            if frac.denominator == fraction.denominator:
                return True
    return False

"""
Generates a list of fractions based on given constraints
"""
def generate_fracs(base_fraction, num_less_than, num_greater_than, num_equal_to, max_num, max_den):
    fraction_list = []
    rand.seed()
    for i in range(0, num_greater_than):
        frac = f.Fraction(rand.randint(base_fraction.numerator, max_num),
        rand.randint(base_fraction.denominator, max_den))
        while frac_in(frac, fraction_list) or frac.value <= base_fraction.value or frac.numerator > frac.denominator:
            frac = f.Fraction(rand.randint(base_fraction.numerator, max_num),
            rand.randint(base_fraction.denominator, max_den))
        fraction_list.append(frac)

    for i in range(0, num_less_than):
        frac = f.Fraction(rand.randint(1, max_num),
        rand.randint(1, max_den))
        while frac_in(frac, fraction_list) or frac.value >= base_fraction.value:
            frac = f.Fraction(rand.randint(1, max_num),
            rand.randint(1, max_den))
        fraction_list.append(frac)

    simplified_base = simplify(base_fraction)
    for i in range(0, num_equal_to):
        mult = rand.randint(1, max_num)
        num = mult * simplified_base.numerator
        den = mult * simplified_base.denominator
        frac = f.Fraction(num, den)
        while frac_in(frac, fraction_list) or num > max_num or den > max_den:
            mult = rand.randint(1, max_num)
            num = mult * simplified_base.numerator
            den = mult * simplified_base.denominator
            frac = f.Fraction(num, den)
        fraction_list.append(frac)
    rand.shuffle(fraction_list)
    return fraction_list