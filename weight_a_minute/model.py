"""
Represents the game model and keeps track of state.
"""

from suitcases import fraction as f
from suitcases import generate_fractions as gfrac
import random

class WAMGameModel:
    def __init__(self, r):
        print("Initializing the game model.")
        self.r = r
        self.score = 0
        self.result = ""
        self.gtk_widget = {}
        self.initialized = False

    def start_game(self):
        if(not self.initialized):
            print("Start of the game.")
            self.base_frac = gfrac.generate_base_frac(10, 4)
            self.num_over = self.r.randint(2, 5)
            self.frac_list = gfrac.generate_fracs(self.base_frac, 7 - self.num_over, self.num_over, 1, 16, 30)
            self.initialized = True

    def check_bag(self, index):
        print("Checking bag at index {idx}".format(idx=index))
        if self.base_frac.compare(self.frac_list[index]) == -1:
            self.frac_list.pop(index)
            self.num_over -= 1
            if self.num_over == 0:
                return 1
            return 0
        return -1

    def add_widget(self, widgetId, widget):
        print("Adding widget {wid}".format(wid=widgetId))
        if widgetId is not None and type(widgetId) == str and len(widgetId) > 0 and widget is not None:
            self.gtk_widget[widgetId] = widget
            return self.get_widget(widgetId)
        return None

    def get_widget(self, widgetId):        
        print("Getting widget {wid}".format(wid=widgetId))
        if widgetId is not None and type(widgetId) == str and len(widgetId) > 0:
            return self.gtk_widget.get(widgetId, None)
        return None

    def increment_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0
