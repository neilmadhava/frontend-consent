import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import os
import sys
from subprocess import Popen


entry = dict()
values = dict()


def buttonClick(self):
	for i in range(1,5):
		values[i] = str(entry[i].get_text())
		if(values[i] == ''):
			print('Missing values')
			return
	tokens = os.popen('./init_setup.sh ' + values[1] + ' ' + values[2] + ' ' + values[3] + ' ' + values[4]).read()
	tokens = tokens.split("\n")
	airport_token = tokens[0]
	ccd_token = tokens[1]
	users_token = tokens[2]
	mcd_token = tokens[3]
	print(airport_token)
	print(ccd_token)
	print(users_token)
	print(mcd_token)
	execute = "python3 UserInterface.py " + airport_token + " " + ccd_token + " " + users_token + " " + mcd_token
	Popen(execute, shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)
	exit(0)

builder = Gtk.Builder()
builder.add_from_file('combined.glade')


entry[1] = builder.get_object('entry1')
entry[2] = builder.get_object('entry2')
entry[3] = builder.get_object('entry3')
entry[4] = builder.get_object('entry4')
button = builder.get_object('submitButton')
button.connect('clicked',buttonClick)
window = builder.get_object('window1')
window.connect('delete-event',Gtk.main_quit)
window.show_all()

Gtk.main()
