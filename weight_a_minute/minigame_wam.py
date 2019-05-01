from gi.repository import Gtk

class WAMMinigameModel:
    def __init__(self):
        
        def create_window():
            window = Gtk.Window()
            window.connect("destroy", Gtk.main_quit)
            return window

        self._window = create_window()
    
    def update(self):
        pass

    def get_window(self):
        return self._window

    def get_panel(self):
        pass

    def get_state(self):
        pass
