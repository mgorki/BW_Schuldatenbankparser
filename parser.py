### Schulenfinder BW - Version 0.7 ### 

import urllib.request
import urllib.parse
import re
import requests
import json
import csv
import schulen_gui as Fenster
import orte

version = "0.7"

Suchparameter = Fenster.ChooseSearchtype(version)
print(Suchparameter)

Suchtyp = Suchparameter['Search_Type']
Schultyp = list(Suchparameter["Types_of_School"])
Suchwort = Suchparameter['Search_Word']
if Suchtyp == 'QUICKSEARCH':
    Ort = ''
    Umkreis = ''
else:
    Ort = str(Suchparameter['Location'])
    print(str(Suchparameter['Location']))
    Ort = str(orte.dscOrt_dict[Ort])
    Umkreis = Suchparameter['Distance']


print(Schultyp)
print(Suchwort)
print(Ort)
print(Umkreis)


#Schultyp = list(input_Schultyp.split(','))

Typindex = (len(Schultyp) - 1)

Speicherpfad = Fenster.Ausgabepfad()
f = open(str(Speicherpfad), 'x')
f.write


#print(len(Schultyp))  #For testing

EXCLUDED = [] # ["04131325", "04130114", "04105016", "04101746", "04118291", "04130242", "04165700", "04100468", "04130229", "04105004", "04100432", "04118369", "04101795", "04104991", "04129884", "04105570", "04118308", "04101771", "04101734", "04101783", "04104978", "04104966", "04129902", "04104954", "04104930", "04100444", "04104942", "04104929", "04118321", "04130047", "04104917", "04130096", "04118345", "04129951", "04118448", "04118333", "04100456", "04129963", "04104486", "04104498", "04104590", "04104759", "04104723", "04104747", "04104504", "04104681", "04104607", "04166455", "04104711", "04104516", "04104619", "04163636", "04104528", "04104656", "04104541", "04104553", "04104644", "04104668", "04104565", "04104735", "04104577", "04104620", "04104693", "04104589", "04161950", "04112501", "04112458", "04112495", "04112422", "04112471", "04163636", "04112483", "04112355", "04112434", "04112409", "04112410", "04112367", "04112446", "04112525", "04112379", "04112380", "04112392"]


url_1 = "https://lobw.kultus-bw.de/didsuche/DienststellenSucheWebService.asmx/SearchDienststellen" 
url_2 = "https://lobw.kultus-bw.de/didsuche/DienststellenSucheWebService.asmx/GetDienststelle"

while Typindex >= 0:

    request_data1 = {'json':'{"command":"%s","data":{"dscSearch":"%s","dscPlz":"","dscOrt":"","dscDienststellenname":"","dscSchulartenSelected":"%s","dscSchulstatusSelected":"0","dscSchulaufsichtSelected":"","dscOrtSelected":"%s","dscEntfernung":"%s","dscAusbildungsSchulenSelected":"","dscAusbildungsSchulenSelectedSart":"","dscPageNumber":"1","dscPageSize":"1213","dscUnique":"1598552788927"}}'%(Suchtyp, Suchwort, Schultyp[Typindex], Ort, Umkreis)}

    response_1 = requests.post(url_1, json=request_data1)

    resp1_data = response_1.json()['d']
    resp1_data = str(resp1_data)
    resp1_data = json.loads(resp1_data)
    resp1_data = resp1_data['Rows']

    #print(resp1_data)
    #print(type(resp1_data))

    ## converting list resp1_data to enumerated dict ##
    def enum_dict(lst):
        result = dict(enumerate(lst))
        return result
            
    resp1_dict = (enum_dict(resp1_data))

    disch_lst = []

    with f:
        fnames = ['Name', 'EMail', 'Telefon', 'Ort', 'DISCH']
        writer = csv.DictWriter(f, fieldnames=fnames) 
        writer.writeheader()
        writer.writerow({'Name' : "*************", 'Ort': "*************", 'Telefon': "*************", 'EMail': "*************", 'DISCH': "*************"})
        if not Schultyp == []:
            writer.writerow({'Name' : Schultyp[Typindex], 'Ort': Schultyp[Typindex], 'Telefon': Schultyp[Typindex], 'EMail': Schultyp[Typindex]})
        writer.writerow({'Name' : "*************", 'Ort': "*************", 'Telefon': "*************", 'EMail': "*************", 'DISCH': "*************"})


        for key in resp1_dict:

            disch_nr = resp1_dict[key]['DISCH']
            
            #print(disch_nr)  # For testing 
            disch_nr = disch_nr.strip("'")
            #print(disch_nr)  # For testing 
            request_data2 = {'disch':str(disch_nr)}
            #print(request_data2)  # For testing 

            response_2 = requests.post(url_2, json=request_data2)
            #print(response_2)  #For testing

            resp_data = (response_2.json()['d'])
            resp_data = json.loads(resp_data)
            #print(resp_data)  #For testing
            
            print("*************")
            try:
                S_Name = resp_data['NAME']
                print("Name: " + S_Name)
            except:
                S_Name = "---"
                print("Name: " + S_Name)
            try:
                S_Mail = resp_data['VERWEMAIL']
                print("Mail: " + S_Mail)
            except:
                S_Mail = "---"
                print("Mail: " + S_Mail)
            try:
                S_Tel = resp_data['TELGANZ']
                print("Telefon: " + S_Tel)
            except:
                S_Tel = "---"
                print("Telefon: " + S_Tel)
            try:
                S_Ort = resp_data['DIORT']
                print("Ort: " + S_Ort)
            except:
                S_Ort = "---"
                S_Ort = resp_data['DIORT']
            try:
                print("DISCH: " + disch_nr)
            except:
                print("Fatal error: no DISCH!")

            if not disch_nr in EXCLUDED:
                writer.writerow({'Name' : S_Name, 'EMail': S_Mail, 'Telefon': S_Tel, 'Ort': S_Ort, 'DISCH': disch_nr})
    
    f = open(str(Speicherpfad), 'a')
    f.write
    Typindex = Typindex - 1

f.close
print("""

*******************************************************
***** Suche abgeschlossen & CSV Datei gespeichert *****
**************  Schulenfinder BW beenden **************
*******************************************************

""")            

Fenster.End(Speicherpfad)
exit