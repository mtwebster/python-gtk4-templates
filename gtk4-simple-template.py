#!/usr/bin/python3

import setproctitle
import signal
import sys

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio

def on_activate(app):
    print("Application activate")

    window = Gtk.ApplicationWindow(application=app)
    window.set_title("Foo Bar")
    window.connect("destroy", lambda w, app: app.quit, app)
    # ...
    # ...
    # box = Gtk.Box() ...
    # ...
    # ...

    window.present()

if __name__ == "__main__":
    setproctitle.setproctitle("foobar")

    app = Gtk.Application(application_id="org.foo.Bar", flags=Gio.ApplicationFlags.DEFAULT_FLAGS)
    app.connect("activate", on_activate)

    signal.signal(signal.SIGINT, app.quit)
    sys.exit(app.run(sys.argv))
