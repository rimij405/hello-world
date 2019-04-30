class Fraction:
    ''
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.value = float(numerator / denominator)

    def __str__(self):
        frac_str = str(self.numerator) + "/" + str(self.denominator)
        return frac_str

    def __repr__(self):
        frac_str = str(self.numerator) + "/" + str(self.denominator)
        return frac_str

    def compare(self, frac2):
        if self.value > frac2.value:
            return 1
        if frac2.value > self.value:
            return -1
        else:
            return 0