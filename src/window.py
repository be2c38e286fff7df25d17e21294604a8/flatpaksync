# window.py
#
# Copyright 2020
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk

from .about import FlatpaksyncAbout
from .flatpak.flatpakcmd import flatpakcmd

@Gtk.Template(resource_path='/com/github/be2c38e286fff7df25d17e21294604a8/flatpaksync/window.ui')
class FlatpaksyncWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'FlatpaksyncWindow'

    headerbar = Gtk.Template.Child()
    menu_btn = Gtk.Template.Child()
    sync_btn = Gtk.Template.Child()
    about_menu = Gtk.Template.Child()
    preferences_menu = Gtk.Template.Child()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup()


    def setup(self):
        self.sync_btn.connect("clicked", self.on_sync)
        self.about_menu.connect("activate", self.on_sync)
        self.preferences_menu.connect("activate", self.on_sync)
        #fp = flatpak()


    def on_sync(self, widget):
        about=FlatpaksyncAbout()
        about.present()
