from datetime import date
from tkinter import *
import time
import tkinter.messagebox
import webbrowser

import signal
import sys
from pirc522 import RFID

run = True
rdr = RFID()
util = rdr.util()
util.debug = True

root = Tk()

C = Canvas(root, bg="blue", height=1200, width=2400 )

backgroundimg = PhotoImage (file="sport.gif")
backgroundlabel = Label(C, image=backgroundimg)
C.create_window(0, 0, anchor="nw", window = backgroundlabel)     # !!!!!!!!!!!!!!!!!!!!!!!

icon = PhotoImage(file='sport2.gif')
root.tk.call('wm', 'iconphoto', root._w, icon)

C.grid()

def quit():
    sys.exit()

def tochIDEAL():
    Paypalknop.lift()
    IDEALknop.lift()
    toch_IDEAL.lower()
    BankMenu.lower()
    kiezen.lower()

def Bankkiezen():
    gekozenbank = str(Gekozen_Bank.get()).lower()
    if gekozenbank == "abn amro":
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je via ABN AMRO wilt betalen?")
        if klik == 'yes':
            url = "https://www.abnamro.nl/nl/prive/index.html"
            webbrowser.open_new(url)
            ERISBETAALD.lift()
    elif gekozenbank == 'ing':
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je via ING wilt betalen?")
        if klik == 'yes':
            url= 'https://www.ing.nl/particulier/index.html'
            webbrowser.open_new(url)
            ERISBETAALD.lift()
    elif gekozenbank == 'rabobank':
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je via Rabobank wilt betalen")
        if klik == 'yes':
            url="https://www.rabobank.nl/particulieren/"
            webbrowser.open_new(url)
            ERISBETAALD.lift()
    elif gekozenbank == 'sns':
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je via SNS wilt betalen?")
        if klik == 'yes':
            url ='https://www.snsbank.nl/particulier/home.html'
            webbrowser.open_new(url)
            ERISBETAALD.lift()
    elif gekozenbank == 'asn bank':
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je via ASN Bank wilt betalen?")
        if klik == 'yes':
            url ='https://www.asnbank.nl/home.html'
            webbrowser.open_new(url)
            ERISBETAALD.lift()
    elif gekozenbank == 'regiobank':
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je via Regiobank wilt betalen?")
        if klik == 'yes':
            url='https://www.regiobank.nl/particulier/home.html'
            webbrowser.open_new(url)
            ERISBETAALD.lift()
    elif gekozenbank == 'bunq':
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je via Bunq wilt betalen?")
        if klik == 'yes':
            url='https://www.bunq.com/nl/'
            webbrowser.open_new(url)
            ERISBETAALD.lift()
    elif gekozenbank == 'knab':
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je via Knab wilt betalen?")
        if klik == 'yes':
            url='https://www.knab.nl/'
            webbrowser.open_new(url)
            ERISBETAALD.lift()
    elif gekozenbank =='triodos bank':
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je via Triodos Bank wilt betalen?")
        if klik == 'yes':
            url='https://www.triodos.nl/nl/particulieren/'
            webbrowser.open_new(url)
            ERISBETAALD.lift()
    elif gekozenbank == 'van lanschot':
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je via Van Lanschot wilt betalen?")
        if klik == 'yes':
            url='https://www.vanlanschot.nl/'
            webbrowser.open_new(url)
            label8.lift()
            ERISBETAALD.lift()
    else:
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Er is geen bank gekozen")
        if klik == 'yes':
            print(gekozenbank)
    return gekozenbank

def bankkiezen():
    BankMenu.lift()
    kiezen.lift()
    IDEALknop.lower()
    Paypalknop.lower()
    toch_IDEAL.lift()

def paypalbetaling():
    klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je met Paypal wilt betalen?")
    if klik == 'yes':
        url = 'https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=G4TY7XUVQRJG4'
        webbrowser.open_new(url)
        IDEALknop.lower()
        Paypalknop.lower()
        toch_IDEAL.lift()
        ERISBETAALD.lift()

def stap_2():
    achternaaminput.lower()
    voornaaminput.lower()
    postcodeinput.lower()
    straatinput.lower()
    woonplaatsinput.lower()
    label1.lower()
    label2.lower()
    label3.lower()
    label4.lower()
    label5.lower()
    label7.lower()
    label8.lower()
    Emailinput.lower()
    afscheiding.lower()
    klaarknop.lower()
    Paypalknop.lift()
    IDEALknop.lift()
    label6.lift()
    print("ik doe het")

def opslaan_gegevens():
    klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat alles goed is ingevult?")
    if klik == 'yes':
        De_naam = str(gegeven_naam.get()).lower()
        De_Achternaam =  str(gegeven_naam2.get()).lower()
        Adres1 = str(gegeven_straat.get()).lower()
        Adres2 = str(gegeven_poscode.get()).lower()
        Adres3 = str(gegeven_woonplaats.get()).lower()

        stap_2()
    else:
        print("TRY AGAIN U N00B")

def betaald():
    gekozenbank = str(Gekozen_Bank.get()).lower()
    if gekozenbank == '--------':
        gekozenbank = ' Paypal'
    else:
        print(gekozenbank)
    De_naam = str(gegeven_naam.get()).lower()
    De_Achternaam = str(gegeven_naam2.get()).lower()
    Adres1 = str(gegeven_straat.get()).lower()
    Adres2 = str(gegeven_poscode.get()).lower()
    Adres3 = str(gegeven_woonplaats.get()).lower()
    Paypalknop.lower()
    IDEALknop.lower()
    BankMenu.lower()
    kiezen.lower()
    ERISBETAALD.lower()
    toch_IDEAL.lower()
    label6.lower()
    label8.lift()
    time.sleep(1)
    while True:
        print ("Je mag nu scannen")
        rdr.wait_for_tag()
        (error, data) = rdr.request()
        (error, uid) = rdr.anticoll()
        if not error:
            # print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
            uniqueID = ""
            for i in range(len(uid)-1):
                uniqueID += str(uid[i])
            print ("This is the ID:", int(uniqueID))
            util.set_tag(uid)
        if len(uniqueID) > 9:
            label8.lower()
            rdr.cleanup()
            break
    bestand = open("registratie.txt", "a")
    bestand.write("\n")
    bestand.write("Volledige Naam: ")
    bestand.write(str(De_naam))
    bestand.write(" ")
    bestand.write(str(De_Achternaam))
    bestand.write("\n")
    bestand.write("Adres: ")
    bestand.write(str(Adres1))
    bestand.write("\n")
    bestand.write(str(Adres2))
    bestand.write(" ")
    bestand.write(str(Adres3))
    bestand.write("\n")
    bestand.write('Datum aanmelding: ')
    bestand.write(datum)
    bestand.write("\n")
    bestand.write("betaald via:")
    bestand.write(gekozenbank)
    bestand.write('\n')
    bestand.write("Pas ID:")
    bestand.write(str(uniqueID))
    bestand.close()
    YAY.lift()
    Afsluiten.lift()

gegeven_naam = StringVar()
gegeven_naam2 = StringVar()
gegeven_poscode = StringVar()
gegeven_straat = StringVar()
gegeven_woonplaats = StringVar()
datum = StringVar()
gegeven_Email = StringVar()

Bank_list = ["--------", "ABN AMRO", "ING", "Rabobank", "SNS", "ASN Bank", "RegioBank", "Bunq", "Knab", "Triodos Bank", "Van Lanschot"]
Gekozen_Bank = StringVar()
Gekozen_Bank.set(Bank_list[0])

BankMenu = OptionMenu(root, Gekozen_Bank, *Bank_list)
BankMenu.config(font=(44))




klaarknop= Button(C, text = "klaar", command = opslaan_gegevens)
klaarknop.config(font=(44))
afscheiding = Label(C, text ="----------------------------------------------persoonlijke informatie----------------------------------------", bg = "blue", fg = "white")
afscheiding.config(font=(44))
label1 = Label(C, text ="Voornaam",bg = "blue", fg ="white" )
label1.config(font=(44))
label2 = Label(C, text = "Achternaam", bg ="blue", fg = "white")
label2.config(font=(44))
label3 = Label(C, text = "Postcode", bg = "blue" , fg = "white")
label3.config(font=(44))
label4 = Label(C, text = "Straatnaam + huisnummer", bg= "blue", fg = "white")
label4.config(font=(44))
label5 = Label(C, text = "Woonplaats", bg= "blue", fg = "white")
label5.config(font=(44))
label6 = Label(C, text = "met welke betaalmethode wilt u betalen?", bg="blue", fg= "white")
label6.config(font=(44))
label7 = Label(C,text= "E-mail", bg='blue', fg='white')
label7.config(font=(44))
label8 = Label(C,text= "Scan uw pasje nu.", bg='blue', fg='white')
label8.config(font=(44))
Paypalknop = Button(C,text = "Ik wil betalen via PayPal", command = paypalbetaling )
Paypalknop.config(font=(44))
IDEALknop = Button(C, text = "Ik wil betalen via IDEAL", command = bankkiezen)
IDEALknop.config(font=(44))
kiezen = Button(C, text = 'Deze Bank kiezen', command= Bankkiezen)
kiezen.config(font=(44))
toch_IDEAL = Button(C, text= 'Andere betalingsmethode kiezen', command = tochIDEAL)
toch_IDEAL.config(font=(44))
ERISBETAALD = Button(C, text= ".", command = betaald)
ERISBETAALD.config(font=(44))
YAY = Label(C,text= 'REGISTRATIE VOLTOOID', fg='red')
YAY.config(font=(44))
Afsluiten = Button(C, text = 'afsluiten', command = quit)
Afsluiten.config(font=(44))

voornaaminput = Entry(C, textvariable= gegeven_naam)
voornaaminput.config(font=(44))
achternaaminput = Entry(C, textvariable= gegeven_naam2)
achternaaminput.config(font=(44))
postcodeinput = Entry(C, textvariable= gegeven_poscode)
postcodeinput.config(font=(44))
straatinput = Entry(C, textvariable= gegeven_straat)
straatinput.config(font=(44))
woonplaatsinput = Entry(C, textvariable= gegeven_woonplaats)
woonplaatsinput.config(font=(44))
Emailinput = Entry(C,textvariable = gegeven_Email)
Emailinput.config(font=(44))

C.create_window(700, 40, anchor="n", window = afscheiding)

C.create_window(500, 200, anchor="w", window = voornaaminput)
C.create_window(500, 220, anchor="w", window = achternaaminput)
C.create_window(500, 240, anchor="w", window = postcodeinput)
C.create_window(500, 260, anchor="w", window = straatinput)
C.create_window(500, 280, anchor="w", window = woonplaatsinput)
C.create_window(500, 300, anchor='w', window = Emailinput)

C.create_window(367,200 , anchor= "w", window= label1)
C.create_window(350,220, anchor= "w", window= label2)
C.create_window(370,240, anchor= "w", window= label3)
C.create_window(223,260,anchor= "w", window= label4)
C.create_window(350,280,anchor= "w", window= label5)
C.create_window(395,300, anchor= 'w', window=label7)
C.create_window(395,310, anchor= 'w', window=label8)
C.create_window(550, 320, anchor= "n", window= klaarknop)
C.create_window(400,320,anchor='w', window= label6)
C.create_window(400,230, anchor= 'w', window= Paypalknop)
C.create_window(400,250, anchor= 'w', window= IDEALknop)
C.create_window(400,200, anchor= 'w', window= kiezen)
C.create_window(400, 320, anchor="w", window=BankMenu)
C.create_window(400,340, anchor="w", window= toch_IDEAL)
C.create_window(0,0, anchor="w", window= ERISBETAALD)
C.create_window(400,360, anchor="w", window= YAY)
C.create_window(500,340, anchor= "w", window=Afsluiten)
datum = str(date.today())
print(datum)


Paypalknop.lower()
IDEALknop.lower()
label6.lower()
label8.lower()
BankMenu.lower()
kiezen.lower()
toch_IDEAL.lower()
ERISBETAALD.lower()
YAY.lower()
Afsluiten.lower()

root.minsize(width=720, height=480)


# root.attributes('-fullscreen', True)


root.mainloop()
