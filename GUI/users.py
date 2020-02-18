
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys
import ast

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
        js = result.split(" ")[3]
        js = ast.literal_eval(js)
        pretty = ' '.join(result.split(" ")[:3])
        stri = ""
        for key in js.keys():
            stri += key + ": \t" + js[key] + "\n"

        result =  pretty + "\n" + stri
        dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Queried data for "+str(value))
        dialog.format_secondary_text(result)
        dialog.run()
        dialog.destroy()
        label.set_text('')

def revokeButton(self):
    value = str(entry.get_text())
    # label.set_text('Revoking Consent')
    result = os.popen('./users.sh ' + token + ' ' + 'revokeconsent' + ' ' + value).read()
    print(result)

def deleteButton(self):
    value = str(entry.get_text())
    # label.set_text('Deleting data from system')
    result = os.popen('./users.sh ' + token + ' ' + 'delete' + ' ' + value).read()
    print(result)

def applicationFormButton(self):
    # label.set_text('Form window is now open')
    os.system('python3 form.py ' + token)


# all widgets
builder = Gtk.Builder()
builder.add_from_file("user.glade")


button1 = builder.get_object('button1')
button1.connect('clicked',queryButton)
button2 = builder.get_object('button2')
button2.connect('clicked',revokeButton)
button3 = builder.get_object('button3')
button3.connect('clicked',deleteButton)
button4 = builder.get_object('button4')
button4.connect('clicked',applicationFormButton)
entry = builder.get_object('entry')
label = builder.get_object('label')
message = builder.get_object('message')
window = builder.get_object("window1")
window.connect('delete-event',Gtk.main_quit)
window.show_all()

Gtk.main()
