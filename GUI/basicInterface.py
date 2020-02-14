
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from subprocess import Popen

# all variables


# all functions
def submitClicked(self):
    combovalue = combo.get_model()[combo.get_active()]
    organization = combovalue[1]
    # print(value[1])
    entryvalue = entry.get_text()
    if(organization and entryvalue):
        dump.set_text(' ')
        token = os.popen('./registration.sh ' + entryvalue + ' ' + organization.lower()).read().strip("\n")
        print(token)
        if organization.lower() == "airport":
            command = "createchannel"
            execute = "python3 test2.py " + token + " " + organization.lower() + " " + command
        else:
            command = "joinchannel"
            execute = "python3 test2.py " + token + " " + organization.lower() + " " + command
        Popen(execute, shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)
        exit(0)
    else:
        dump.set_text('Fields are empty.')
        print('Fields are empty')

def comboValueChange(self):
    combovalue = combo.get_model()[combo.get_active()]
    organization = combovalue[1]
    window.set_title(organization)


# all widgets
builder = Gtk.Builder()
builder.add_from_file("basic.glade")


orgstore=Gtk.ListStore(int,str)
orgOptions = ["Users","Airport","CCD"]
for org in orgOptions:
    orgstore.append([None,org])
combo = builder.get_object("comboBox")
combo.set_model(orgstore)
combo.set_entry_text_column(1)
combo.connect('changed',comboValueChange)

entry = builder.get_object('entryBox')
label1 = builder.get_object('usernameLabel')
label2 = builder.get_object('organizationLabel')
dump = builder.get_object('dumpLabel')
button = builder.get_object('submitButton')

button.connect('clicked',submitClicked)

window = builder.get_object("window1")
window.connect('delete-event',Gtk.main_quit)
window.show_all()

Gtk.main()