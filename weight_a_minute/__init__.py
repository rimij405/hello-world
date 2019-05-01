"""
Module containing code for the WAMMinigame.
"""

import threading

from gi.repository import Gtk
from suitcases import fraction
from weight_a_minute import model
import random

class WAMMinigame:
    def __init__(self, r):
        """
        Initialize state variables, etc. GUI elements should be initialized
        in get_panel -- you can still set properties on `self` in any method.
        """
        self.game = model.WAMGameModel(r)
        self.return_start = threading.Event()

    def get_name(self):
        """
        This is the name of the app, as displayed in the main menu.
        """
        return "Weight A Minute!"

    def get_panel(self):
        """
        Gets the panel to put into the window when the minigame is chosen.

        Its size will automatically be set by the manager class. Don't depend
        on it remaining the same if it's set in here.

        This panel is shown with show_all, so you don't need to manually call
        .show() on every child element.
        """

        if(not self.game.initialized):
            self.game.start_game()

        print("Creating the game UI.")

        # Create the main Grid.
        panel = Gtk.Grid()
        panel.set_column_spacing(20)
        panel.set_row_spacing(20)

        """
        panel.set_margin_left(10)
        panel.set_margin_right(10)
        panel.set_margin_bottom(10)
        panel.set_margin_top(10)
        panel.set_column_spacing(10)
        panel.set_row_spacing(10)
        """
        # Create labels.
        self.create_labels()

        # Create the buttons.
        self.create_buttons()

        # Create the top row.
        top_row = Gtk.Grid()
        top_row.set_column_spacing(20)
        top_row.set_row_spacing(20)

        # Add labels to the top row.    
        top_row.add(self.labels["minigame"])
        top_row.add(self.labels["instructions"])
        top_row.add(self.labels["score"])

        # Add buttons to the top row.
        top_row.add(self.buttons["quit"])        

        # Create the middle row.
        middle_row = Gtk.Grid()
        middle_row.set_column_spacing(20)
        middle_row.set_row_spacing(20)
        
        # Create labels.
        middle_row.add(self.labels["weight-limit"])
        middle_row.add(self.labels["bags"])
        middle_row.add(self.labels["remaining"])

        # Create the bottom row.
        bottom_row = Gtk.Grid()
        bottom_row.set_column_spacing(20)
        bottom_row.set_row_spacing(20)

        # Create the labels.
        bottom_row.add(self.labels["result"])

        # Create the buttons.        
        for idx in range(0, len(self.game.frac_list)):
            if(idx == 0):
                bottom_row.attach_next_to(self.buttons["bag-{}".format(idx)], self.labels["result"], Gtk.PositionType.BOTTOM, 1, 1)
            else:
                bottom_row.attach_next_to(self.buttons["bag-{}".format(idx)], self.buttons["bag-{}".format(idx - 1)], Gtk.PositionType.BOTTOM, 1, 1)

        """        
        score_btn = Gtk.Button.new_with_label("Increase scores")
        score_btn.connect("clicked", self.score_up)
        panel.attach(score_btn, 0, 1, 1, 1)
        """

        panel.attach(top_row, 0, 0, 1, 1)
        panel.attach_next_to(middle_row, top_row, Gtk.PositionType.BOTTOM, 1, 1)
        panel.attach_next_to(bottom_row, middle_row, Gtk.PositionType.BOTTOM, 1, 1)
        return panel

    def start(self, panel):
        """
        Used to pass control to the minigame. Sort of a "main method". When
        the minigame ends, return from this method to return to the main menu.
        
        Takes the panel returned by get_panel(), after it's been slotted into
        the GUI.
        """ 
        # Start the game.
        self.game.start_game()
        self.return_start.clear()
        self.return_start.wait()

    def update_score(self, _):
        self.labels["score"].set_text("Score: {}".format(str(self.game.score)))

    def create_labels(self):
        print("Create labels for game.")
        self.labels = {}

        self.labels["minigame"] = Gtk.Label("Weight a Minute!")
        self.labels["instructions"] = Gtk.Label("Select all the fractions that are over the weight limit!")
        self.labels["score"] = Gtk.Label("Score: {}".format(str(self.game.score)))

        self.labels["weight-limit"] = Gtk.Label("Weight Limit: {}".format(self.game.base_frac))
        self.labels["bags"] = Gtk.Label("Bags: {}".format(self.game.frac_list))
        self.labels["remaining"] = Gtk.Label("There are {} bag(s) left!".format(self.game.num_over))
        self.labels["result"] = Gtk.Label("")

        return self.labels

    def create_buttons(self):
        print("Create buttons for game.")
        self.buttons = {}

        btn_quit = Gtk.Button.new_with_label("Quit!")
        btn_quit.connect("clicked", self.done)
        self.buttons["quit"] = btn_quit

        # Create one button for each fraction in fraction list.
        def create_fraction_button(label):
            btn = Gtk.Button.new_with_label("Bag: {}".format(label))
            return btn

        for idx in range(0, len(self.game.frac_list)):
            print("Creating bag-{}.".format(idx))
            bag_label = "bag-{}".format(idx)
            bag_value = idx
            bag_btn = create_fraction_button(bag_label)
            bag_btn.connect("clicked", self.on_bag_select, bag_value)
            self.buttons[bag_label] = bag_btn

        return self.buttons

    def on_bag_select(self, _, value):
        print("Selected bag with {}".format(value))
        check = self.game.check_bag(int(value))
        if(check == 0):
            self.game.result = "Nice one! Bag {} is over the weight limit!".format(value)
            _.set_sensitive(False)
            self.game.increment_score()
        if(check == -1):
            self.game.result = "Try again, that bag isn't over the weight limit."            
            self.game.decrement_score()
        if(check == 1):
            self.game.result = "Congratulations! You've found all of the bags!\nQuit to the main menu and return here to play again."
            self.game.increment_score()
        self.update_result()
        self.update_remaining()

    def update_result(self):
        self.labels["result"].set_text(self.game.result)  
        self.labels["score"].set_text("Score: {}".format(str(self.game.score)))

    def update_remaining(self):
        self.labels["bags"].set_text("Bags: {}".format(self.game.frac_list))
        self.labels["remaining"].set_text("There are {} bag(s) left!".format(self.game.num_over))

    def done(self, _):
        self.return_start.set()

