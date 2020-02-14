
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys
# all variables
args = sys.argv
token = args[1]
org = args[2]

# all functions
def queryButton(self):
    value = str(entry.get_text())
    if value == '':
        label.set_text('username field is empty')
    else:
        label.set_text('Querying Data for '+str(value))
        result = os.popen('./query.sh ' + token + ' ' + org + ' ' + value).read()
        print(result)
        dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Queried data for "+str(value))
        # result = 'some text' # insert your querying data command here after formatting it as required
        dialog.format_secondary_text(result)
        dialog.run()
        dialog.destroy()

# all widgets
builder = Gtk.Builder()
builder.add_from_file("CCD.glade")


button2 = builder.get_object('button2')
button2.connect('clicked',queryButton)
entry = builder.get_object('entry')
label = builder.get_object('label')
message = builder.get_object('message')
window = builder.get_object("window1")
window.connect('delete-event',Gtk.main_quit)
window.set_title(org.upper() + " Query")
window.show_all()

Gtk.main()
