import requests
import re
import datetime
import time
from email import utils
from bs4 import BeautifulSoup
from datetime import datetime
lista_linkow = ["https://dutchcharts.nl/showitem.asp?interpret=Al+Martino&titel=The+Voice+To+Your+Heart&cat=a",
"https://dutchcharts.nl/showitem.asp?interpret=Semino+Rossi&titel=Best+Of+Semino+Rossi+%2D+Live&cat=a"]

baza_danychh = []
baza_danych_jedenar = []
tds = []
wiersz_tabelki = []
wynik_wiersz = []
wynik_item = []

kuwa = []
for i in range(len(lista_linkow)):
    baza_danych_jedenar.clear()
    sprawdzany_link = lista_linkow[i]
    print(sprawdzany_link)
    sprawdzana_odpowiedz = requests.get(sprawdzany_link, timeout=5)
    sprawdzany_html = sprawdzana_odpowiedz.text
    sprawdzana_soup = BeautifulSoup(sprawdzany_html, 'html.parser')
    tytul = sprawdzana_soup.title.string
    naszatabelka = sprawdzana_soup.find("table", class_="chartrun")
    lista_tr = naszatabelka.find_all("tr")
    for i in range(len(lista_tr)):
        tds.clear()
        lista_td = lista_tr[i].find_all("td")
        tds.append(tytul)
        for j in range(len(lista_td)):
            if lista_td[j].string is None:
                if lista_td[j].a is None:
                    tds.append(" ")
                else:
                    tds.append(lista_td[j].a.string)
            else:
                tds.append(lista_td[j].string)
        second = tds.copy()        
        wiersz_tabelki.append(second)
    sprawdzana_odpowiedz.close()
        
for i in range(len(wiersz_tabelki)):
    tmp = ';'.join(wiersz_tabelki[i])
    wynik_item.append(tmp)
 
    
wynik_intro = ''''''
wynik_outro = ''''''
wynik_item2 = ';\n'.join(wynik_item)
f = open("holandia_seminoaddialmartino.csv", "w", encoding="utf-8")
f.write(wynik_intro + wynik_item2 + wynik_outro)
f.close()
