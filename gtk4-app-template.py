#!/usr/bin/python3

import setproctitle
import signal
import sys

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio
class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self,
                                 application_id="org.foo.Bar",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)
        print("Application init")
        self.window = None
        # ...
        # ...

    def do_startup(self):
        print("Application startup")
        # ...
        # ...
        Gtk.Application.do_startup(self) # if you're going to be a dbus service, set up and export before this.
        # ...
        # ...

    def do_activate(self):
        print("Application activate")

        if self.window is None:
            print("Application new window")
            self.window = Gtk.ApplicationWindow(application=self)
            self.window.set_title("Foo Bar")
            self.window.connect("destroy", self.quit)

        self.window.present()

    def do_shutdown(self):
        print("Application shutdown")
        # ...
        # ...
        Gtk.Application.do_shutdown(self)

if __name__ == "__main__":
    setproctitle.setproctitle("foobar")

    app = MyApplication()

    signal.signal(signal.SIGINT, lambda a, b: app.quit())
    sys.exit(app.run(sys.argv))
