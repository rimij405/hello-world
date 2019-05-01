"""
Simple fraction class that takes care of comparisons
"""
class Fraction:
    
    """
    Initializes a new fraction
    numerator   -- numerator of the fraction
    denominator -- denominatorof the fraction
    """
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.value = float(numerator) / float(denominator)
        print("Creating fraction: {n} / {d} ({v})".format(n=self.numerator, d=self.denominator, v=self.value))
        

    def __str__(self):
        frac_str = str(self.numerator) + "/" + str(self.denominator)
        return frac_str

    def __repr__(self):
        frac_str = str(self.numerator) + "/" + str(self.denominator)
        return frac_str

    """
    Compares this fraction iwth another given fraction
    frac2 -- fraction to compare size with
    """
    def compare(self, frac2):
        if self.value > frac2.value:
            return 1
        if frac2.value > self.value:
            return -1
        else:
            return 0