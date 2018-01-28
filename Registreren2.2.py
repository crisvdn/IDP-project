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
C.create_window(0, 0, anchor="nw", window = backgroundlabel)

C.grid()

def terug_1():
    Stappie3.lower()
    label9.lower()
    label10.lower()
    label11.lower()
    label12.lower()
    LengteInput.lower()
    GewichtInput.lower()
    GeslachtMenu.lower()
    achternaaminput.lift()
    voornaaminput.lift()
    postcodeinput.lift()
    straatinput.lift()
    woonplaatsinput.lift()
    label1.lift()
    label2.lift()
    label3.lift()
    label4.lift()
    label5.lift()
    label7.lift()
    Emailinput.lift()
    afscheiding.lift()
    klaarknop.lift()
    TerugNaar1.lower()

def terug_2():
    Paypalknop.lower()
    IDEALknop.lower()
    label6.lower()
    label9.lift()
    label10.lift()
    label11.lift()
    label12.lift()
    LengteInput.lift()
    GewichtInput.lift()
    GeslachtMenu.lift()
    Stappie3.lift()
    TerugNaar2.lower()
    TerugNaar1.lift()

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
            TerugNaar2.lower()
    elif gekozenbank == 'ing':
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je via ING wilt betalen?")
        if klik == 'yes':
            url= 'https://www.ing.nl/particulier/index.html'
            webbrowser.open_new(url)
            ERISBETAALD.lift()
            TerugNaar2.lower()
    elif gekozenbank == 'rabobank':
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je via Rabobank wilt betalen")
        if klik == 'yes':
            url="https://www.rabobank.nl/particulieren/"
            webbrowser.open_new(url)
            ERISBETAALD.lift()
            TerugNaar2.lower()
    elif gekozenbank == 'sns':
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je via SNS wilt betalen?")
        if klik == 'yes':
            url ='https://www.snsbank.nl/particulier/home.html'
            webbrowser.open_new(url)
            ERISBETAALD.lift()
            TerugNaar2.lower()
    elif gekozenbank == 'asn bank':
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je via ASN Bank wilt betalen?")
        if klik == 'yes':
            url ='https://www.asnbank.nl/home.html'
            webbrowser.open_new(url)
            ERISBETAALD.lift()
            TerugNaar2.lower()
    elif gekozenbank == 'regiobank':
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je via Regiobank wilt betalen?")
        if klik == 'yes':
            url='https://www.regiobank.nl/particulier/home.html'
            webbrowser.open_new(url)
            ERISBETAALD.lift()
            TerugNaar2.lower()
    elif gekozenbank == 'bunq':
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je via Bunq wilt betalen?")
        if klik == 'yes':
            url='https://www.bunq.com/nl/'
            webbrowser.open_new(url)
            ERISBETAALD.lift()
            TerugNaar2.lower()
    elif gekozenbank == 'knab':
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je via Knab wilt betalen?")
        if klik == 'yes':
            url='https://www.knab.nl/'
            webbrowser.open_new(url)
            ERISBETAALD.lift()
            TerugNaar2.lower()
    elif gekozenbank =='triodos bank':
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je via Triodos Bank wilt betalen?")
        if klik == 'yes':
            url='https://www.triodos.nl/nl/particulieren/'
            webbrowser.open_new(url)
            ERISBETAALD.lift()
            TerugNaar2.lower()
    elif gekozenbank == 'van lanschot':
        klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je via Van Lanschot wilt betalen?")
        if klik == 'yes':
            url='https://www.vanlanschot.nl/'
            webbrowser.open_new(url)
            label8.lift()
            ERISBETAALD.lift()
            TerugNaar2.lower()
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
        TerugNaar2.lower()

def stap_3():
    klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat alles goed is ingevult?")
    if klik == 'yes':
        Paypalknop.lift()
        IDEALknop.lift()
        label6.lift()
        label9.lower()
        label10.lower()
        label11.lower()
        label12.lower()
        LengteInput.lower()
        GewichtInput.lower()
        GeslachtMenu.lower()
        Stappie3.lower()
        TerugNaar2.lift()
        TerugNaar1.lower()
        print("ik doe het")

def stap_2():
    Stappie3.lift()
    label9.lift()
    label10.lift()
    label11.lift()
    label12.lift()
    LengteInput.lift()
    GewichtInput.lift()
    GeslachtMenu.lift()
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
    Emailinput.lower()
    afscheiding.lower()
    klaarknop.lower()
    TerugNaar1.lift()

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
gegeven_lengte = StringVar()
gegeven_gewicht = StringVar()

Bank_list = ["--------", "ABN AMRO", "ING", "Rabobank", "SNS", "ASN Bank", "RegioBank", "Bunq", "Knab", "Triodos Bank", "Van Lanschot"]
Gekozen_Bank = StringVar()
Gekozen_Bank.set(Bank_list[0])

BankMenu = OptionMenu(root, Gekozen_Bank, *Bank_list)
BankMenu.config(font=(44))

Geslacht = ["--------", "Man", "Vrouw"]
Gekozen_Geslacht = StringVar()
Gekozen_Geslacht.set(Geslacht[0])

GeslachtMenu = OptionMenu(root, Gekozen_Geslacht, *Geslacht)
GeslachtMenu.config(font=(44))

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
label9 = Label(C, text = 'Hoeveel weegt u? (KG)',bg="blue", fg='white')
label9.config(font=(44))
label10  = Label(C, text = "Wat is uw lengte? (m)",bg="blue", fg='white')
label10.config(font=(44))
label11  = Label(C, text = "----------------------------------------------Overige informatie----------------------------------------",bg="blue", fg='white')
label11.config(font=(44))
label12 = Label(C, text= "Wat is uw geslacht?",bg="blue", fg='white')
label12.config(font=(44))
YAY = Label(C,text= 'REGISTRATIE VOLTOOID', fg='red')
YAY.config(font=(44))

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
Afsluiten = Button(C, text = 'afsluiten', command = quit)
Afsluiten.config(font=(44))
klaarknop= Button(C, text = "klaar", command = opslaan_gegevens)
klaarknop.config(font=(44))
Stappie3 = Button(C,text = "Klaar", command = stap_3)
Stappie3.config(font=(44))
TerugNaar1 = Button(C,text = "Stap Terug", command = terug_1)
TerugNaar1.config(font=(44))
TerugNaar2 = Button(C,text = "Stap Terug", command = terug_2)
TerugNaar2.config(font=(44))

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
GewichtInput = Entry(C,textvariable = gegeven_gewicht)
GewichtInput.config(font=(44))
LengteInput = Entry(C, textvariable = gegeven_lengte)
LengteInput.config(font=(44))

C.create_window(700, 40, anchor="n", window = afscheiding)
C.create_window(500, 200, anchor="w", window = voornaaminput)
C.create_window(500, 220, anchor="w", window = achternaaminput)
C.create_window(500, 240, anchor="w", window = postcodeinput)
C.create_window(500, 260, anchor="w", window = straatinput)
C.create_window(500, 280, anchor="w", window = woonplaatsinput)
C.create_window(500, 300, anchor='w', window = Emailinput)
C.create_window(750, 350, anchor="w", window = GewichtInput)
C.create_window(750, 400, anchor="w", window = LengteInput)
C.create_window(367,200 , anchor= "w", window= label1)
C.create_window(350,220, anchor= "w", window= label2)
C.create_window(370,240, anchor= "w", window= label3)
C.create_window(223,260,anchor= "w", window= label4)
C.create_window(350,280,anchor= "w", window= label5)
C.create_window(395,300, anchor= 'w', window=label7)
C.create_window(395,310, anchor= 'w', window=label8)
C.create_window(750, 650, anchor="n" , window=Stappie3)
C.create_window(490,350,anchor= 'w',window=label9)
C.create_window(500,400,anchor='w', window=label10)
C.create_window(700,250,anchor='n', window=label11)
C.create_window(518,500,anchor="w", window=label12)
C.create_window(750, 500, anchor="w", window=GeslachtMenu)
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
C.create_window(300,650,anchor="n",window=TerugNaar1)
C.create_window(300,650,anchor="n",window=TerugNaar2)

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
label9.lower()
label10.lower()
label11.lower()
label12.lower()
GeslachtMenu.lower()
GewichtInput.lower()
LengteInput.lower()
Stappie3.lower()
TerugNaar1.lower()
TerugNaar2.lower()

root.minsize(width=720, height=480)


root.attributes('-fullscreen', True)


root.mainloop()
