import gi
import os
import subprocess
import ast
from time import sleep
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Handler:

    def __init__(self, org, spinner, window):
    	self.org = org
    	self.spinner = spinner
    	self.window = window

    def regClicked(self, button):
    	self.spinner.start()
    	user = builder.get_object("user")
    	username = user.get_text()
    	tree_iter = self.org.get_active_iter()
    	if tree_iter is not None:
            model = self.org.get_model()
            org = model[tree_iter][0].lower()

    	token = os.popen('./registration.sh ' + username + ' ' + org).read()
    	print(token)
    	sleep(5)
    	window.close()
    	os.system('python3 test2.py ' + token.strip("\n") + ' ' + org + " " + "x")



builder = Gtk.Builder()
builder.add_from_file("register.glade")

userLabel = builder.get_object("userLabel")
userLabel.set_label("Username: ")

orgLabel = builder.get_object("orgLabel")
orgLabel.set_label("Organization: ")

org_store = Gtk.ListStore(str)
orgs = ["Airport", "CCD", "Users"]
for org in orgs:
    org_store.append([org])

org_combo = builder.get_object("orgCombo")
org_combo.set_model(org_store)


regButton = builder.get_object("regSubmit")
regButton.set_label("Submit")
spin = builder.get_object("spin")

window = builder.get_object("main")
window.set_title("Hello")
window.connect("delete-event", Gtk.main_quit)
window.show_all()

builder.connect_signals(Handler(org_combo, spin, window))


Gtk.main()