
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys
import ast
from pprint import pprint,pformat
import json

args = sys.argv
airport_token = args[1]
ccd_token = args[2]
users_token = args[3]
mcd_token = args[4]



UI_FILE = "UserInterface.glade"




class GUI:
    entry = dict()
    values = dict()


    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(UI_FILE)
        self.builder.connect_signals(self)
        opts=Gtk.ListStore(int,str)
        options = ["High","Medium","Low"]
        for o in options:
            opts.append([None,o])

        optsOrg=Gtk.ListStore(int,str)
        options = ["MCD","CCD"]
        for o in options:
            optsOrg.append([None,o])
        self.entry[9] = self.builder.get_object("entry9") #access level
        self.entry[9].set_model(opts)
        self.entry[9].set_entry_text_column(1)
        self.entry[10] = self.builder.get_object("entry10") #access level
        self.entry[10].set_model(opts)
        self.entry[10].set_entry_text_column(1)
        self.entry[11] = self.builder.get_object("entry11") #access level
        self.entry[11].set_model(optsOrg)
        self.entry[11].set_entry_text_column(1)
        self.entry[12] = self.builder.get_object("entry12") #access level
        self.entry[12].set_model(optsOrg)
        self.entry[12].set_entry_text_column(1)
        self.window = self.builder.get_object('window')
        self.window.show_all()








    def on_window_destroy(self, window):
        Gtk.main_quit()



    def home_clicked (self, button):
        stack = self.builder.get_object('stack')
        home_button = self.builder.get_object('home_button')
        stack.set_visible_child(home_button)


    def button_clicked (self, button):
        stack = self.builder.get_object('stack')
        notebook_box = self.builder.get_object('notebook_box')
        stack.set_visible_child(notebook_box)


    def applicationFormOpenButton(self,button):
        stack = self.builder.get_object('stack')
        applicationForm = self.builder.get_object('ApplicationFormBox')
        stack.set_visible_child(applicationForm)


    def updateButton(self,button):
        stack = self.builder.get_object('stack')
        consentWindow = self.builder.get_object('updateConsentWindow')
        stack.set_visible_child(consentWindow)

    def revokeButton(self,button):
        stack = self.builder.get_object('stack')
        revokeconsentWindow = self.builder.get_object('revokeConsentWindow')
        stack.set_visible_child(revokeconsentWindow)



    def queryButtonAirport(self,button):
        entry = self.builder.get_object('usernameEntry')
        infoLabel = self.builder.get_object('infoLabel')
        value = str(entry.get_text())
        if value == '':
            infoLabel.set_text('Username field is empty')
        else:
            infoLabel.set_text('')
            result = os.popen('./query.sh ' + airport_token + ' ' + 'airport' + ' ' + value + ' ' + 'queryprivate').read()
            print(result)
            dialog = Gtk.MessageDialog(parent=self.window, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="Queried data for "+str(value))
            if(result[0]!='E'):
                result = ast.literal_eval(result)
                dialog.format_secondary_text(pformat(result))
            else:
                dialog.format_secondary_text(result)
            dialog.run()
            dialog.destroy()

    def queryButtonCCD(self,button):
        entry = self.builder.get_object('usernameEntry')
        infoLabel = self.builder.get_object('infoLabel')
        value = str(entry.get_text())
        if value == '':
            infoLabel.set_text('Username field is empty')
        else:
            infoLabel.set_text('')
            result = os.popen('./query.sh ' + ccd_token + ' ' + 'ccd' + ' ' + value).read()
            print(result)
            dialog = Gtk.MessageDialog(parent=self.window, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="Queried data for "+str(value))
            if(result[0]!='E'):
                result = ast.literal_eval(result)
                dialog.format_secondary_text(pformat(result))
            else:
                dialog.format_secondary_text(result)
            dialog.run()
            dialog.destroy()

    def queryButtonUser(self,button):
        entry = self.builder.get_object('usernameEntry')
        infoLabel = self.builder.get_object('infoLabel')
        value = str(entry.get_text())
        if value == '':
            infoLabel.set_text('Username field is empty')
        else:
            infoLabel.set_text('')
            result = os.popen('./query.sh ' + users_token + ' ' + 'users' + ' ' + value).read()
            print(result)
            dialog = Gtk.MessageDialog(parent=self.window, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="Queried data for "+str(value))
            if(result[0]!='E'):
                result = ast.literal_eval(result)
                dialog.format_secondary_text(pformat(result))
            else:
                dialog.format_secondary_text(result)
            dialog.run()
            dialog.destroy()

    def queryButtonMCD(self,button):
        entry = self.builder.get_object('usernameEntry')
        infoLabel = self.builder.get_object('infoLabel')
        value = str(entry.get_text())
        if value == '':
            infoLabel.set_text('Username field is empty')
        else:
            infoLabel.set_text('')
            result = os.popen('./query.sh ' + mcd_token + ' ' + 'mcd' + ' ' + value).read()
            print(result)
            dialog = Gtk.MessageDialog(parent=self.window, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="Queried data for "+str(value))
            if(result[0]!='E'):
                result = ast.literal_eval(result)
                dialog.format_secondary_text(pformat(result))
            else:
                dialog.format_secondary_text(result)
            dialog.run()
            dialog.destroy()

    def queryPublic(self, button):
        entry = self.builder.get_object('usernameEntry')
        infoLabel = self.builder.get_object('infoLabel')
        value = str(entry.get_text())
        if value == '':
            infoLabel.set_text('Username field is empty')
        else:
            infoLabel.set_text('')
            result = os.popen('./query.sh ' + airport_token + ' ' + 'airport' + ' ' + value + ' ' + 'querypublic').read()
            print(result)
            dialog = Gtk.MessageDialog(parent=self.window, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="Queried data for "+str(value))
            if(result[0]!='E'):
                result = ast.literal_eval(result)
                dialog.format_secondary_text(pformat(result))
            else:
                dialog.format_secondary_text(result)
            dialog.run()
            dialog.destroy()

    def queryAll(self, button):
        entry = self.builder.get_object('usernameEntry')
        infoLabel = self.builder.get_object('infoLabel')
        value = str(entry.get_text())
        if value == '':
            infoLabel.set_text('Username field is empty')
        else:
            infoLabel.set_text('')
            result = os.popen('./query.sh ' + airport_token + ' ' + 'airport' + ' ' + value + ' ' + 'queryall').read()
            print(result)
            dialog = Gtk.MessageDialog(parent=self.window, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="Queried data for "+str(value))
            if(result[0]!='E'):
                # result = ast.literal_eval(result)
                js = json.loads(result)
                pprint(js)
                stack = self.builder.get_object('stack')
                query_box = self.builder.get_object('scrollBox')
                stack.set_visible_child(query_box)
                audit_result = self.builder.get_object('scrollResult')
                output = ""
                i=1
                for key in js :
                    output+="\n\nKey: " + key['Key']
                    for k in key['Record']:
                        output+=str("\n\t\t"+str(k)+" : "+str(key['Record'][k]))
                audit_result.set_text(output)
            else:
                dialog.format_secondary_text(result)
                dialog.run()
                dialog.destroy()





    def updateConsent(self,button):
        entry = self.builder.get_object('userEntry')
        value = str(entry.get_text())
        access = self.entry[10].get_model()[self.entry[10].get_active()]
        consent = access[1]
        org = self.entry[12].get_model()[self.entry[12].get_active()]
        orgSelected = org[1]
        print(value + " " + consent + " " + orgSelected)
        dialog = Gtk.MessageDialog(parent=self.window, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="Update Result")
        result = os.popen('./users.sh ' + users_token + ' ' + 'update' + ' ' + value + ' ' + consent + ' ' + orgSelected).read()
        dialog.format_secondary_text(result)
        dialog.run()
        dialog.destroy()
        stack = self.builder.get_object('stack')
        notebook_box = self.builder.get_object('notebook_box')
        stack.set_visible_child(notebook_box)

    def revokeConsent(self,button):
        entry = self.builder.get_object('userEntry1')
        value = str(entry.get_text())
        org = self.entry[11].get_model()[self.entry[11].get_active()]
        orgSelected = org[1]
        print(value + " " + orgSelected)
        dialog = Gtk.MessageDialog(parent=self.window, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="Revoke Result")
        result = os.popen('./users.sh ' + users_token + ' ' + 'revokeconsent' + ' ' + value + ' ' + orgSelected).read()
        dialog.format_secondary_text(result)
        dialog.run()
        dialog.destroy()
        stack = self.builder.get_object('stack')
        notebook_box = self.builder.get_object('notebook_box')
        stack.set_visible_child(notebook_box)

    def deleteDataButton(self,button):
        entry = self.builder.get_object('usernameEntry')
        infoLabel = self.builder.get_object('infoLabel')
        value = str(entry.get_text())
        if value == '':
            infoLabel.set_text('Username field is empty')
        else:
            infoLabel.set_text('')
            dialog = Gtk.MessageDialog(parent=self.window, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="Delete Result")
            result = os.popen('./users.sh ' + users_token + ' ' + 'delete' + ' ' + value).read()
            print(result)
            dialog.format_secondary_text(result)
            dialog.run()
            dialog.destroy()
            stack = self.builder.get_object('stack')
            notebook_box = self.builder.get_object('notebook_box')
            stack.set_visible_child(notebook_box)

    def applicationFormSubmitButton(self,button):
        self.entry[1] = self.builder.get_object('entry1') #userID
        self.entry[2] = self.builder.get_object('entry2') #Src
        self.entry[3] = self.builder.get_object('entry3') #Name
        self.entry[4] = self.builder.get_object('entry4') #Date
        self.entry[5] = self.builder.get_object('entry5') #phone
        self.entry[6] = self.builder.get_object('entry6') #creditcard
        self.entry[7] = self.builder.get_object('entry7') #aadhar
        self.entry[8] = self.builder.get_object('entry8') #email
        noticeLabel = self.builder.get_object('noticeLabel')
        emptyCheck = True
        for i in range(1,9):
            if i == 4 :
                continue
            self.values[i] = str(self.entry[i].get_text())
            if(self.values[i] == ''):
                emptyCheck = True
                notice = "\n Entry field "+str(i)+" is empty."
                print(notice)
                noticeLabel.set_text(notice)
                break
            emptyCheck = False
        if(emptyCheck == False):
            file = open("result.txt","w")
            for i in range(1,10):
                if i == 4 :
                    date = self.entry[4].get_date()
                    val = str(date[2])+'-'+str(date[1])+'-'+str(date[0])
                elif i == 9 :
                    access = self.entry[9].get_model()[self.entry[9].get_active()]
                    val = access[1]
                else:
                    val = self.entry[i].get_text()
                self.values[i] = str(val)
                file.write(self.values[i]+"\n")
            file.write(" ")
            file.close()
            dialog = Gtk.MessageDialog(parent=self.window, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="Application Form")
            execute = "./init_ledger.sh "  + users_token
            result = os.popen(execute).read()
            dialog.format_secondary_text(result)
            dialog.run()
            dialog.destroy()
            for i in range(1,9):
                if i == 4 :
                    continue
                elif i == 9 :
                    continue
                else :
                    self.entry[i].set_text('')
            stack = self.builder.get_object('stack')
            notebook_box = self.builder.get_object('notebook_box')
            stack.set_visible_child(notebook_box)




    def blockNumQuery(self,button):
        entry = self.builder.get_object('usernameEntry')
        value = str(entry.get_text())
        result = os.popen('./blockchain.sh ' + users_token + ' ' + 'blocknum' + ' ' + value).read()
        # print(result)
        dialog = Gtk.MessageDialog(parent=self.window, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="Result for Query")
        dialog.format_secondary_text(result)
        dialog.run()
        dialog.destroy()

    def blocktx(self,button):
        entry = self.builder.get_object('usernameEntry')
        value = str(entry.get_text())
        result = os.popen('./blockchain.sh ' + users_token + ' ' + 'blocktx' + ' ' + value).read()
        pprint(json.loads(result)['transactionEnvelope']['payload']['data']['actions'][0]['payload']['action']['proposal_response_payload'], width=300, depth=10, compact=True)
        dialog = Gtk.MessageDialog(parent=self.window, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="Result for Query")
        dialog.format_secondary_text(pformat(json.loads(result)['transactionEnvelope']['payload']['data']['actions'][0]['payload']['action']['proposal_response_payload'], width=300, depth=10, compact=True))
        dialog.run()
        dialog.destroy()

    def chainInfo(self,button):
        entry = self.builder.get_object('usernameEntry')
        value = str(entry.get_text())
        result = os.popen('./blockchain.sh ' + users_token + ' ' + 'chaininfo' + ' ' + value).read()
        dialog = Gtk.MessageDialog(parent=self.window, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="Result for Query")
        dialog.format_secondary_text(pformat(json.loads(result), compact=True))
        dialog.run()
        dialog.destroy()


    def getHistory(self,button):
        entry = self.builder.get_object('usernameEntry')
        infoLabel = self.builder.get_object('infoLabel')
        value = str(entry.get_text())
        if value == '':
            infoLabel.set_text('Username field is empty')
        else:
            infoLabel.set_text('')
            result = os.popen('./users.sh ' + airport_token + ' ' + 'gethistory' + ' ' + value).read()
            js = json.loads(result)
            pprint(js)
            stack = self.builder.get_object('stack')
            audit_box = self.builder.get_object('scrollBox')
            stack.set_visible_child(audit_box)
            audit_result = self.builder.get_object('scrollResult')
            output = ""
            i=1
            for key in js :
                output+=str("\n\n\tTxn ID : \n\t"+str(key['TxId']))
                output+=("\n\tVALUES: " )
                i+=1
                for k in key['Value']:
                    output+=str("\n\t\t"+str(k)+" : "+str(key['Value'][k]))
            audit_result.set_text(output)





app = GUI()
Gtk.main()
