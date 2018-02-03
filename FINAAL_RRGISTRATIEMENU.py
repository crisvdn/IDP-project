from datetime import date
from tkinter import *
import time
import tkinter.messagebox
from tkinter.messagebox import *
import webbrowser
import signal
import sys
from pirc522 import *
import RPi.GPIO as GPIO
import psycopg2
import os
import subprocess, sys



GPIO.setwarnings(False)
conn = psycopg2.connect('host=192.168.42.1 user=hysen password=2140321maya dbname=sportschool')
cur = conn.cursor()

run = True
rdr = RFID()
util = rdr.util()
util.debug = True


root = Tk()
C = Canvas(root, bg="blue", height=2400, width=1200 )


backgroundimg = PhotoImage(file = 'sporter.gif')
backgroundlabel = Label(C, image = backgroundimg)
C.create_window(0, 0, anchor="nw", window = backgroundlabel)

C.grid()

def end_read(signal,frame):
    global run
    print("\nCtrl+C captured, ending read.")
    run = False
    rdr.cleanup()
    sys.exit()

def add_klant(klant_id, voornaam, achternaam, geslacht, geboortedatum, emailadres, telefoonnr, datuminschrijving):
    query = """
    INSERT INTO
        klant
    VALUES
        (%s, %s, %s,%s, %s, %s,%s, %s, %s, (SELECT MAX(adres_id) FROM adres),(SELECT MAX(id) FROM sportgegevens))
    """
    values = (klant_id, voornaam, achternaam, geslacht, geboortedatum, emailadres, telefoonnr, datuminschrijving, 1)
    cur.execute(query, values)
    conn.commit()


def add_adres(postcode, straat_huisnr, woonplaats):
    query = """
    INSERT INTO
        adres(postcode, straat_huisnr, woonplaats)
    VALUES
        (%s, %s, %s)
    """
    values = (postcode, straat_huisnr, woonplaats)
    cur.execute(query, values)
    conn.commit()

def add_sportgegevens(lengte, gewicht):
    query = """
    INSERT INTO
        sportgegevens(lengte, gewicht)
    VALUES
        (%s, %s)
    """
    values = (lengte, gewicht)
    cur.execute(query, values)
    conn.commit()


def get_all_persons():
    query = """
    SELECT
        *
    FROM
        persoon
    """
    cur.execute(query)
    return cur.fetchall()


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
    geboortedatuminput.lift()
    postcodeinput.lift()
    straatinput.lift()
    woonplaatsinput.lift()
    telefoonnummerinput.lift()
    label1.lift()
    label2.lift()
    label13.lift()
    label3.lift()
    label4.lift()
    label5.lift()
    label7.lift()
    label14.lift()
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
    label16.lower()
    BedrijfsInput.lower()
    Bedrijfscheck.lower()

def quit():
	opener ="open" if sys.platform == "darwin" else "xdg-open"
	subprocess.call([opener, 'menu.py'])
	sys.exit()

def klaar():
    label8.lower()
    YAY.lift()
    Afsluiten.lift()


def tochIDEAL():
    Paypalknop.lift()
    IDEALknop.lift()
    toch_IDEAL.lower()
    BankMenu.lower()
    kiezen.lower()
    TerugNaar2.lift()

def tochIDEAL2():
	Paypalknopbedrijf.lift()
	IDEALknop.lift()
	tochIDEAL2.lower()
	BankMenu.lower()
	kiezen.lower()
	TerugNaar2.lift()

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
    TerugNaar2.lower()

def paypalbetalingstandaard():
    klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat je met Paypal wilt betalen?")
    if klik == 'yes':
    	Abbonementen = str(Gekozen_Abbonement.get()).lower()
    	if Abbonementen == 'standaardabbonement':
    		url = 'https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=FT5EANXWLCQWJ'
    	elif Abbonementen == 'bedrijfsabbonement':
    		url = 'https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=6C27PPWM7B2C6'
    	else:
    		showerror('Error', 'Uw heeft geen abbonement gekozen')
    	webbrowser.open_new(url)
    	IDEALknop.lower()
    	Paypalknop.lower()
    	toch_IDEAL.lift()
    	ERISBETAALD.lift()
    	TerugNaar2.lower()


def bedrijfInvoeren():
	label16.lift()
	BedrijfsInput.lift()
	Bedrijfscheck.lift()


def bedrijfChecken():
	bedrijfs = str(gegeven_bedrijf.get()).lower()
	if bedrijfs in Samenwerkingsbedrijven:
		betalen()
	else:
		showerror('error', 'Het bedrijf wat u heeft ingevult heeft geen recht op een bedrijfsabbonement')

def betalen():
	IDEALknop.lift()
	Paypalknop.lift()
	label6.lift()
	label16.lower()
	BedrijfsInput.lower()
	Bedrijfscheck.lower()

def stap_4():
	Abbonementen = str(Gekozen_Abbonement.get()).lower()
	if Abbonementen == 'standaardabbonement':
		AbbonementMenu.lower()
		label15.lower()
		Abbonementgekozen.lower()
		betalen()
	elif Abbonementen == 'bedrijfsabbonement':
		AbbonementMenu.lower()
		label15.lower()
		Abbonementgekozen.lower()
		bedrijfInvoeren()
	else:
		showerror('Error', 'er is geen abbonement gekozen.')


def stap_3():
    klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat alles goed is ingevult?")
    if klik == 'yes':
        AbbonementMenu.lift()
        label15.lift()
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
        Abbonementgekozen.lift()

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
    geboortedatuminput.lower()
    postcodeinput.lower()
    straatinput.lower()
    woonplaatsinput.lower()
    telefoonnummerinput.lower()
    label1.lower()
    label2.lower()
    label13.lower()
    label3.lower()
    label4.lower()
    label5.lower()
    label7.lower()
    label14.lower()
    Emailinput.lower()
    afscheiding.lower()
    klaarknop.lower()
    TerugNaar1.lift()

def opslaan_gegevens():
	klik = tkinter.messagebox.askquestion("Waarschuwing", "Weet je zeker dat alles goed is ingevult?")
	if klik == 'yes': 
		stap_2()
	else:
		os.startfile('sport.gif')
#        	showerror('Error', 'Er staat een fout in de voornaam')
#        else:
#        	De_Achternaam =  str(gegeven_naam2.get()).lower()
#        	if ',' or '' in De_Achternaam:
#        		showerror('Error', 'Er staat een fout in de achternaam')
#        	else:
#        		Adres1 = str(gegeven_straat.get()).lower()
#        		if ',' or '' in Adres1:
#        			showerror('Error', 'Er staat een fout in de straat')
#        		else:
#        			Adres2 = str(gegeven_poscode.get()).lower()
#        			if '' or ',' in Adres2:
#        				showerror('Error', 'Er staat een fout in de Postcode')
#        			else:
#        				Adres3 = str(gegeven_woonplaats.get()).lower()
#        				if '' or ',' in Adres3:
#       					showerror('Error', 'Er staat een fout in de Woonplaats')
#        				else:
#        					De_geboortedatum = str(gegeven_geboortedatum.get()).lower()
#        					if ',' or '' in De_geboortedatum:
#        						showerror('Error', 'Er staat een fout in de Postcode')
#        					else:
#        						De_telfoon = str(gegeven_telefoonnummer.get()).lower()
#        						if ',' or '' in De_telfoon:
#       								showerror('Error', 'Er staat een fout in het telefoonnummer')
#        						else:
#        							stap_2()
def scannenPAS():
	De_naam = str(gegeven_naam.get()).lower()
	De_Achternaam = str(gegeven_naam2.get()).lower()
	De_geboortedatum = str(gegeven_geboortedatum.get()).lower()
	De_telfoon = str(gegeven_telefoonnummer.get()).lower()
	Adres1 = str(gegeven_straat.get()).lower()
	Adres2 = str(gegeven_poscode.get()).lower()
	Adres3 = str(gegeven_woonplaats.get()).lower()
	Gewicht = str(gegeven_gewicht.get()).lower()
	Man_Vrouw = str(Gekozen_Geslacht.get()).lower()
	Het_email = str(gegeven_Email.get()).lower()
	Datum_inschrijving = str(date.today())
	De_lengte = str(gegeven_lengte.get()).lower()
	while run:
		rdr.wait_for_tag()
		(error, data) = rdr.request()
		(error, uid) = rdr.anticoll()
		if not error:
			Unique_id = ''
			for i in uid:
				Unique_id += str(i)
			break
	add_sportgegevens(De_lengte , Gewicht)
	add_adres(Adres2 ,Adres1, Adres3)
	add_klant(Unique_id, De_naam, De_Achternaam , Man_Vrouw, De_geboortedatum, Het_email, De_telfoon, Datum_inschrijving)
	cur.close()
	conn.close()
	klaar()
    

def betaald():
    gekozenbank = str(Gekozen_Bank.get()).lower()
    if gekozenbank == '--------':
        gekozenbank = ' Paypal'
    else:
        print(gekozenbank)

    # variablen voor de database
    Paypalknop.lower()
    label8.lift()
    IDEALknop.lower()
    BankMenu.lower()
    kiezen.lower()
    ERISBETAALD.lower()
    toch_IDEAL.lower()
    label6.lower()
    print("scan uw pasje >> Database")
    scannenPAS()


gegeven_naam = StringVar()
gegeven_naam2 = StringVar()
gegeven_poscode = StringVar()
gegeven_geboortedatum = StringVar()
gegeven_telefoonnummer = StringVar()
gegeven_straat = StringVar()
gegeven_woonplaats = StringVar()
datum = StringVar()
gegeven_Email = StringVar()
gegeven_lengte = StringVar()
gegeven_gewicht = StringVar()
gegeven_bedrijf = StringVar()

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

Abbonement = ['-------','Bedrijfsabbonement', 'Standaardabbonement']
Gekozen_Abbonement = StringVar()
Gekozen_Abbonement.set(Abbonement[0])

AbbonementMenu = OptionMenu(root,Gekozen_Abbonement, *Abbonement)
AbbonementMenu.config(font=(44))




#De eerste scherm
afscheiding = Label(C, text ="---------------------Persoonlijke Informatie------------------------", bg = "blue", fg = "white")
afscheiding.config(font=(44))

label1 = Label(C, text ="Voornaam",bg = "blue", fg ="white" )
label1.config(font=(44))

label2 = Label(C, text = "Achternaam", bg ="blue", fg = "white")
label2.config(font=(44))

label13 = Label(C, text= "Geboortedatum (dd-mm-yyyy)",bg="blue", fg='white')
label13.config(font=(44))

label3 = Label(C, text = "Postcode (0000AA)", bg = "blue" , fg = "white")
label3.config(font=(44))

label4 = Label(C, text = "Straatnaam + Huisnummer", bg= "blue", fg = "white")
label4.config(font=(44))

label5 = Label(C, text = "Woonplaats", bg= "blue", fg = "white")
label5.config(font=(44))

label7 = Label(C,text= "E-mail (@gmail.com)", bg='blue', fg='white')
label7.config(font=(44))

label14 = Label(C, text= "Telefoonnummer (06-12345678",bg="blue", fg='white')
label14.config(font=(44))

label6 = Label(C, text = "Met welke betaalmethode wilt u betalen?", bg="blue", fg= "white")
label6.config(font=(44))

#De tweede scherm
label11  = Label(C, text = "----------------------Overige Informatie------------------------",bg="blue", fg='white')
label11.config(font=(44))

label12 = Label(C, text= "Wat is uw geslacht?",bg="blue", fg='white')
label12.config(font=(44))

label9 = Label(C, text = 'Hoeveel weegt u? (KG)',bg="blue", fg='white')
label9.config(font=(44))

label10  = Label(C, text = "Wat is uw lengte? (m)",bg="blue", fg='white')
label10.config(font=(44))

label15 = Label(C,text = 'Wat voor Abbonement wilt u?',bg = 'blue', fg = 'white')
label15.config(font=(44))

label16 = Label(C,text = 'Voor welk bedrijf werkt u?', bg= 'blue', fg = 'white')
label16.config(font=(44))

#scan pasje
label8 = Label(C,text= "Scan uw pasje nu.", bg='blue', fg='white')
label8.config(font=(44))






# klaar scherm
YAY = Label(C,text= 'REGISTRATIE VOLTOOID', fg='red')
YAY.config(font=(44))

Paypalknop = Button(C,text = "Ik wil betalen via PayPal", command = paypalbetalingstandaard )
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
Abbonementgekozen = Button(C,text = 'Dit abbonement kiezen', command = stap_4)
Abbonementgekozen.config(font=44)
Bedrijfscheck = Button(C, text = 'Dit bedrijf kiezen', command = bedrijfChecken)
Bedrijfscheck.config(font=44)


voornaaminput = Entry(C, textvariable= gegeven_naam)
voornaaminput.config(font=(44))

achternaaminput = Entry(C, textvariable= gegeven_naam2)
achternaaminput.config(font=(44))

geboortedatuminput = Entry(C, textvariable= gegeven_geboortedatum)
geboortedatuminput.config(font=(44))

telefoonnummerinput = Entry(C, textvariable= gegeven_telefoonnummer)
telefoonnummerinput.config(font=(44))

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

BedrijfsInput = Entry(C, textvariable = gegeven_bedrijf)
BedrijfsInput.config(font=44)
Samenwerkingsbedrijven = ['hogeschool utrecht', 'universiteit utrecht']

#De eerste scherm
C.create_window(500, 40, anchor="n", window = afscheiding)
C.create_window(500, 100, anchor="w", window = voornaaminput)
C.create_window(363,100, anchor= "w", window= label1)
C.create_window(500, 130, anchor="w", window = achternaaminput)
C.create_window(350,130, anchor= "w", window= label2)
C.create_window(500, 160, anchor="w", window = geboortedatuminput)
C.create_window(208,160, anchor= 'w', window=label13)
C.create_window(500, 210, anchor="w", window = postcodeinput)
C.create_window(293,210, anchor= "w", window= label3)
C.create_window(500, 240, anchor="w", window = straatinput)
C.create_window(230,240,anchor= "w", window= label4)
C.create_window(500, 270, anchor="w", window = woonplaatsinput)
C.create_window(350,270,anchor= "w", window= label5)
C.create_window(500, 320, anchor='w', window = Emailinput)
C.create_window(286,320, anchor= 'w', window=label7)
C.create_window(500, 350, anchor="w", window = telefoonnummerinput)
C.create_window(194,350, anchor= 'w', window=label14)
C.create_window(465, 400, anchor= "n", window= klaarknop)

# het tweede scherm
C.create_window(500,40,anchor='n', window=label11)
C.create_window(500, 160, anchor="w", window=GeslachtMenu)
C.create_window(300,160,anchor="w", window=label12)
C.create_window(500, 200, anchor="w", window = GewichtInput)
C.create_window(300,200,anchor= 'w',window=label9)
C.create_window(500, 240, anchor="w", window = LengteInput)
C.create_window(300,240,anchor='w', window=label10)
C.create_window(550, 480, anchor="n" , window=Stappie3)
C.create_window(300,350,anchor="n",window=TerugNaar1)


# het derde scherm
C.create_window(400,150,anchor='w',window = label15)
C.create_window(400,230, anchor='w', window= AbbonementMenu)
C.create_window(400,300,anchor = 'w', window= Abbonementgekozen)

# het vierde scherm
C.create_window(400,160,anchor='w', window= label6)
C.create_window(400,230, anchor= 'w', window= Paypalknop)
C.create_window(400,280, anchor= 'w', window= IDEALknop)
C.create_window(300,450,anchor="n",window=TerugNaar2)
C.create_window(400,280,anchor='w', window = label16)
C.create_window(400,310,anchor= 'w', window = BedrijfsInput)
C.create_window(400,340,anchor='w', window= Bedrijfscheck)

# IDEAL scherm
C.create_window(400, 200, anchor="w", window=BankMenu)
C.create_window(400,300, anchor= 'w', window= kiezen)
C.create_window(400,340, anchor="w", window= toch_IDEAL)


# Geheim betaal knoop
C.create_window(0,0, anchor="w", window= ERISBETAALD)

#scan uw pasje
C.create_window(395,310, anchor= 'w', window=label8)

# De proses is gelukt (gegevens naar de database)
C.create_window(400,340, anchor="w", window= YAY)
C.create_window(500,380, anchor= "w", window=Afsluiten)



datum = str(date.today())
print(datum)


label15.lower()
Paypalknop.lower()
AbbonementMenu.lower()
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
Abbonementgekozen.lower()
label16.lower()
BedrijfsInput.lower()
Bedrijfscheck.lower()

root.minsize(width=960, height=544)

root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen', True)

width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width, height))


root.mainloop()
