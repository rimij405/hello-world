# Copyright 2009 Simon Schampijer
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""MainMenuActivity: The main menu of the game app."""

import threading

# Import and set up the GTK libraires.
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import random as r

# Import the sugar activity materials.
from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityButton
from sugar3.activity.widgets import TitleEntry
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ShareButton
from sugar3.activity.widgets import DescriptionItem

# Import the mini games.
from demo_minigame import DemoMinigame
from weight_a_minute import WAMMinigame

# Seed random.
r.seed()

# List of mini-games to create.
MINIGAMES = [
    WAMMinigame(r),
    DemoMinigame(),
]

class MainMenuActivity(activity.Activity):
    def __init__(self, handle):
        """Set up the activity."""
        activity.Activity.__init__(self, handle)

        # we do not have collaboration features
        # make the share option insensitive
        self.max_participants = 1

        # toolbar with the new toolbar redesign
        toolbar_box = ToolbarBox()

        activity_button = ActivityButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()

        title_entry = TitleEntry(self)
        toolbar_box.toolbar.insert(title_entry, -1)
        title_entry.show()

        description_item = DescriptionItem(self)
        toolbar_box.toolbar.insert(description_item, -1)
        description_item.show()

        share_button = ShareButton(self)
        toolbar_box.toolbar.insert(share_button, -1)
        share_button.show()

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        self.display_menu()

    def display_menu(self):
        """Display a menu option for each mini game using GTK."""
        
        # Set up constants.
        COLS = 3

        # Create the GTK objects.
        grid = Gtk.Grid()
        l = Gtk.Label(None)
        l.set_markup("<span font='20' weight='ultrabold'>Pick a minigame</span>")
        grid.attach(l, 0, 0, COLS, 1)

        # Create the buttons for each mini game.
        for idx, mg in enumerate(MINIGAMES):
            grid.attach(self.make_button(idx, mg), idx % 3, 1 + idx / 3, 1, 1)

        # Set the spacing for the grid.
        grid.set_margin_left(10)
        grid.set_margin_right(10)
        grid.set_margin_bottom(10)
        grid.set_margin_top(10)
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)

        # Show the grid.
        self.set_canvas(grid)
        grid.show_all()

    def make_button(self, idx, mg):
        print("Creating button {id} for {mgn}".format(id=str(idx), mgn=mg.get_name()))
        btn = Gtk.Button.new_with_label(mg.get_name())
        btn.connect("clicked", lambda _: self.run_minigame(mg))
        return btn

    def run_minigame(self, mg):
        """Start the mini game that was selected."""
        print("Getting the panel for minigame '{mgn}'".format(mgn=mg.get_name()))
        cv = mg.get_panel()
        self.set_canvas(cv)
        cv.show_all()
        
        def runner():
            print("Running minigame '{mgn}'".format(mgn=mg.get_name()))
            mg.start(cv)
            # start only completes when the minigame is done
            self.display_menu()

        print("Starting thread for minigame '{mgn}'".format(mgn=mg.get_name()))
        threading.Thread(target=runner).start()

