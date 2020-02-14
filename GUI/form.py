
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys
from subprocess import Popen

# all variables
entry = dict()
values = dict()
args = sys.argv
token = args[1]

# all functions
def setBlanks():
    for i in range(1,9):
        if i == 4 :
            continue
        entry[i].set_text('')


def submitClicked(self):
    emptyCheck = True

    for i in range(1,9):
        if i == 4 :
            continue
        values[i] = str(entry[i].get_text())
        if(values[i] == ''):
            emptyCheck = True
            print("\n Entry field "+str(i)+" is empty.")
            break
        emptyCheck = False

    if(emptyCheck == False):
        file = open("result.txt","w")
        for i in range(1,9):
            if i == 4 :
                date = entry[4].get_date()
                val = str(date[2])+'-'+str(date[1])+'-'+str(date[0])
            else:
                val = entry[i].get_text()

            values[i] = str(val)
            print(values[i])
            file.write(values[i]+"\n")

        access = entry[9].get_model()[entry[9].get_active()]
        val = access[1]
        values[9] = str(val)
        file.write(values[9]+"\n")

        file.write(" ")
        file.close()
        setBlanks()
    print(token)
    execute = "./init_ledger.sh "  + token
    print(execute)
    # Popen(execute, shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)
    result = os.popen(execute).read()
    # print(result)
    exit(0)

def comboValueChange(self):
    access = entry[9].get_model()[entry[9].get_active()]
    value = access[1]
    print('Access level set as ' + str(value))



# all widgets
builder = Gtk.Builder()
builder.add_from_file("form.glade")


entry[1] = builder.get_object('entry1') #userID
entry[2] = builder.get_object('entry2') #Src
entry[3] = builder.get_object('entry3') #Name
entry[5] = builder.get_object('entry5') #phone
entry[6] = builder.get_object('entry6') #creditcard
entry[7] = builder.get_object('entry7') #aadhar
entry[8] = builder.get_object('entry8') #email

entry[4] = builder.get_object('entry4') #Date

optionStore=Gtk.ListStore(int,str)
optionOptions = ["High","Medium","Low"]
for ops in optionOptions:
    optionStore.append([None,ops])
entry[9] = builder.get_object("entry9") #access level
entry[9].set_model(optionStore)
entry[9].set_entry_text_column(1)
entry[9].connect('changed',comboValueChange)

button = builder.get_object('submit')
button.connect('clicked',submitClicked)

window = builder.get_object("window1")
window.connect('delete-event',Gtk.main_quit)
window.show_all()

Gtk.main()
