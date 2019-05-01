"""
Module containing code for the WAMMinigame.
"""

import threading

from gi.repository import Gtk
from minigame_wam import WAMMinigameModel

class WAMMinigame:
    def __init__(self):
        """
        Initialize state variables, etc. GUI elements should be initialized
        in get_panel -- you can still set properties on `self` in any method.
        """
        self.score = 0
        self.model = WAMMinigameModel()
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
        # Create the main Grid.
        panel = Gtk.Grid()

        """
        panel.set_margin_left(10)
        panel.set_margin_right(10)
        panel.set_margin_bottom(10)
        panel.set_margin_top(10)
        panel.set_column_spacing(10)
        panel.set_row_spacing(10)
        """

        # Create widgets.
        self.minigame_label = Gtk.Label("Weight a Minute!")
        self.minigame_label.set_hexpand(True)

        # Add widgets.
        panel.add(self.minigame_label, 0, 0, 1, 1)

        """
        
        score_btn = Gtk.Button.new_with_label("Increase scores")
        score_btn.connect("clicked", self.score_up)
        panel.attach(score_btn, 0, 1, 1, 1)
        self.score_lbl = Gtk.Label("Increase your scores!")
        panel.attach(self.score_lbl, 0, 2, 1, 1)
        quit_btn = Gtk.Button.new_with_label("Quit!")
        quit_btn.connect("clicked", self.done)
        panel.attach(quit_btn, 0, 3, 1, 1)
        """

        return panel

    def start(self, panel):
        """
        Used to pass control to the minigame. Sort of a "main method". When
        the minigame ends, return from this method to return to the main menu.
        
        Takes the panel returned by get_panel(), after it's been slotted into
        the GUI.
        """        
        self.return_start.clear()
        self.return_start.wait()

    def score_up(self, _):
        self.score += 1
        self.score_lbl.set_text(str(self.score))

    def done(self, _):
        self.return_start.set()

