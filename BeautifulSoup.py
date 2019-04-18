from bs4 import BeautifulSoup
import requests
import re
import csv
import os
import numbers

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   passwd="yourpassword",
#   database="mydatabase"
# )

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


url = 'https://www.paginegialle.it/ricerca/via%20liguria?'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
r  = requests.get(url)
response = requests.get(url,headers=headers)
html = response.content
soup = BeautifulSoup(response.content,'html.parser')

data = r.text



#--- QUANTI RISULTATI CI SONO DA ESTRARRE ---#
results = soup.find("span" , class_="searchResNum").text
numpagetot = results.split()[0]
risultatpag = results.split()[-1]  #-- VEDERE SE E' RISULATI O RISULTATO -- #
print(numpagetot)
print(risultatpag)


#--- CALCOLO PAGINE ---#
checknumpage = int(numpagetot) / 20
if risultatpag == "risultati" :

    if isinstance(checknumpage, float):
        print("e' un float")
        print("Il numero e' " + str(checknumpage) + " lo divido e aggiungo 1 in modo tale da renderlo un intero")
        p =(str(checknumpage).rsplit('.')[0]) and int(checknumpage)+1
        print(p)

    else:
        print("e'un intero")
        p = int(checknumpage)
        print(p)

else:

    print("una sola pag")

#pages = [str(i) for i in range(1,5)]



# numpage = 1
# while numpage < numpagetot
rows = soup.find_all("div" , class_="col contentCol")
for i in range(0,1):
    for row in rows:
        try:
            tel = row.find("span", class_="phone-label", href=False).text
            name = row.find("h1", class_="fn itemTitle", href=False).text
            addr = row.find("div", class_="street-address", href=False).text
            codpostale = row.find("span", class_="postal-code", href=False).text
            citta = row.find("span", class_="locality", href=False).text
            provincia = row.find("span", class_="region", href=False).text

            #---clean---#
            name = name.replace('\n\n\t\t','').replace('\n\t\n','').replace('\n\n','')
            addr = addr.replace('\n', '').rsplit('-\t\t\t')[0]     #sto minchia di 0 toglie il resto dei caratteri splittati da destra
            provincia = provincia.replace('(','').replace(')','')


            pref = tel.split()[0]
            pref2 = tel.split(',')[-1].rsplit()[0]

            telpref2 = tel
            tel = tel.split()
            tel = "".join(tel)
            #tel2 = tel.split(',')[-1]

            parts = tel.split(",", 1)
            if len(parts) >= 2 and parts[1]:
                tel2=tel.split(',')[-1]
                pref2 = telpref2.split(',')[-1].rsplit()[0]
            else:
                tel2 = ''
                pref2 = ''

            tel=tel.rsplit(",")[0]

            dizionario = {"TEL1": tel,
                          "PREF1": pref,
                          "TEL2": tel2,
                          "PREF2": pref2,
                          "NAME": name,
                          "ADDRESS": addr,
                          "ZIPCODE": codpostale,
                          "CITY": citta,
                          "PROV": provincia
                          }
            #print(dizionario)







        except AttributeError:
            pass



# rows = soup.find_all("div" , class_="col contentCol")
# print(type(rows))
# print(len(rows))
