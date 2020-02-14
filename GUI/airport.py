
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# all variables


# all functions
def queryButton(self):
    value = str(entry.get_text())
    if value == '':
        label.set_text('username field is empty')
    else:
        label.set_text('Querying Data for '+str(value))
        dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Queried data for "+str(value))
        result = 'some text' # insert your querying data command here after formatting it as required
        dialog.format_secondary_text(result)
        dialog.run()
        dialog.destroy()


def instantiateButton(self):
    label.set_text('Instantiate Data')



# all widgets
builder = Gtk.Builder()
builder.add_from_file("airport.glade")


button2 = builder.get_object('button2')
button2.connect('clicked',queryButton)
button1 = builder.get_object('button1')
button1.connect('clicked',instantiateButton)
entry = builder.get_object('entry')
label = builder.get_object('label')
message = builder.get_object('message')
window = builder.get_object("window1")
window.connect('delete-event',Gtk.main_quit)
window.show_all()

Gtk.main()
