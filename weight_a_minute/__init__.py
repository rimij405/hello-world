"""
Module containing code for the WAMMinigame.
"""

import threading

from gi.repository import Gtk

class WAMMinigame:
    def __init__(self):
        """
        Initialize state variables, etc. GUI elements should be initialized
        in get_panel -- you can still set properties on `self` in any method.
        """
        self.score = 0
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
        panel = Gtk.Grid()
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

    def done(self, _):
        self.return_start.set()

