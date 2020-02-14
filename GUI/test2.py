import gi
import os
import sys
from time import sleep

gi.require_version("Gtk", "3.0")
args = sys.argv
token = args[1]
org = args[2]
command = args[3]

from gi.repository import Gtk
from subprocess import Popen

class Handler:

	def __init__(self, token, org, command, thingsDone):
		self.token = token
		self.org = org.lower()
		self.command = command
		self.thingsDone = thingsDone

	def button1_clicked(self, button):
		if self.command.lower() == "createchannel":
			r = os.popen('./init_setup.sh ' + self.token + ' ' + self.org + ' ' + self.command.lower()).read()
			print(r)
			self.command = "joinchannel"
			execute = "python3 test2.py " + self.token + " " + self.org.lower() + " " + self.command
			Popen(execute, shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)
			exit(0)
		if self.command.lower() == "joinchannel":
			r = os.popen('./init_setup.sh ' + self.token + ' ' + self.org + ' ' + self.command.lower()).read()
			print(r)
			self.command = "updateanchorpeers"
			execute = "python3 test2.py " + self.token + " " + self.org.lower() + " " + self.command
			Popen(execute, shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)
			exit(0)
		if self.command.lower() == "updateanchorpeers":
			r = os.popen('./init_setup.sh ' + self.token + ' ' + self.org + ' ' + self.command.lower()).read()
			print(r)
			self.command = "installchaincode"
			execute = "python3 test2.py " + self.token + " " + self.org.lower() + " " + self.command
			Popen(execute, shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)
			exit(0)
		if self.command.lower() == "installchaincode":
			r = os.popen('./init_setup.sh ' + self.token + ' ' + self.org + ' ' + self.command.lower()).read()
			print(r)
			self.command = "instantiatechaincode"
			execute = "python3 test2.py " + self.token + " " + self.org.lower() + " " + self.command
			Popen(execute, shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)
			exit(0)
		if self.command.lower() == "instantiatechaincode":
			r = os.popen('./init_setup.sh ' + self.token + ' ' + self.org + ' ' + self.command.lower()).read()
			print(r)
			if self.org == "airport" or self.org == "ccd":
				execute = "python3 query.py " + self.token + " " + self.org.lower()
			if self.org == "users":
				execute = "python3 users.py " + self.token + " " + self.org.lower()
			Popen(execute, shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)
			exit(0)

builder = Gtk.Builder()
builder.add_from_file("nextButton.glade")

button1 = builder.get_object("button1")
button1.set_label("Next")

label = builder.get_object("nextID")
thingsDone = builder.get_object("thingsDone")

if command == "createchannel":
	label.set_text("➕  Create Channel")
if command == "joinchannel":
	label.set_text("➕  Join Channel")
	if org == "airport":
		thingsDone.set_text("✔ Channel created successfully")
if command == "updateanchorpeers":
	label.set_text("➕  Update Anchor Peers")
	thingsDone.set_text("✔ Channel created successfully\n✔ "\
		+ org.upper() + " joined channel successfully")

if command == "installchaincode":
	label.set_text("➕  Install Chaincode")
	thingsDone.set_text("✔ Channel created successfully\n✔ "\
		+ org.upper() + " joined channel successfully\n✔ "\
		+ org.upper() + " anchor peers updated successfully")

if command == "instantiatechaincode":
	label.set_text("➕  Instantiate Chaincode")
	thingsDone.set_text("✔ Channel created successfully\n✔ "\
		+ org.upper() + " joined channel successfully\n✔ "\
		+ org.upper() + " anchor peers updated successfully\n✔ "\
		+ org.upper() + "installed chaincode")


window = builder.get_object("window1")
if org.lower() == "ccd":
	window.set_title(org.upper())
else:
	window.set_title(org.title())

window.connect("delete-event", Gtk.main_quit)
window.show_all()

builder.connect_signals(Handler(token, org, command, thingsDone))

Gtk.main()