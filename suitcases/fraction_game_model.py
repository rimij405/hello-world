import fraction as f
import generate_fractions as gfrac
import random as rand

class FractionGameModel:
    def __init__(self):
        rand.seed()

    def start_game(self):
        self.base_frac = gfrac.generate_base_frac(4, 10)
        self.num_over = rand.randint(2, 5)
        self.frac_list = gfrac.generate_fracs(self.base_frac, 7 - self.num_over, self.num_over, 1, 16, 30)

    def check_bag(self, index):
        if self.base_frac.compare(self.frac_list[index]) == -1:
            self.frac_list.pop(index)
            self.num_over -= 1
            if self.num_over == 0:
                return 1
            
            return 0
        
        return -1