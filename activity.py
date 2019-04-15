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

"""HelloWorld Activity: A case study for developing an activity."""

import threading

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityButton
from sugar3.activity.widgets import TitleEntry
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ShareButton
from sugar3.activity.widgets import DescriptionItem

from demo_minigame import DemoMinigame

MINIGAMES = [
    DemoMinigame()
]

class HelloWorldActivity(activity.Activity):
    def __init__(self, handle):
        """Set up the HelloWorld activity."""
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

        # label with the text, make the string translatable
        self.display_menu()

    def display_menu(self):
        grid = Gtk.Grid()
        grid.set_hexpand(True)
        grid.set_vexpand(True)
        COLS = 3
        l = Gtk.Label("Pick a minigame")
        grid.attach(l, 0, 0, COLS, 1)
        l.show()
        for idx, mg in enumerate(MINIGAMES):
            btn = Gtk.Button.new_with_label(mg.get_name())
            btn.connect("clicked", lambda _: self.run_minigame(mg))
            grid.attach(btn, idx % 3, 1 + idx / 3, 1, 1)
            btn.show()
        self.set_canvas(grid)
        grid.show()

    def run_minigame(self, mg):
        cv = mg.get_panel()
        cv.set_hexpand(True)
        cv.set_vexpand(True)
        self.set_canvas(cv)
        cv.show_all()
        
        def runner():
            mg.start(cv)
            # start only completes when the minigame is done
            self.display_menu()

        threading.Thread(target=runner).start()

