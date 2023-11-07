import requests
import csv
from bs4 import BeautifulSoup
count = 0
name = []
names = []
ssilki = []

url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

headers = {

    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=headers)
src = req.text

with open ("index.html", "w") as file:
    file.write(src)

with open ("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "html.parser")
s = soup.find_all(class_="mzr-tc-group-item-href")
for i in s:
    names.append(i.text)
    name.append(i.get("title"))
    ss = i.get("href")
    ssilki.append('https://health-diet.ru' + ss)

while count<55:
    for prod in ssilki:
        req1 = requests.get(prod)
        src = req1.text
        with open (str(names[count])+".html", "w") as file:
            file.write(src)
            count+=1



c = 0
while c<55:
    with open(str(names[c])+".html") as file:
        try:
            src1 = file.read()
            pr = BeautifulSoup(src1, "html.parser")
            table = pr.find(class_="uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed").find_all("tr")
            dlina = len(table)
            with open(str(names[c])+'.csv', "a", encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(
                        (
                            "Nazvanie",
                            "Kaloriinost",
                            "Belki",
                            "Zhiri",
                            "Uglevodi"


                    )
                    )
            for j in range(1,dlina):
                product = table[j].find_all("td")
                product_name = product[0].text
                product_kaloriinost = product[1].text
                product_belki = product[2].text
                product_zhiri = product[3].text
                product_uglevodi = product[4].text
                
                with open(str(names[c])+'.csv', "a", encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(
                        (
                            product_name,
                            product_kaloriinost,
                            product_belki,
                            product_zhiri,
                            product_uglevodi


                    )
                    )
            print(f"Записанных файлов:{c+1}")
        except:
             print(c)
    c+=1

