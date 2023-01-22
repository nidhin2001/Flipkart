from bs4 import BeautifulSoup
import requests
import openpyxl

excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="smart_phones"
sheet.append(['phone_name','rating','price'])


try:
    for a in range(1,25):
        res=requests.get(f"https://www.flipkart.com/search?q=smart+phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=price_desc&page={a}")
        soup=BeautifulSoup(res.text,"html.parser")
        phone=soup.find_all("div",class_="_3pLy-c row")
        for i in phone:
            phone_name=i.find("div",class_="_4rR01T").text
            price=i.find("div",class_="_30jeq3 _1_WHN1").text
            rateing=i.find("div",class_="_3LWZlK").text
            #views = i.find('span', class_="_2_R_DZ").text
            print(phone_name,rateing,price)
            #break
            sheet.append([phone_name,rateing,price])




except Exception as e:
    print(e)

excel.save("mobiles.xlsx")
